from coeficienteDesvanecimento_GlobalLib import coeficiente_desvanecimento
import numpy as np
import pandas as pd
import cmath

# !pip install -U git+https://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@github.com/Yuripds/Coeficiente-de-desvanecimento-global.git@main



################## testaar com distancia máxima de 20 KM
def desvanecimento_global_usuarios(qtd_usuarios,flag,tamanho_v,seed_=12):
  cg_obj = coeficiente_desvanecimento.Coeficiente_de_Desvanecimento()
  d=np.random.uniform(1000,20000,qtd_usuarios)
  dGlobal = np.zeros((qtd_usuarios,tamanho_v),dtype=complex)
  if flag == "metodo_padrao":
    for i in range(qtd_usuarios):
      dGlobal[i,:] = cg_obj.desvanecimento_modelo4(d=d[i],NN=20,tamanho=tamanho_v,seed=i+seed_,fc=2000,dmin=1000)
  else:
    for i in range(qtd_usuarios):
      dGlobal[i,:] = cg_obj.desvanecimento_modelo4(d=d[i],NN=20,tamanho=tamanho_v,seed=i,fc=2000,dmin=1000)

  return d,dGlobal

