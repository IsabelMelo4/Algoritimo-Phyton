i = 0.0

while i <= 2:
  for n in range(3):
      j = n + i +1
      if int(i*10) % 10 == 0:
       print("I={} J={}".format(int(i), int(j)))
      else:
          print("I={:.1f} J={:.1f}".format(i, j))
  i = round(i+ 0.2,1) #ele soma 0.2 no i e arredonda para 1 casa decimal só, sem fica o 1.000000 ele fica so 1
    