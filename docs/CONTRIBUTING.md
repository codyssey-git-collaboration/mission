# Contributing Guide

우리 팀의 협업 규칙을 정리한 문서입니다. 모든 팀원은 작업 전 이 문서를 읽고 규칙을 따릅니다.

## 브랜치 전략 (GitHub Flow)

- `main`: 항상 배포 가능한(깨지지 않는) 상태를 유지한다. 직접 push 금지, PR 병합만 허용한다.
- `feature/*`: 작업 단위 브랜치. main에서 분기하여 작업하고, 완료되면 PR로 main에 병합한다.

**우리 팀이 GitHub Flow를 선택한 이유 (3줄):**
1. 브랜치 구조가 `main` + `feature/*`로 단순해 소규모 팀이 바로 익히고 적용하기 쉽다.
2. 모든 변경이 PR을 거치므로 코드 리뷰와 이슈 추적이 자연스럽게 강제된다.
3. main을 항상 배포 가능한 상태로 유지해, 언제든 안정된 결과물을 공유할 수 있다.

## 브랜치 네이밍 규칙

- 형식: `feature/<name>-<topic>`
  - `<name>`: 작업자 GitHub 아이디 또는 이름
  - `<topic>`: 작업 주제 (kebab-case)
- 예시
  - `feature/whitecy01-math-utils`
  - `feature/doritoss-string-utils`
  - 버그 수정은 `fix/<name>-<topic>` 사용 가능 (예: `fix/kim-divide-bug`)

## 커밋 메시지 컨벤션

- 형식: `<type>: <subject>`
- 사용 타입
  - `feat`: 새 기능 추가
  - `fix`: 버그 수정
  - `docs`: 문서 변경
  - `refactor`: 기능 변화 없는 코드 개선
  - `test`: 테스트 추가/수정
  - `chore`: 빌드/설정 등 기타 변경
- 좋은 예시
  - `feat: add math utils (add, subtract)`
  - `fix: handle divide by zero in divide()`
  - `docs: add branch naming rule to contributing guide`

### 금지 (의미없는 커밋 메시지)

아래 중 하나라도 해당하면 **의미없는 메시지**로 간주하고 재작성한다.

- 변경 대상을 유추할 수 없는 단어만 있는 경우: `update`, `fix`, `temp`, `wip`, `final` 등
- 무엇을/왜 바꿨는지 드러나지 않는 경우: `bug fix`, `edit file` 등 (구체 대상/효과 없음)

## PR 작성 규칙

- 모든 `feature` 브랜치는 PR로 `main`에 병합한다.
- PR 제목: `<type>: <작업 요약>`
- PR 본문에 **반드시 포함**할 항목:
  - **연결 이슈**: `Closes #<issue_number>` (또는 `Fixes #`)
  - **변경 사항(What)**: 무엇을 바꿨는가
  - **변경 이유(Why)**: 왜 바꿨는가
  - **테스트/검증(How)**: 어떻게 확인했는가

### PR 본문 템플릿

```md
## 연결 이슈
- Closes #<issue_number>

## 변경 사항(What)
- ...

## 변경 이유(Why)
- ...

## 테스트/검증(How)
- [ ] 로컬 실행/간단 테스트
- [ ] 충돌 가능성 체크(필요 시)
```

### 병합 조건

- 최소 1명 이상의 리뷰 승인(approve)
- main 직접 push 금지 (Branch Protection Rule 적용)

## 코드 리뷰 규칙

- `LGTM` / `좋아요`만 남기는 리뷰는 금지한다.
- 각 PR에는 **실질 코멘트 1개 이상**을 남긴다.
  - 예: 특정 라인/파일을 근거로 한 질문, 대안 제안, 리스크 지적, 개선 제안
- 리뷰어와 작성자 간 **최소 1회 이상 상호작용**(답글/수정 반영)이 기록으로 남아야 한다.
- 팀원별 최소 기준
  - PR 생성 및 병합: 최소 2개
  - 코드 리뷰 작성: 최소 2개 (본인 PR 제외)
  - 본인 PR에서 리뷰 코멘트 반영: 최소 1회

## 충돌 대응 흐름

1. **발생**: 병합/리베이스 중 충돌 마커(`<<<<<<<`, `=======`, `>>>>>>>`)를 확인한다.
2. **공유**: 팀 채널에 어떤 브랜치/파일에서 충돌이 났는지 즉시 공유한다.
3. **해결**: 관련 작업자끼리 keep both / choose one / refactor 중 전략을 합의해 해결한다.
4. **기록**: 해결 과정을 `docs/conflict-resolution.md`에 템플릿에 맞춰 기록한다.

> 공유 브랜치(main 포함)에서 팀 합의 없는 강제 푸시/히스토리 재작성은 금지한다.
