import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mean 
import main_oma as oma
import pandas as pd

sns.set()
def grafico_oma_noma(R_global):
    ############################################################################################# OMA 

    train = pd.read_csv('train.csv')
    dados = train[0:12]

    sum_dr,_ = oma.simulacao_OMA(dados=dados)


    ############################################################################################# OMA 


    tempo_gp = 40
   
    x_index = ['NOMA C0','NOMA C1', 'NOMA C2','OMA']
   # x_index = ['NOMA C0','NOMA C1', 'NOMA C2', 'NOMA C2','OMA']

        
    color = ['navy','darkblue','mediumblue','b','royalblue','midnightblue','cornflowerblue','dodgerblue','deepskyblue','skyblue','lightskyblue']


    plt.rcParams['xtick.labelsize'] = 30
    plt.rcParams['ytick.labelsize'] = 30
 
   
    dr_bar = R_global[tempo_gp]+sum_dr
    

    plt.bar(x_index,dr_bar,color = 'k')
    


    plt.xticks(x_index, fontsize=15,rotation = 45)
    plt.xlabel('Multiple Access Techniques',fontsize=30, weight='bold')
    plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
    plt.legend(loc='upper right',fontsize=30)

    plt.title('Data rate NOMA x OMA system',fontsize=30, weight='bold')
    plt.grid(True)

    plt.show()
