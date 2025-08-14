pecas = []

pecas_retiradas = input("Digite as peças separadas por espaço: ").split()
pecas.extend(pecas_retiradas)  # <-- isso espalha os elementos dentro de pecas

pecas.reverse()
print(pecas)