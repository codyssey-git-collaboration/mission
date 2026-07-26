"""할인율 계산 유틸 (실습용)."""

# 잘못된 값: 할인율이 1.5(150%)로 잘못 설정됨
DISCOUNT_RATE = 1.5


def apply_discount(price: float) -> float:
    """할인 적용 가격을 반환한다."""
    return price * (1 - DISCOUNT_RATE)
