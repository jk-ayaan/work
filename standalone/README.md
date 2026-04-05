# Standalone (API 연동 버전)

Admin API 연동 기능이 포함된 사업자번호 생성기입니다.
프록시 서버를 통해 Admin 시스템에 로그인하고, 생성된 사업자번호로 API를 호출할 수 있습니다.

## 실행 방법

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

### 2. 프록시 서버 실행

```bash
python proxy.py
```

서버가 `http://localhost:8099`에서 시작됩니다.

### 3. HTML 파일 열기

`main.html`을 브라우저에서 열고, Admin 로그인 설정에서 프록시 URL과 로그인 정보를 입력합니다.

## 파일 구성

| 파일 | 설명 |
|------|------|
| `main.html` | 통합 도구 (사업자번호/QR/조합 생성기 + 어드민 대시보드, API 연동 포함) |
| `proxy.py` | FastAPI 기반 CORS 프록시 서버 |
| `requirements.txt` | Python 의존성 |
