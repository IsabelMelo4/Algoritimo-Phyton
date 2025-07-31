def Subtrai_digitos(num):
    if num < 10:
        return num
    s = str(num)
    return int(s[0]) - soma(int(s[1:]))

def soma(n):
    if n < 10:
        return n
    s = str(n)
    return int(s[0]) + soma(int(s[1:]))


