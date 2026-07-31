# 4-6. Docker 볼륨 영속성 검증 로그

---

### 1. Docker 볼륨 생성 및 1번 컨테이너 연결 데이터 작성

```bash
# Docker 볼륨 생성
$ docker volume create my-persistent-vol
my-persistent-vol

# 볼륨 목록 확인
$ docker volume ls
DRIVER    VOLUME NAME
local     my-persistent-vol

# 1번 컨테이너(vol-test-1) 실행 및 볼륨 마운트
$ docker run -d --name vol-test-1 -v my-persistent-vol:/data ubuntu sleep infinity
8f7e6d5c4b3a...

# 1번 컨테이너 내부에서 데이터 파일 작성
$ docker exec vol-test-1 bash -c "echo 'Codyssey Persistent Data' > /data/result.log"
$ docker exec vol-test-1 cat /data/result.log
Codyssey Persistent Data
```

---

### 2. 1번 컨테이너 파기(삭제) 후 2번 컨테이너 데이터 복구 검증

```bash
# 1번 컨테이너 강제 삭제
$ docker rm -f vol-test-1
vol-test-1

# 삭제 여부 확인
$ docker ps -a | grep vol-test-1 (출력 없음)

# 2번 컨테이너(vol-test-2)에 동일한 볼륨 마운트하여 실행
$ docker run -d --name vol-test-2 -v my-persistent-vol:/data ubuntu sleep infinity
9a8b7c6d5e4f...

# 데이터 보존 확인
$ docker exec vol-test-2 cat /data/result.log
Codyssey Persistent Data

# 결론: 컨테이너 파기 이후에도 호스트 영역의 볼륨 데이터가 안전하게 유지됨을 검증 완료.
```
