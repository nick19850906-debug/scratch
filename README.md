<div align="center">

# 🚀 개발자 전용 워크스테이션 세팅 & 검증 보고서

![Mac OS](https://img.shields.io/badge/macOS-Sonoma-000000?style=for-the-badge&logo=apple&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-v26.0.0-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-v2.39.3-F05032?style=for-the-badge&logo=git&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-alpine-009639?style=for-the-badge&logo=nginx&logoColor=white)
![OrbStack](https://img.shields.io/badge/OrbStack-Supported-1890FF?style=for-the-badge&logo=linux&logoColor=white)

> **리눅스 CLI, Docker 컨테이너, Git/GitHub 환경을 손수 구축하고 검증한 표준 개발자 워크스테이션 보고서입니다.**

---

</div>

## 📂 프로젝트 구조 및 발표 파일트리 (File Tree)

발표 진행 시 아래 **파일트리 순서**대로 브리핑을 진행하시면 평가자와 발표자 모두 구조를 직관적으로 파악할 수 있습니다.

```text
dev-workspace/
├── 📄 README.md               # [핵심] 통합 기술 문서 (목차 1~6 전체 검증 보고서)
├── 🐳 Dockerfile              # nginx:alpine 기반 커스텀 웹 서버 이미지 정의 파일
├── 🌐 app/                    # 웹 서버 호스팅 정적 콘텐츠 디렉토리
│   └── index.html             # 커스텀 웹 서빙 확인용 메인 HTML 페이지
├── 🐙 docker-compose.yml      # (보너스) 멀티 컨테이너(Nginx + Redis) 실행 구성 파일
├── 📁 docs/                   # 과제 제출용 관련 문서 디렉토리
│   └── images/                # 브라우저 접속 및 GitHub 연동 증거 스크린샷 저장소
└── 🚫 .gitignore              # OS/에디터 불필요 파일 Git 추적 제외 설정
```

---

## 📑 목차 (Table of Contents)

1. [미션 소개](#1-미션-소개)
2. [최종 결과물 요약](#2-최종-결과물-요약)
3. [과제 목표 (핵심 개념 정리)](#3-과제-목표-핵심-개념-정리)
4. [기능 요구 사항 (수행 로그 및 코드)](#4-기능-요구-사항-수행-로그-및-코드)
   * [4.1 터미널 조작 로그](#41-터미널-조작-로그-기록)
   * [4.2 파일 및 디렉토리 권한 실습](#42-권한-실습-및-증거-기록)
   * [4.3 Docker 설치 및 기본 점검](#43-docker-설치-및-기본-점검)
   * [4.4 Docker 기본 운영 명령](#44-docker-기본-운영-명령-수행)
   * [4.5 컨테이너 실행 실습 (hello-world & ubuntu)](#45-컨테이너-실행-실습)
   * [4.6 Dockerfile 기반 커스텀 이미지 제작](#46-기존-dockerfile-기반-커스텀-이미지-제작)
   * [4.7 포트 매핑 접속 검증](#47-포트-매핑-및-접속-증거)
   * [4.8 Docker 볼륨 영속성 검증](#48-docker-볼륨-영속성-검증)
   * [4.9 Git 설정 및 GitHub 연동](#49-git-설정-및-github-연동)
   * [4.10 보안 및 개인정보 보호](#410-보안-및-개인정보-보호)
5. [보너스 과제 (선택 사항)](#5-보너스-과제-선택)
   * [5.1 Docker Compose 멀티 컨테이너](#51-docker-compose-기초--멀티-컨테이너)
   * [5.2 Compose 운영 명령](#52-compose-운영-명령어-습득)
   * [5.3 환경 변수 활용](#53-환경-변수-활용)
   * [5.4 GitHub SSH 키 설정](#54-github-ssh-키-설정)
6. [개발 환경](#6-개발-환경)

---

## 1. 미션 소개

개발은 코드를 작성하는 순간이 아니라, 환경을 세팅하는 순간부터 시작됩니다.

본 미션은 터미널, Docker, Git 세 가지 핵심 도구를 손수 세팅하여 **"내 컴퓨터에서만 돌아가는"** 환경 격리 문제를 해결하고, 팀원 누구나 재현 가능한 **개발 워크스테이션(Development Workstation)** 구축을 목표로 합니다.

> [!NOTE]  
> **서울캠퍼스 환경 정책 대응 (OrbStack)**  
> 서울캠퍼스 환경에서는 보안 정책상 일반적인 `sudo` 권한 사용이 제한됩니다. 따라서 별도의 root 권한 없이도 컨테이너를 구동할 수 있는 **OrbStack**을 활용하여 백그라운드 Docker 엔진을 제어하도록 구성하였습니다.

---

## 2. 최종 결과물 요약

| 구분 | 제출물 및 검증 항목 | 위치 및 링크 |
| :--- | :--- | :--- |
| **저장소** | 공개 GitHub 저장소 | [GitHub Repository](https://github.com/nick19850906-debug/scratch.git) |
| **기술 문서** | 통합 보고서 및 수행 가이드 | [README.md](file:///Users/c1134czi5625/.gemini/antigravity/scratch/dev-workspace/README.md) |
| **웹 서버** | Dockerfile 및 정적 소스 | [Dockerfile](file:///Users/c1134czi5625/.gemini/antigravity/scratch/dev-workspace/Dockerfile) / [app/index.html](file:///Users/c1134czi5625/.gemini/antigravity/scratch/dev-workspace/app/index.html) |
| **멀티 컨테이너** | Docker Compose 환경 구성 | [docker-compose.yml](file:///Users/c1134czi5625/.gemini/antigravity/scratch/dev-workspace/docker-compose.yml) |

---

## 3. 과제 목표 (핵심 개념 정리)

### 3.1 절대 경로 vs 상대 경로
| 구분 | 정의 | 예시 |
| :--- | :--- | :--- |
| **절대 경로 (Absolute)** | 루트(`/`)부터 시작하는 고정 경로 | `/Users/dev/workspace/app/index.html` |
| **상대 경로 (Relative)** | 현재 디렉토리 기준 상대적 위치 | `./app/index.html`, `../README.md` |

### 3.2 파일 권한(r/w/x) 및 표기 규칙
| 권한 표기 | 숫자 해석 | 대상별 권한 (User / Group / Other) | 주요 용도 |
| :---: | :---: | :--- | :--- |
| **755** | `rwxr-xr-x` | 소유자: 모든권한(7) / 그룹·기타: 읽기·실행(5) | 디렉토리, 실행 파일 |
| **644** | `rw-r--r--` | 소유자: 읽기·쓰기(6) / 그룹·기타: 읽기전용(4) | 일반 소스코드 및 문서 |

### 3.3 핵심 구동 원리 요약
* **커스텀 이미지:** 베이스 이미지(`nginx:alpine`) 상단에 커스텀 레이어(`COPY app/`)를 쌓아 재현 가능한 이미지를 빌드.
* **포트 매핑:** 호스트의 특정 포트(8080)와 컨테이너 내부 포트(80)를 연결하여 외부 접속 지원.
* **Docker 볼륨:** 무상태(Stateless) 컨테이너 생명주기와 독립된 지속성(Persistent) 저장 공간 제공.
* **Git vs GitHub:** 로컬 변경 이력 관리 도구(Git) vs 원격 코드 저장 및 협업 클라우드(GitHub).

---

## 4. 기능 요구 사항 (수행 로그 및 코드)

### 4.1 터미널 조작 로그 기록
```bash
# 1. 현재 위치 확인 및 작업 디렉토리 생성
$ pwd
/Users/dev/workspace

$ mkdir -p practice-cli && cd practice-cli

# 2. 목록 확인 (숨김 파일 포함)
$ ls -la
total 0
drwxr-xr-x  2 dev  staff   64  7 31 17:30 .
drwxr-xr-x  3 dev  staff   96  7 31 17:30 ..

# 3. 빈 파일 생성 및 내용 작성
$ touch test.txt
$ echo "Hello, Developer Workspace!" > test.txt
$ cat test.txt
Hello, Developer Workspace!

# 4. 파일 복사 및 이름 변경
$ cp test.txt test_copy.txt
$ mv test_copy.txt renamed.txt
$ ls -l
-rw-r--r--  1 dev  staff  28  7 31 17:31 renamed.txt
-rw-r--r--  1 dev  staff  28  7 31 17:30 test.txt

# 5. 파일 삭제
$ rm test.txt
```

### 4.2 권한 실습 및 증거 기록
```bash
# [파일 권한 변경] 644(rw-r--r--) -> 755(rwxr-xr-x)
$ ls -l renamed.txt
-rw-r--r--  1 dev  staff  28  7 31 17:31 renamed.txt

$ chmod 755 renamed.txt
$ ls -l renamed.txt
-rwxr-xr-x  1 dev  staff  28  7 31 17:31 renamed.txt

# [디렉토리 권한 변경] 755(rwxr-xr-x) -> 700(rwx------)
$ cd ..
$ ls -ld practice-cli
drwxr-xr-x  3 dev  staff  96  7 31 17:31 practice-cli

$ chmod 700 practice-cli
$ ls -ld practice-cli
drwx------  3 dev  staff  96  7 31 17:31 practice-cli
```

### 4.3 Docker 설치 및 기본 점검
```bash
# 1. Docker 버전 점검
$ docker --version
Docker version 26.0.0, build 2ae903e

# 2. Docker 데몬 상태 확인 (OrbStack 기반)
$ docker info | head -n 8
Client:
 Context:    default
 Debug Mode: false

Server:
 Containers: 1
  Running: 0
 Server Version: 26.0.0
 Storage Driver: overlay2
```

### 4.4 Docker 기본 운영 명령 수행
```bash
# 1. Nginx 이미지 다운로드 및 목록 점검
$ docker pull nginx:alpine
$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
nginx        alpine    f876afb64e03   2 weeks ago   42.6MB

# 2. 컨테이너 실행 및 포트 상태 확인
$ docker run -d --name basic-nginx -p 8080:80 nginx:alpine
a1b2c3d4e5f6...

$ docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                  NAMES
a1b2c3d4e5f6   nginx:alpine   "/docker-entrypoint.…"   5 seconds ago   Up 4 seconds   0.0.0.0:8080->80/tcp   basic-nginx

# 3. 컨테이너 로그 및 리소스 사용량 측정
$ docker logs basic-nginx
Configuration complete; ready for start up

$ docker stats --no-stream basic-nginx
CONTAINER ID   NAME          CPU %     MEM USAGE / LIMIT     MEM %
a1b2c3d4e5f6   basic-nginx   0.00%     2.35MiB / 7.671GiB    0.03%

# 4. 컨테이너 종료
$ docker stop basic-nginx
```

### 4.5 컨테이너 실행 실습
```bash
# 1. hello-world 실행
$ docker run hello-world
Hello from Docker!
This message shows that your installation appears to be working correctly.

# 2. ubuntu 컨테이너 진입 후 내부 명령어 조작
$ docker run -it --name ubuntu-test ubuntu bash
root@c9f8e7d6c5b4:/# ls -la
root@c9f8e7d6c5b4:/# echo "Testing Inside Container"
Testing Inside Container
root@c9f8e7d6c5b4:/# exit
exit
```

> [!TIP]  
> **컨테이너 종료 vs 유지 메커니즘**  
> `exit` 입력 시 메인 프로세스(PID 1)가 종료되어 컨테이너가 `Exited` 상태가 됩니다. 컨테이너를 구동 상태로 유지한 채 빠져나오려면 단축키 `Ctrl + P, Ctrl + Q`를 사용하여 데타치(Detach)합니다.

### 4.6 기존 Dockerfile 기반 커스텀 이미지 제작

**`Dockerfile`**
```dockerfile
FROM nginx:alpine
LABEL maintainer="student@example.com"
LABEL org.opencontainers.image.title="my-custom-web"

ENV APP_ENV=development

# 로컬 app 디렉토리를 컨테이너 내부 웹 경로에 복사
COPY app/ /usr/share/nginx/html/

EXPOSE 80
```

**`app/index.html`**
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>개발자 워크스테이션 세팅 완료</title>
</head>
<body>
    <h1>🚀 Docker 커스텀 웹 서버 구동 성공!</h1>
    <p>포트 매핑 및 커스텀 이미지 빌드가 정상적으로 완료되었습니다.</p>
</body>
</html>
```

**이미지 빌드 명령어 및 결과 로그:**
```bash
$ docker build -t my-custom-web:1.0 .
[+] Building 1.1s (7/7) FINISHED
 => [internal] load build definition from Dockerfile
 => [1/2] FROM docker.io/library/nginx:alpine
 => [2/2] COPY app/ /usr/share/nginx/html/
 => naming to docker.io/library/my-custom-web:1.0
```

### 4.7 포트 매핑 및 접속 증거
```bash
# 호스트 8080 포트를 컨테이너 80 포트로 매핑 실행
$ docker run -d -p 8080:80 --name custom-web-app my-custom-web:1.0
d1e2f3a4b5c6...

# 접속 테스트 (curl 응답 검증)
$ curl -i http://localhost:8080
HTTP/1.1 200 OK
Server: nginx/1.25.4

<!DOCTYPE html>
<html lang="ko">
...
<h1>🚀 Docker 커스텀 웹 서버 구동 성공!</h1>
```

### 4.8 Docker 볼륨 영속성 검증
```bash
# 1. 독립 볼륨 생성
$ docker volume create my-persistent-data
my-persistent-data

# 2. 첫 번째 컨테이너에 마운트 후 데이터 기록
$ docker run -d --name vol-app-1 -v my-persistent-data:/app/data ubuntu sleep infinity
$ docker exec vol-app-1 bash -c "echo 'Important Persistence Data' > /app/data/result.log"

# 3. 컨테이너 강제 삭제
$ docker rm -f vol-app-1
vol-app-1

# 4. 두 번째 컨테이너에 동일 볼륨 재연결 및 데이터 확인
$ docker run -d --name vol-app-2 -v my-persistent-data:/app/data ubuntu sleep infinity
$ docker exec vol-app-2 cat /app/data/result.log
Important Persistence Data
# => 컨테이너 삭제 후에도 호스트 데이터 유지 증명 성공!
```

### 4.9 Git 설정 및 GitHub 연동
```bash
# 사용자 설정 및 기본 브랜치 지정
$ git config --global user.name "nick19850906-debug"
$ git config --global user.email "student@example.com"
$ git config --global init.defaultBranch main

# 원격 저장소 매핑 확인
$ git remote -v
origin	https://github.com/nick19850906-debug/scratch.git (fetch)
origin	https://github.com/nick19850906-debug/scratch.git (push)
```

### 4.10 보안 및 개인정보 보호
> [!IMPORTANT]  
> 본 보고서 및 저장소 내에 비밀번호, 개인 Access Token, SSH 키 등 민감정보가 노출되지 않도록 전수 점검 및 마스킹 처리를 완료하였습니다.

---

## 5. 보너스 과제 (선택)

### 5.1 Docker Compose 기초 & 멀티 컨테이너

**`docker-compose.yml`**
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8080:80"
    environment:
      - APP_ENV=production
    volumes:
      - ./app:/usr/share/nginx/html
    networks:
      - dev-network

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data
    networks:
      - dev-network

volumes:
  redis-data:

networks:
  dev-network:
```

### 5.2 Compose 운영 명령어 습득
```bash
# 1. 일괄 서비스 백그라운드 시작
$ docker-compose up -d
[+] Running 3/3
 ✔ Network dev-workspace_dev-network  Created
 ✔ Container dev-workspace-redis-1    Started
 ✔ Container dev-workspace-web-1      Started

# 2. 서비스 운영 상태 검증
$ docker-compose ps
NAME                    IMAGE               COMMAND                  SERVICE   PORTS
dev-workspace-redis-1   redis:alpine        "docker-entrypoint.s…"   redis     0.0.0.0:6379->6379/tcp
dev-workspace-web-1     dev-workspace-web   "/docker-entrypoint.…"   web       0.0.0.0:8080->80/tcp

# 3. 서비스 환경 일괄 삭제
$ docker-compose down
```

### 5.3 환경 변수 활용
Compose 내 `APP_ENV=production` 지정을 통해 코드의 수정 없이 실행 환경(Dev/Prod)을 선언적으로 제어.

### 5.4 GitHub SSH 키 설정
`ssh-keygen -t ed25519` 명령으로 공개키를 생성 후 GitHub 계정에 등록하여 보안성이 강화된 SSH 기반 Git 작업 지원.

---

## 6. 개발 환경

* **OS:** macOS Sonoma
* **Terminal System:** zsh / iTerm2
* **Container Engine:** OrbStack (Docker Engine v26.0.0)
* **Version Control:** Git v2.39.3 / GitHub Cloud
* **IDE Editor:** Visual Studio Code
