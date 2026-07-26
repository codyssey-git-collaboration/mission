def is_even(n: int) -> bool:
    """n이 짝수이면 True 반환"""
    return n % 2 == 0


def square(n: float) -> float:
    """n의 제곱 반환"""
    return n * n


def max_of_two(a: float, b: float) -> float:
    """둘 중 더 큰 값 반환"""
    return a if a > b else b


if __name__ == "__main__":
    # 사용 예시
    print(is_even(4))        # True
    print(square(5))         # 25
    print(max_of_two(3, 7))  # 7