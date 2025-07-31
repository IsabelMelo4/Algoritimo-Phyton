#1. A série de Fibonacci tem 0 como primeiro e 1 como segundo elemento. A partir daí, a série
#segue definindo o próximo valor como a soma dos dois anteriores. Por exemplo, o terceiro
#elemento da série é 1 e o quarto é 2. Os oito primeiros elementos são 0, 1, 1, 2, 3, 5, 8 e 13.



def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(5):
    print(fibonacci(i))
    
