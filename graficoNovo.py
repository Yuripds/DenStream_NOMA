import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mean 
import main_oma as oma
import pandas as pd

sns.set()


def zero_to_nan(list_zero):

    listnan = list_zero
    for i in range(len(listnan)) :
        if listnan[i]==0:
            listnan[i] = np.nan


    return listnan

def grafico_novo_plot(drList):
    
    plt.rcParams['xtick.labelsize'] = 30
    plt.rcParams['ytick.labelsize'] = 30

    fig = plt.figure(figsize=(10,8))


    plot_01 =[]
    plot_02 =[]
    plot_03 =[]
    plot_04 =[]
    plot_05 =[]
    plot_06 =[]
    plot_07 =[]
    plot_08 =[]
    for i in range(len(drList)):
        plot_01_aux =[]
        plot_02_aux =[]
        plot_03_aux =[]
        plot_04_aux =[]
        plot_05_aux =[]
        plot_06_aux =[]
        plot_07_aux =[]
        plot_08_aux =[]

        for j in drList[i][0]:
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
            elif(len(cluster)  ==8):
                plot_08_aux.append(sum(cluster))


        if len(plot_01_aux) ==0:
            plot_01.append(0)
        else:
            plot_01.append(mean(plot_01_aux))
        
        if len(plot_02_aux) ==0:
            plot_02.append(0)
        else:
            plot_02.append(mean(plot_02_aux))
        
        if len(plot_03_aux) ==0:
            plot_03.append(0)
        else:
            plot_03.append(mean(plot_03_aux))

        if len(plot_04_aux) ==0:
            plot_04.append(0)
        else:
            plot_04.append(mean(plot_04_aux))


        if len(plot_05_aux) ==0:
            plot_05.append(0)
        else:
            plot_05.append(mean(plot_05_aux))

        if len(plot_06_aux) ==0:
            plot_06.append(0)
        else:
            plot_06.append(mean(plot_06_aux))
        
        if len(plot_07_aux) ==0:
            plot_07.append(0)
        else:
            plot_07.append(mean(plot_07_aux))
        
        if len(plot_08_aux) ==0:
            plot_08.append(0)
        else:
            plot_08.append(mean(plot_08_aux))
        
    
    
    plot_01 = zero_to_nan(plot_01)
    plot_02 = zero_to_nan(plot_02)
    plot_03 = zero_to_nan(plot_03)
    plot_04 = zero_to_nan(plot_04)
    plot_05 = zero_to_nan(plot_05)
    plot_06 = zero_to_nan(plot_06)
    plot_07 = zero_to_nan(plot_07)
    plot_08 = zero_to_nan(plot_08)

    tempo = [18,27,37,48,59,69,80,91,103,115,125,136,147,159,171,183,195,208,220,230,241,251,262,274,286,298,309,321,333,345,354,364,376,386,396,404,412,420,427,434,439,444,448,453,458,463,468,476,484,493]
    #for i in range(len(drList)):
    #    tempo.append(' '+ str(i+12))
    


    plt.plot(tempo,plot_01,marker='o',label="1 UE")
    plt.plot(tempo,plot_02,marker='v',label="2 UE")
    plt.plot(tempo,plot_03,marker='s',label="3 UE")
    plt.plot(tempo,plot_04,marker='1',label="4 UE")
    plt.plot(tempo,plot_05,marker='x',label="5 UE") 
    plt.plot(tempo,plot_06,marker="P",label="6 UE") 
    plt.plot(tempo,plot_07,marker="d",label="7 UE") 
    plt.plot(tempo,plot_08,marker="*",label="8 UE") 

    plt.xticks(tempo, fontsize=10,rotation = 45)
    plt.xlabel('time',fontsize=15, weight='bold')
    plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
    plt.legend(loc='best',fontsize=30)

    plt.title('Data rate NOMA system',fontsize=30, weight='bold')
    plt.grid(True)
    
    
    plt.show()