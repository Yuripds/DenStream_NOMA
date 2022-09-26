import numpy as np
import seaborn as sns
import pandas as pd
import cmath
from multiprocessing import Pool, freeze_support, cpu_count
from coeficienteDesvanecimento_GlobalLib import coeficiente_desvanecimento
from scipy import stats
import graficos as gf
from denStream import *

sns.set()


def desvanecimentoGlobal_usuarios(qtd_usuarios):
  cg_obj = coeficiente_desvanecimento.Coeficiente_de_Desvanecimento()
  d=np.random.uniform(500,2000,qtd_usuarios)
  dGlobal = np.zeros((qtd_usuarios,10**3),dtype=complex)
  for i in range(qtd_usuarios):
    dGlobal[i,:] = cg_obj.desvanecimentoGlobal(d=d[i],LOS=False,NN=20,tamanho=10**6,seed=i,fc=2.0*(10**9))

  return d,dGlobal



def allocPower(gamaL,alpha):
  p_list = []

  den = 0
  for i in range(len(gamaL)):
    den = den + ((abs(gamaL[-1])/abs(gamaL[i]))**(alpha))

  for i in range(len(gamaL)):
    p = ((abs(gamaL[-1])/abs(gamaL[i]))**(alpha)) / den
    p_list.append(p)

  return p_list

def dataRate(w,B,Pt,gamaUser,N0,p_list,index):
 
  num = p_list[index]*Pt*gamaUser

  p_list = p_list[index+1:]
  p_array = np.array(p_list)
  den_list = p_array*Pt*gamaUser

  den = np.sum(den_list)
  den = den+(w*(N0*B))
  r = w*B*np.log2(1+(num/den))

  return r

def sumDataRate(w,B,Pt,N0,gamaL,alpha):
  gamaL.sort()
  p_list = allocPower(gamaL,alpha)
  print("p_list: ",p_list)
 
  r_array = np.ones((7,1))
  r_array[:] = float(np.NaN)
  
  for ind in range(len(gamaL)):
    gamaUser = gamaL[ind]
    r = dataRate(w,B,Pt,gamaUser,N0,p_list,ind)
    print("r_teste: ", r)
    r_array[ind] = r

  output = r_array[np.isfinite(r_array)]
  R_global = np.sum(output)

  return r_array,R_global


def get_index_vc(vect):
  index =[]
  for i in range(len(vect)-1):
    if vect[i]-vect[i+1] != 0:
      index.append(i+1)

  return index


def simulacao(dados,modelo,w,B,N0,alpha,etNU_list,nU_list,eT_list):

  saida = modelo._addUsers(X=dados,estimacao_tempo=eT_list,novos_users =nU_list,estimacao_tempo_novosUsers = etNU_list, ad_users=True)
  
  
  for idx in range(len(saida)):
    print("rotulos:" ,len(saida[idx]))

  for idx in range(len(saida)):
    print("rotulos:" ,saida[idx])

  usuarioRotulos = np.zeros((12,3))


  drList_final = []
  dr_global_final = []
  for tempo in range(len(saida)):
    usuarioRotulos[:,0] = saida[tempo]
    usuarioRotulos[:,1] = h[0:12, 0]
    usuarioRotulos[:,2] = h[0:12, 1]

    rotulo = saida[tempo]
    unique, counts = np.unique(rotulo, return_counts=True)
    n_clusters = len(unique)
    Pt = (((10**(4.6))*(10**-3)))/n_clusters

    usuarioRotulos_sort = usuarioRotulos[np.argsort(usuarioRotulos[:, 0])]
    index = get_index_vc(usuarioRotulos_sort[:, 0])
    usuarioRotulos_sort_split = np.split(usuarioRotulos_sort,index)
    print("usuarioRotulos_sort_split: ",usuarioRotulos_sort_split)

    drList = []
    dr_global = []
    for i in range(len(usuarioRotulos_sort_split)):
      gamaL = []
      cluster = usuarioRotulos_sort_split[i]
      for m in range(len(cluster)):
        gamaL.append(cluster[m][1])
      r,R_global = sumDataRate(w,B,Pt,N0,gamaL,alpha)
      dr_global.append(R_global)

      drList.append(r)

    dr_global_final.append(dr_global)
    drList_final.append(drList)
    
  return drList_final,dr_global_final
  

############################################################################################
qtd_usuarios = 24
d,dGlobal = desvanecimentoGlobal_usuarios(qtd_usuarios)


h=np.zeros((2,qtd_usuarios))
for i in range(qtd_usuarios):
  h[0][i] = abs(dGlobal[i][0])    
  h[1][i] = cmath.phase(dGlobal[i][0])
  
h=h.T


train = pd.DataFrame(data=h,columns=['0','1'])
train = train.sample(frac = 1)


modelo = DenStream(lambd=0.5, eps=800, beta=0.4, mu=3, eps_dbscan =1200 , min_samples_dbscan = 1,zeta = 10.0)


df_dGlobal = pd.DataFrame(dGlobal)
df_dGlobal = abs(df_dGlobal)

w =100
B = 180*(10**3)
N0 = 10**(-17.3)
alpha_= 0.2

dados = train[0:10]
nU_list= train[10:qtd_usuarios]

etNU_list = df_dGlobal.iloc[nU_list.index.values.astype(int)].values.tolist()


eT_list =  df_dGlobal.iloc[dados.index.values.astype(int)].values.tolist()



drList,R_global = simulacao(dados=dados,modelo = modelo,w=w,B=B,N0=N0,alpha=alpha_,etNU_list=etNU_list,nU_list = nU_list,eT_list=eT_list)


print("cenário 01: ",R_global)

gf.graficos_plot(drList,R_global,str(qtd_usuarios))

