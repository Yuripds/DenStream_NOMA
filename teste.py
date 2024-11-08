import numpy as np
import seaborn as sns
import geradorGanhoCanal as ggc
from denStream import *
import pandas as pd
import cmath


sns.set()


def simulacao(dados,modelo,etNU_list,nU_list,eT_list,sd_param):

  y_tempo = modelo._addUsers(X=dados,estimacao_tempo=eT_list,novos_users =nU_list,estimacao_tempo_novosUsers = etNU_list, ad_users=True,sd_param=sd_param)
  
  return y_tempo
  

############################################################################################
qtd_usuarios = 12

modelo = DenStream(lambd=0.5, beta=0.4, mu=3,zeta = 5,p_tol=((10**(10*0.1))*(10**-3)),alpha=0.2, N0 =10**(-21),B=180*(10**3), Pt = ((10**(4.6))*(10**-3)),sd_out=10**3)


########################################### gerando amostras ######################################

qtd_usuarios = 12
flag ="metodo_proposto"
tamanho_v = 10**4
d,dGlobal = ggc.desvanecimento_global_usuarios(qtd_usuarios,flag,tamanho_v)


h=np.zeros((2,qtd_usuarios))
for i in range(qtd_usuarios):
  h[0][i] = abs(dGlobal[i][0])    
  h[1][i] = cmath.phase(dGlobal[i][0])
  
h=h.T


train = pd.DataFrame(data=h,columns=['modulo','fase'])
train = train.sample(frac = 1)


df_dGlobal = pd.DataFrame(dGlobal)

###################################################################################################


dados = train[0:10]
nU_list= train[10:qtd_usuarios]

etNU_list = df_dGlobal.iloc[nU_list.index.values.astype(int)].values.tolist()
eT_list =  df_dGlobal.iloc[dados.index.values.astype(int)].values.tolist()

### medida dada em porcento
sd_param = 30

y_tempo = simulacao(dados=dados,modelo = modelo,etNU_list=etNU_list,nU_list = nU_list,eT_list=eT_list,sd_param=sd_param)

