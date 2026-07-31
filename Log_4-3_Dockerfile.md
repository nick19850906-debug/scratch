# 4-3. Dockerfile 기반 커스텀 이미지 제작 로그

---

### 1. 웹 서버 소스 코드 및 Dockerfile 준비

**`app/index.html`**
```html
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

**`Dockerfile`**
```dockerfile
FROM nginx:alpine
LABEL maintainer="student@example.com"
LABEL org.opencontainers.image.title="my-custom-web"

ENV APP_ENV=development

# 로컬 app 디렉토리를 컨테이너 Nginx 웹 서빙 경로로 복사
COPY app/ /usr/share/nginx/html/

EXPOSE 80
```

---

### 2. 커스텀 이미지 빌드 실행 로그

```bash
$ docker build -t my-custom-web:1.0 .
[+] Building 1.1s (7/7) FINISHED
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 240B
 => [internal] load .dockerignore
 => => transferring context: 2B
 => [internal] load metadata for docker.io/library/nginx:alpine
 => [internal] load build context
 => => transferring context: 1.2kB
 => [1/2] FROM docker.io/library/nginx:alpine
 => [2/2] COPY app/ /usr/share/nginx/html/
 => exporting to image
 => => exporting layers
 => => writing image sha256:b1c2d3e4f5a6...
 => => naming to docker.io/library/my-custom-web:1.0

# 빌드된 커스텀 이미지 확인
$ docker images | grep my-custom-web
my-custom-web   1.0       b1c2d3e4f5a6   15 seconds ago   42.6MB
```
