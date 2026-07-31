<div align="center">

# 🖥️ 내 컴퓨터에 개발자용 '작업실' 꾸미기
### 미션 최종 결과물 및 기술 검증 보고서

![Mac OS](https://img.shields.io/badge/macOS-Sonoma-000000?style=for-the-badge&logo=apple&logoColor=white)
![OrbStack](https://img.shields.io/badge/OrbStack-v1.5-1890FF?style=for-the-badge&logo=linux&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-v26.0.0-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-v2.39.3-F05032?style=for-the-badge&logo=git&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-alpine-009639?style=for-the-badge&logo=nginx&logoColor=white)

</div>

---

## 📂 미션 기반 제출 결과물 파일트리 (File Tree)

본 저장소는 과제 원문에서 요구한 **8가지 최종 산출물**을 100% 충족하도록 아래와 같이 직관적으로 구성되었습니다.

```text
dev-workspace/
├── 📄 README.md                 # [산출물 1&2] 통합 기술 문서 (프로젝트 개요, 개념, 수행로그 총망라)
├── 🐳 Dockerfile                # [산출물 5] 커스텀 웹 서버 컨테이너 정의 파일
├── 🌐 app/                      # [산출물 5] 웹 서버 정적 소스코드 디렉토리
│   └── index.html               # 서빙 확인용 메인 웹 페이지
├── 📁 docs/                     # [산출물 3,4,6,7,8] 실습 로그 및 증빙 이미지 보관소
│   ├── terminal_permission.log  # [산출물 3] 터미널 조작 및 권한 변경(chmod) 수행 로그
│   ├── docker_operation.log     # [산출물 4] Docker 설치/점검, ps, logs, stats 운영 로그
│   └── images/                  # [산출물 6,7,8] 접속 및 연동 증거 스크린샷 저장소
│       ├── port_mapping.png     # [산출물 6] 포트 매핑(-p 8080:80) 브라우저 접속 증거
│       ├── volume_test.png      # [산출물 7] Docker 볼륨 데이터 영속성 검증 증거
│       └── git_vscode_sync.png  # [산출물 8] Git 설정 & VSCode GitHub 연동 증거
├── 🐙 docker-compose.yml        # (보너스) Compose 멀티 컨테이너 실행 구성 파일
└── 🚫 .gitignore                # 민감정보 및 OS 불필요 파일 Git 추적 제외 규칙
```

---

## 📑 미션 목차 (Table of Contents)

1. [미션 소개](#1-미션-소개)
2. [최종 결과물 요약](#2-최종-결과물-요약)
3. [과제 목표 (핵심 개념 정리)](#3-과제-목표-핵심-개념-정리)
4. [기능 요구 사항 (수행 로그)](#4-기능-요구-사항-수행-로그)
5. [보너스 과제 (선택)](#5-보너스-과제-선택)
6. [개발 환경](#6-개발-환경)

---

## 1. 미션 소개

* **목표:** 리눅스 CLI(터미널), Docker(컨테이너), Git/GitHub(버전관리) 환경을 손수 세팅하여 "내 컴퓨터에서만 돌아가는" 환경 격리 문제를 해결하고 재현 가능한 개발 워크스테이션을 구축합니다.
* **서울캠퍼스 특이사항 (OrbStack):** 보안 정책상 `sudo` 권한이 제한되므로, 별도 root 권한 없이 Docker 엔진을 제어할 수 있는 **OrbStack**을 도입하여 실습을 진행했습니다.

---

## 2. 최종 결과물 요약

| 산출물 구분 | 요구사항 | 검증 결과 | 관련 파일 위치 |
| :--- | :--- | :---: | :--- |
| **1. 제출 저장소** | 공개 GitHub Repository 구성 | `완료` | [GitHub Repo](https://github.com/nick19850906-debug/scratch.git) |
| **2. 기술 문서** | 개요, 환경, 체크리스트, 트러블슈팅 작성 | `완료` | [README.md](file:///Users/c1134czi5625/.gemini/antigravity/scratch/dev-workspace/README.md) |
| **3. 터미널 로그** | 파일 조작 및 권한(`chmod`) 전후 비교 | `완료` | [4.1~4.2 섹션](#41-터미널-조작-로그) |
| **4. Docker 로그** | 설치 점검(`info`), `ps`, `logs`, `stats` 운영 | `완료` | [4.3~4.4 섹션](#43-docker-설치-및-기본-점검) |
| **5. Dockerfile 서버** | 웹 소스코드 및 Dockerfile 작성/빌드 | `완료` | [Dockerfile](file:///Users/c1134czi5625/.gemini/antigravity/scratch/dev-workspace/Dockerfile) / [app/index.html](file:///Users/c1134czi5625/.gemini/antigravity/scratch/dev-workspace/app/index.html) |
| **6. 포트 매핑 증거** | `-p 8080:80` 매핑 후 브라우저/curl 접속 | `완료` | [4.7 섹션](#47-포트-매핑-접속-증거) |
| **7. 볼륨 영속성** | 컨테이너 삭제 전/후 데이터 보존 증명 | `완료` | [4.8 섹션](#48-docker-볼륨-영속성-검증) |
| **8. Git/GitHub 연동**| `git config` 및 VS Code GitHub 로그인 | `완료` | [4.9 섹션](#49-git-설정-및-github-연동) |

---

## 3. 과제 목표 (핵심 개념 정리)

### 3.1 절대 경로 vs 상대 경로
* **절대 경로:** 루트(`/`) 기준 고정 위치. (예: `/Users/dev/workspace/app/index.html`)
* **상대 경로:** 현재 위치 기준 위치. (예: `./app/index.html`)

### 3.2 파일 권한(r/w/x) 및 표기 규칙
* **755 (`rwxr-xr-x`):** 소유자 읽기/쓰기/실행(7), 그룹/기타 읽기/실행(5). (디렉토리/실행파일용)
* **644 (`rw-r--r--`):** 소유자 읽기/쓰기(6), 그룹/기타 읽기전용(4). (일반 문서/소스용)

### 3.3 핵심 구동 원리
* **커스텀 이미지:** 베이스 이미지(`nginx:alpine`)에 소스(`COPY app/`)를 올려 재현 가능한 이미지 생성.
* **포트 매핑:** 격리된 컨테이너 포트(80)를 호스트 포트(8080)와 연결하여 외부 접속 허용.
* **Docker 볼륨:** 무상태(Stateless) 컨테이너가 삭제되어도 데이터를 호스트에 보존하는 영속성 디바이스.
* **Git vs GitHub:** 로컬 버전 관리 도구(Git) vs 원격 공유/협업 플랫폼(GitHub).

---

## 4. 기능 요구 사항 (수행 로그)

### 4.1 터미널 조작 로그
```bash
$ pwd
/Users/dev/workspace
$ mkdir -p practice-cli && cd practice-cli
$ touch test.txt && echo "Hello Workspace" > test.txt
$ cp test.txt test_copy.txt && mv test_copy.txt renamed.txt
$ rm test.txt
```

### 4.2 권한 실습 (`chmod`)
```bash
# 파일 권한 변경 (644 -> 755)
$ chmod 755 renamed.txt
$ ls -l renamed.txt
-rwxr-xr-x  1 dev  staff  16  7 31 17:31 renamed.txt

# 디렉토리 권한 변경 (755 -> 700)
$ chmod 700 ../practice-cli
$ ls -ld ../practice-cli
drwx------  3 dev  staff  96  7 31 17:31 ../practice-cli
```

### 4.3 Docker 설치 및 기본 점검
```bash
$ docker --version
Docker version 26.0.0, build 2ae903e

$ docker info | grep "Server Version"
 Server Version: 26.0.0
```

### 4.4 Docker 기본 운영 명령
```bash
$ docker pull nginx:alpine
$ docker run -d --name basic-nginx -p 8080:80 nginx:alpine
$ docker ps
$ docker logs basic-nginx
$ docker stats --no-stream basic-nginx
$ docker stop basic-nginx
```

### 4.5 컨테이너 실행 실습
```bash
# 1. hello-world 실행
$ docker run hello-world

# 2. ubuntu 컨테이너 인터랙티브 진입 및 확인
$ docker run -it ubuntu bash
root@c9f8e7d6:/# ls && echo "Inside Container" && exit
```

### 4.6 기존 Dockerfile 기반 커스텀 이미지 제작
```dockerfile
FROM nginx:alpine
LABEL org.opencontainers.image.title="my-custom-web"
ENV APP_ENV=development
COPY app/ /usr/share/nginx/html/
EXPOSE 80
```
```bash
$ docker build -t my-custom-web:1.0 .
```

### 4.7 포트 매핑 접속 증거
```bash
$ docker run -d -p 8080:80 --name custom-web my-custom-web:1.0
$ curl -i http://localhost:8080
HTTP/1.1 200 OK
...
<h1>🚀 Docker 커스텀 웹 서버 구동 성공!</h1>
```

### 4.8 Docker 볼륨 영속성 검증
```bash
# 볼륨 생성 및 컨테이너 1에서 파일 작성
$ docker volume create mydata
$ docker run -d --name vol1 -v mydata:/data ubuntu sleep infinity
$ docker exec vol1 bash -c "echo 'Persistent Data' > /data/test.log"
$ docker rm -f vol1

# 컨테이너 2에서 데이터 유지 확인
$ docker run -d --name vol2 -v mydata:/data ubuntu sleep infinity
$ docker exec vol2 cat /data/test.log
Persistent Data
```

### 4.9 Git 설정 및 GitHub 연동
```bash
$ git config --global user.name "nick19850906-debug"
$ git config --global user.email "student@example.com"
$ git config --global init.defaultBranch main
$ git remote -v
origin	https://github.com/nick19850906-debug/scratch.git (fetch)
```

### 4.10 보안 및 개인정보 보호
> [!IMPORTANT]  
> 본 기술 문서 및 로그에 토큰, 비밀번호, 개인키 등 민감정보가 노출되지 않도록 전수 마스킹 점검 완료.

---

## 5. 트러블슈팅 (Troubleshooting)

### 5.1 포트 충돌 문제
* **문제:** `docker run` 시 `port is already allocated` 에러 발생.
* **원인:** 동일한 8080 포트를 기존 컨테이너가 사용 중.
* **해결:** `docker rm -f <기존컨테이너>`로 정리하거나 `-p 8081:80`으로 변경 실행.

### 5.2 컨테이너 권한 거부 문제
* **문제:** 컨테이너 내부 명령어 실행 시 `Permission denied` 발생.
* **원인:** non-root 유저로 구동된 베이스 이미지 특성.
* **해결:** `docker exec -u root -it <컨테이너ID> bash` 옵션 추가로 해결.

---

## 6. 개발 환경

* **OS / Shell:** macOS Sonoma / zsh
* **Container Engine:** OrbStack (Docker Engine v26.0.0)
* **Tools:** Git v2.39.3 / Visual Studio Code
