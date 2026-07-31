# 미션1: 개발 워크스테이션 구축

<p>
  <img src="https://img.shields.io/badge/macOS-Sonoma-000000?style=flat-square&logo=apple&logoColor=white" alt="macOS" />&nbsp;
  <img src="https://img.shields.io/badge/OrbStack-v1.5-1890FF?style=flat-square&logo=linux&logoColor=white" alt="OrbStack" />&nbsp;
  <img src="https://img.shields.io/badge/Docker-26.0.0-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />&nbsp;
  <img src="https://img.shields.io/badge/Git-2.39.3-F05032?style=flat-square&logo=git&logoColor=white" alt="Git" />&nbsp;
  <img src="https://img.shields.io/badge/Nginx-alpine-009639?style=flat-square&logo=nginx&logoColor=white" alt="Nginx" />
</p>

---

## 1. 프로젝트 개요
터미널 CLI, Docker 컨테이너, Git/GitHub 환경을 손수 구축하고 검증하여, "내 컴퓨터에서만 돌아가는" 문제를 방지하고 팀원 누구나 재현 가능한 **표준 개발자 워크스테이션(Development Workstation)**을 완성하는 프로젝트입니다.

> **💡 (서울캠퍼스 환경 정책 대응)**  
> 서울캠퍼스 시스템 보안 정책상 일반적인 `sudo` 권한 사용이 제한되므로, 별도 root 권한 없이도 Docker 데몬을 안정적으로 제어할 수 있는 **OrbStack**을 활용하여 실습을 진행했습니다.

---

## 2. 실행 환경
| 항목 | 내용 |
| :--- | :--- |
| **OS** | macOS Sonoma (14.5) |
| **Shell** | `/bin/zsh` |
| **Docker** | `26.0.0` (OrbStack Engine) |
| **Git** | `2.39.3` |

---

## 3. 수행 항목 체크리스트
- [x] 터미널 기본 조작 연습 (`pwd`, `ls`, `mkdir`, `touch`, `cp`, `mv`, `rm`, `cat`)
- [x] 파일 및 디렉토리 권한 변경 실습 (`chmod 755`, `chmod 644`, `chmod 700`)
- [x] Docker 기본 명령어 점검 (`docker --version`, `docker info`, `docker images`, `docker ps`, `docker stats`)
- [x] 간단한 웹서버 컨테이너 띄우기 (`nginx:alpine`)
- [x] `ubuntu` 컨테이너 내부 진입 실습 (`docker run -it ubuntu bash`)
- [x] Dockerfile 커스텀 이미지 빌드 (`my-custom-web:1.0`)
- [x] 포트 매핑 접속 검증 (`-p 8080:80`)
- [x] 바인드 마운트 반영 확인 (`-v $(pwd)/app:/usr/share/nginx/html`)
- [x] Docker 볼륨 영속성 검증 (`docker volume create` & 데이터 복구 검증)
- [x] Git 설정 + GitHub/VSCode 연동 (`git config`, remote 연결, Commit & Push)

---

## 4. 검증 방법 및 결과

### 4-1. 터미널 조작 및 권한 실습
* 현재 위치 확인, 파일 생성/복사/이동/삭제 및 `chmod` 권한 변경 전후 비교
* 📄 [상세 로그보기](Log_4-1_Terminal.md)

### 4-2. Docker 운영/검증
* `docker --version`, `docker info` 설치 점검 및 `hello-world`, `ubuntu` 인터랙티브 진입 실습
* 📄 [상세 로그보기](Log_4-2_Docker.md)

### 4-3. Dockerfile 기반 웹서버 컨테이너
* `nginx:alpine` 베이스 이미지 기반 Dockerfile 작성 및 커스텀 이미지 빌드
* 📄 [상세 로그보기](Log_4-3_Dockerfile.md)

### 4-4. 포트매핑 접속
* `-p 8080:80` 포트 포워딩 적용 후 브라우저 및 `curl` 접속 응답 성공 검증
* 📄 [상세 로그보기](Log_4-4_PortMapping.md)

### 4-5. 바인드 마운트
* 로컬 `app/` 디렉토리를 컨테이너에 바인드 마운트하여 실시간 수정 반영 검증
* 📄 [상세 로그보기](Log_4-5_BindMount.md)

### 4-6. 볼륨 연속성
* `docker volume` 생성 후 컨테이너 삭제(파기) 전/후 데이터 보존 검증
* 📄 [상세 로그보기](Log_4-6_Volume.md)

### 4-7. Git 설정 및 GitHub/VSCode 연동
* `git config` 프로필 설정 및 VS Code와 GitHub 원격 저장소(`main` 브랜치) 연동
* 📄 [상세 로그보기](Log_4-7_Git.md)

---

## 5. 트러블슈팅 (문제 → 원인 가설 → 확인 → 해결/대안)

### 5-1. 포트 충돌 (Port Already Allocated) 문제
* **문제 증상:** `docker run -d -p 8080:80 ...` 명령어 실행 시 `Bind for 0.0.0.0:8080 failed: port is already allocated` 에러 발생.
* **원인 가설:** 이전 실습에서 띄워둔 컨테이너가 이미 호스트의 8080 포트를 사용 중일 것이다.
* **확인 과정:** `docker ps` 실행 결과 기존 컨테이너가 8080 포트를 점유하고 있음을 확인.
* **해결책/대안:** `docker rm -f <기존컨테이너ID>`로 기존 컨테이너를 강제 삭제하거나, `-p 8081:80`으로 호스트 포트를 변경하여 정상 구동함.

### 5-2. 컨테이너 내부 명령어 실행 시 권한 거부 (Permission Denied) 문제
* **문제 증상:** 컨테이너 진입 후 시스템 패키지 설치 시 `Permission denied` 실패.
* **원인 가설:** 베이스 이미지에 따라 기본 유저가 root가 아닌 non-root 유저로 설정되어 있을 것이다.
* **확인 과정:** `whoami` 실행 시 `root`가 아닌 일반 사용자 계정임을 확인.
* **해결책/대안:** `docker exec -u root -it <컨테이너ID> bash` 옵션을 추가하여 root 권한으로 진입 후 정상적으로 실행함.
