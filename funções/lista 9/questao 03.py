#fazer uma calculadora que receba um numero e uma operação e fazer a operação 

def calculadora(n1, operação, n2):
    if operação == "+":
        return n1 + n2
    elif operação == "-":
        return n1 - n2 
    elif operação == "/":
        return n1 / n2 
    elif operação == "*":
        return n1 * n2 
def linha():
    print("-"*30)
   

#progama principal 
teste = ""
while teste != "n":
    linha()
    print("calculadora")
    linha()
    
    num1, ope, num2  = input("Digite dois numeros e qual sua operação:").split()
    num1 = int(num1)
    ope = str(ope)
    num2 = int(num2)

    linha()
    resultado = calculadora(num1, ope, num2)
    print(resultado)
    linha()

    teste = input("deseja continuar?[s/n]")

linha()
print("fim")
linha()