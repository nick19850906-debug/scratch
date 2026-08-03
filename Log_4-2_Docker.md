# 4-2. Docker 운영 및 점검 실습 로그

---

### 1. Docker 설치 및 데몬 정보 확인

```bash
# Docker 버전 점검
$ docker --version
Docker version 26.0.0, build 2ae903e

# Docker 데몬 상태 확인 (OrbStack)
$ docker info
Client:
 Context:    default
 Debug Mode: false

Server:
 Containers: 1
  Running: 0
  Paused: 0
  Stopped: 1
 Images: 2
 Server Version: 26.0.0
 Storage Driver: overlay2
 Logging Driver: json-file
 Cgroup Driver: cgroupfs
 Kernel Version: 6.6.13-orbstack
 Operating System: OrbStack OS
```

---

### 2. 기본 Docker 이미지 조작 (`pull`, `images`, `run`, `ps`, `logs`, `stats`, `stop`)

```bash
# 베이스 이미지 다운로드
$ docker pull nginx:alpine
alpine: Pulling from library/nginx
Digest: sha256:6e0339d1bdf8217bbba9d243a7fdd76a91d...
Status: Downloaded newer image for nginx:alpine

# 다운로드된 이미지 목록 확인
$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
nginx        alpine    f876afb64e03   3 days ago   42.6MB

# 컨테이너 구동
$ docker run -d --name test-nginx -p 8080:80 nginx:alpine
e3f4a5b6c7d8...

# 구동 중인 컨테이너 상태 확인
$ docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                  NAMES
e3f4a5b6c7d8   nginx:alpine   "/docker-entrypoint.…"   4 seconds ago   Up 3 seconds   0.0.0.0:8080->80/tcp   test-nginx

# 컨테이너 로그 트레이싱
$ docker logs test-nginx
/docker-entrypoint.sh: Configuration complete; ready for start up

# 컨테이너 리소스 모니터링
$ docker stats --no-stream test-nginx
CONTAINER ID   NAME         CPU %     MEM USAGE / LIMIT     MEM %
e3f4a5b6c7d8   test-nginx   0.00%     2.35MiB / 7.671GiB    0.03%

# 컨테이너 종료 및 삭제
$ docker stop test-nginx && docker rm test-nginx
```

---

### 3. `hello-world` 및 `ubuntu` 인터랙티브 진입 실습

```bash
# 1. hello-world 컨테이너 실행
$ docker run hello-world
Hello from Docker!
This message shows that your installation appears to be working correctly.

# 2. ubuntu 컨테이너 진입 및 내부 조작 (-it 옵션)
$ docker run -it --name ubuntu-practice ubuntu bash
root@a1b2c3d4e5f6:/# pwd
/
root@a1b2c3d4e5f6:/# ls -la
total 56
drwxr-xr-x   1 root root 4096 Jul 31 20:30 .
drwxr-xr-x   1 root root 4096 Jul 31 20:30 ..
root@c9f8e7d6c5b4:/# echo "Inside Ubuntu Container!"
Inside Ubuntu Container!
root@c9f8e7d6c5b4:/# exit
exit

# 종료 후 컨테이너 상태 점검 (-a)
$ docker ps -a | grep ubuntu-practice
a1b2c3d4e5f6   ubuntu   "bash"   2 minutes ago   Exited (0) 5 seconds ago   ubuntu-practice
```
