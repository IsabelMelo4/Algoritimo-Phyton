def remover_espaços_e_consoantes(texto):
    vogais ="aeiouyAEIOUY"
    if texto == "":
        return ""
    
    if texto[0] in vogais:
        return 
