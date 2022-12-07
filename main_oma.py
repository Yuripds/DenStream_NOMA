import numpy as np
import seaborn as sns
import pandas as pd
import math
from statistics import mean 

sns.set()

def get_index_vc(vect):
  roturlos = vect[:,1]
  index =[]
  for i in range(len(roturlos)-1):
    if roturlos[i]-roturlos[i+1] != 0:
      index.append(i+1)

  return index

def data_rate(g_canal,n_usuarios):
  w=100
  B = 20*(10**6)
  N0 = 10**(-17.3)
  pot_total = ((10**(4.6))*(10**-3))


  num = pot_total*(g_canal**2)
  den = N0*B

  d_rate = (1/n_usuarios)*B*np.log2(1+(num/den))

  return d_rate


def sum_data_rate(g_canal):
    g_canal_list = []
    for i in g_canal:
      g_canal_list.append(i[0])

    sum_dr_list = []
    for i in g_canal_list:
        sum_dr_list.append(data_rate(i,len(g_canal_list)))
    sum_dr =sum(sum_dr_list)

    return sum_dr,sum_dr_list


def simulacao_OMA(dados):
   

   sum_dr_list = []
   dr_list_list = []
   # sum data rate de grupos
   index = get_index_vc(dados)
   dados_split = np.split(dados,index)
   for i in dados_split:
    sum_dr,dr_list = sum_data_rate(i)
    sum_dr_list.append(sum_dr)
    dr_list_list.append(dr_list)


   # média dos sum data rates
   media_sum_dr_list = mean(sum_dr_list)

   return media_sum_dr_list,dr_list_list


