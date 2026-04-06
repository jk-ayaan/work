# Standalone (API 연동 버전)

Admin API 연동 기능이 포함된 사업자번호 생성기입니다.
별도 서버 없이 HTML 파일 하나만 열면 모든 기능이 동작합니다.

## 실행 방법

`index.html`을 브라우저에서 열면 바로 사용할 수 있습니다.

### Admin API 연동

1. Admin 로그인 설정에서 로그인 API URL, ID, Password를 입력합니다.
2. CORS 제한이 있는 API의 경우, CORS 프록시 URL을 설정합니다 (기본값: `https://corsproxy.io/?url=`).
3. API가 CORS를 허용하면 CORS 프록시 URL을 비워두고 직접 호출할 수 있습니다.

## 파일 구성

| 파일 | 설명 |
|------|------|
| `index.html` | 통합 도구 (사업자번호/QR/조합 생성기 + 어드민 대시보드, API 연동 포함) |
