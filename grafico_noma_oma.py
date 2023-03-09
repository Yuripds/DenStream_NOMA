import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mean 
import main_oma as oma
import pandas as pd
from matplotlib import ticker


sns.set()
def grafico_oma_noma(R_global):
    ############################################################################################# OMA 

    train_t0 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/csv_ganhos_de_canal/usuarioRotulos_sort_df_18_.csv')
    train_t1 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/csv_ganhos_de_canal/usuarioRotulos_sort_df_89_.csv')
    train_t2 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/csv_ganhos_de_canal/usuarioRotulos_sort_df_164_.csv')
    train_t3 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/csv_ganhos_de_canal/usuarioRotulos_sort_df_236_.csv')
    train_t4 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/csv_ganhos_de_canal/usuarioRotulos_sort_df_308_.csv')

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
    tempo = ['18','89','164','236','308']
    
    #n_lusters= len(R_global[tempo_gp][0])
    #x_index = []
    #for i in range(n_lusters):
    #    x_index.append('NOMA C'+str(i)) 
    #x_index.append('OMA')
        
    color_ = ['darkblue','mediumblue','b','royalblue','midnightblue','cornflowerblue','dodgerblue','deepskyblue','skyblue','lightskyblue']

    fig, ax = plt.subplots()
    
    plt.rcParams['xtick.labelsize'] = 30
    plt.rcParams['ytick.labelsize'] = 30
 
    dr_bar=[]
    for i in range(len(R_global)):
        if i%10==0:
            aux_ = mean(R_global[i][0])
            dr_bar.append(aux_)
    
    dr_bar_OMA=[sum_dr_oma_t0,sum_dr_oma_t1,sum_dr_oma_t2,sum_dr_oma_t3,sum_dr_oma_t4]

    #pot = np.log10(dr_bar)
    #label = f"x10$^{pot}$"
    

    plt.bar(tempo,dr_bar,color = color_[0])
    plt.bar(tempo,dr_bar_OMA,color = 'r')


   

    plt.xticks(tempo, fontsize=30,rotation = 45)
    plt.xlabel('time',fontsize=30, weight='bold')
    formatter = ticker.ScalarFormatter(useMathText=True)
    formatter.set_scientific(True) 
    formatter.set_powerlimits((-1,1)) 
    
    ax.yaxis.set_major_formatter(formatter) 
    plt.yticks(fontsize=30)

    plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
    plt.legend(("NOMA","OMA") ,loc=4,prop={'size': 40})

    plt.title('Data rate NOMA x OMA system',fontsize=30, weight='bold')
    plt.grid(True)

    plt.show()
