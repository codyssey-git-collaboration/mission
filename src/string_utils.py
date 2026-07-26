def reverse(text):
    result = ""

    for i in range(len(text) - 1, -1, -1):
        result += text[i]

    return result


def to_upper(text):
    result = ""

    for ch in text:
        code = ord(ch)

        if 97 <= code <= 122:
            result += chr(code - 32)
        else:
            result += ch

    return result


def to_lower(text):
    result = ""

    for ch in text:
        code = ord(ch)

        if 65 <= code <= 90:
            result += chr(code + 32)
        else:
            result += ch

    return result