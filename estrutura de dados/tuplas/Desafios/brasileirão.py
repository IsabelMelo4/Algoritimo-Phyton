#mostrar a lista do brasileirão, os 5 primeiros, os 4 ultimos, e mostrar em qual tá o seu time
def linha():
    print("-"*30)
brasileirao = (
    "Palmeiras",
    "Flamengo",
    "Botafogo",
    "Atlético-MG",
    "Bragantino",
    "Grêmio",
    "São Paulo",
    "Athletico-PR",
    "Internacional",
    "Fortaleza",
    "Cuiabá",
    "Cruzeiro",
    "Bahia",
    "Corinthians",
    "Vasco",
    "Atlético-GO",
    "Juventude",
    "Vitória",
    "Santos",
    "Fluminense"
)


time_fav = input("qual o seu time favorito")

linha()
print(brasileirao)
linha()


linha()
print(sorted(brasileirao))
linha()



linha()
print("os cincos primeiros")
print(brasileirao[:6])
linha()

linha()
print("os cincos ultimos")
print(brasileirao[-4:])
linha()

linha()
print("posicao do seu time")
print(brasileirao.index(time_fav))
linha()







