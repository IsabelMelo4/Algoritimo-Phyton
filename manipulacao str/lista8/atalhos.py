def italico():      
          
          global novoTexto
          global novoCaractere

          if palavra.startswith("_"):
               novoCaractere = palavra.replace("_", "<i>",1)
               novoTexto += novoCaractere 

          elif palavra.endswith("_"):    
               novoCaractere = palavra.replace("_", "</i>", 1)
               novoTexto += novoCaractere 
          else:
             novoTexto += novoCaractere 

palavra =(input())
novoTexto = " "

italico()
print(novoTexto)

