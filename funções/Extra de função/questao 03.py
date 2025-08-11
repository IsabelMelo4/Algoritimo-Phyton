def subtrai_Pares(num):
    if num < 10:
        return num
    if num %2 == 0:
        return subtrai_Pares(num // 10) - num % 10
    else: 
        return subtrai_Pares(num // 10)
print(subtrai_Pares(8564))

