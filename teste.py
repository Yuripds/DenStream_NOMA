import numpy as np
import seaborn as sns
import graficos as gf
import graficoNovo as gfn
from denStream import *
import pandas as pd

sns.set()


def alloc_power(gamaL,alpha):
  p_list = []

  den = 0
  for i in range(len(gamaL)):
    den = den + ((abs(gamaL[-1])/abs(gamaL[i]))**(alpha))

  for i in range(len(gamaL)):
    p = ((abs(gamaL[-1])/abs(gamaL[i]))**(alpha)) / den
    p_list.append(p)

  return p_list

def data_rate(w,B,Pt,gamaUser,N0,p_list,index):
 
  num = p_list[index]*Pt*gamaUser

  p_list = p_list[index+1:]
  p_array = np.array(p_list)
  den_list = p_array*Pt*gamaUser

  den = np.sum(den_list)
  den = den+(w*(N0*B))
  r = w*B*np.log2(1+(num/den))

  return r

def sum_data_rate(w,B,Pt,N0,gamaL,alpha):
  gamaL.sort()
  p_list = alloc_power(gamaL,alpha)
  print("p_list: ",p_list)
 
  r_array = np.ones((24,1))
  r_array[:] = float(np.NaN)
  
  for ind in range(len(gamaL)):
    gamaUser = gamaL[ind]
    r = data_rate(w,B,Pt,gamaUser,N0,p_list,ind)
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


def simulacao(dados,modelo,w,B,N0,alpha,etNU_list,nU_list,eT_list,qts_u):


  saida = modelo._addUsers(X=dados,estimacao_tempo=eT_list,novos_users =nU_list,estimacao_tempo_novosUsers = etNU_list, ad_users=True)
  
  
  for idx in range(len(saida)):
    print("rotulos:" ,len(saida[idx]))

  for idx in range(len(saida)):
    print("rotulos:" ,saida[idx])



  usuarioRotulos = np.zeros((qts_u,3))
  drList_final = []
  dr_global_final = []


  h = pd.concat([dados, nU_list], ignore_index=True) 
  for tempo in range(len(saida)):
    usuarioRotulos[:,0] = saida[tempo]
    usuarioRotulos[:,1] = np.array(h['0'])
    usuarioRotulos[:,2] = np.array(h['1'])

    rotulo = saida[tempo]
    unique, counts = np.unique(rotulo, return_counts=True)
    n_clusters = len(unique)
    Pt = ((10**(4.6))*(10**-3))/n_clusters

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
      r,R_global = sum_data_rate(w,B,Pt,N0,gamaL,alpha)
      dr_global.append(R_global)

      drList.append(r)

    dr_global_final.append(dr_global)
    drList_final.append(drList)
    
  return drList_final,dr_global_final
  

############################################################################################
qtd_usuarios = 12

modelo = DenStream(lambd=0.5, eps=800, beta=0.4, mu=3, eps_dbscan =1200 , min_samples_dbscan = 1,zeta = 10.0)
train = pd.read_csv('train.csv')
df_dGlobal= pd.read_csv('df_dGlobal.csv')


w =100
B = 180*(10**3)
N0 = 10**(-17.3)
alpha_= 0.2

dados = train[0:10]
nU_list= train[10:qtd_usuarios]

etNU_list = df_dGlobal.iloc[nU_list.index.values.astype(int)].values.tolist()
eT_list =  df_dGlobal.iloc[dados.index.values.astype(int)].values.tolist()



drList,R_global = simulacao(dados=dados,modelo = modelo,w=w,B=B,N0=N0,alpha=alpha_,etNU_list=etNU_list,nU_list = nU_list,eT_list=eT_list,qts_u=qtd_usuarios)

# gf.graficos_plot(drList,R_global,str(qtd_usuarios))
gfn.grafico_novo_plot(drList)
