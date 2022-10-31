from coeficienteDesvanecimento_GlobalLib import coeficiente_desvanecimento
import numpy as np
import pandas as pd
import cmath




def desvanecimento_global_usuarios(qtd_usuarios):
  tamanho_v = 10**3
  cg_obj = coeficiente_desvanecimento.Coeficiente_de_Desvanecimento()
  d=np.random.uniform(500,2000,qtd_usuarios)
  dGlobal = np.zeros((qtd_usuarios,tamanho_v),dtype=complex)
  for i in range(qtd_usuarios):
    dGlobal[i,:] = cg_obj.desvanecimentoGlobal(d=d[i],LOS=False,NN=20,tamanho=tamanho_v,seed=i,fc=2.0*(10**9))

  return d,dGlobal

qtd_usuarios = 12
d,dGlobal = desvanecimento_global_usuarios(qtd_usuarios)


h=np.zeros((2,qtd_usuarios))
for i in range(qtd_usuarios):
  h[0][i] = abs(dGlobal[i][0])    
  h[1][i] = cmath.phase(dGlobal[i][0])
  
h=h.T


train = pd.DataFrame(data=h,columns=['0','1'])
train = train.sample(frac = 1)


df_dGlobal = pd.DataFrame(dGlobal)
df_dGlobal = abs(df_dGlobal)


train.to_csv('train.csv')
df_dGlobal.to_csv('df_dGlobal.csv')