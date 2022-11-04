import numpy as np
import seaborn as sns
import pandas as pd
import math

sns.set()


def data_rate(g_canal):
  w=100
  B = 180*(10**3)
  N0 = 10**(-17.3)
  pot_total = ((10**(4.6))*(10**-3))


  num = pot_total*g_canal
  den = N0*B*w/12

  d_rate = (1/12)*B*w*np.log2(1+(num/den))

  return d_rate


def sum_data_rate(g_canal_list):
    sum_dr_list = []
    for i in g_canal_list:
        sum_dr_list.append(data_rate(i))
    sum_dr =sum(sum_dr_list)

    return sum_dr,sum_dr_list


def simulacao_OMA(dados):

   sum_dr,dr_list = sum_data_rate(dados)

   return sum_dr,dr_list


