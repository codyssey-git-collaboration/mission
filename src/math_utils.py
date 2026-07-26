"""수학 관련 유틸 함수 모음.

사용 예시:
    >>> from src.math_utils import add, divide
    >>> add(2, 3)
    5
    >>> divide(10, 2)
    5.0
"""


def add(a: float, b: float) -> float:
    """두 수를 더한 값을 반환한다.

    >>> add(2, 3)
    5
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """a에서 b를 뺀 값을 반환한다.

    >>> subtract(5, 2)
    3
    """
    return a - b


def divide(a: float, b: float) -> float:
    """a를 b로 나눈 값을 반환한다.

    b가 0이면 ValueError를 발생시킨다.

    >>> divide(10, 2)
    5.0
    """
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b


if __name__ == "__main__":
    print("add(2, 3) =", add(2, 3))
    print("subtract(5, 2) =", subtract(5, 2))
    print("divide(10, 2) =", divide(10, 2))
