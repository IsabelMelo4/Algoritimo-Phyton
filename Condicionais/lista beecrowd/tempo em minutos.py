horaInicial, minInicial, horaFinal, minFinal = map(float, input())

inicio = horaInicial * 60 * + minInicial
fim = horaFinal * 60 * + minFinal

duração = fim - inicio

if duração <= 0:
    duração += 1440

horas = duração // 60
minutos = duração % 60 

print ("O jogo durou {} HORAS e {} MINUTOS(S)".format(horas, minutos))