# 🖥️ 내 컴퓨터에 개발자용 '작업실' 꾸미기

---

## 📁 미션 원문 목차(1~6) 기반 파일트리 (File Tree)

본 저장소의 파일 구조는 미션 원문의 대항목(1~6)에 1:1로 대응되도록 구성되었습니다.

```text
dev-workspace/
├── 📄 README.md                        # [통합 보고서] 미션 1~6 전체 요구사항 기술 문서
│
├── 📂 1_미션_소개/                      # [미션 1] 개요 및 서울캠퍼스 보안 정책
│   └── orbstack_setup.md               # OrbStack (sudo 권한 없는 Docker 구동) 환경 설정
│
├── 📂 2_최종_결과물/                    # [미션 2] 커스텀 웹 서버 소스 코드
│   ├── Dockerfile                      # Nginx 베이스 커스텀 이미지 정의 파일
│   └── app/
│       └── index.html                  # 서빙 확인용 메인 HTML
│
├── 📂 3_과제_목표_핵심개념/             # [미션 3] 6대 핵심 기술 개념 정리
│   └── concepts_summary.md             # 절대/상대경로, 권한, 포트매핑, 볼륨, Git/GitHub
│
├── 📂 4_기능_요구_사항/                 # [미션 4] 기능 요구사항 수행 로그 & 검증 증거
│   ├── 4.1_4.2_terminal_permission.log # 터미널 조작 및 chmod 권한 변경 로그
│   ├── 4.3_4.5_docker_operation.log    # docker info, ps, logs, stats, ubuntu 실습 로그
│   └── proof_images/                   # 검증 완료 증거 스크린샷 모음
│       ├── port_mapping_proof.png      # 포트 매핑(-p 8080:80) 접속 증거
│       ├── volume_persistence.png      # Docker 볼륨 영속성 검증 증거
│       └── git_github_sync.png         # Git 설정 & VSCode GitHub 연동 증거
│
├── 📂 5_보너스_과제/                    # [미션 5] 선택 보너스 과제
│   └── docker-compose.yml              # Nginx + Redis 멀티 컨테이너 구성
│
└── 📂 6_개발_환경/                      # [미션 6] 시스템 사양 및 런타임 환경
    └── environment_spec.md             # OS, Shell, Docker, Git 버전 정보
```

---

## 1. 미션 소개

* **개요:** 리눅스 CLI, Docker, Git/GitHub 환경을 구축하여 재현 가능한 개발 워크스테이션을 세팅합니다.
* **OrbStack 활용 (서울캠퍼스):** `sudo` 권한이 제한되는 환경 정책을 준수하기 위해 별도 root 권한 없이 작동하는 OrbStack으로 Docker 데몬을 구동합니다.

---

## 2. 최종 결과물

| 구분 | 주요 제출물 | 결과 위치 |
| :--- | :--- | :--- |
| **저장소 & 기술문서** | GitHub 공개 저장소 & README.md | `README.md` |
| **웹 서버 컨테이너** | Dockerfile & `app/index.html` | `2_최종_결과물/` |
| **실습/검증 로그** | 터미널 조작, 권한 변경, Docker 운영 로그 | `4_기능_요구_사항/` |
| **증거 스크린샷** | 포트 매핑 접속, 볼륨 영속성, Git 연동 증거 | `4_기능_요구_사항/proof_images/` |

---

## 3. 과제 목표 (핵심 개념 정리)

* **절대 경로 vs 상대 경로:** 루트(`/`) 기준 고정 위치 vs 현재 디렉토리 기준 상대 위치
* **파일 권한 (755 vs 644):** `755`(소유자 7/그룹 5/기타 5, 디렉토리용) vs `644`(소유자 6/그룹 4/기타 4, 문서용)
* **커스텀 이미지:** `nginx:alpine` 위에 `COPY app/` 소스를 얹어 재현 가능한 전용 이미지 빌드
* **포트 매핑:** 격리된 컨테이너 내부 포트(80)를 호스트 포트(8080)와 연결하여 외부 접속 허용
* **Docker 볼륨:** 무상태(Stateless) 컨테이너가 파기되어도 호스트 영역에 데이터를 유지하는 보존 디바이스
* **Git vs GitHub:** 로컬 분산 버전 관리 도구(Git) vs 원격 공유/협업 클라우드 플랫폼(GitHub)

---

## 4. 기능 요구 사항 (수행 로그 및 검증)

### 4.1 터미널 조작 로그
```bash
$ pwd && mkdir -p practice-cli && cd practice-cli
$ touch test.txt && echo "Hello Workspace" > test.txt
$ cp test.txt copy.txt && mv copy.txt renamed.txt && rm test.txt
```

### 4.2 권한 실습 (`chmod`)
```bash
# 파일 권한 644 -> 755
$ chmod 755 renamed.txt && ls -l renamed.txt
-rwxr-xr-x  1 dev  staff  16  7 31 17:31 renamed.txt

# 디렉토리 권한 755 -> 700
$ chmod 700 ../practice-cli && ls -ld ../practice-cli
drwx------  3 dev  staff  96  7 31 17:31 ../practice-cli
```

### 4.3 Docker 설치 및 기본 점검
```bash
$ docker --version
Docker version 26.0.0, build 2ae903e
$ docker info | grep "Server Version"
 Server Version: 26.0.0
```

### 4.4 Docker 기본 운영 명령
```bash
$ docker pull nginx:alpine
$ docker run -d --name basic-nginx -p 8080:80 nginx:alpine
$ docker ps && docker logs basic-nginx && docker stats --no-stream basic-nginx
$ docker stop basic-nginx
```

### 4.5 컨테이너 실행 실습 (`hello-world` & `ubuntu`)
```bash
$ docker run hello-world
$ docker run -it ubuntu bash -c "ls && echo 'Inside Ubuntu' && exit"
```

### 4.6 Dockerfile 기반 커스텀 이미지 제작
```dockerfile
FROM nginx:alpine
ENV APP_ENV=development
COPY app/ /usr/share/nginx/html/
EXPOSE 80
```
```bash
$ docker build -t my-custom-web:1.0 .
```

### 4.7 포트 매핑 접속 증거
```bash
$ docker run -d -p 8080:80 --name custom-web my-custom-web:1.0
$ curl -i http://localhost:8080
HTTP/1.1 200 OK
...
<h1>🚀 Docker 커스텀 웹 서버 구동 성공!</h1>
```

### 4.8 Docker 볼륨 영속성 검증
```bash
$ docker volume create mydata
$ docker run -d --name vol1 -v mydata:/data ubuntu sleep infinity
$ docker exec vol1 bash -c "echo 'Persistent Data' > /data/test.log"
$ docker rm -f vol1

$ docker run -d --name vol2 -v mydata:/data ubuntu sleep infinity
$ docker exec vol2 cat /data/test.log
Persistent Data
```

### 4.9 Git 설정 및 GitHub 연동
```bash
$ git config --global user.name "nick19850906-debug"
$ git config --global user.email "student@example.com"
$ git config --global init.defaultBranch main
$ git remote -v
origin	https://github.com/nick19850906-debug/scratch.git (fetch)
```

### 4.10 보안 및 개인정보 보호
> [!IMPORTANT]  
> 본 보고서 및 로그 내 토큰, 비밀번호, 개인키 등 민감정보 전수 마스킹 점검 완료.

---

## 5. 보너스 과제 (선택)

### 5.1 Docker Compose (`docker-compose.yml`)
```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8080:80"
    environment:
      - APP_ENV=production
    networks:
      - dev-network
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    networks:
      - dev-network
networks:
  dev-network:
```

### 5.2 Compose 운영 명령
```bash
$ docker-compose up -d
$ docker-compose ps
$ docker-compose down
```

---

## 6. 개발 환경

* **OS / Shell:** macOS Sonoma / zsh
* **Container Engine:** OrbStack (Docker Engine v26.0.0)
* **Tools:** Git v2.39.3 / Visual Studio Code
