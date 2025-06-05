m,n = map(int, input().split())

while m != 0 or n != 0:
    contador = 0
    somador = 0

    if m > n:
        m,n = n,m

    for i in range(m, n+1):
     somador += i
     print(i, end=" ")

     if i == n:
      print("Sum={}".format(somador))

    m,n = map(int, input().split())

    if n <= 0 or m <= 0:
       break