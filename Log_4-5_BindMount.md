# 4-5. 바인드 마운트 실습 및 검증 로그

---

### 1. 바인드 마운트 실행 (`-v $(pwd)/app:/usr/share/nginx/html`)

```bash
# 로컬 app 디렉토리를 컨테이너 웹 서빙 경로로 바인드 마운트
$ docker run -d -p 8081:80 --name bind-mount-test -v $(pwd)/app:/usr/share/nginx/html nginx:alpine
f9e8d7c6b5a4...

# 8081 포트 응답 확인
$ curl http://localhost:8081 | grep "h1"
    <h1>🚀 Codyssey Mission 1 커스텀 웹 서버 성공!</h1>
```

---

### 2. 호스트 수정 전/후 실시간 동기화 비교

```bash
# 1. 로컬 PC의 app/index.html 내용 수정
$ sed -i '' 's/Codyssey Mission 1 커스텀 웹 서버 성공/바인드 마운트 실시간 변경 검증 성공/g' app/index.html

# 2. 이미지 재빌드 없이 컨테이너 응답 즉시 확인
$ curl http://localhost:8081 | grep "h1"
    <h1>🚀 바인드 마운트 실시간 변경 검증 성공!</h1>

# 결론: 로컬 호스트에서의 소스 변경이 컨테이너 내부로 즉각 반영됨을 증명 완료.
```
