# Troubleshooting Log

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
