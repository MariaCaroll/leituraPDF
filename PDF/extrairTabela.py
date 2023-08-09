import tabula
import pandas as pd
import os
#pandas_options={"header": None}
#, pandas_options={"header": None}
lista = []
var_strTabelas = tabula.read_pdf("fatura.pdf", pages="all")
df = var_strTabelas[1].values.tolist()
#print(df)
teste = ""
contador = 0
for item in df:
    
    if contador == 0:
        teste = item[1] 
        print(teste)  
    contador = 1 +  contador
    outro =  teste +", " + item[1]



print(outro)