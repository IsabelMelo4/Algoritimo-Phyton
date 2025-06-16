def funcaoRafael(x,y): #os paramentros que a funcao recebe aqui, tipo onde tiver x, y ele subistitui na funcao
    return (3*x)**2  + y**2 #quando eu chamar a funcao ele retorna essa expressao 

def funcaobeto(x,y):
    return  2*(x**2) + (5*y) ** 2

def funcaoCarlos(x,y):
    return -100*x + y**3

teste = int(input())

for n in range(teste):
    x, y = map(int, input().split())

    rafael = funcaoRafael(x,y)
    carlos = funcaoCarlos(x,y)
    beto = funcaobeto(x,y)

    if rafael > carlos and rafael > beto:
        print("Rafael ganhou")
    elif carlos > rafael and carlos > beto:
        print("Carlos ganhou")
    else:
        print("Beto ganhou")
        