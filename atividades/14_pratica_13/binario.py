def binario(n):
    bin = ''
    while(n // 2 != 0):
        bin = str(n % 2) + bin
        n //= 2
    bin = str(n) + bin
    return bin
