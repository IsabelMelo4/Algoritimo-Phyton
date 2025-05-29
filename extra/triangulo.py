a, b, c = map(float, input().split())

if (a + b) > c or (a + c) > b or (b + c) > a:
    p = a + b + c
    print("Perimetro = {:.1f}".format(p))

else:
    area = ((a + b) * c) // 2
    print("Area = {:.1f}".format (area))

