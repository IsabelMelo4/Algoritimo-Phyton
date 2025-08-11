def fib(n):
    global chamada
    chamada += 1
    if n == 0:
     return 0
    elif n == 1:
       return 1
    return fib(n-1) + fib(n-2)
 

testes = int(input())

for _ in range(testes):
    chamada = -1 
    num = int(input())
    resultado = fib(num)
    print("fib({}) = {} calls = {}".format(num, chamada, resultado))
