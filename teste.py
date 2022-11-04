import numpy as np
import seaborn as sns
import graficos as gf
import graficoNovo as gfn
import geradorGanhoCanal as ggc
from denStream import *
import pandas as pd
import cmath
import grafico_noma_oma as gon
import desempenho as dsp

sns.set()


def simulacao(dados,modelo,etNU_list,nU_list,eT_list):

  drList_final,dr_global_final = modelo._addUsers(X=dados,estimacao_tempo=eT_list,novos_users =nU_list,estimacao_tempo_novosUsers = etNU_list, ad_users=True)
  
  return drList_final,dr_global_final
  

############################################################################################
qtd_usuarios = 12

modelo = DenStream(lambd=0.5, eps=700, beta=0.4, mu=3, eps_dbscan =1200 , min_samples_dbscan = 1,zeta = 100.0)
train = pd.read_csv('train.csv')
df_dGlobal= pd.read_csv('df_dGlobal.csv')


########################################### gerando amostras ######################################

qtd_usuarios = 12
d,dGlobal = ggc.desvanecimento_global_usuarios(qtd_usuarios)


h=np.zeros((2,qtd_usuarios))
for i in range(qtd_usuarios):
  h[0][i] = abs(dGlobal[i][0])    
  h[1][i] = cmath.phase(dGlobal[i][0])
  
h=h.T


train = pd.DataFrame(data=h,columns=['0','1'])
train = train.sample(frac = 1)


df_dGlobal = pd.DataFrame(dGlobal)

###################################################################################################


dados = train[0:10]
nU_list= train[10:qtd_usuarios]

etNU_list = df_dGlobal.iloc[nU_list.index.values.astype(int)].values.tolist()
eT_list =  df_dGlobal.iloc[dados.index.values.astype(int)].values.tolist()



drList,R_global = simulacao(dados=dados,modelo = modelo,etNU_list=etNU_list,nU_list = nU_list,eT_list=eT_list)


#gf.graficos_plot(drList,R_global)
gfn.grafico_novo_plot(drList)
#gon.grafico_oma_noma(R_global)
