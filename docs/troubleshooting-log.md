# .
# Troubleshooting Log

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