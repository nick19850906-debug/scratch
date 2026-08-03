# 🚀 [EPIC] Developer Workstation Infrastructure
**루키마리너 2기 | nick19850906-debug**

<p align="center">
  <img src="https://img.shields.io/badge/OS-macOS_Sonoma_14.5-000000?style=for-the-badge&logo=apple&logoColor=white" alt="macOS" />
  <img src="https://img.shields.io/badge/Container_Engine-OrbStack_v1.5-1890FF?style=for-the-badge&logo=linux&logoColor=white" alt="OrbStack" />
  <img src="https://img.shields.io/badge/Docker-v26.0.0-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Git-v2.39.3-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
  <img src="https://img.shields.io/badge/Web_Server-NGINX_Alpine-009639?style=for-the-badge&logo=nginx&logoColor=white" alt="Nginx" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
</p>

---

## 📌 Executive Summary

본 저장소는 **Linux CLI, Docker 컨테이너 가상화, Git/GitHub 형상관리** 3대 핵심 개발 인프라 도구를 결합하여, **"내 컴퓨터에서만 돌아가는(It works on my machine)"** 격차 문제를 원천 해결하는 **표준 개발자 워크스테이션(Developer Workstation)** 구축 검증 프로젝트입니다.

> [!IMPORTANT]
> **💡 서울캠퍼스 시스템 보안 정책 완벽 대응 (OrbStack)**  
> 서울캠퍼스 PC 환경의 `sudo` 루트 권한 제한 정책에 대응하여, 관리자 권한 없이도 고성능 Docker 엔진을 안정적으로 구동하는 **OrbStack 런타임** 기반으로 가상화 인프라를 구축하였습니다.

---


## 📋 Table of Contents

1. [시스템 환경 명세 (System Specs)](#1-시스템-환경-명세-system-specs)
2. [수행 항목 체크리스트 (Deliverables Checklist)](#2-수행-항목-체크리스트-deliverables-checklist)
3. [프로젝트 디렉토리 구조 (Directory Structure)](#3-프로젝트-디렉토리-구조-directory-structure)
4. [단계별 세부 수행 및 검증 로그 (Verification Logs)](#4-단계별-세부-수행-및-검증-로그-verification-logs)
5. [핵심 엔지니어링 개념 정리 (6 Core Principles)](#5-핵심-엔지니어링-개념-정리-6-core-principles)
6. [실무 관점 트러블슈팅 (Troubleshooting TS-01 & TS-02)](#6-실무-관점-트러블슈팅-troubleshooting-ts-01--ts-02)

---

## 1. 시스템 환경 명세 (System Specs)

| 항목 | 실측 명세 | 비고 |
| :--- | :--- | :--- |
| **Operating System** | macOS Sonoma (v14.5) | Apple Silicon / Intel Core x86_64 |
| **Shell Engine** | `/bin/zsh` | Z Shell 터미널 |
| **Container Engine** | **OrbStack Engine (Docker v26.0.0)** | `sudo` 권한 없이 데몬 구동 |
| **Version Control** | Git v2.39.3 | 프로젝트 단위 `--local` 스코프 설정 |
| **Web Server** | NGINX v1.25.4 (Alpine Linux Base) | 62.4MB 경량화 이미지 |
| **Remote Repository** | [nick19850906-debug/scratch](https://github.com/nick19850906-debug/scratch) | GitHub Public Repository |

---

## 2. 수행 항목 체크리스트 (Deliverables Checklist)

- [x] **CLI & 파일 제어:** `pwd`, `ls -la`, `mkdir`, `touch`, `cp`, `mv`, `rm`, `cat`, `echo` 수행
- [x] **권한 관리 (PoLP):** 파일 `644` (rw-r--r--), 디렉토리 `755` (rwxr-xr-x) 변경 전/후 검증
- [x] **Docker 설치 & 점검:** `docker --version`, `docker info` 데몬 동작 확인
- [x] **기본 운영 명령:** `docker pull`, `docker images`, `docker ps -a`, `docker logs`, `docker stats`
- [x] **컨테이너 진입 실습:** `hello-world` 실행, `ubuntu` 셸 진입 (`docker run -it ubuntu bash`)
- [x] **Dockerfile 빌드:** `nginx:alpine` 베이스 이미지 커스텀 빌드 (`my-custom-web:1.0`)
- [x] **포트 매핑 (NAT):** `-p 8080:80` 포트 포워딩 적용 및 브라우저/`curl` 접속 성공
- [x] **바인드 마운트:** `-v ./app:/usr/share/nginx/html` 실시간 소스 동기화 검증
- [x] **볼륨 영속성:** `docker volume create` 데이터 파기 전/후 생존 증명
- [x] **Git & GitHub 연동:** `--local` 사용자 설정, VS Code Source Control 및 원격 `push` 완수

---

## 3. 프로젝트 디렉토리 구조 (Directory Structure)

```text
scratch/
 ├── 📄 README.md                # [본 문서] 메인 기술 문서 및 아키텍처 가이드
 ├── 🐳 Dockerfile               # NGINX Alpine 기반 커스텀 웹 서버 이미지 명세서 (IaC)
 ├── 🐙 docker-compose.yml       # 멀티 컨테이너(웹 + Redis) 오케스트레이션 명세서
 ├── 🛡️ .gitignore               # macOS 및 임시 파일 버전관리 제외 규칙
 ├── 📁 app/                     # 웹 서버 서빙 소스 디렉토리
 │    └── 💎 index.html          # [Version 2] 사이버 글래스모피즘 & 애니메이션 대시보드
 ├── 📄 Log_4-1_Terminal.md      # 4-1. 터미널 CLI 조작 및 권한(644/755) 실습 로그
 ├── 📄 Log_4-2_Docker.md        # 4-2. Docker 설치 점검, hello-world, ubuntu 진입 로그
 ├── 📄 Log_4-3_Dockerfile.md    # 4-3. Dockerfile 작성 및 커스텀 이미지 빌드 로그
 ├── 📄 Log_4-4_PortMapping.md   # 4-4. 포트 매핑(-p 8080:80) 및 curl 접속 응답 로그
 ├── 📄 Log_4-5_BindMount.md     # 4-5. 바인드 마운트 실시간 소스 변경 반영 검증 로그
 ├── 📄 Log_4-6_Volume.md        # 4-6. Docker Volume 컨테이너 삭제 전/후 데이터 영속성 로그
 └── 📄 Log_4-7_Git.md           # 4-7. Git Local 프로필 설정 및 GitHub 원격 연동 로그
```

---

## 4. 단계별 세부 수행 및 검증 로그 (Verification Logs)

각 단계별 수행 명령과 실제 터미널 출력 결과는 독립된 상세 기술 문서로 격리 저장되어 있습니다.

| 단계 | 실습 항목 | 검증 내용 요약 | 상세 로그 링크 |
| :---: | :--- | :--- | :---: |
| **4-1** | **Linux CLI & 권한** | `pwd`, `ls -la`, `chmod 644/755` 파일/디렉토리 비교 | 📄 [Log_4-1_Terminal.md](Log_4-1_Terminal.md) |
| **4-2** | **Docker 설치 & 진입** | `docker info` 점검, `hello-world`, `ubuntu` 셸 진입 | 📄 [Log_4-2_Docker.md](Log_4-2_Docker.md) |
| **4-3** | **Dockerfile 빌드** | `nginx:alpine` 기반 커스텀 빌드 (`my-custom-web:1.0`) | 📄 [Log_4-3_Dockerfile.md](Log_4-3_Dockerfile.md) |
| **4-4** | **포트 매핑** | `-p 8080:80` 포트 포워딩 적용 및 `curl` 200 OK 수신 | 📄 [Log_4-4_PortMapping.md](Log_4-4_PortMapping.md) |
| **4-5** | **바인드 마운트** | `-v ./app:/usr/share/nginx/html` 실시간 코드 반영 | 📄 [Log_4-5_BindMount.md](Log_4-5_BindMount.md) |
| **4-6** | **볼륨 영속성** | `docker volume` 컨테이너 삭제 후 데이터 100% 보존 | 📄 [Log_4-6_Volume.md](Log_4-6_Volume.md) |
| **4-7** | **Git & GitHub 연동** | `--local` 스코프 설정, VS Code 연동 및 `push` 완료 | 📄 [Log_4-7_Git.md](Log_4-7_Git.md) |

---

## 5. 핵심 엔지니어링 개념 정리 (6 Core Principles)

<details>
<summary><b>💡 1. 절대 경로(Absolute Path) vs 상대 경로(Relative Path)</b></summary>
<br>

- **절대 경로 (Absolute Path):** 최상위 루트 디렉토리(`/`)에서 시작하는 전체 경로. 위치와 무관하게 항상 동일한 파일 접근을 보장하며, **Dockerfile 및 자동화 스크립트의 멱등성(Idempotency)**을 위해 반드시 사용된다. (예: `/usr/share/nginx/html`)
- **상대 경로 (Relative Path):** 현재 작업 위치(`pwd`)를 기준으로 상대적 이동 경로. (예: `./app`, `../src`)
</details>

<details>
<summary><b>💡 2. 파일 권한 (r/w/x) 및 644, 755 표기 규칙</b></summary>
<br>

- **최소 권한의 원칙 (Principle of Least Privilege, PoLP)** 적용:
  - **파일 (`644` / `rw-r--r--`):** 소유자 읽기+쓰기(6), 그룹/타인 읽기전용(4). 실행 권한(x)을 제거하여 악성 스크립트 실행(RCE) 원천 차단.
  - **디렉토리 (`755` / `rwxr-xr-x`):** 소유자 전체권한(7), 그룹/타인 탐색/진입 허용(5). 타인의 무단 쓰기는 차단하되 디렉토리 탐색(x)은 허용.
</details>

<details>
<summary><b>💡 3. Dockerfile 기반 커스텀 이미지 제작 원리</b></summary>
<br>

- 무거운 OS 베이스(Ubuntu ~100MB) 대신 **`nginx:alpine` 경량 베이스(62.4MB)**를 선택하여 공격 표면(Attack Surface)을 최소화함.
- `COPY app/ /usr/share/nginx/html/` 명령으로 불변 레이어(Immutable Layer)를 구성하여 재현 가능한 이미지 생성.
</details>

<details>
<summary><b>💡 4. 포트 매핑 (Port Mapping)이 필요한 이유</b></summary>
<br>

- Docker 컨테이너는 격리된 **네트워크 네임스페이스(Network Namespace)**에서 구동되므로, 컨테이너 내부 80번 포트는 외부에서 접근 불가능함.
- `-p 8080:80` 옵션은 호스트 OS의 8080 포트를 컨테이너 80 포트로 포워딩하는 **NAT 규칙**을 생성하여 외부 접속을 선택적으로 허용함.
</details>

<details>
<summary><b>💡 5. Docker 볼륨 (Volume) 데이터 영속성</b></summary>
<br>

- 컨테이너는 생명주기가 끝나면 파일시스템이 소멸하는 **휘발성(Ephemeral)**을 가짐.
- Docker Volume (`-v redis-data:/data`)은 컨테이너 생명주기와 완전히 독립된 저장소로, 컨테이너를 강제 삭제(`docker rm -f`)해도 데이터가 100% 보존됨.
</details>

<details>
<summary><b>💡 6. Git과 GitHub의 역할 차이</b></summary>
<br>

- **Git (로컬 버전 관리):** 내 컴퓨터에서 파일 변경 이력을 추적하고 커밋(스냅샷)을 관리하는 독립 소프트웨어.
- **GitHub (원격 협업 플랫폼):** Git 저장소를 클라우드에 호스팅하여 팀원 간 코드 공유, 이슈 관리, CI/CD를 제공하는 웹 서비스.
</details>

---

## 6. 실무 관점 트러블슈팅 (Troubleshooting TS-01 & TS-02)

> [!NOTE]
> 본 미션 수행 중 경험한 실제 인프라 문제와 기술적 해결 절차를 기록합니다.

### TS-01: 호스트 8080 포트 선점(Conflict) 문제
- **문제 증상:** `docker run -d -p 8080:80 ...` 실행 시 `Bind for 0.0.0.0:8080 failed: port is already allocated` 에러 발생.
- **원인 분석:** 이전 실습 과정에서 생성된 백그라운드 프로세스가 호스트의 `8080` 포트를 이미 선점함.
- **해결책:** `docker rm -f <기존컨테이너ID>`로 기존 프로세스를 정리하거나, `-p 8081:80`으로 우회 매핑하여 해결함.

### TS-02: 컨테이너 내부 명령어 실행 시 권한 거부 (Permission Denied)
- **문제 증상:** 컨테이너 진입 후 패키지 설치 시 `Permission denied` 에러 발생.
- **원인 분석:** 베이스 이미지의 기본 계정이 non-root 사용자로 설정됨.
- **해결책:** `docker exec -u root -it <컨테이너ID> bash` 옵션으로 root 권한을 명시하여 안전하게 진입함.

---

<p align="center">
  <b>© 2026 nick19850906-debug | Rookie Mariner 2nd Gen Workstation Project</b>
</p>
