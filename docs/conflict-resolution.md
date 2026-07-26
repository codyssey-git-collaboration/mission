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
