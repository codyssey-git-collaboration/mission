def first(lst):
    """리스트의 첫 번째 요소 반환"""
    if not lst:
        raise ValueError("빈 리스트입니다")
    return lst[0]


def last(lst):
    """리스트의 마지막 요소 반환"""
    if not lst:
        raise ValueError("빈 리스트입니다")
    return lst[-1]


def length(lst):
    """리스트의 길이 반환"""
    return len(lst)