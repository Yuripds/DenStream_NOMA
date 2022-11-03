import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

def graficos_plot(drList,R_global):

    tempo_gp = 0

    x_index = range(len(drList[tempo_gp][0]))

    
    color = ['navy','darkblue','mediumblue','b','royalblue','midnightblue','cornflowerblue','dodgerblue','deepskyblue','skyblue','lightskyblue']


    plt.rcParams['xtick.labelsize'] = 30
    plt.rcParams['ytick.labelsize'] = 30


    plt.figure(figsize=(10,8))


    lab = []
    max =0
    for i in range(len(drList[tempo_gp][0])):
        output = drList[tempo_gp][0][i][np.isfinite(drList[tempo_gp][0][i])]
        if len(output)>max:
            max = len(output)
    
    for i in range(max):
        lab.append('r'+ str(i))

            
    va_final = []
    for r in range(max):
        variavel_auxiliar=[]
        for i in range(len(drList[tempo_gp][0])):
            variavel_auxiliar.append(drList[tempo_gp][0][i][r][0])
        va_final.append(variavel_auxiliar)

    
    x1 = np.arange(len(x_index))
    

    barWidth = 0.10
    
    for l in range(max):
        lista=[]
        for j in range(len(va_final[l])):
            lista.append(va_final[l][j][0])
        plt.bar([x + barWidth for x in x1],lista, width=barWidth, label = lab[l] , color = color[l])
        x1 = [x + barWidth for x in x1]

    plt.bar([x + barWidth for x in x1],R_global[tempo_gp][0], width=barWidth, label = "R" , color = 'k')
    



    plt.xticks([x + barWidth for x in np.arange(len(x_index))], x_index)
    plt.xlabel('index cluster tx',fontsize=30, weight='bold')
    plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
    plt.legend(loc='upper right',fontsize=30)

    plt.title('Data rate NOMA system',fontsize=30, weight='bold')
    plt.grid(True)
    
    plt.show()

    
   ######################################################################################################################3
        
    tempo_gp = 10


    lab = []
    max =0
    for i in len(drList[tempo_gp][0]):
        output = drList[tempo_gp][0][i][np.isfinite(drList[tempo_gp][0][i])]
        if len(output)>max:
            max = len(output)
    
    for i in range(max):
        lab.append('r'+ str(i))


    va_final = []
    for r in range(max):
        variavel_auxiliar=[]
        for i in range(len(drList[tempo_gp][0])):
            variavel_auxiliar.append(drList[tempo_gp][0][i][r][0])
        va_final.append(variavel_auxiliar)


 
    x_index = range(len(drList[tempo_gp][0]))
    x1 = np.arange(len(x_index))

    for l in range(max):
        lista=[]
        for j in range(len(va_final[l])):
            lista.append(va_final[l][j][0])
        plt.bar([x + barWidth for x in x1],lista, width=barWidth, label = lab[l] , color = color[l])
        x1 = [x + barWidth for x in x1]

    plt.bar([x + barWidth for x in x1],R_global[tempo_gp][0], width=barWidth, label = "R" , color = 'k')




    plt.xticks([x + barWidth for x in np.arange(len(x_index))], x_index)
    plt.xlabel('index cluster tx',fontsize=30, weight='bold')
    plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
    plt.legend(loc='upper right',fontsize=30)

    plt.title('Data rate NOMA system',fontsize=30, weight='bold')
    plt.grid(True)
    
    plt.show()
   ######################################################################################################################3


    tempo_gp = 20


    lab = []
    max =0
    for i in len(drList[tempo_gp][0]):
        output = drList[tempo_gp][0][i][np.isfinite(drList[tempo_gp][0][i])]
        if len(output)>max:
            max = len(output)
    
    for i in range(max):
        lab.append('r'+ str(i))

    va_final = []
    for r in range(max):
        variavel_auxiliar=[]
        for i in range(len(drList[tempo_gp][0])):
            variavel_auxiliar.append(drList[tempo_gp][0][i][r][0])
        va_final.append(variavel_auxiliar)



    x_index = range(len(drList[tempo_gp][0]))
    x1 = np.arange(len(x_index))

    for l in range(max):
        lista=[]
        for j in range(len(va_final[l])):
            lista.append(va_final[l][j][0])
        plt.bar([x + barWidth for x in x1],lista, width=barWidth, label = lab[l] , color = color[l])
        x1 = [x + barWidth for x in x1]

    plt.bar([x + barWidth for x in x1],R_global[tempo_gp][0], width=barWidth, label = "R" , color = 'k')




    plt.xticks([x + barWidth for x in np.arange(len(x_index))], x_index)
    plt.xlabel('index cluster tx',fontsize=30, weight='bold')
    plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
    plt.legend(loc='upper right',fontsize=30)

    plt.title('Data rate NOMA system',fontsize=30, weight='bold')
    plt.grid(True)
    
    plt.show()
   ######################################################################################################################3

    tempo_gp = 30

    lab = []
    max =0
    for i in len(drList[tempo_gp][0]):
        output = drList[tempo_gp][0][i][np.isfinite(drList[tempo_gp][0][i])]
        if len(output)>max:
            max = len(output)
    
    for i in range(max):
        lab.append('r'+ str(i))


    va_final = []
    for r in range(max):
        variavel_auxiliar=[]
        for i in range(len(drList[tempo_gp][0])):
            variavel_auxiliar.append(drList[tempo_gp][0][i][r][0])
        va_final.append(variavel_auxiliar)


    x_index = range(len(drList[tempo_gp][0]))
    x1 = np.arange(len(x_index))

    for l in range(max):
        lista=[]
        for j in range(len(va_final[l])):
            lista.append(va_final[l][j][0])
        plt.bar([x + barWidth for x in x1],lista, width=barWidth, label = lab[l] , color = color[l])
        x1 = [x + barWidth for x in x1]

    plt.bar([x + barWidth for x in x1],R_global[tempo_gp][0], width=barWidth, label = "R" , color = 'k')




    plt.xticks([x + barWidth for x in np.arange(len(x_index))], x_index)
    plt.xlabel('index cluster tx',fontsize=30, weight='bold')
    plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
    plt.legend(loc='upper right',fontsize=30)

    plt.title('Data rate NOMA system',fontsize=30, weight='bold')
    plt.grid(True)
    
    plt.show()
   ######################################################################################################################3


    tempo_gp = 40

    lab = []
    max =0
    for i in len(drList[tempo_gp][0]):
        output = drList[tempo_gp][0][i][np.isfinite(drList[tempo_gp][0][i])]
        if len(output)>max:
            max = len(output)
    
    for i in range(max):
        lab.append('r'+ str(i))


    va_final = []
    for r in range(max):
        variavel_auxiliar=[]
        for i in range(len(drList[tempo_gp][0])):
            variavel_auxiliar.append(drList[tempo_gp][0][i][r][0])
        va_final.append(variavel_auxiliar)


    x_index = range(len(drList[tempo_gp][0]))
    x1 = np.arange(len(x_index))

    for l in range(max):
        lista=[]
        for j in range(len(va_final[l])):
            lista.append(va_final[l][j][0])
        plt.bar([x + barWidth for x in x1],lista, width=barWidth, label = lab[l] , color = color[l])
        x1 = [x + barWidth for x in x1]

    plt.bar([x + barWidth for x in x1],R_global[tempo_gp][0], width=barWidth, label = "R" , color = 'k')




    plt.xticks([x + barWidth for x in np.arange(len(x_index))], x_index)
    plt.xlabel('index cluster tx',fontsize=30, weight='bold')
    plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
    plt.legend(loc='upper right',fontsize=30)

    plt.title('Data rate NOMA system',fontsize=30, weight='bold')
    plt.grid(True)
    
    plt.show()


######################## Gráfico 2 --  quantidade de clusters no tempo #########################################

    max_lcluster = 0
    for i in range(len(R_global)):
        if len(R_global[i][0]) > max_lcluster:
            max_lcluster = len(R_global[i][0])
        
    label_c = []
    for i in range(max_lcluster):
        label_c.append('Cluster '+ str(i))


    ####### quantidade de clusters em cada tempo
    qtd_c_list = []
    for i in range(len(R_global)):
        qtd_c_list.append(len(R_global[i][0]))


    ####### número de usuários em cada cluster, em cada tempo
    qtd_clusters=[]
    for j in range(len(drList)):
        qtd_clusters_aux = []
        for i in range(len(drList[j][0])):
            qtd_clusters_aux.append(len(drList[j][0][i][np.isfinite(drList[j][0][i])]))
        qtd_clusters.append(qtd_clusters_aux)
           



    # Plota as barras
    plt.figure(figsize=(25,10))

    max_qtd_clusters =0
    for i in qtd_clusters:
        if len(i)>max_qtd_clusters:
            max_qtd_clusters=len(i)

    
    vetorBase = np.zeros((10,max_qtd_clusters))*np.NAN
    var =0
    for i in range(10):
        for j in range(len(qtd_clusters[var])):
            vetorBase[i][j] = qtd_clusters[var][j]
        var =var+5
        

################################################################################## verificar este grafico ###############################################################

    cluster =[]
    idx_aux=0
    for m in range(len(vetorBase[idx_aux])):
        aux_v = []
        for k in range(len(vetorBase)):
            aux_v.append(vetorBase[k][m])
        cluster.append(aux_v)
        idx_aux =idx_aux+1


    x1 = np.arange(len(cluster[0]))
    for k in range(len(cluster)):
        plt.bar([x + 0.15 for x in x1], cluster[k], width=0.15, label = label_c[k] , color = color[k])
        x1 = [x + 0.15 for x in x1]

    # coloca o nome no label do eixo x
    tempo = range(0,500,50)
    plt.xticks([x + 0.25 for x in np.arange(len(cluster[0]))], tempo)
    plt.xlabel('Time',fontsize=30, weight='bold')
    plt.ylabel('User quantity in a cluster',fontsize=30, weight='bold')

    # inseri uma legenda no gráfico
    plt.legend(loc='upper right',fontsize=30)

    plt.title("User in a cluster x Time",fontsize=30, weight='bold')
    
    plt.show()
