# 4-7. Git 설정 및 GitHub/VSCode 연동 로그

---

### 1. Git 글로벌 설정 및 브랜치 지정

```bash
# 사용자 프로필 설정
$ git config --global user.name "nick19850906-debug"
$ git config --global user.email "student@example.com"

# 기본 브랜치 main 지정
$ git config --global init.defaultBranch main

# 설정 내역 점검
$ git config --list | grep "user\|init"
user.name=nick19850906-debug
user.email=student@example.com
init.defaultbranch=main
```

---

### 2. 저장소 초기화, 원격 바인딩 및 커스텀/푸시 로그

```bash
# Git 초기화 및 커밋
$ git init
$ git add .
$ git commit -m "Initial commit: Codyssey Mission 1 개발 워크스테이션 구축 완료"

# 원격 저장소 매핑
$ git remote add origin https://github.com/nick19850906-debug/scratch.git
$ git branch -M main

# 원격 저장소 정보 확인
$ git remote -v
origin	https://github.com/nick19850906-debug/scratch.git (fetch)
origin	https://github.com/nick19850906-debug/scratch.git (push)

# GitHub 푸시 완료
$ git push -u origin main
Branch 'main' set up to track remote branch 'main' from 'origin'.
Everything up-to-date
```
