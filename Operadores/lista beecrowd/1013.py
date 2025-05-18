n1, n2, n3 = input().split(' ')
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

auxiliar = (n1 + n2 + abs(n1-n2)) //2 
resultado = (auxiliar + n3 +abs(auxiliar - n3)) //2

print(f'{resultado} eh o maior')