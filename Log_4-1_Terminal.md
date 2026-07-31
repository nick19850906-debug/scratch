# 4-1. 터미널 조작 및 권한 변경 실습 로그

---

### 1. 개발 환경 정보 및 현재 위치 확인
```bash
$ sw_vers
ProductName:		macOS
ProductVersion:		14.5

$ echo $SHELL
/bin/zsh

$ pwd
/Users/dev/workspace
```

---

### 2. 터미널 기본 조작 (`mkdir`, `cd`, `touch`, `echo`, `cat`, `cp`, `mv`, `rm`)

```bash
# 디렉토리 생성 및 이동
$ mkdir -p practice && cd practice

# 빈 파일 생성 및 내용 작성
$ touch hello.txt
$ echo "Hello, Codyssey Workspace!" > hello.txt

# 파일 내용 확인
$ cat hello.txt
Hello, Codyssey Workspace!

# 파일 복사 (cp)
$ cp hello.txt hello_copy.txt

# 디렉토리 내용 확인 (숨김 파일 포함)
$ ls -la
total 16
drwxr-xr-x  4 dev  staff  128  7 31 20:25 .
drwxr-xr-x  3 dev  staff   96  7 31 20:25 ..
-rw-r--r--  1 dev  staff   26  7 31 20:25 hello.txt
-rw-r--r--  1 dev  staff   26  7 31 20:25 hello_copy.txt

# 파일 이름 변경 (mv)
$ mv hello_copy.txt renamed_hello.txt
$ ls -l
-rw-r--r--  1 dev  staff   26  7 31 20:25 hello.txt
-rw-r--r--  1 dev  staff   26  7 31 20:25 renamed_hello.txt

# 파일 삭제 (rm)
$ rm hello.txt
$ ls -l
-rw-r--r--  1 dev  staff   26  7 31 20:25 renamed_hello.txt
```

---

### 3. 파일 및 디렉토리 권한 변경 실습 (`chmod`)

```bash
# [파일 권한 변경전] 644 (rw-r--r--)
$ ls -l renamed_hello.txt
-rw-r--r--  1 dev  staff  26  7 31 20:25 renamed_hello.txt

# [파일 권한 변경후] 755 (rwxr-xr-x)
$ chmod 755 renamed_hello.txt
$ ls -l renamed_hello.txt
-rwxr-xr-x  1 dev  staff  26  7 31 20:25 renamed_hello.txt

# [디렉토리 권한 변경전] 755 (rwxr-xr-x)
$ cd ..
$ ls -ld practice
drwxr-xr-x  3 dev  staff  96  7 31 20:25 practice

# [디렉토리 권한 변경후] 700 (rwx------)
$ chmod 700 practice
$ ls -ld practice
drwx------  3 dev  staff  96  7 31 20:25 practice
```
