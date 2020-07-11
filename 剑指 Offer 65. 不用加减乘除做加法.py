def add(a: int, b: int) -> int:
    if not b:
        return a
    return add(a^b, (a&b)<<1)


