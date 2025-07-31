# ============================== ÍNDICES DE STRING ==============================

texto = "Eu estou Fazendo faculdade no IFPB de Esperança"

print(texto[10])  # Acessa o caractere no índice 10


# ========================== INTERVALOS DE STRING (FATIAMENTO) ==========================

print(texto[0:5])        # Vai da letra 0 até a 4 (intervalo não inclui o último índice)
print(texto[0:50:2])     # Vai da letra 0 até 49, pulando de 2 em 2
print(texto.strip())     # Remove espaços antes e depois da string


# ========================== TRANSFORMAÇÃO DO TEXTO ==========================

print(texto.upper())         # Transforma tudo em maiúsculo
print(texto.lower())         # Transforma tudo em minúsculo
print(texto.capitalize())    # Deixa só a primeira letra em maiúscula
print(texto.title())         # Coloca a primeira letra de cada palavra em maiúscula
print(texto.swapcase())      # Inverte maiúsculas por minúsculas e vice-versa


# ========================== VERIFICAÇÃO DE TEXTO ==========================

print(texto.startswith("E"))     # Verifica se começa com "E"
print(texto.endswith("a"))       # Verifica se termina com "a"
print(texto.isalpha())           # Verifica se só há letras (sem espaços)
print(texto.isdigit())           # Verifica se só há números
print(texto.isalnum())           # Verifica se é alfanumérico (sem espaço)
print(texto.isspace())           # Verifica se só há espaços


# ========================== CONTAGEM E BUSCA ==========================

print(texto.count("a"))          # Conta quantas vezes "a" aparece
print(texto.find("faculdade"))   # Retorna o índice da primeira ocorrência
print(texto.rfind("a"))          # Retorna o índice da última ocorrência


# ========================== SUBSTITUIÇÃO ==========================

print(texto.replace("faculdade", "curso"))  # Troca uma palavra por outra


# ========================== DIVISÃO E JUNÇÃO ==========================

print(texto.split())             # Divide a string em palavras (gera lista)
palavras = texto.split()
print("-".join(palavras))       # Junta as palavras com hífen
print(" ".join(palavras))       # Junta as palavras com espaço

print("================== Exercícios Fáceis ==========================================")

print("1. Imprimir o primeiro e o último caractere de uma string.")

nome = "Eu estou Fazendo faculdade no IFPB de Esperança"
print(nome[0], nome[-1])

print("2. Transformar uma string em maiúsculas e minúsculas.")

print(nome.upper())
print(nome.lower())

print("3. Contar quantas vezes a letra -a- aparece.")

print(nome.count("a"))

print("4. Verificar se uma palavra está contida na frase.")

"estudando" in nome  # Resultado não impresso, mas é uma verificação válida

print("5. Substituir todas as ocorrências de -a- por -@-")

print(nome.replace("a", "@"))


print("================= Exercícios Intermediários ===================================")

print("1. Inverter uma string.")

print(nome[::-1])

print("2. Separar uma frase em palavras (split) e contar quantas são.")

palavras = nome.split()
print(palavras)
print(len(palavras))

print("3. Juntar uma lista de palavras em uma frase (join).")

palavras = ["phyton é massa"]
print(palavras)
print("".join(palavras))

print("4. Remover espaços em branco antes e depois da string.")

exDetexto = "  exemplo de texto   "
print(exDetexto)
print(exDetexto.strip())

print("5. Capitalizar apenas a primeira letra da string.")

print(nome.capitalize())
print(nome.title())


print("================= Exercícios Desafio ==========================================")

print("1. Verifique se uma string é um palíndromo (lê igual de trás para frente)")

palavra = "radar"
novo_nome = palavra[::-1]

if novo_nome == palavra:
    print("é palindromo")
else:
    print("é palindromo")
