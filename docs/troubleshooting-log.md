## 시나리오: reset --soft (로컬 커밋 취소, 변경 내용 유지)

### 참여자
- 도희

### 상황
- `feature/teamB-reset-troubleshoot` 브랜치에서 실습용으로 `test.txt` 파일을 작성하고 커밋했다.
- 아직 원격에 push하지 않은 로컬 커밋이므로, 히스토리를 자유롭게 수정해도 안전한 상태였다.
- 이 커밋을 취소하되, 작업한 파일 내용은 그대로 유지하고 싶어 `reset --soft`를 사용했다.

### 시도한 명령/절차
```bash
# 1. 작업 브랜치 생성 및 이동
git checkout main
git pull origin main
git checkout -b feature/dohee-reset-troubleshoot

# 2. 실습용 실수 커밋 만들기 (test.txt 작성)
git add .
git commit -m "feat: temporary commit for reset test"

# 3. reset --soft HEAD~1 실행 (핵심)
git reset --soft HEAD~1

# 4. 확인
git status
#   Changes to be committed:
#     new file:   test.txt
```

### 결과
- `git reset --soft HEAD~1` 실행 후 방금 만든 커밋(`feat: temporary commit for reset test`)은 히스토리에서 사라졌다.
- 하지만 `git status`로 확인한 결과, `test.txt`의 변경 내용은 **staged(인덱스) 상태로 그대로 남아있음**을 확인했다. 즉, `git add`까지 마친 상태로 되돌아간 것이다.
- 커밋만 취소되고 작업 내용은 유실되지 않으므로, 이후 원하는 메시지로 다시 커밋하거나 파일을 추가 수정한 뒤 커밋할 수 있다.
- **주의점**: 이번 실습은 아직 push하지 않은 로컬 커밋에 대해서만 진행했다. 만약 이미 원격에 push된 커밋이었다면 `reset`으로 히스토리를 재작성한 뒤 `--force` push가 필요했을 것이고, 이는 다른 팀원의 로컬 히스토리와 어긋나 협업 문제를 일으킬 수 있다. (→ 그 경우는 `revert`를 사용해야 함)

### 왜 이 방법을 선택했는가(Why)
- 아직 **원격에 push하지 않은 로컬 커밋**이었기 때문에 히스토리를 자유롭게 수정해도 다른 팀원에게 영향이 없어 안전했다.
- 커밋 자체는 취소하고 싶었지만, 작업한 파일 변경 내용은 잃고 싶지 않았기 때문에 변경 내용까지 삭제하는 `reset --hard` 대신 `reset --soft`를 선택했다.
- 커밋 메시지를 잘못 작성했거나 커밋 단위를 다시 정리하고 싶을 때, `reset --soft`는 변경 내용을 보존하면서 커밋만 되돌릴 수 있는 가장 안전하고 간단한 방법이다.