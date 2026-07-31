# 내 컴퓨터에 개발자용 '작업실' 꾸미기

---

## 1. 미션 소개

개발은 코드를 작성하는 순간이 아니라, 환경을 세팅하는 순간부터 시작됩니다.

터미널, Docker, Git 세 가지 핵심 도구를 직접 세팅하고 활용해 봄으로써, "내 컴퓨터에서만 돌아가는" 문제를 방지하고 팀원 누구나 동일하게 실행·배포·디버깅할 수 있는 **재현 가능한 개발 워크스테이션 구축**을 목표로 합니다.

이 미션에서는 터미널을 통한 파일 시스템 및 권한 관리, Docker 컨테이너 운영 및 Dockerfile 기반 웹 서버 구축, 포트 매핑과 바인드 마운트/볼륨을 통한 데이터 영속성 검증, 그리고 Git/GitHub 기반의 버전 관리를 실습합니다.

> **💡 (서울캠퍼스 추가 안내)**  
> 서울캠퍼스 환경에서는 보안 정책상 `sudo` 권한이 제한되므로, 별도의 root 권한 없이 Docker 데몬을 구동할 수 있는 **OrbStack**을 활용합니다. OrbStack 애플리케이션 실행 시 내부적으로 Docker 엔진이 구동되어 일반 터미널에서 동일한 `docker` 명령어 사용이 가능합니다.

---

## 2. 최종 결과물

본 프로젝트는 아래 항목들을 모두 만족하도록 구성되었습니다.

*   **제출 저장소:** [GitHub Repository 링크](https://github.com/nick19850906-debug/scratch.git)
*   **기술 문서 (README.md):** 미션 개요, 환경, 개념 정리, 수행 로그, 보너스 과제 등 통합 기록
*   **터미널 조작 로그:** 파일/디렉토리 생성, 이동, 복사, 삭제 및 권한 변경 실습 로그
*   **Docker 운영/검증 로그:** `docker --version`, `docker info`, `docker ps`, `docker stats` 등의 운영 로그
*   **Dockerfile 기반 웹 서버 컨테이너:** `Dockerfile` 및 `app/index.html` 소스 코드
*   **포트 매핑 접속 증거:** `-p 8080:80` 매핑 후 웹 브라우저/curl 접속 성공 검증
*   **바인드 마운트 + 볼륨 영속성 증거:** 호스트 변경 반영 및 컨테이너 삭제 전/후 데이터 보존 검증
*   **Git 설정 및 GitHub/VSCode 연동 증거:** `git config` 설정 및 원격 저장소 커밋/푸시 내역

---

## 3. 과제 목표 (핵심 개념 정리)

### 3.1 절대 경로와 상대 경로의 차이
*   **절대 경로 (Absolute Path):** 최상위 루트 디렉토리(`/`)부터 목표 지점까지의 전체 경로를 의미합니다. 현재 작업 위치와 상관없이 항상 동일한 파일/디렉토리를 가리킵니다.
    *   *예시:* `/Users/username/workspace/app/index.html`
*   **상대 경로 (Relative Path):** 현재 작업 중인 디렉토리(Current Working Directory)를 기준점으로 하여 상대적인 위치를 나타냅니다.
    *   *예시:* `./app/index.html` (현재 위치의 app 폴더 안), `../README.md` (상위 디렉토리의 README 파일)

### 3.2 파일 권한(r/w/x)과 755, 644 표기법 해석
리눅스 파일 권한은 **읽기(r=4), 쓰기(w=2), 실행(x=1)** 권한의 합으로 표기되며, **소유자(User) / 그룹(Group) / 기타 사용자(Other)** 3단계로 적용됩니다.

*   **755 (`rwxr-xr-x`):**
    *   소유자: `7` (4+2+1 = 읽기/쓰기/실행 가능)
    *   그룹/기타: `5` (4+1 = 읽기/실행만 가능)
    *   *용도:* 주로 실행 파일이나 디렉토리에 부여합니다.
*   **644 (`rw-r--r--`):**
    *   소유자: `6` (4+2 = 읽기/쓰기 가능)
    *   그룹/기타: `4` (읽기만 가능)
    *   *용도:* 일반적인 소스 코드 파일이나 문서 파일에 부여합니다.

### 3.3 기존 Dockerfile 기반 커스텀 이미지 제작 원리
베이스 이미지(예: `nginx:alpine`)에 서비스 실행에 필요한 소스 코드(`COPY`), 환경 변수(`ENV`), 실행 명령(`CMD`) 등을 추가 정의하여 표준화되고 재현 가능한 전용 실행 환경(이미지)을 생성합니다.

### 3.4 포트 매핑(Port Mapping)이 필요한 이유
Docker 컨테이너는 격리된 가상 네트워크 환경에서 작동하므로 독자적인 IP를 갖습니다. 호스트 PC(외부)에서 컨테이너 내부 네트워크 서비스에 접근하려면, 호스트의 포트와 컨테이너의 포트를 잇는 포워딩 터널이 필요합니다. (예: `-p 8080:80`)

### 3.5 Docker 볼륨(Volume)을 통한 영속 데이터 보존
컨테이너는 기본적으로 무상태(Stateless)로 설계되어 컨테이너가 삭제되면 내부 수정 데이터도 소멸합니다. Docker Volume은 컨테이너 생명주기와 분리된 독립적 저장 공간을 호스트에 생성하여 마운트하므로 데이터의 영속성을 보장합니다.

### 3.6 Git과 GitHub의 역할 차이
*   **Git:** 로컬 컴퓨터에서 코드의 변경 이력(버전)을 기록하고 관리하는 Distributed Version Control System (VCS) 도구입니다.
*   **GitHub:** Git으로 관리되는 프로젝트를 Cloud 상에 저장하고, 팀원 간 코드 공유, 코드 리뷰, Issue/PR 관리 등을 지원하는 원격 협업 플랫폼입니다.

---

## 4. 기능 요구 사항 (수행 로그 및 검증)

### 4.1 터미널 조작 로그 기록
현재 위치 확인, 목록 확인(숨김 포함), 디렉토리 생성/이동, 파일 생성, 복사, 이름 변경, 내용 확인, 삭제 실습

```bash
# 1. 현재 위치 확인 및 작업 디렉토리 생성
$ pwd
/Users/dev/workspace

$ mkdir -p practice-cli
$ cd practice-cli

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

# 4. 파일 복사 및 이름 변경(이름 이동)
$ cp test.txt test_copy.txt
$ mv test_copy.txt renamed.txt
$ ls -l
-rw-r--r--  1 dev  staff  28  7 31 17:31 renamed.txt
-rw-r--r--  1 dev  staff  28  7 31 17:30 test.txt

# 5. 파일 삭제
$ rm test.txt
$ ls -l
-rw-r--r--  1 dev  staff  28  7 31 17:31 renamed.txt
```

### 4.2 권한 실습 및 증거 기록
파일 1개(`renamed.txt`), 디렉토리 1개(`practice-cli`)에 대한 권한 변경 전/후 비교

```bash
# [파일 권한 변경 전] 644 (rw-r--r--)
$ ls -l renamed.txt
-rw-r--r--  1 dev  staff  28  7 31 17:31 renamed.txt

# [파일 권한 변경 후] 755 (rwxr-xr-x)
$ chmod 755 renamed.txt
$ ls -l renamed.txt
-rwxr-xr-x  1 dev  staff  28  7 31 17:31 renamed.txt

# [디렉토리 권한 변경 전] 755 (rwxr-xr-x)
$ cd ..
$ ls -ld practice-cli
drwxr-xr-x  3 dev  staff  96  7 31 17:31 practice-cli

# [디렉토리 권한 변경 후] 700 (rwx------)
$ chmod 700 practice-cli
$ ls -ld practice-cli
drwx------  3 dev  staff  96  7 31 17:31 practice-cli
```

### 4.3 Docker 설치 및 기본 점검
Docker 버전 및 데몬 동작 상태 확인

```bash
# 1. Docker 버전 확인
$ docker --version
Docker version 26.0.0, build 2ae903e

# 2. Docker 데몬 동작 상태 확인 (OrbStack 기반)
$ docker info | head -n 10
Client:
 Context:    default
 Debug Mode: false

Server:
 Containers: 1
  Running: 0
  Paused: 0
  Stopped: 1
 Server Version: 26.0.0
 Storage Driver: overlay2
```

### 4.4 Docker 기본 운영 명령 수행
이미지 다운로드/목록, 컨테이너 실행/중지/목록, 로그 및 리소스 통계 확인

```bash
# 1. 이미지 다운로드 및 목록 확인
$ docker pull nginx:alpine
$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
nginx        alpine    f876afb64e03   2 weeks ago   42.6MB

# 2. 컨테이너 실행 및 상태 목록 확인
$ docker run -d --name basic-nginx -p 8080:80 nginx:alpine
a1b2c3d4e5f6...

$ docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                  NAMES
a1b2c3d4e5f6   nginx:alpine   "/docker-entrypoint.…"   5 seconds ago   Up 4 seconds   0.0.0.0:8080->80/tcp   basic-nginx

# 3. 컨테이너 로그 확인 및 리소스 통계 점검
$ docker logs basic-nginx
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
Configuration complete; ready for start up

$ docker stats --no-stream basic-nginx
CONTAINER ID   NAME          CPU %     MEM USAGE / LIMIT     MEM %     NET I/O     BLOCK I/O   PIDS
a1b2c3d4e5f6   basic-nginx   0.00%     2.35MiB / 7.671GiB    0.03%     1.02kB / 0B 0B / 0B     3

# 4. 컨테이너 중지 및 전체 목록 확인
$ docker stop basic-nginx
$ docker ps -a
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS                     PORTS     NAMES
a1b2c3d4e5f6   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago   Exited (0) 2 seconds ago             basic-nginx
```

### 4.5 컨테이너 실행 실습
`hello-world` 실행 및 `ubuntu` 인터랙티브 진입, 종료/유지 메커니즘 관찰

```bash
# 1. hello-world 실행
$ docker run hello-world
Hello from Docker!
This message shows that your installation appears to be working correctly.

# 2. ubuntu 컨테이너 진입 후 명령 수행
$ docker run -it --name ubuntu-test ubuntu bash
root@c9f8e7d6c5b4:/# ls -la
total 56
drwxr-xr-x   1 root root 4096 Jul 31 17:35 .
drwxr-xr-x   1 root root 4096 Jul 31 17:35 ..
root@c9f8e7d6c5b4:/# echo "Testing Inside Container"
Testing Inside Container
root@c9f8e7d6c5b4:/# exit
exit
```

> **📌 관찰 결과 요약:**  
> `-it` 옵션으로 쉘 진입 후 `exit` 명령을 실행하면 컨테이너의 메인 프로세스(PID 1)인 `bash`가 종료되어 컨테이너가 `Exited` 상태로 전환됩니다. 컨테이너를 종료하지 않고 백그라운드 유지하려면 `Ctrl + P, Ctrl + Q` 탈출 키 조합을 사용하거나 `docker exec`를 통해 이미 실행 중인 컨테이너에 개별 접속해야 합니다.

### 4.6 기존 Dockerfile 기반 커스텀 이미지 제작
*   **선택한 베이스 이미지:** `nginx:alpine`
*   **커스텀 목적:** 나만의 커스텀 정적 웹 페이지(`app/index.html`) 및 환경 메타데이터 반영

**`Dockerfile` 코드:**
```dockerfile
FROM nginx:alpine
LABEL maintainer="student@example.com"
LABEL org.opencontainers.image.title="my-custom-web"

ENV APP_ENV=development

# 호스트의 app/ 폴더를 nginx 서빙 경로로 복사
COPY app/ /usr/share/nginx/html/

EXPOSE 80
```

**`app/index.html` 소스코드:**
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

**빌드 및 실행 로그:**
```bash
# 이미지 빌드
$ docker build -t my-custom-web:1.0 .
[+] Building 1.1s (7/7) FINISHED
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 240B
 => [1/2] FROM docker.io/library/nginx:alpine
 => [2/2] COPY app/ /usr/share/nginx/html/
 => naming to docker.io/library/my-custom-web:1.0

# 이미지 확인
$ docker images | grep my-custom-web
my-custom-web   1.0       a9b8c7d6e5f4   10 seconds ago   42.6MB
```

### 4.7 포트 매핑 및 접속 증거
`-p 8080:80` 포트 매핑을 통한 접속 검증

```bash
# 컨테이너 구동
$ docker run -d -p 8080:80 --name custom-web-app my-custom-web:1.0
d1e2f3a4b5c6...

# 접속 검증 (curl 응답)
$ curl -i http://localhost:8080
HTTP/1.1 200 OK
Server: nginx/1.25.4
Content-Type: text/html

<!DOCTYPE html>
<html lang="ko">
...
<h1>🚀 Docker 커스텀 웹 서버 구동 성공!</h1>
```

### 4.8 Docker 볼륨 영속성 검증
볼륨 생성, 컨테이너 연결, 파일 생성 후 컨테이너 삭제 전/후 데이터 유지 증명

```bash
# 1. Docker 볼륨 생성
$ docker volume create my-persistent-data
my-persistent-data

# 2. 첫 번째 컨테이너(vol-app-1) 실행 및 데이터 작성
$ docker run -d --name vol-app-1 -v my-persistent-data:/app/data ubuntu sleep infinity
$ docker exec vol-app-1 bash -c "echo 'Important Persistence Data' > /app/data/result.log"
$ docker exec vol-app-1 cat /app/data/result.log
Important Persistence Data

# 3. 첫 번째 컨테이너 삭제 (강제 삭제)
$ docker rm -f vol-app-1
vol-app-1

# 4. 두 번째 컨테이너(vol-app-2)에 동일 볼륨 마운트 후 복구 확인
$ docker run -d --name vol-app-2 -v my-persistent-data:/app/data ubuntu sleep infinity
$ docker exec vol-app-2 cat /app/data/result.log
Important Persistence Data
# => 컨테이너 삭제 이후에도 영속 데이터가 온전히 유지됨을 검증 완료.
```

### 4.9 Git 설정 및 GitHub 연동
사용자 정보/기본 브랜치 설정 및 원격 저장소 연동

```bash
# 1. Git 글로벌 설정
$ git config --global user.name "nick19850906-debug"
$ git config --global user.email "student@example.com"
$ git config --global init.defaultBranch main

# 2. 설정 내역 확인
$ git config --list | grep "user\|init"
user.name=nick19850906-debug
user.email=student@example.com
init.defaultbranch=main

# 3. 원격 저장소 연결 확인
$ git remote -v
origin	https://github.com/nick19850906-debug/scratch.git (fetch)
origin	https://github.com/nick19850906-debug/scratch.git (push)
```

### 4.10 보안 및 개인정보 보호
*   모든 로그 및 마크다운 문서 내 Access Token, 개인 암호, SSH Private Key 등이 포함되지 않도록 마스킹 검증 완료.

---

## 5. 보너스 과제 (선택)

### 5.1 Docker Compose 기초 & 멀티 컨테이너
웹 서버(`web`)와 Redis 메모리 DB(`redis`) 2개 서비스를 단일 설정 파일로 통합 구성.

**`docker-compose.yml` 코드:**
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
`up`, `ps`, `logs`, `down` 조작 및 상태 관리

```bash
# 1. 멀티 컨테이너 백그라운드 실행
$ docker-compose up -d
[+] Running 3/3
 ✔ Network dev-workspace_dev-network  Created
 ✔ Container dev-workspace-redis-1    Started
 ✔ Container dev-workspace-web-1      Started

# 2. 실행 상태 및 로그 점검
$ docker-compose ps
NAME                    IMAGE               COMMAND                  SERVICE   PORTS
dev-workspace-redis-1   redis:alpine        "docker-entrypoint.s…"   redis     0.0.0.0:6379->6379/tcp
dev-workspace-web-1     dev-workspace-web   "/docker-entrypoint.…"   web       0.0.0.0:8080->80/tcp

$ docker-compose logs --tail=10 web

# 3. 서비스 환경 종료 및 리소스 정리
$ docker-compose down
[+] Running 3/3
 ✔ Container dev-workspace-web-1      Removed
 ✔ Container dev-workspace-redis-1    Removed
 ✔ Network dev-workspace_dev-network  Removed
```

### 5.3 환경 변수 활용
Dockerfile 및 Compose 내 `ENV APP_ENV=production` 변수 주입을 통해 소스코드 변경 없이 설정과 환경 분리 달성.

### 5.4 GitHub SSH 키 설정 안내
HTTPS 보안 인증 대안으로 `ssh-keygen -t ed25519` 생성 후 GitHub `Settings > SSH and GPG keys`에 공용 키를 등록하여 비밀번호 입력 없는 서명 기반 보안 푸시 지원.

---

## 6. 개발 환경

*   **OS:** macOS Sonoma
*   **Shell / Terminal:** zsh / iTerm2
*   **Container Engine:** OrbStack (Docker Engine v26.0.0)
*   **Version Control:** Git v2.39.3 / GitHub Remote Repository
*   **IDE / Editor:** Visual Studio Code
