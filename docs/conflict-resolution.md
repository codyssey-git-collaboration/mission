# Conflict Resolution Log

## 충돌 기록 #1 (비자명 충돌 - 동일 라인 수정)

### 참여자
- 작성자(해결): 여원
- 상대: 재윤

### 상황(What happened)
- `src/common_utils.py`의 `team_info()` 반환 줄을 재윤(A)과 여원(B)이 각각 다르게 수정했다.
- 재윤 PR이 먼저 `main`에 병합된 뒤, 여원 PR을 병합하려 하자 **같은 파일의 같은 줄**에서 충돌이 발생했다.
- 비자명 충돌 유형: **같은 hunk(동일 라인)를 서로 다르게 수정**.

### 충돌 내용(Conflict markers)
```txt
"""팀 공용 유틸 모음."""


def team_info() -> str:
    """우리 팀 정보를 반환한다."""
<<<<<<< feature/yeowon-team-info
    return "우리 팀: 주영(string), 여원(number)"
=======
    return "우리 팀: 재윤(math), 도희(list)"
>>>>>>> main


if __name__ == "__main__":
    print(team_info())
```

- `<<<<<<< feature/yeowon-team-info` ~ `=======` : 현재 브랜치(여원 B)의 내용
- `=======` ~ `>>>>>>> main` : 병합 대상(main = 재윤 A)의 내용

### 해결 과정(How)
- 해결 위치: **GitHub PR의 "Resolve conflicts" 웹 에디터**에서 처리
- 전략: **keep both** (두 팀 정보를 모두 유지)
- 충돌 마커(`<<<<<<<`, `=======`, `>>>>>>>`) 3줄을 삭제하고 두 내용을 아래 한 줄로 통합:
  ```python
  return "우리 팀: 재윤(math), 도희(list), 주영(string), 여원(number)"
  ```
- "Mark as resolved" → "Commit merge" 로 충돌 해결 커밋 생성 후 병합

### 결과(Outcome)
- 두 팀원의 내용이 모두 반영된 상태로 병합 완료
- 관련 PR: <여원 PR 링크>
- 병합 커밋: <커밋 해시>

### 배운 점(Learnings)
- 같은 파일의 같은 줄을 여러 명이 동시에 수정하면 충돌이 발생한다 → 작업 분담 시 파일/영역을 나누면 예방할 수 있다.
- 충돌은 "누가 먼저 병합했는지"와 무관하게, 공통 조상 이후 같은 줄이 서로 다르게 바뀌면 발생한다.
- GitHub PR의 웹 에디터로도 간단한 충돌은 바로 해결할 수 있다(마커 제거 → Mark as resolved).




## 충돌 기록 #2 (비자명 충돌: 파일 이름 변경 vs 파일 내용 수정)

### 참여자
- 작성자: dohee (`feature/dohee-temp-modify`)
- 상대: juice (`feature/juice-temp` 또는 main 반영 브랜치)

### 상황 (What happened)
- juice가 `src/temp_file.py`의 파일 이름을 `src/temp_conflict.py`로 변경하여 `main`에 먼저 병합함.
- dohee는 동일한 기존 파일(`src/temp_file.py`)의 내부 출력 메시지를 수정하는 작업을 진행함.
- dohee 브랜치에서 `main`의 최신 변경 사항을 병합(`git merge origin/main`)하는 과정에서 파일 추적 및 자동 병합에 따른 비자명 충돌/병합 상황 발생.

### 충돌 내용 (Conflict markers / Merge behavior)
- 충돌 마커가 직접 생성되는 대신 Git의 `ort` 머지 전략이 파일 이동(Rename)과 내용 변경(Modify)을 감지함:
```txt
Merge made by the 'ort' strategy.
 docs/conflict-resolution.md             | 53 +++++++++++++++++++++++++++++++++-
 src/common_utils.py                     |  5 ++--
 src/{temp_file.py => temp_conflict.py} |  0
 3 files changed, 54 insertions(+), 4 deletions(-)
 rename src/{temp_file.py => temp_conflict.py} (100%)

### 해결 과정 (How)
1. git fetch origin 및 git merge origin/main 명령어를 실행하여 main 브랜치의 파일 이름 변경 이력을 가져옴.

2. Git의 3-way merge(ort 전략)가 기존 temp_file.py의 수정 내역을 C가 변경한 파일명(temp_conflict.py)에 자동으로 적용해 준 것을 확인함.

3. Vim 에디터 화면에서 머지 커밋 메시지 확인 후 저장(:wq)하여 병합 완료.

4. 로컬에서 src/temp_conflict.py 파일의 변경 내용이 정상 작동하는지 테스트 후 원격 브랜치로 git push 실행.

### 결과 (Outcome)
-파일명 변경(src/temp_conflict.py)과 내용 수정 사항이 안전하게 하나로 병합됨.
-PR 페이지의 병합 블락(Block) 경고가 해제되어 Able to merge 상태로 전환됨.

###배운 점 (Learnings)
-Git은 최신 머지 전략(ort)을 통해 파일 이름이 바뀌더라도 변경 이력을 추적하여 내용 수정을 자동으로 합성해 준다는 점을 배움.
-상대방이 파일 구조나 이름을 크게 바꾸는 작업을 할 때는 사전에 팀 채널에 공유하고 빠르게 main에 병합받는 것이 충돌 리스크를 줄이는 방법임을 체득함.