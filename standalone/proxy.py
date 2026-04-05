import time
import logging

import httpx
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Admin Proxy Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class LoginRequest(BaseModel):
    loginUrl: str
    id: str
    password: str

    model_config = {"extra": "allow"}


class CallRequest(BaseModel):
    apiUrl: str
    method: str = "POST"
    headers: dict = {}
    body: dict = {}


@app.post("/api/login")
async def proxy_login(req: LoginRequest):
    start = time.time()
    login_url = req.loginUrl
    payload = req.model_dump(exclude={"loginUrl"})

    logger.info("LOGIN -> %s", login_url)
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(login_url, json=payload)
        elapsed = time.time() - start
        logger.info("LOGIN <- %s %d (%.2fs)", login_url, resp.status_code, elapsed)

        try:
            data = resp.json()
        except Exception:
            data = resp.text

        return JSONResponse(status_code=resp.status_code, content=data)
    except httpx.RequestError as e:
        elapsed = time.time() - start
        logger.error("LOGIN ERROR %s (%.2fs): %s", login_url, elapsed, e)
        return JSONResponse(status_code=502, content={"error": str(e)})


@app.post("/api/call")
async def proxy_call(req: CallRequest):
    start = time.time()
    api_url = req.apiUrl
    method = req.method.upper()

    logger.info("CALL -> %s %s", method, api_url)
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.request(
                method=method,
                url=api_url,
                headers=req.headers,
                json=req.body,
            )
        elapsed = time.time() - start
        logger.info("CALL <- %s %d (%.2fs)", api_url, resp.status_code, elapsed)

        try:
            data = resp.json()
        except Exception:
            data = resp.text

        return JSONResponse(status_code=resp.status_code, content=data)
    except httpx.RequestError as e:
        elapsed = time.time() - start
        logger.error("CALL ERROR %s (%.2fs): %s", api_url, elapsed, e)
        return JSONResponse(status_code=502, content={"error": str(e)})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8099)
