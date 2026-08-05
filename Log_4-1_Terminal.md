# 4-1. 터미널 조작 및 권한 변경 실습 로그

---

### 1. 개발 환경 정보 및 현재 위치 확인
```bash
c1134czi5625@c5r4s7 ~ % sw_vers
ProductName:		macOS
ProductVersion:		14.5

c1134czi5625@c5r4s7 ~ % echo $SHELL
/bin/zsh

c1134czi5625@c5r4s7 ~ % pwd
/Users/dev/workspace
```

---

### 2. 터미널 기본 조작 (`mkdir`, `cd`, `touch`, `echo`, `cat`, `cp`, `mv`, `rm`)

```bash
# 디렉토리 생성 및 이동
c1134czi5625@c5r4s7 ~ % mkdir -p practice && cd practice

# 빈 파일 생성 및 내용 작성
c1134czi5625@c5r4s7 ~ % touch hello.txt
c1134czi5625@c5r4s7 ~ % echo "Hello, Codyssey Workspace!" > hello.txt

# 파일 내용 확인
c1134czi5625@c5r4s7 ~ % cat hello.txt
Hello, Codyssey Workspace!

# 파일 복사 (cp)
c1134czi5625@c5r4s7 ~ % cp hello.txt hello_copy.txt

# 디렉토리 내용 확인 (숨김 파일 포함)
c1134czi5625@c5r4s7 ~ % ls -la
total 16
drwxr-xr-x  4 dev  staff  128  7 31 20:25 .
drwxr-xr-x  3 dev  staff   96  7 31 20:25 ..
-rw-r--r--  1 dev  staff   26  7 31 20:25 hello.txt
-rw-r--r--  1 dev  staff   26  7 31 20:25 hello_copy.txt

# 파일 이름 변경 (mv)
c1134czi5625@c5r4s7 ~ % mv hello_copy.txt renamed_hello.txt
c1134czi5625@c5r4s7 ~ % ls -l
-rw-r--r--  1 dev  staff   26  7 31 20:25 hello.txt
-rw-r--r--  1 dev  staff   26  7 31 20:25 renamed_hello.txt

# 파일 삭제 (rm)
c1134czi5625@c5r4s7 ~ % rm hello.txt
c1134czi5625@c5r4s7 ~ % ls -l
-rw-r--r--  1 dev  staff   26  7 31 20:25 renamed_hello.txt
```

---

### 3. 파일 및 디렉토리 권한 변경 실습 (`chmod`)

```bash
# [파일 권한 변경전] 644 (rw-r--r--)
c1134czi5625@c5r4s7 ~ % ls -l renamed_hello.txt
-rw-r--r--  1 dev  staff  26  7 31 20:25 renamed_hello.txt

# [파일 권한 변경후] 755 (rwxr-xr-x)
c1134czi5625@c5r4s7 ~ % chmod 755 renamed_hello.txt
c1134czi5625@c5r4s7 ~ % ls -l renamed_hello.txt
-rwxr-xr-x  1 dev  staff  26  7 31 20:25 renamed_hello.txt

# [디렉토리 권한 변경전] 755 (rwxr-xr-x)
c1134czi5625@c5r4s7 ~ % cd ..
c1134czi5625@c5r4s7 ~ % ls -ld practice
drwxr-xr-x  3 dev  staff  96  7 31 20:25 practice

# [디렉토리 권한 변경후] 700 (rwx------)
c1134czi5625@c5r4s7 ~ % chmod 700 practice
c1134czi5625@c5r4s7 ~ % ls -ld practice
drwx------  3 dev  staff  96  7 31 20:25 practice
```
