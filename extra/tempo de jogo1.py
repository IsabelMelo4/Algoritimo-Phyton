hora_inicial, hora_final = map(int, input().split())

if hora_inicial < hora_final:
    tempo = hora_final - hora_inicial

else:
    tempo = 24 - hora_inicial + hora_final


print("O JOGO DUROU {} HORA(S)".format(tempo))