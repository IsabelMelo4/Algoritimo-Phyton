dias = 400

anos = dias // 365
restoAnos = dias % 365

meses = restoAnos//30
dias = restoAnos%30

print(anos)
print(meses)
print(dias)