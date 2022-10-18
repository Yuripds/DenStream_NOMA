import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

def grafico_novo_plot(drList,qtd_usuarios):
    
    plt.rcParams['xtick.labelsize'] = 30
    plt.rcParams['ytick.labelsize'] = 30

    plt.rcParams["savefig.bbox"] = 'standard'
    plt.rcParams["savefig.pad_inches"] = 1.0

    fig = plt.figure(figsize=(10,8))


    plot_01 =[]
    plot_02 =[]
    plot_03 =[]
    plot_04 =[]
    plot_05 =[]
    plot_06 =[]
    plot_07 =[]
   ####### somar o data rate depois do segundo loop / verificar o funcionamento desse codigo
    for i in range(len(drList)):
        plot_01_aux =[]
        plot_02_aux =[]
        plot_03_aux =[]
        plot_04_aux =[]
        plot_05_aux =[]
        plot_06_aux =[]
        plot_07_aux =[]

        for j in drList[i]:
            cluster = j[~(np.isnan(j))]
            if (len(cluster) ==1):
                plot_01_aux.append(sum(cluster))
            elif (len(cluster) ==2):
                plot_02_aux.append(sum(cluster))
            elif(len(cluster)  ==3):
                plot_03_aux.append(sum(cluster))
            elif(len(cluster)  ==4):
                plot_04_aux.append(sum(cluster))   
            elif(len(cluster)  ==5):
                plot_05_aux.append(sum(cluster))
            elif(len(cluster)  ==6):
                plot_06_aux.append(sum(cluster))
            elif(len(cluster)  ==7):
                plot_07_aux.append(sum(cluster))

            plot_01.append(sum(plot_01_aux))
            plot_02.append(sum(plot_02_aux))
            plot_03.append(sum(plot_03_aux))
            plot_04.append(sum(plot_04_aux))
            plot_05.append(sum(plot_05_aux))
            plot_06.append(sum(plot_06_aux))
            plot_07.append(sum(plot_07_aux))

            





    tempo = []
    for i in range(len(drList)):
        tempo.append('t'+ str(i))
    



    plt.xticks(tempo)
    plt.xlabel('time',fontsize=30, weight='bold')
    plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
    plt.legend(loc='upper right',fontsize=30)

    plt.title('Data rate NOMA system',fontsize=30, weight='bold')
    plt.grid(True)
    
    plt.savefig('../graficos/'+qtd_usuarios+'usuarios/fig01.png', dpi=fig.dpi)
    plt.show()
