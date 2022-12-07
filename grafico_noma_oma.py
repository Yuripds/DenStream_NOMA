import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mean 
import main_oma as oma
import pandas as pd

sns.set()
def grafico_oma_noma(R_global):
    ############################################################################################# OMA 

    train_t0 = pd.read_csv('/home/yuri/Documentos/github/DenStream_NOMA/csv_ganhos_de_canal/usuarioRotulos_sort_df_15_.csv')
    train_t1 = pd.read_csv('/home/yuri/Documentos/github/DenStream_NOMA/csv_ganhos_de_canal/usuarioRotulos_sort_df_87_.csv')
    train_t2 = pd.read_csv('/home/yuri/Documentos/github/DenStream_NOMA/csv_ganhos_de_canal/usuarioRotulos_sort_df_150_.csv')
    train_t3 = pd.read_csv('/home/yuri/Documentos/github/DenStream_NOMA/csv_ganhos_de_canal/usuarioRotulos_sort_df_208_.csv')
    train_t4 = pd.read_csv('/home/yuri/Documentos/github/DenStream_NOMA/csv_ganhos_de_canal/usuarioRotulos_sort_df_227_.csv')

    dados_t0 = np.array(train_t0[["Ganho","Rotulo"]])
    dados_t1 = np.array(train_t1[["Ganho","Rotulo"]])
    dados_t2 = np.array(train_t2[["Ganho","Rotulo"]])
    dados_t3 = np.array(train_t3[["Ganho","Rotulo"]])
    dados_t4 = np.array(train_t4[["Ganho","Rotulo"]])


    sum_dr_oma_t0,_t0 = oma.simulacao_OMA(dados=dados_t0)
    sum_dr_oma_t1,_t1 = oma.simulacao_OMA(dados=dados_t1)
    sum_dr_oma_t2,_t2 = oma.simulacao_OMA(dados=dados_t2)
    sum_dr_oma_t3,_t3 = oma.simulacao_OMA(dados=dados_t3)
    sum_dr_oma_t4,_t4 = oma.simulacao_OMA(dados=dados_t4)


    ############################################################################################# OMA 


    #tempo_gp = 0
    ma_tec = ['NOMA','OMA']
    tempo = ['15','87','150','208','227']
    
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
            aux_ = mean(R_global[i][0])
            dr_bar.append(aux_)
    
    dr_bar_OMA=[sum_dr_oma_t0,sum_dr_oma_t1,sum_dr_oma_t2,sum_dr_oma_t3,sum_dr_oma_t4]
    

    plt.bar(tempo,dr_bar,color = color_[0])
    plt.bar(tempo,dr_bar_OMA,color = 'r')



    plt.xticks(tempo, fontsize=15,rotation = 45)
    plt.xlabel('time',fontsize=30, weight='bold')
    plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
    plt.legend(("NOMA","OMA"))

    plt.title('Data rate NOMA x OMA system',fontsize=30, weight='bold')
    plt.grid(True)

    plt.show()
