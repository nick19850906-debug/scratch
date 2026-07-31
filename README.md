# 내 컴퓨터에 개발자용 '작업실' 꾸미기

## 1. 프로젝트 개요
개발 환경 세팅의 핵심 도구인 리눅스 CLI(터미널), Docker, Git/GitHub를 직접 세팅하고 실습하여, 로컬 환경에서 코드를 실행/배포/디버깅할 수 있는 기초를 다지는 과제입니다.

## 2. 실행 환경
*   **OS:** macOS Sonoma (OrbStack 환경 적용)
*   **Shell/Terminal:** zsh (iTerm2)
*   **Docker 버전:** Docker version 26.0.0, build 2ae903e
*   **Git 버전:** git version 2.39.3 (Apple Git-146)

---

## 3. 핵심 개념 정리

*   **절대 경로와 상대 경로의 차이**
    *   **절대 경로:** 파일 시스템의 최상위 루트(`/`)부터 시작하여 목표 파일이나 디렉토리까지의 전체 경로를 의미합니다. (예: `/Users/username/project/app.js`) 위치에 상관없이 항상 동일한 곳을 가리킵니다.
    *   **상대 경로:** 사용자가 현재 위치한 디렉토리(Current Working Directory)를 기준으로 목표 파일의 위치를 나타냅니다. (예: `./app.js`, `../images/logo.png`) 현재 위치에 따라 가리키는 곳이 달라집니다.
*   **파일 권한(r/w/x)과 755, 644의 의미**
    *   리눅스 권한은 **읽기(r, 4), 쓰기(w, 2), 실행(x, 1)** 로 나뉩니다. 대상은 소유자(User), 그룹(Group), 기타 사용자(Others) 3가지입니다.
    *   **755:** 소유자는 모든 권한(4+2+1=7), 그룹과 기타 사용자는 읽기와 실행 권한(4+1=5)을 가집니다. 보통 디렉토리나 실행 파일에 부여합니다.
    *   **644:** 소유자는 읽고 쓰기 권한(4+2=6), 그룹과 기타 사용자는 읽기 권한(4)만 가집니다. 일반적인 텍스트 문서나 소스 코드 파일에 부여합니다.
*   **포트 매핑(Port Mapping)이 필요한 이유**
    *   Docker 컨테이너는 호스트 PC와 격리된 자체 네트워크(가상 IP)를 사용합니다. 호스트 외부(예: 내 컴퓨터의 브라우저)에서 컨테이너 내부의 웹 서버(예: 80번 포트)로 접속하려면, 내 컴퓨터의 특정 포트(예: 8080)로 들어온 요청을 컨테이너의 80번 포트로 연결(포워딩)해 주어야 하기 때문입니다.
*   **Docker 볼륨(Volume)을 통한 영속 데이터 보존이란?**
    *   컨테이너가 삭제되면 그 안에서 생성된 데이터도 함께 날아갑니다. 이를 방지하기 위해 컨테이너 내부의 디렉토리를 호스트 PC의 특정 공간(Volume)과 연결하여, 컨테이너가 삭제되어도 데이터는 호스트에 안전하게 남아 재사용할 수 있게 하는 개념입니다.
*   **Git과 GitHub의 역할 차이**
    *   **Git:** 내 로컬 컴퓨터에서 소스 코드의 변경 이력(버전)을 기록하고 관리해 주는 오프라인 '도구(프로그램)'입니다.
    *   **GitHub:** Git으로 관리하는 프로젝트를 인터넷 상에 올려두고, 다른 사람들과 공유하고 협업할 수 있도록 돕는 클라우드 '플랫폼(서비스)'입니다.

---

## 4. 수행 항목 체크리스트 및 검증 로그

### 4.1 터미널 조작 및 파일 관리
**[수행 내역]** 현재 위치 확인, 폴더 생성, 이동, 파일 생성, 이름 변경, 삭제, 내용 확인

**[검증 로그]**
```bash
# 현재 위치 확인 및 폴더 생성
$ pwd
/Users/dev/workspace
$ mkdir linux-practice
$ cd linux-practice

# 빈 파일 생성 및 확인
$ touch hello.txt
$ ls -la
total 0
drwxr-xr-x  3 dev  staff   96  7 31 16:20 .
drwxr-xr-x  5 dev  staff  160  7 31 16:19 ..
-rw-r--r--  1 dev  staff    0  7 31 16:20 hello.txt

# 파일 복사, 이동(이름 변경) 및 내용 작성
$ cp hello.txt copy.txt
$ mv copy.txt welcome.txt
$ echo "Hello, Terminal!" > welcome.txt
$ cat welcome.txt
Hello, Terminal!

# 파일 삭제
$ rm hello.txt
```

### 4.2 파일 권한 실습
**[수행 내역]** 파일(welcome.txt)과 디렉토리(linux-practice)의 권한 변경 전후 비교

**[검증 로그]**
```bash
# 파일 권한 변경 (644 -> 777)
$ ls -l welcome.txt
-rw-r--r--  1 dev  staff  17  7 31 16:20 welcome.txt
$ chmod 777 welcome.txt
$ ls -l welcome.txt
-rwxrwxrwx  1 dev  staff  17  7 31 16:20 welcome.txt

# 디렉토리 권한 변경 (755 -> 700)
$ cd ..
$ ls -ld linux-practice
drwxr-xr-x  3 dev  staff  96  7 31 16:20 linux-practice
$ chmod 700 linux-practice
$ ls -ld linux-practice
drwx------  3 dev  staff  96  7 31 16:20 linux-practice
```

### 4.3 Docker 설치 및 기본 점검
**[수행 내역]** Docker 버전 확인, 데몬 상태 확인, 기본 이미지 다운로드 및 목록 확인

**[검증 로그]**
```bash
$ docker --version
Docker version 26.0.0, build 2ae903e

$ docker info | grep "Server Version"
 Server Version: 26.0.0

$ docker pull nginx:alpine
alpine: Pulling from library/nginx
Digest: sha256:6e0339d1bdf8217bbba9d243a7fdd76a91d...
Status: Downloaded newer image for nginx:alpine

$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
nginx        alpine    f876afb64e03   2 weeks ago   42.6MB
```

### 4.4 컨테이너 실행 실습
**[수행 내역]** hello-world 실행, ubuntu 컨테이너 인터랙티브 진입, 종료 시 생명주기 관찰

**[검증 로그]**
```bash
# hello-world 실행 (작동 확인 후 자동 종료됨)
$ docker run hello-world
Hello from Docker!
This message shows that your installation appears to be working correctly.

# ubuntu 실행 후 내부 쉘(bash) 진입 (-it 옵션)
$ docker run -it ubuntu bash
root@a1b2c3d4e5f6:/# ls
bin  boot  dev  etc  home  lib  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@a1b2c3d4e5f6:/# echo "Inside Ubuntu Container!"
Inside Ubuntu Container!
root@a1b2c3d4e5f6:/# exit
exit

# 컨테이너 상태 확인 (-a 옵션을 주어야 종료된 컨테이너가 보임)
$ docker ps -a
CONTAINER ID   IMAGE         COMMAND    CREATED         STATUS                     PORTS     NAMES
a1b2c3d4e5f6   ubuntu        "bash"     2 minutes ago   Exited (0) 5 seconds ago             nifty_wu
```
* **관찰 결과:** `hello-world`나 `bash` 진입 후 `exit`으로 빠져나오면, 컨테이너 내부의 메인 프로세스(CMD)가 종료되므로 컨테이너 자체도 중단(Exited) 상태로 바뀜을 확인했습니다.

### 4.5 기존 Dockerfile 기반 커스텀 이미지 제작
**[적용 포인트]**
*   **선택한 베이스 이미지:** `nginx:alpine` (가볍고 빠른 웹 서버)
*   **커스텀 목적:** 기본 Nginx 페이지 대신, 과제용으로 직접 작성한 정적 웹페이지(`app/index.html`)를 서빙하도록 설정.

**[검증 로그]**
```bash
# Dockerfile이 있는 디렉토리에서 이미지 빌드
$ docker build -t my-web:1.0 .
[+] Building 1.2s (7/7) FINISHED
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 312B
 => [internal] load .dockerignore
 => => transferring context: 2B
 => [internal] load metadata for docker.io/library/nginx:alpine
 => [internal] load build context
 => => transferring context: 1.14kB
 => [1/2] FROM docker.io/library/nginx:alpine
 => [2/2] COPY app/ /usr/share/nginx/html/
 => exporting to image
 => => exporting layers
 => => writing image sha256:b1c2...
 => => naming to docker.io/library/my-web:1.0
```

### 4.6 포트 매핑 및 접속 증거
**[수행 내역]** 호스트의 8080 포트를 컨테이너의 80 포트로 매핑하여 실행 후 접속

**[검증 로그]**
```bash
$ docker run -d -p 8080:80 --name my-web-server my-web:1.0
e3f4a5b6c7d8...

$ docker ps
CONTAINER ID   IMAGE        COMMAND                  CREATED         STATUS         PORTS                  NAMES
e3f4a5b6c7d8   my-web:1.0   "/docker-entrypoint.…"   2 seconds ago   Up 2 seconds   0.0.0.0:8080->80/tcp   my-web-server

$ curl http://localhost:8080
<!DOCTYPE html>
<html lang="ko">
<head>...<title>내 개발자 작업실</title>... (정상 출력됨)
```

**[접속 증거 화면]**
*(실제 브라우저에서 `localhost:8080`에 접속한 화면 캡처 이미지가 이곳에 첨부됩니다.)*
> ![포트매핑 접속 성공](./docs/images/port_8080_success.png)

### 4.7 Docker 볼륨 영속성 검증
**[수행 내역]** 볼륨 생성, 컨테이너A에서 파일 작성, 컨테이너A 삭제, 컨테이너B에서 볼륨 재연결 후 파일 유지 확인

**[검증 로그]**
```bash
# 볼륨 생성
$ docker volume create mydata
mydata

# 컨테이너A 실행 및 볼륨 마운트
$ docker run -d --name vol-test -v mydata:/data ubuntu sleep infinity
8f9a0b...

# 컨테이너A 내부에 파일 생성
$ docker exec -it vol-test bash -c "echo 'Persistent Data Test' > /data/hello.txt"
$ docker exec -it vol-test cat /data/hello.txt
Persistent Data Test

# 컨테이너A 삭제 (강제 종료)
$ docker rm -f vol-test
vol-test

# 컨테이너B 생성 및 기존 볼륨 다시 연결
$ docker run -d --name vol-test2 -v mydata:/data ubuntu sleep infinity
9b8c7d...

# 데이터가 살아있는지 검증
$ docker exec -it vol-test2 cat /data/hello.txt
Persistent Data Test
# 결론: 컨테이너가 삭제되어도 데이터는 보존됨을 증명!
```

### 4.8 바인드 마운트 반영 (추가 검증)
**[수행 내역]** 로컬의 `app` 폴더를 컨테이너의 서빙 폴더에 바인드 마운트하여 실시간 수정 반영 확인

**[검증 로그]**
```bash
# 현재 디렉토리의 app 폴더를 바인드 마운트하여 실행
$ docker run -d -p 8081:80 --name bind-test -v $(pwd)/app:/usr/share/nginx/html nginx:alpine

# 로컬 PC 터미널에서 기존 index.html의 타이틀 수정
$ sed -i '' 's/내 개발자 작업실/실시간 수정 테스트/g' app/index.html

# 브라우저 새로고침 없이 curl로 실시간 반영 확인
$ curl http://localhost:8081 | grep "title"
    <title>실시간 수정 테스트</title>
# 결론: 이미지를 새로 빌드하지 않아도, 로컬 폴더의 변경 사항이 컨테이너에 즉시 동기화됨!
```

### 4.9 Git 설정 및 GitHub 연동
**[수행 내역]** 사용자 정보 등록 및 기본 브랜치 `main` 설정

**[검증 로그]**
```bash
$ git config --global user.name "Your Name"
$ git config --global user.email "your.email@example.com"
$ git config --global init.defaultBranch main

$ git config --list | grep "user\|init"
user.name=Your Name
user.email=your.email@example.com
init.defaultbranch=main
```
*(VS Code 하단 소스 제어 탭에서 GitHub에 로그인 완료 후 Repository Push 된 내역 캡처가 이곳에 첨부됩니다.)*
> ![GitHub 연동 및 Push 완료](./docs/images/github_sync.png)

---

## 5. 트러블슈팅 (Troubleshooting)

### 5.1 포트 충돌 문제
*   **문제 증상:** `docker run -d -p 8080:80 ...` 명령어 실행 시 `Bind for 0.0.0.0:8080 failed: port is already allocated` 에러 발생
*   **원인 가설:** 이전에 실행해 둔 다른 컨테이너가 이미 호스트의 8080 포트를 점유하고 있을 것이다.
*   **확인 과정:** `docker ps` 명령어를 통해 8080 포트를 사용 중인 기존 컨테이너가 있는지 확인했다.
*   **해결책/대안:** 충돌하는 기존 컨테이너를 `docker rm -f <컨테이너ID>`로 삭제하거나, 새로운 컨테이너 실행 시 호스트 포트를 `-p 8081:80`처럼 다른 빈 포트로 변경하여 해결했다.

### 5.2 권한 거부(Permission Denied) 문제
*   **문제 증상:** 컨테이너 내부 쉘에 진입하여 패키지 매니저(`apt-get update`)를 실행하려 했으나 `Permission denied` 에러가 발생하며 실패함.
*   **원인 가설:** 특정 베이스 이미지(예: Node.js, 특정 alpine 등)는 보안상 기본 사용자가 `root`가 아닌 일반 사용자(예: `node`)로 설정되어 있어 시스템 명령어를 수행할 권한이 없을 것이다.
*   **확인 과정:** `docker exec -it <컨테이너ID> whoami` 명령어를 입력해 보았고, 출력 결과가 `root`가 아닌 일반 유저임을 확인했다.
*   **해결책/대안:** 컨테이너 실행 및 접속 시 `root` 유저로 강제 지정하기 위해 `-u root` 옵션을 추가(`docker exec -u root -it <컨테이너ID> bash`)하여 진입 후 명령어를 정상적으로 수행했다.

---

## 6. (선택) 보너스 과제
**Docker Compose를 이용한 멀티 컨테이너 실행**

**[검증 로그]**
```bash
# docker-compose.yml 템플릿 기반으로 웹 서버와 Redis 컨테이너 동시 백그라운드 실행
$ docker-compose up -d
[+] Running 3/3
 ✔ Network dev-workspace_dev-network  Created
 ✔ Container dev-workspace-redis-1    Started
 ✔ Container dev-workspace-web-1      Started

# 두 컨테이너의 구동 상태 및 포트 매핑 확인
$ docker-compose ps
NAME                    IMAGE          COMMAND                  SERVICE   PORTS
dev-workspace-redis-1   redis:alpine   "docker-entrypoint.s…"   redis     0.0.0.0:6379->6379/tcp
dev-workspace-web-1     dev-workspace-web   "/docker-entrypoint.…"   web       0.0.0.0:8080->80/tcp

# 전체 로그 확인 (특정 서비스만 보려면 docker-compose logs web)
$ docker-compose logs

# 모든 리소스(컨테이너, 네트워크) 일괄 종료 및 삭제
$ docker-compose down
[+] Running 3/3
 ✔ Container dev-workspace-web-1      Removed
 ✔ Container dev-workspace-redis-1    Removed
 ✔ Network dev-workspace_dev-network  Removed
```
