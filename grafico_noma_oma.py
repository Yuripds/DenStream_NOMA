import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mean 
import main_oma as oma
import pandas as pd

sns.set()
def grafico_oma_noma(R_global):
    ############################################################################################# OMA 

    train = pd.read_csv('/home/yuri/Documentos/github/DenStream_NOMA/csv_ganhos_de_canal/usuarioRotulos_sort_df_18_.csv')

    dados = np.array(train["Ganho"])

    sum_dr_oma,_ = oma.simulacao_OMA(dados=dados)


    ############################################################################################# OMA 


    #tempo_gp = 0
   
    x_index = ['NOMA t0','NOMA t1','NOMA t2','NOMA t3','NOMA t4','OMA']
    #n_lusters= len(R_global[tempo_gp][0])
    #x_index = []
    #for i in range(n_lusters):
    #    x_index.append('NOMA C'+str(i)) 
    #x_index.append('OMA')
        
    color_ = ['darkblue','mediumblue','b','royalblue','midnightblue','cornflowerblue','dodgerblue','deepskyblue','skyblue','lightskyblue']


    plt.rcParams['xtick.labelsize'] = 30
    plt.rcParams['ytick.labelsize'] = 30
 
    dr_bar=[]
    for i in range(len(R_global)):
        if i%10==0:
            aux_ = sum(R_global[i][0])
            dr_bar.append(aux_)
    dr_bar.append(sum_dr_oma)
    

    plt.bar(x_index,dr_bar,color = color_[0])
    


    plt.xticks(x_index, fontsize=15,rotation = 45)
    plt.xlabel('Multiple Access Techniques',fontsize=30, weight='bold')
    plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
    

    plt.title('Data rate NOMA x OMA system',fontsize=30, weight='bold')
    plt.grid(True)

    plt.show()
