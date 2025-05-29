n = int(input())
for i in range(n):
    x, y = int(input().split())

    if x < y :
     x, y = y, x
