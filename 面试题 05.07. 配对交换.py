def exchangeBits(num: int) -> int:
    even, odd = num&0x55555555, num&0xaaaaaaaa;
    return even<<1 | odd>>1