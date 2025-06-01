n1,n2 = map(int, input().split())

while n1 != n2:
    if n1 > n2:
        print("Decrescente")
    elif n1 < n2:
        print("Crescente")


    n1,n2 = map(int, input().split())