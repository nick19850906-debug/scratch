FROM nginx:alpine
# 작성자 또는 이미지 메타데이터
LABEL maintainer="student@example.com"
LABEL org.opencontainers.image.title="my-custom-web"

# 컨테이너 내에서 사용할 환경변수 (예시)
ENV APP_ENV=development

# 로컬의 app 디렉토리 안의 파일들을 nginx의 기본 서빙 경로로 복사
COPY app/ /usr/share/nginx/html/

# 컨테이너가 80번 포트를 리스닝한다는 것을 명시
EXPOSE 80

# 베이스 이미지에 이미 CMD["nginx", "-g", "daemon off;"] 가 포함되어 있으므로 생략 가능
