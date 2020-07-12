def maximum(a: int, b: int) -> int:
    k = ((a-b)>>31)&0x1
    sa, sb =(a>>31)&0x1, (b>>31)&0x1
    diff = sa^sb
    k = (k*(diff^1)) | (sa&diff)
    return (a*(k^1) | (b*k)) #k=0,a>b; k=1,a<b
print(maximum(-1,6))
