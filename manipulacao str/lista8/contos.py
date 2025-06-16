while True:

    try:
        n,l, c = map(int, input().split())
        palavra = input()

        linha = 0
        paginas = 1

        while len(palavra) > 0:
            recorte = palavra[:c]
            palavra = palavra[c:]

            while len(palavra) > 0 and recorte[-1] != " " and palavra[0] != " ":
                 palavra  = recorte[-1] + palavra
                 recorte = recorte[:-1] 

            palavra = palavra.strip()

            linha += 1 

            if linha > l:
                 paginas += 1
                 linha = 1 

        print(paginas)

    except EOFError:
        break