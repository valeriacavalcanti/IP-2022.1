def octal(n):
    n_octal = ''
    while(n // 8 != 0):
        n_octal = str(n % 8) + n_octal
        n //= 8
    n_octal = str(n) + n_octal
    return n_octal
