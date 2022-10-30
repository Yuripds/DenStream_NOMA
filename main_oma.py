import numpy as np
import seaborn as sns
import pandas as pd
import math

sns.set()


def data_rate(g_canal):
  #w =math.floor(100/12)
  B = 20*(10**6)
  N0 = 10**(-17.3)
  pot_total = ((10**(4.6))*(10**-3))


  num = pot_total*g_canal
  den = (N0)

  d_rate = (1/12)*B*np.log2(1+(num/den))

  return d_rate


def sum_data_rate(g_canal_list):
    sum_dr_list = []
    for i in g_canal_list:
        sum_dr_list.append(data_rate(i))
    sum_dr =sum(sum_dr_list)

    return sum_dr,sum_dr_list


def simulacao_OMA(dados):
   array_dados =np.array(dados['0'])

   sum_dr,dr_list = sum_data_rate(array_dados)

   return sum_dr,dr_list


train = pd.read_csv('train.csv')
dados_OMA = train[0:12]

sum_dr,dr_list = simulacao_OMA(dados=dados_OMA)
print("Lista de data rate:",dr_list)
print("Data rate global:",sum_dr)