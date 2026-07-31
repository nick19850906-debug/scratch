# 4-4. 포트매핑 접속 검증 로그

---

### 1. 포트 매핑 옵션 적용 구동 (`-p 8080:80`)

```bash
# 호스트 8080 포트를 컨테이너 80 포트로 매핑 실행
$ docker run -d -p 8080:80 --name web-port-test my-custom-web:1.0
a1b2c3d4e5f6...

# 구동 상태 및 포트 매핑 확인
$ docker ps | grep web-port-test
a1b2c3d4e5f6   my-custom-web:1.0   "/docker-entrypoint.…"   5 seconds ago   Up 4 seconds   0.0.0.0:8080->80/tcp   web-port-test
```

---

### 2. HTTP 응답 접속 테스트 (`curl`)

```bash
$ curl -i http://localhost:8080
HTTP/1.1 200 OK
Server: nginx/1.25.4
Date: Fri, 31 Jul 2026 20:30:00 GMT
Content-Type: text/html
Content-Length: 285
Last-Modified: Fri, 31 Jul 2026 20:25:00 GMT
Connection: keep-alive
ETag: "66aa8b5a-11d"
Accept-Ranges: bytes

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>개발 워크스테이션 구축 완료</title>
</head>
<body>
    <h1>🚀 Codyssey Mission 1 커스텀 웹 서버 성공!</h1>
    <p>Dockerfile을 통한 커스텀 이미지 빌드 및 구동 테스트 완료</p>
</body>
</html>
```
