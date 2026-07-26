# Troubleshooting Log

## 시나리오: commit --amend (최근 커밋 메시지 오타 수정)
### 참여자
- 여원

### 상황
- `src/example.py`를 수정하면서 커밋 메시지에 오타(`fx: 예시 파일 수정`)를 남긴 채 커밋했다.
- 아직 원격(origin)에는 push하지 않은 상태라, 히스토리를 재작성해도 다른 팀원에게 영향이 없다.

### 시도한 명령/절차
```bash
# 오타가 포함된 커밋 생성
git add src/example.py
git commit -m "fx: 예시 파일 수정"

git log --oneline -1
#   a1b2c3d fx: 예시 파일 수정

# 직전 커밋의 메시지를 수정 (새 커밋 해시로 대체됨)
git commit --amend -m "fix: 예시 파일 수정"

git log --oneline -1
#   e4f5g6h fix: 예시 파일 수정
```

### 결과
- `--amend`는 새로운 커밋을 생성해 직전 커밋을 **교체**하는 방식이므로, 메시지만 바꿔도 커밋 해시(`a1b2c3d` → `e4f5g6h`)가 변경된다.
- 즉, amend는 "기존 커밋 수정"이 아니라 "기존 커밋을 대체하는 새 커밋 생성"이다(메시지만 바꿔도, 파일을 추가로 stage해도 동일하게 적용됨).
- **주의점**: 아직 push하지 않은 로컬 커밋이었기 때문에 별도 force-push 없이 안전하게 히스토리를 정리할 수 있었다.

### 왜 이 방법을 선택했는가(Why)
- 커밋 메시지 오타는 **내용 변경 없이 메시지만 고치면 되는 상황**이라, `reset` 후 재커밋하는 것보다 `--amend`가 더 간단하고 직관적이다.
- 아직 원격에 push되지 않은 로컬 커밋이므로 히스토리 재작성이 팀원 누구에게도 영향을 주지 않는다 → amend 사용에 제약이 없는 안전한 상황.
- 만약 이미 원격에 push된 커밋이었다면, amend 후 `--force`(또는 `--force-with-lease`) push가 필요해 공유 히스토리를 깨뜨릴 위험이 있으므로 이 경우엔 사용을 피해야 한다(재윤님의 revert 실습과 대비되는 지점).

## 시나리오: git stash / git stash pop (커밋하지 않은 작업 임시 저장)

### 참여자
- 주영

### 상황
- `feature/juice-temp` 브랜치에서 `src/temp_stash.py` 파일을 새로 생성하여 작업하던 중 다른 브랜치로 이동해야 하는 상황이 발생했다.
- 작업이 아직 완료되지 않아 커밋하기에는 이른 상태였으며, 현재 작업 내용을 유지한 채 브랜치를 전환해야 했다.
- 새로 생성한 파일은 Git에서 **Untracked file** 상태로 관리되고 있었다.

### 시도한 명령/절차
```bash
# 현재 작업 상태 확인
git status

# 추적되지 않는 파일까지 포함하여 임시 저장
git stash -u

# 다른 브랜치로 이동
git switch main

# 다시 작업 브랜치로 복귀
git switch feature/juice-temp

# 임시 저장한 작업 내용 복원
git stash pop

# 복원 결과 확인
git status
```

### 결과
- `git stash -u`를 통해 `src/temp_stash.py`를 포함한 작업 내용을 안전하게 임시 저장할 수 있었다.
- 브랜치 이동 후 `git stash pop`을 실행하여 작업 내용과 새로 생성한 파일이 정상적으로 복원되었다.
- **주의점**: 새로 생성한 파일(Untracked file)은 기본 `git stash`로는 저장되지 않으며, `-u`(`--include-untracked`) 옵션을 사용해야 함께 저장된다.

### 왜 이 방법을 선택했는가(Why)
- 작업이 완료되지 않은 상태에서 임시 커밋을 생성하지 않고도 브랜치를 이동할 수 있기 때문이다.
- `git stash`를 사용하면 작업 중인 변경 사항을 안전하게 보관한 뒤 필요할 때 다시 이어서 작업할 수 있다.
- 특히 새로 생성한 파일이 있는 경우 `git stash -u`를 사용하면 작업 내용을 모두 보존할 수 있어 협업 과정에서 불필요한 커밋을 줄일 수 있다.

## 시나리오: revert (원격에 push된 커밋 취소)

### 참여자
- 재윤

### 상황
- `src/discount.py`를 추가하면서 할인율 상수를 `DISCOUNT_RATE = 1.5`(150%)로 **잘못 설정한 커밋을 원격에 push**했다.
- 이미 push되어 다른 팀원이 받아갔을 수 있으므로, 히스토리를 재작성하는 `reset`은 사용할 수 없다.

### 시도한 명령/절차
```bash
# 잘못된 커밋이 이미 origin에 push된 상태
git log --oneline -1
#   bb0183d feat: add discount util (wrong rate 1.5)

# 되돌리는 새 커밋 생성 (원본은 히스토리에 보존)
# --no-edit: revert 커밋 메시지 편집기를 띄우지 않고 기본 메시지("Revert ...")로 바로 커밋
git revert HEAD --no-edit
#   04eee6c Revert "feat: add discount util (wrong rate 1.5)"

# 일반 push (force-push 아님)
git push
```

### 결과
- `feat: add discount util` 커밋은 파일을 **새로 추가**하는 커밋이었으므로, 이를 revert하면 결과적으로 `src/discount.py`가 삭제된다. 즉, revert는 항상 **"그 커밋이 한 일의 반대"**를 수행한다(추가 → 삭제, 삭제 → 복원, 수정 → 원복).
- 원본 커밋 `bb0183d`는 히스토리에 그대로 남아 있어, "무엇을 왜 되돌렸는지" 추적이 가능하다.
- **주의점**: revert는 히스토리를 지우지 않으므로 `git push`만으로 충분하다. 반면 `reset`으로 push된 커밋을 지우면 `--force`가 필요하고, 이는 공유 브랜치의 히스토리를 깨뜨려 협업에 문제를 일으킨다.

### 왜 이 방법을 선택했는가(Why)
- 이미 원격(공유)에 올라간 커밋이라 **히스토리 재작성(reset + force-push)은 금지**된다(다른 팀원의 로컬과 어긋남).
- `revert`는 원본을 유지한 채 "취소 커밋"을 추가하므로, 공유 히스토리를 안전하게 보존하면서 변경만 되돌릴 수 있다.
- 커밋 단위로 안전하게 롤백 이력을 남기는 것이 팀 협업에서 재현·추적에 유리하다.

