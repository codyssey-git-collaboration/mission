# Submission Index

제출물을 한 곳에서 확인할 수 있는 인덱스 문서입니다.

## Team
- 팀명: codyssey-git-collaboration
- 저장소: https://github.com/codyssey-git-collaboration/mission
- 팀원(GitHub): 재윤(@whitecy01), 주영(@juice), 도희(@dohee), 여원(@yeowon083)

## Member Issues / PRs

각 항목은 `PR — 연결 이슈(Closes)` 형식입니다.

### 재윤 (@whitecy01)
- Issues: [#1](https://github.com/codyssey-git-collaboration/mission/issues/1), [#7](https://github.com/codyssey-git-collaboration/mission/issues/7), [#12](https://github.com/codyssey-git-collaboration/mission/issues/12), [#21](https://github.com/codyssey-git-collaboration/mission/issues/21)
- PRs:
  - [#2 docs: add contributing guide](https://github.com/codyssey-git-collaboration/mission/pull/2) — Closes [#1](https://github.com/codyssey-git-collaboration/mission/issues/1)
  - [#8 feat: add math utils](https://github.com/codyssey-git-collaboration/mission/pull/8) — Closes [#7](https://github.com/codyssey-git-collaboration/mission/issues/7)
  - [#13 feat: add common_utils (충돌 base)](https://github.com/codyssey-git-collaboration/mission/pull/13) — Closes [#12](https://github.com/codyssey-git-collaboration/mission/issues/12)
  - [#15 feat: fill team_info 재윤, 도희 (충돌 A)](https://github.com/codyssey-git-collaboration/mission/pull/15)
  - [#22 docs: revert troubleshooting](https://github.com/codyssey-git-collaboration/mission/pull/22) — Closes [#21](https://github.com/codyssey-git-collaboration/mission/issues/21)

### 주영 (@juice-devlog)
- Issues: [#5](https://github.com/codyssey-git-collaboration/mission/issues/5), [#25](https://github.com/codyssey-git-collaboration/mission/issues/25)
- PRs:
  - [#6 feat: add string utils](https://github.com/codyssey-git-collaboration/mission/pull/6) — Closes [#5](https://github.com/codyssey-git-collaboration/mission/issues/5)
  - [#14 refactor: rename temporary file (충돌2)](https://github.com/codyssey-git-collaboration/mission/pull/14)
  - [#17 refactor: rename temporary file (충돌2)](https://github.com/codyssey-git-collaboration/mission/pull/17)
  - [#26 feat: git stash troubleshooting](https://github.com/codyssey-git-collaboration/mission/pull/26) — Closes [#25](https://github.com/codyssey-git-collaboration/mission/issues/25)

### 도희 (@dori943)
- Issues: [#3](https://github.com/codyssey-git-collaboration/mission/issues/3), [#19](https://github.com/codyssey-git-collaboration/mission/issues/19), [#24](https://github.com/codyssey-git-collaboration/mission/issues/24)
- PRs:
  - [#4 feat: add list utils](https://github.com/codyssey-git-collaboration/mission/pull/4) — Closes [#3](https://github.com/codyssey-git-collaboration/mission/issues/3)
  - [#11 feat: add temp.py (충돌2 base)](https://github.com/codyssey-git-collaboration/mission/pull/11)
  - [#20 feat: modify temp.py (충돌2)](https://github.com/codyssey-git-collaboration/mission/pull/20) — Closes [#19](https://github.com/codyssey-git-collaboration/mission/issues/19)
  - [#23 docs: conflict2 resolution log](https://github.com/codyssey-git-collaboration/mission/pull/23) — Closes [#19](https://github.com/codyssey-git-collaboration/mission/issues/19)
  - [#28 docs: reset --soft troubleshooting](https://github.com/codyssey-git-collaboration/mission/pull/28) — Closes [#24](https://github.com/codyssey-git-collaboration/mission/issues/24)

### 여원 (@yeowon083)
- Issues: [#9](https://github.com/codyssey-git-collaboration/mission/issues/9), [#18](https://github.com/codyssey-git-collaboration/mission/issues/18), [#29](https://github.com/codyssey-git-collaboration/mission/issues/29)
- PRs:
  - [#10 feat: add number utils](https://github.com/codyssey-git-collaboration/mission/pull/10) — Closes [#9](https://github.com/codyssey-git-collaboration/mission/issues/9)
  - [#16 feat: fill team_info 주영, 여원 (충돌 B 해결)](https://github.com/codyssey-git-collaboration/mission/pull/16) — Closes [#18](https://github.com/codyssey-git-collaboration/mission/issues/18)
  - [#27 docs: commit --amend troubleshooting](https://github.com/codyssey-git-collaboration/mission/pull/27) — Closes [#29](https://github.com/codyssey-git-collaboration/mission/issues/29)

## Key Docs
- Contributing: [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)
- Conflict log: [docs/conflict-resolution.md](docs/conflict-resolution.md)
- Troubleshooting: [docs/troubleshooting-log.md](docs/troubleshooting-log.md)

## 간단한 결과물 (유틸 함수 모음)
- [src/math_utils.py](src/math_utils.py) — 재윤 (add, subtract, divide)
- [src/string_utils.py](src/string_utils.py) — 주영 (reverse, to_upper, to_lower)
- [src/list_utils.py](src/list_utils.py) — 도희
- [src/number_utils.py](src/number_utils.py) — 여원 (is_even, square, max_of_two)
- [src/common_utils.py](src/common_utils.py) — 팀 공용 (team_info)

## 충돌 해결 기록 (2회, 모두 비자명)
| # | 유형 | 참여자 | 관련 PR |
|---|------|--------|---------|
| 1 | 같은 파일 같은 줄(동일 hunk) 수정 | 재윤 ↔ 여원 | #15, #16 |
| 2 | 파일 rename ↔ 내용 수정 | 도희 ↔ 주영 | #20, #23 |

## 트러블슈팅 4종
| 시나리오 | 명령 | 담당 | PR |
|----------|------|------|-----|
| 최근 커밋 메시지 수정 | `git commit --amend` | 여원 | #27 |
| 로컬 커밋 취소 + 변경 유지 | `git reset --soft HEAD~1` | 도희 | #28 |
| 원격 push된 커밋 취소 | `git revert` | 재윤 | #22 |
| 작업 보관 후 전환 | `git stash` / `stash pop` | 주영 | #26 |

## 코드 리뷰 & 리뷰 반영
| 팀원 | 코드 리뷰 작성 (본인 PR 제외) | 본인 PR 리뷰 반영 |
|------|------------------------------|-------------------|
| 재윤 (@whitecy01) | [#10](https://github.com/codyssey-git-collaboration/mission/pull/10) (2건) | [#22](https://github.com/codyssey-git-collaboration/mission/pull/22) |
| 주영 (@juice-devlog) | [#4](https://github.com/codyssey-git-collaboration/mission/pull/4), [#8](https://github.com/codyssey-git-collaboration/mission/pull/8) | [#6](https://github.com/codyssey-git-collaboration/mission/pull/6) |
| 도희 (@dori943) | [#2](https://github.com/codyssey-git-collaboration/mission/pull/2), [#6](https://github.com/codyssey-git-collaboration/mission/pull/6) | [#4](https://github.com/codyssey-git-collaboration/mission/pull/4) |
| 여원 (@yeowon083) | [#22](https://github.com/codyssey-git-collaboration/mission/pull/22), [#26](https://github.com/codyssey-git-collaboration/mission/pull/26) | [#10](https://github.com/codyssey-git-collaboration/mission/pull/10) |

→ 전원 리뷰 2개 이상 작성 + 본인 PR에서 리뷰 반영 1회 이상 충족

## Evidence

`git log --oneline --graph --all` 결과 (PR 기반 병합 흐름 + 충돌 해결 머지 커밋 확인 가능)

![git history graph 1](images/evidence1.png)
![git history graph 2](images/evidence2.png)
![git history graph 3](images/evidence3.png)
![git history graph 4](images/evidence4.png)