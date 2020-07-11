def sumNums(n: int) -> int: #不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
    return n and n + sumNums(n-1)

