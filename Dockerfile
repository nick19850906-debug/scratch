# ============================================================
# Dockerfile
# 목적: NGINX 기반 커스텀 웹 서버 이미지 빌드 명세서
# 작성자: nick19850906-debug | 루키마리너 2기
# ============================================================

FROM nginx:alpine

# 작성자 및 이미지 메타데이터
LABEL maintainer="nick19850906-debug"
LABEL org.opencontainers.image.title="my-custom-web"

# 컨테이너 환경변수
ENV APP_ENV=development

# 로컬 app 디렉토리 소스를 NGINX 기본 서빙 경로로 복사
COPY app/ /usr/share/nginx/html/

# 포트 선언
EXPOSE 80
