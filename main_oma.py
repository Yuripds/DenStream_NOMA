import numpy as np
import seaborn as sns
from statistics import mean 

sns.set()

def get_index_vc(vect):
  roturlos = vect[:,1]
  index =[]
  for i in range(len(roturlos)-1):
    if roturlos[i]-roturlos[i+1] != 0:
      index.append(i+1)

  return index

def data_rate(g_canal,n_usuarios,B,N0,Pt):
  w =100
  num = Pt*(g_canal**2)
  den = N0*B*w

  d_rate = (1/n_usuarios)*B*w*np.log2(1+(num/den))

  return d_rate


def sum_data_rate(g_canal,B,N0,Pt):
    g_canal_list = []
    for i in g_canal:
      g_canal_list.append(i)

    sum_dr_list = []
    for i in g_canal_list:
        sum_dr_list.append(data_rate(i,len(g_canal_list),B,N0,Pt))
    sum_dr =sum(sum_dr_list)

    return sum_dr,sum_dr_list


def simulacao_OMA(usuarios_gc,cluster_id,B,N0,Pt):

  usuarios_f=[]
  y_tempo=[]
  idx_=0
  for bloco_ue in usuarios_gc:
    for ue in range(len(bloco_ue)):
      usuarios_f.append(bloco_ue[ue])
      y_tempo.append(cluster_id[idx_])
    idx_ = idx_+1
  
  usuarioRotulos = np.zeros((len(usuarios_f),2))
    
  idx =0 
  for valor in usuarios_f:
    usuarioRotulos[idx,0] = valor
    usuarioRotulos[idx,1] = y_tempo[idx]
    idx= idx+1
    
  usuarioRotulos_sort = usuarioRotulos[np.argsort(usuarioRotulos[:, 1])]
   

  sum_dr_list = []
  dr_list_final = []
  # sum data rate de grupos
  index = get_index_vc(usuarioRotulos_sort)
  gama_aux = usuarioRotulos_sort[:,0]
  dados_split = np.split(gama_aux,index)
  for i in dados_split:
    sum_dr,dr_list = sum_data_rate(i,B,N0,Pt)
    sum_dr_list.append([sum_dr])
    dr_list_final.append(dr_list)


   # média dos sum data rates
  #media_sum_dr_list = mean(sum_dr_list)

  return sum_dr_list,dr_list_final


