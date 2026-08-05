# 🐣 초보자를 위한 파이썬 & Git 퀴즈 게임 제작 친절 가이드 (`beginner_guide.md`)

> **"환영합니다! 코딩이 처음이어도 전혀 걱정하지 마세요. 멘토와 함께 한 단계씩 따라하다 보면 나만의 멋진 퀴즈 게임과 GitHub 저장소가 완성됩니다!"** 💖

---

## 📋 전체 미션 진행 상황 체크리스트

코딩을 진행하면서 완성한 단계의 `[ ]`를 `[x]`로 체크하며 성취감을 느껴보세요!

- [ ] **[Step 1]** 개발 준비 & 저장소 만들기 (`git init`) - **Commit #1**
- [ ] **[Step 2]** 퀴즈 붕어빵 틀 만들기 (`Quiz` 클래스) - **Commit #2**
- [ ] **[Step 3]** 기본 퀴즈 5개 준비하기 - **Commit #3**
- [ ] **[Step 4]** 게임 대문(메뉴)과 무한 루프 만들기 - **Commit #4**
- [ ] **[Step 5]** [연습장 브랜치] 퀴즈 풀기 기능 만들기 (`git checkout`, `merge`) - **Commit #5, #6**
- [ ] **[Step 6]** 퀴즈 추가 & 목록 보기 & 삭제 기능 만들기 - **Commit #7, #8**
- [ ] **[Step 7]** 데이터 다이어리 만들기 (`state.json` 영속성) - **Commit #9**
- [ ] **[Step 8]** 최고 점수 & 에어백 예외 처리 (Ctrl+C 방어) - **Commit #10, #11**
- [ ] **[Step 9]** [Git 실습] 내 코드 복사하고 가져오기 (`git clone`, `git pull`) - **Git 실습**

---

## 💡 초보자를 위한 쏙쏙 들어오는 용어 사전

본격적으로 시작하기 전, 자주 나오는 어려운 단어들을 쉬운 비유로 알아볼까요?

* 🥐 **클래스 (Class)**: 붕어빵을 찍어내는 **"붕어빵 틀"**입니다. 퀴즈의 기본 모양을 정의합니다.
* 🐟 **객체 (Instance/Object)**: 붕어빵 틀에서 구워져 나온 **"진짜 붕어빵"**입니다. 실제로 움직이는 개별 퀴즈 1개를 의미합니다.
* 📓 **JSON (`state.json`)**: 컴퓨터를 꺼도 기록이 사라지지 않게 적어두는 **"비밀 다이어리"**입니다.
* 🛡️ **Try-Except (예외 처리)**: 사용자가 이상한 글자를 입력하거나 `Ctrl+C`를 눌러도 프로그램이 튕기지 않게 지켜주는 **"안전 에어백"**입니다.
* 📸 **Git Commit**: 게임에서 중요한 순간에 누르는 **"세이브 포인트(저장)"**입니다.
* 📝 **Git Branch**: 원본 코드를 망치지 않고 마음껏 테스트해보는 **"연습장 지면"**입니다.
* ☁️ **Git Push / Pull**: 내 컴퓨터 저장본을 구글 드라이브 같은 인터넷(GitHub)에 **"올리기(Push)"** 및 **"내려받기(Pull)"**입니다.
* 👯 **Git Clone**: 다른 사람이나 내가 올려둔 저장소를 내 컴퓨터로 **"똑같이 복사해 가져오기"**입니다.

---

## 🏃 Step-by-Step 실습 가이드

---

### Step 1: 개발 환경 준비 & Git 저장소 시작하기 🚀

#### 1) 이번 단계 목표
프로젝트 폴더를 만들고, Git 저울판을 켠 뒤, 기본 문서(`README.md`, `.gitignore`)를 생성합니다.

#### 2) 개념 설명
* **`git init`**: "지금부터 이 폴더의 변경사항을 Git이 기록해줘!"라고 명령하는 첫 인사입니다.
* **`.gitignore`**: Git이 인터넷에 올릴 필요 없는 쓸데없는 임시 파일들을 자동으로 무시하게 만드는 목록표입니다.

#### 3) 코드 작성 가이드

폴더 안에 `.gitignore` 파일을 만들고 아래 코드를 붙여넣으세요.

📁 **`.gitignore`**
```gitignore
# 파이썬 임시 파일 무시하기
__pycache__/
*.pyc
.vscode/
.idea/
state.json.bak
```

📁 **`README.md`**
```markdown
# 🎯 나만의 파이썬 터미널 퀴즈 게임

파이썬 기초 문법과 클래스(OOP), JSON 파일 입출력을 배워 만드는 CLI 퀴즈 게임입니다.

## 📌 주요 기능
1. 📝 퀴즈 풀기 (랜덤 출제 & 힌트 지원)
2. 📌 새 퀴즈 추가
3. 📋 등록된 퀴즈 목록 보기 및 삭제
4. 🏆 최고 점수 및 플레이 히스토리 확인
```

#### 4) 💳 Git 명령어 카드 #1

터미널에 아래 명령어를 한 줄씩 그대로 입력하세요!

```bash
git init
git add .
git commit -m "Chore: 프로젝트 초기 설정 (.gitignore, README.md 작성)"
```

---

### Step 2: 퀴즈 붕어빵 틀 만들기 (`Quiz` 클래스) 🥐

#### 1) 이번 단계 목표
퀴즈 1개가 가져야 할 문제, 선택지 4개, 정답, 힌트 정보를 담는 `Quiz` 클래스를 만듭니다.

#### 2) 개념 설명
* **`__init__` (초기화 메서드)**: 붕어빵을 처음 찍어낼 때 팥이나 슈크림을 넣듯이, 퀴즈가 처음 만들어질 때 속성(문제, 선택지, 정답)을 채워주는 일종의 "생성 단추"입니다.
* **`self`**: "바로 이 퀴즈 자신"을 가리키는 파이썬만의 대명사입니다.

#### 3) 코드 작성 가이드

`quiz_game.py` 파일 생성 후 아래 코드를 작성하세요.

📁 **`quiz_game.py`**
```python
class Quiz:
    """개별 퀴즈 하나를 표현하는 붕어빵 틀(클래스)입니다."""
    def __init__(self, question: str, choices: list, answer: int, hint: str = ""):
        self.question = question   # 질문 문구
        self.choices = choices     # 선택지 4개 리스트
        self.answer = answer       # 정답 번호 (1~4 정수)
        self.hint = hint           # (보너스) 힌트 문구

    def display(self, show_hint: bool = False):
        """터미널 화면에 퀴즈와 선택지를 예쁘게 출력합니다."""
        print(f"\n📝 [문제] {self.question}")
        for idx, choice in enumerate(self.choices, 1):
            print(f"  {idx}. {choice}")
        if show_hint and self.hint:
            print(f"  💡 [힌트] {self.hint}")

    def check_answer(self, user_input: int) -> bool:
        """사용자가 입력한 번호가 정답인지 확인합니다."""
        return user_input == self.answer

    def to_dict(self) -> dict:
        """JSON 다이어리에 저장하기 위해 퀴즈를 딕셔너리로 변환합니다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint
        }

    @classmethod
    def from_dict(cls, data: dict):
        """JSON 다이어리에서 읽어온 딕셔너리를 다시 Quiz 객체로 복원합니다."""
        return cls(
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"],
            hint=data.get("hint", "")
        )
```

#### 4) 💳 Git 명령어 카드 #2

```bash
git add quiz_game.py
git commit -m "Feat: 개별 퀴즈 관리용 Quiz 클래스 구현"
```

---

### Step 3: 기본 퀴즈 5개 데이터 준비하기 📝

#### 1) 이번 단계 목표
프로그램을 처음 켰을 때 제공할 기본 파이썬/IT 퀴즈 5개를 코드로 준비합니다.

#### 2) 개념 설명
* **리스트(`[]`)**: 퀴즈 붕어빵 여러 개를 예쁘게 모아두는 "퀴즈 상자"입니다.

#### 3) 코드 작성 가이드

`quiz_game.py` 파일 아랫부분에 기본 퀴즈를 만드는 함수를 추가하세요.

📁 **`quiz_game.py` (이어서 작성)**
```python
def get_default_quizzes() -> list:
    """처음 실행하거나 파일이 없을 때 사용할 기본 퀴즈 5개 목록입니다."""
    return [
        Quiz("파이썬에서 변수를 만들 때 옳지 않은 이름은?", 
             ["my_var", "2nd_num", "_secret", "user_name"], 2, 
             "변수 이름은 숫자로 시작할 수 없어요!"),
        Quiz("Python에서 값을 변경할 수 없는(Immutable) 리스트 형태의 자료형은?", 
             ["list", "dict", "tuple", "set"], 3, 
             "소괄호 ()를 사용해서 만들어요."),
        Quiz("Git에서 로컬 저장소를 처음 초기화할 때 쓰는 명령어는?", 
             ["git add", "git commit", "git init", "git push"], 3, 
             "초기화를 뜻하는 initialization의 약자입니다."),
        Quiz("파이썬에서 조건을 만족할 때까지 반복하는 제어문은?", 
             ["for", "while", "if", "switch"], 2, 
             "~하는 동안 계속 반복한다는 뜻의 영어 단어입니다."),
        Quiz("JSON 파일 저장 시 한글이 깨지지 않도록 지정하는 권장 인코딩은?", 
             ["EUC-KR", "ASCII", "UTF-8", "CP949"], 3, 
             "전 세계 공용 표준 인코딩 형식입니다.")
    ]
```

#### 4) 💳 Git 명령어 카드 #3

```bash
git add quiz_game.py
git commit -m "Feat: 파이썬 및 IT 주제 기본 퀴즈 5개 데이터 작성"
```

---

### Step 4: 게임 대문(메뉴)과 무한 루프 만들기 🚪

#### 1) 이번 단계 목표
사용자가 번호를 누르면 원하는 기능을 실행하고, 5번이나 6번을 누르기 전까지 꺼지지 않는 메뉴 시스템을 구축합니다.

#### 2) 개념 설명
* **`while True` (무한 루프)**: 사용자가 종료를 선택할 때까지 게임을 계속 켜두는 엔진입니다.
* **입력 검증 함수**: 사용자가 이상한 문자(`abc`)나 엔터만 쳤을 때 차분히 "다시 입력해주세요" 안내하는 파수꾼 역할입니다.

#### 3) 코드 작성 가이드

`quiz_game.py`에 `QuizGame` 클래스의 기본 구조와 안전한 입력 함수를 작성합니다.

📁 **`quiz_game.py` (이어서 작성)**
```python
import sys

class QuizGame:
    """게임 전체 흐름과 데이터 입출력을 총괄하는 관리자 클래스입니다."""
    def __init__(self):
        self.quizzes = get_default_quizzes()
        self.best_score = {"score": 0, "correct_count": 0, "total_count": 0}
        self.history = []

    def get_valid_input(self, prompt: str, min_val: int, max_val: int) -> int:
        """입력 공백 제거, 숫자 변환, 범위 검사를 수행하는 안전 입력 파수꾼입니다."""
        while True:
            try:
                user_str = input(prompt).strip()
                if not user_str:
                    print("⚠️ 빈 입력입니다. 숫자를 입력해주세요.")
                    continue
                val = int(user_str)
                if min_val <= val <= max_val:
                    return val
                print(f"⚠️ 잘못된 입력입니다. {min_val}~{max_val} 사이의 숫자를 입력하세요.")
            except ValueError:
                print(f"⚠️ 문자는 입력할 수 없습니다. {min_val}~{max_val} 사이의 숫자를 입력하세요.")

    def show_menu(self):
        """메인 메뉴 화면을 출력합니다."""
        print("\n========================================")
        print("        🎯 나만의 파이썬 퀴즈 게임 🎯")
        print("========================================")
        print(" 1. 퀴즈 풀기")
        print(" 2. 퀴즈 추가")
        print(" 3. 퀴즈 목록")
        print(" 4. 점수 확인")
        print(" 5. 퀴즈 삭제 (보너스)")
        print(" 6. 게임 종료")
        print("========================================")
```

그리고 메인 실행 파일 `main.py`를 만듭니다.

📁 **`main.py`**
```python
from quiz_game import QuizGame

def main():
    game = QuizGame()
    print("🎮 퀴즈 게임을 준비 중입니다...")
    # 추후 game.run() 연결 예정

if __name__ == "__main__":
    main()
```

#### 4) 💳 Git 명령어 카드 #4

```bash
git add quiz_game.py main.py
git commit -m "Feat: 메뉴 출력 및 사용자 입력 선택 기본 구조 작성"
```

---

### Step 5: [브랜치 실습] 퀴즈 풀기 기능 완성하기 🌿

#### 1) 이번 단계 목표
**원본 코드를 건드리지 않는 연습장 브랜치(`feature/play-quiz`)**를 새로 파서 퀴즈 풀기 기능을 만든 후, 완벽히 작동하면 메인 코드(`main`)에 합칩니다.

#### 2) 개념 설명
* **`git checkout -b [브랜치명]`**: "기존 메인 방은 놔두고, 임시 연습장 방을 하나 만들어서 그리로 이동해줘!"라는 뜻입니다.
* **`git merge [브랜치명]`**: "연습장에서 만든 신기능이 잘 작동하니까, 이제 원본 방으로 합쳐줘!"라는 뜻입니다.

#### 3) 코드 작성 가이드

가장 먼저 터미널에서 브랜치를 만듭니다!
```bash
git checkout -b feature/play-quiz
```

이제 `quiz_game.py` 안에 `play_quiz` 메서드를 구현하세요.

📁 **`quiz_game.py` (내부에 메서드 추가)**
```python
    def play_quiz(self):
        """퀴즈를 하나씩 풀어보는 게임 진행 로직입니다."""
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요!")
            return

        print(f"\n📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        correct_count = 0

        for idx, quiz in enumerate(self.quizzes, 1):
            print(f"\n----------------------------------------")
            print(f"[문제 {idx}]")
            quiz.display()

            user_ans = self.get_valid_input("정답 입력 (1~4): ", 1, 4)
            if quiz.check_answer(user_ans):
                print("✅ 정답입니다!")
                correct_count += 1
            else:
                print(f"❌ 오답입니다. (정답은 {quiz.answer}번)")

        total = len(self.quizzes)
        score = int((correct_count / total) * 100)
        print("\n========================================")
        print(f"🏆 결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")
        
        if score > self.best_score.get("score", 0):
            print("🎉 축하합니다! 새로운 최고 점수입니다!")
            self.best_score = {"score": score, "correct_count": correct_count, "total_count": total}
        print("========================================")
```

#### 4) 💳 Git 명령어 카드 #5 & #6 (브랜치 생성 및 병합 필수!)

**Commit #5 (연습장 브랜치에서 커밋)**
```bash
git add quiz_game.py
git commit -m "Feat: 퀴즈 출제 및 정답 판별 기능 구현"
```

**Commit #6 (메인으로 돌아와서 병합!)**
```bash
git checkout main
git merge feature/play-quiz
```
*(성공 메시지가 나오면 브랜치 병합 성공입니다! 🎉)*

---

### Step 6: 퀴즈 추가 & 목록 보기 & 삭제 기능 만들기 📌

#### 1) 이번 단계 목표
새로운 문제 퀴즈를 직접 등록하고, 등록된 문제 목록을 보거나 필요 시 삭제하는 기능을 추가합니다.

#### 2) 코드 작성 가이드

`quiz_game.py`에 퀴즈 추가/목록/삭제 메서드를 구현합니다.

📁 **`quiz_game.py` (내부에 메서드 추가)**
```python
    def add_quiz(self):
        """새로운 퀴즈를 등록합니다."""
        print("\n📌 새로운 퀴즈를 추가합니다.")
        question = input("문제를 입력하세요: ").strip()
        while not question:
            print("⚠️ 문제는 빈칸일 수 없습니다.")
            question = input("문제를 입력하세요: ").strip()

        choices = []
        for i in range(1, 5):
            choice = input(f"선택지 {i}: ").strip()
            while not choice:
                print("⚠️ 선택지는 빈칸일 수 없습니다.")
                choice = input(f"선택지 {i}: ").strip()
            choices.append(choice)

        answer = self.get_valid_input("정답 번호 (1-4): ", 1, 4)
        hint = input("힌트 (선택사항, 없으면 Enter): ").strip()

        new_quiz = Quiz(question, choices, answer, hint)
        self.quizzes.append(new_quiz)
        print("✅ 퀴즈가 성공적으로 추가되었습니다!")

    def list_quizzes(self):
        """등록된 퀴즈 목록을 보여줍니다."""
        if not self.quizzes:
            print("\n📋 등록된 퀴즈가 없습니다.")
            return
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("----------------------------------------")
        for idx, quiz in enumerate(self.quizzes, 1):
            print(f"[{idx}] {quiz.question}")

    def delete_quiz(self):
        """등록된 퀴즈 중 하나를 삭제합니다."""
        self.list_quizzes()
        if not self.quizzes:
            return
        del_num = self.get_valid_input("\n삭제할 퀴즈 번호를 입력하세요 (취소: 0): ", 0, len(self.quizzes))
        if del_num == 0:
            print("취소되었습니다.")
            return
        removed = self.quizzes.pop(del_num - 1)
        print(f"🗑️ '{removed.question}' 퀴즈가 삭제되었습니다.")
```

#### 3) 💳 Git 명령어 카드 #7 & #8

**Commit #7 (퀴즈 추가 기능)**
```bash
git add quiz_game.py
git commit -m "Feat: 사용자 정의 퀴즈 추가 기능 구현 및 입력 검증"
```

**Commit #8 (목록 및 삭제 기능)**
```bash
git add quiz_game.py
git commit -m "Feat: 전체 퀴즈 목록 조회 및 퀴즈 삭제 기능 구현"
```

---

### Step 7: 다이어리 만들기! JSON 파일 저장 & 불러오기 📓

#### 1) 이번 단계 목표
프로그램을 꺼도 내가 추가한 퀴즈와 최고 점수가 남아있도록 `state.json` 다이어리에 저장하고 복구하는 로직을 작성합니다.

#### 2) 개념 설명
* **`json.dump(..., ensure_ascii=False, indent=4)`**: 파이썬 데이터를 다이어리(JSON) 파일에 예쁜 한글 그대로 저장하는 명령입니다.
* **파일 부재/손상 에어백 (`try-except FileNotFoundError, json.JSONDecodeError`)**: 파일이 없거나 파일 내용이 깨져있어도 튕기지 않고 기본 데이터로 자동 복구해 줍니다.

#### 3) 코드 작성 가이드

`quiz_game.py`에 파일 저장 및 불러오기 기능을 넣습니다.

📁 **`quiz_game.py` (내부에 메서드 추가)**
```python
import json
import os

    def load_data(self, filename="state.json"):
        """state.json 파일에서 데이터를 불러오거나 손상 시 자동 복구합니다."""
        if not os.path.exists(filename):
            print("📂 저장된 파일이 없어 기본 퀴즈 데이터로 시작합니다.")
            self.quizzes = get_default_quizzes()
            return

        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
                self.best_score = data.get("best_score", {"score": 0, "correct_count": 0, "total_count": 0})
                self.history = data.get("history", [])
                print(f"📂 저장된 데이터를 성공적으로 불러왔습니다. (퀴즈 {len(self.quizzes)}개)")
        except (json.JSONDecodeError, KeyError, Exception) as e:
            print(f"⚠️ 파일이 손상되어 기본 데이터로 초기화합니다. (사유: {e})")
            self.quizzes = get_default_quizzes()

    def save_data(self, filename="state.json"):
        """state.json 파일에 현재 퀴즈와 점수를 저장합니다."""
        try:
            data = {
                "quizzes": [q.to_dict() for q in self.quizzes],
                "best_score": self.best_score,
                "history": self.history
            }
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("💾 데이터가 state.json에 안심 저장되었습니다!")
        except Exception as e:
            print(f"❌ 저장 중 오류 발생: {e}")
```

#### 4) 💳 Git 명령어 카드 #9

```bash
git add quiz_game.py
git commit -m "Feat: state.json 파일 저장 및 자동 복구 예외 처리 구현"
```

---

### Step 8: 메인 제어 루프 & Ctrl+C 에어백 완비하기 🛡️

#### 1) 이번 단계 목표
`Ctrl+C`나 입력 스트림이 끊겨도 비정상 종료 없이 데이터를 안전하게 저장하고 나가는 최종 메인 루프를 `main.py`에 완성합니다.

#### 2) 코드 작성 가이드

`quiz_game.py`에 `run()` 컨트롤러 메서드를 작성합니다.

📁 **`quiz_game.py` (최종 완성)**
```python
    def show_score(self):
        """최고 점수를 확인합니다."""
        score_info = self.best_score
        print("\n========================================")
        print(f"🏆 최고 점수: {score_info.get('score', 0)}점")
        if score_info.get('total_count', 0) > 0:
            print(f"   ({score_info['total_count']}문제 중 {score_info['correct_count']}문제 정답)")
        print("========================================")

    def run(self):
        """게임 실행 메인 제어 루프입니다."""
        self.load_data()
        while True:
            try:
                self.show_menu()
                choice = self.get_valid_input("선택: ", 1, 6)
                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                    self.save_data()
                elif choice == 3:
                    self.list_quizzes()
                elif choice == 4:
                    self.show_score()
                elif choice == 5:
                    self.delete_quiz()
                    self.save_data()
                elif choice == 6:
                    print("\n👋 게임을 종료합니다. 감사합니다!")
                    self.save_data()
                    break
            except (KeyboardInterrupt, EOFError):
                print("\n\n⚠️ 비정상 종료 시도가 감지되었습니다. 데이터를 안전하게 저장하고 종료합니다.")
                self.save_data()
                sys.exit(0)
```

`main.py` 수정:

📁 **`main.py`**
```python
from quiz_game import QuizGame

def main():
    game = QuizGame()
    game.run()

if __name__ == "__main__":
    main()
```

#### 3) 💳 Git 명령어 카드 #10 & #11

**Commit #10 (Ctrl+C 예외 처리 및 메인 루프)**
```bash
git add quiz_game.py main.py
git commit -m "Feat: 최고 점수 기록 및 비정상 종료(Ctrl+C) 방어 로직 구현"
```

**Commit #11 (README 문서 완성)**
```bash
git add README.md
git commit -m "Docs: README.md 최종 업데이트 및 데이터 스키마 작성"
```

---

### Step 9: [Git 실습] Clone & Pull 마스터하기 👯

#### 1) 이번 단계 목표
Git 7대 명령어 중 **`clone`**과 **`pull`**을 직접 테스트하여 원격 저장소 복제 및 업데이트 흐름을 익힙니다.

#### 2) 실습 가이드

1. **내 프로젝트를 다른 폴더로 복제하기 (`git clone`)**
   ```bash
   # 현재 프로젝트 폴더 밖으로 나와서 다른 위치에 복제해봅니다.
   cd ..
   git clone [내_GitHub_저장소_주소].git test_quiz_folder
   cd test_quiz_folder
   ```

2. **복제된 저장소에서 수정 후 올리기 (`git push`)**
   ```bash
   # 복제된 test_quiz_folder 안의 README.md에 한 줄을 추가해봅니다.
   echo "\n- Clone & Pull 실습 완료!" >> README.md
   git add README.md
   git commit -m "Docs: Clone 저장소에서 README 내용 추가"
   git push origin main
   ```

3. **원래 내 작업 폴더로 돌아와서 최신 내용 가져오기 (`git pull`)**
   ```bash
   # 원래 프로젝트 폴더로 이동합니다.
   cd ../안티그래비티
   git pull origin main
   ```
   *(새로 추가한 README 내용이 내 원래 폴더로 쏙 들어오면 최종 합격입니다! 🎉)*

---

## 🏆 축하합니다! 제출 전 최종 확인표

모든 미션을 완수하셨습니다! 제출하기 전 아래 항목이 모두 준비되었는지 체크해보세요.

- [x] 터미널에서 `python main.py`로 게임이 정상 동작하는가?
- [x] 문자나 이상한 범위를 입력해도 튕기지 않고 재입력을 안내하는가?
- [x] 게임 실행 중 `Ctrl+C`를 눌러도 안전하게 저장하고 종료되는가?
- [x] `state.json` 파일이 생성되고 데이터가 유지되는가?
- [x] `git log --oneline` 실행 시 **10개 이상의 예쁜 커밋**이 존재하는가?
- [x] 브랜치 생성 및 병합(`feature/play-quiz` → `main`) 기록이 남아있는가?

수고 많으셨습니다! 당신은 이제 파이썬 기초와 Git 활용법을 정복한 개발자입니다! 🚀
