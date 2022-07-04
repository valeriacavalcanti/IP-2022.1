def digito_hexa(n):
    if (n < 10):
        return str(n)
    else:
        return 'ABCDEF'[n - 10]

def hexa(n):
    st = ''
    while(n // 16 != 0):
        st = digito_hexa(n) + st
        n //= 16
    st = digito_hexa(n) + st
    return st
