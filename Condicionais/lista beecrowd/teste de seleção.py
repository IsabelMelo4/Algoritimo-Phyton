n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())

if n2 > n3 and n4 > n1 and (n3 + n4) > (n1 + n2) and n3 > 0 and n4 > 0 and n1 % 2 == 0:
    print('valores aceitos')
else:
    print('valores não aceitos')