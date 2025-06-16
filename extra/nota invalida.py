nota1 = float(input())
nota2 = float(input())
while True:
       
       if nota1 > 10 or nota2 > 10:
         print("nota invalida")

         nota1 = float(input())
         nota2 = float(input())
         
       elif nota1 < 0 or nota2 < 0:
         print("nota invalida")

         nota1 = float(input())
         nota2 = float(input())

       else:
        media = (nota1+nota2) // 2

        print("media = {:.2f}".format(media))

        break