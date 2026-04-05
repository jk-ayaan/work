# 업무 도우미 (Work Assistant)

업무 효율성을 높이기 위한 통합 웹 도구 모음입니다. 가맹점 관리, 데이터 생성, 토큰 관리 등 다양한 업무 도구들을 하나의 인터페이스에서 제공합니다.

## 🚀 바로 시작하기

### GitHub Pages로 접속
별도 설치 없이 바로 사용 가능합니다:
👉 **[https://jk-ayaan.github.io/work-assistant/main.html](https://jk-ayaan.github.io/work-assistant/main.html)**

### 로컬 실행
```bash
# 프로젝트 클론
git clone https://github.com/jk-ayaan/work-assistant.git

# 디렉토리 이동
cd work-assistant

# HTML 파일 직접 열기
open main.html
```

## 📋 주요 기능

### 🏠 대시보드
- **실시간 통계**: 일일 활동, 완료 작업, 저장된 토큰, 생성된 파일 수
- **활동 기록**: 최근 사용한 도구 및 작업 히스토리
- **기간별 필터**: 일간, 주간, 월간, 연간 통계 조회
- **데이터 시각화**: 인터랙티브 차트 및 그래프

### 🛠 어드민 활용
- **가맹점 생성 및 QR 활성화**: 새로운 가맹점 등록 및 QR 코드 생성
- **가맹점 QR 복구**: 손상된 QR 코드 복구 및 재활성화
- **매장 권한 변경**: 매장별 사용자 권한 관리 및 수정
- **동적 관리 시스템**: 
  - 어드민 도구 추가/삭제 관리
  - JSON 설정 파일 내보내기/가져오기
  - 로컬 저장소 연동

### 📊 데이터 생성 도구
- **샘플 이미지 생성기**: 
  - 다양한 크기와 포맷의 테스트 이미지 생성
  - 커스텀 텍스트 및 배경색 설정
- **QR XLSX 생성기**: 
  - QR 코드 정보가 포함된 엑셀 파일 생성
  - 배치 처리 및 대량 데이터 지원
- **CSV 생성기**: 
  - 커스텀 CSV 파일 생성 및 다운로드
  - 템플릿 기반 데이터 생성
- **프로필 이미지 생성기**: 
  - 텍스트 기반 프로필 이미지 생성
  - 환경별 칩 추가 (QA, DEV, STAGE, PROD)
  - 실시간 미리보기 및 사이즈 조절
- **환경 뱃지 생성기**: 
  - 개발 환경 구분용 뱃지 생성
  - 다양한 스타일 (사각형, 둥근 모서리, 원형)
  - PNG/SVG 포맷 지원
- **사업자등록번호 생성기**: 
  - 유효한 한국 사업자등록번호 생성
  - **유형별 정확한 경계값 분할**:
    - 개인사업자 (01-79)
    - 개인사업자 (90-99)  
    - 법인 영리 국내 (81, 85-88)
    - 법인 영리 해외 (84)
    - 비영리/국가 및 지자체 (82-83)
    - 임의단체 (80, 89)
  - **생성 모드**:
    - 단일 유형별 생성
    - 전체 랜덤 생성
    - MAX 생성 (모든 유형별 최대량 생성)
  - **고급 설정**:
    - 각 유형별 최대 생성 개수 설정
    - 전체 생성 상한선 제어
    - 유형별 분류 표시 및 통계

### ⚙️ 설정
- **토큰 관리**: 
  - 브라우저 저장 토큰 상태 확인
  - 토큰 동기화 및 내보내기
  - 쿠키 관리 도구
- **테마 설정**: 
  - 다크/라이트 모드 전환
  - 자동 저장 설정
- **언어 지원**: 한국어/영어 다국어 지원
- **시스템 정보**: 버전 정보, 업데이트 내역, 사용자 통계

## 🎨 특징

### 반응형 디자인
- 모바일, 태블릿, 데스크톱 완벽 지원
- 터치 친화적 인터페이스
- 모바일 전용 네비게이션

### 사용자 경험
- 직관적인 탭 네비게이션
- 실시간 미리보기 및 피드백
- 토스트 알림 시스템
- 키보드 단축키 지원

### 데이터 관리
- 로컬 스토리지 활용
- JSON 기반 설정 관리
- 자동 백업 및 복원
- 데이터 무결성 보장

## 🛡️ 보안 및 프라이버시

- 모든 데이터는 브라우저 로컬에서 처리
- 외부 서버로 데이터 전송 없음
- HTTPS를 통한 안전한 접속 (GitHub Pages)
- 토큰 및 민감 정보 암호화 저장

## 🔧 기술 스택

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **UI Framework**: Tailwind CSS
- **Icons**: Heroicons
- **Storage**: Browser LocalStorage
- **Deployment**: GitHub Pages

## 📱 브라우저 지원

- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

## 🚀 배포

### GitHub Pages 자동 배포
1. `main` 브랜치에 푸시
2. GitHub Pages가 자동으로 업데이트
3. 몇 분 후 변경사항이 웹에 반영

### 로컬 개발
```bash
# 개발 서버 실행 (Python)
python -m http.server 8000

# 개발 서버 실행 (Node.js)
npx serve .

# 브라우저에서 접속
http://localhost:8000/main.html
```

## 📝 업데이트 로그

- **v2.1.0** (2024-09-04)
  - 사업자등록번호 생성기 완전 개선
  - 프로필 이미지 생성기 칩 렌더링 수정
  - 유형별 경계값 분할 정확성 향상
  - MAX 생성 모드 및 고급 설정 추가

- **v2.0.0** (2024-08-15)
  - 프로필 이미지 생성기 추가
  - 환경 뱃지 생성기 추가
  - 사업자등록번호 생성기 추가
  - 다국어 지원 (한국어/영어)

## 🤝 기여하기

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 있습니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 📞 문의

프로젝트에 대한 문의사항이나 버그 신고는 [Issues](https://github.com/jk-ayaan/work-assistant/issues)를 이용해 주세요.

---

⭐ 이 프로젝트가 도움이 되셨다면 Star를 눌러주세요!