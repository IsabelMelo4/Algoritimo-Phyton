import time

def contagem(cont):
    for i in range(cont, 0, -1):
        print(i, end=" ")
        time.sleep(1.5)

num = int(input())

print(contagem(num))       