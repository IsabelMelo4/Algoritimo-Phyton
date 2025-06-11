while True:

    try:
       
       string1 = input()
       string2 = input()

       if len(string2) > len (string1):
           string1, string2 = string2, string1
       
       encontrou = False
       for i in range(len(string2), 0 -1):
         
           if encontrou:
             break

           for j in range(0, len(string2)-i +1):
               if string1.find(string2[j:j + i]) != -1:
                   print(i)

                   encontrou = True
                   break

       if not encontrou:
           print(0)

    except EOFError:
        break