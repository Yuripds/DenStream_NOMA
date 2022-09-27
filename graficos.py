import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

def graficos_plot(drList,R_global,qtd_usuarios):

    tempo_gp = 0

    x_index = range(len(drList[tempo_gp]))

    
    color = ['#191970','#000080','#6495ED','#483D8B','	#6A5ACD','#7B68EE','#8470FF','#0000CD','#4169E1','#0000FF','#1E90FF','#00BFFF','#87CEEB','#87CEFA','#B0C4DE','#ADD8E6','#B0E0E6','#AFEEEE']



    plt.rcParams['xtick.labelsize'] = 30
    plt.rcParams['ytick.labelsize'] = 30

    plt.rcParams["savefig.bbox"] ='tight'
    plt.rcParams["savefig.pad_inches"] = 1.0

    fig = plt.figure(figsize=(10,8))


    lab = []
    for i in range(len(drList[tempo_gp][0])):
        lab.append('r'+ str(i))


    va_final = []
    for r in range(len(drList[tempo_gp][0])):
        variavel_auxiliar=[]
        for i in range(len(drList[tempo_gp])):
            variavel_auxiliar.append(drList[tempo_gp][i][r])
        va_final.append(variavel_auxiliar)


    tamanho = len(va_final)
    for h in range(len(va_final)):
        vetor_nanTest = np.isnan(va_final[h])
        if all(vetor_nanTest) :
            tamanho = tamanho - 1


    x1 = np.arange(len(x_index))

    for l in range(tamanho):
        lista=[]
        for j in range(len(va_final[l])):
            lista.append(va_final[l][j][0])
        plt.bar([x + 0.15 for x in x1],lista, width=0.15, label = lab[l] , color = color[l])
        x1 = [x + 0.15 for x in x1]

    plt.bar([x + 0.15 for x in x1],R_global[tempo_gp], width=0.15, label = "R" , color = 'k')




    plt.xticks([x + 0.5 for x in np.arange(len(x_index))], x_index)
    plt.xlabel('index cluster tx',fontsize=30, weight='bold')
    plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
    plt.legend(loc='upper right',fontsize=30)

    plt.title('Data rate NOMA system',fontsize=30, weight='bold')
    plt.grid(True)
    
    plt.savefig('../graficos/'+qtd_usuarios+'usuarios/fig01.png', dpi=fig.dpi)
    plt.show()
   ######################################################################################################################3

    tempo_gp = 10


    lab = []
    for i in range(len(drList[tempo_gp][0])):
        lab.append('r'+ str(i))


    va_final = []
    for r in range(len(drList[tempo_gp][0])):
        variavel_auxiliar=[]
        for i in range(len(drList[tempo_gp])):
            variavel_auxiliar.append(drList[tempo_gp][i][r])
        va_final.append(variavel_auxiliar)


    tamanho = len(va_final)
    for h in range(len(va_final)):
        vetor_nanTest = np.isnan(va_final[h])
        if all(vetor_nanTest) :
            tamanho = tamanho - 1



    x1 = np.arange(len(x_index))

    for l in range(tamanho):
        lista=[]
        for j in range(len(va_final[l])):
            lista.append(va_final[l][j][0])
        plt.bar([x + 0.15 for x in x1],lista, width=0.15, label = lab[l] , color = color[l])
        x1 = [x + 0.15 for x in x1]

    plt.bar([x + 0.15 for x in x1],R_global[tempo_gp], width=0.15, label = "R" , color = 'k')




    plt.xticks([x + 0.5 for x in np.arange(len(x_index))], x_index)
    plt.xlabel('index cluster tx',fontsize=30, weight='bold')
    plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
    plt.legend(loc='upper right',fontsize=30)

    plt.title('Data rate NOMA system',fontsize=30, weight='bold')
    plt.grid(True)
    
    plt.savefig('../graficos/'+qtd_usuarios+'usuarios/fig02.png', dpi=fig.dpi)
    plt.show()
   ######################################################################################################################3


    tempo_gp = 20


    lab = []
    for i in range(len(drList[tempo_gp][0])):
        lab.append('r'+ str(i))


    va_final = []
    for r in range(len(drList[tempo_gp][0])):
        variavel_auxiliar=[]
        for i in range(len(drList[tempo_gp])):
            variavel_auxiliar.append(drList[tempo_gp][i][r])
        va_final.append(variavel_auxiliar)


    tamanho = len(va_final)
    for h in range(len(va_final)):
        vetor_nanTest = np.isnan(va_final[h])
        if all(vetor_nanTest) :
            tamanho = tamanho - 1


    x1 = np.arange(len(x_index))

    for l in range(tamanho):
        lista=[]
        for j in range(len(va_final[l])):
            lista.append(va_final[l][j][0])
        plt.bar([x + 0.15 for x in x1],lista, width=0.15, label = lab[l] , color = color[l])
        x1 = [x + 0.15 for x in x1]

    plt.bar([x + 0.15 for x in x1],R_global[tempo_gp], width=0.15, label = "R" , color = 'k')




    plt.xticks([x + 0.5 for x in np.arange(len(x_index))], x_index)
    plt.xlabel('index cluster tx',fontsize=30, weight='bold')
    plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
    plt.legend(loc='upper right',fontsize=30)

    plt.title('Data rate NOMA system',fontsize=30, weight='bold')
    plt.grid(True)
    
    plt.savefig('../graficos/'+qtd_usuarios+'usuarios/fig03.png', dpi=fig.dpi)
    plt.show()
   ######################################################################################################################3

    tempo_gp = 30


    lab = []
    for i in range(len(drList[tempo_gp][0])):
        lab.append('r'+ str(i))


    va_final = []
    for r in range(len(drList[tempo_gp][0])):
        variavel_auxiliar=[]
        for i in range(len(drList[tempo_gp])):
            variavel_auxiliar.append(drList[tempo_gp][i][r])
        va_final.append(variavel_auxiliar)


    tamanho = len(va_final)
    for h in range(len(va_final)):
        vetor_nanTest = np.isnan(va_final[h])
        if all(vetor_nanTest) :
            tamanho = tamanho - 1


    x1 = np.arange(len(x_index))

    for l in range(tamanho):
        lista=[]
        for j in range(len(va_final[l])):
            lista.append(va_final[l][j][0])
        plt.bar([x + 0.15 for x in x1],lista, width=0.15, label = lab[l] , color = color[l])
        x1 = [x + 0.15 for x in x1]

    plt.bar([x + 0.15 for x in x1],R_global[tempo_gp], width=0.15, label = "R" , color = 'k')




    plt.xticks([x + 0.5 for x in np.arange(len(x_index))], x_index)
    plt.xlabel('index cluster tx',fontsize=30, weight='bold')
    plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
    plt.legend(loc='upper right',fontsize=30)

    plt.title('Data rate NOMA system',fontsize=30, weight='bold')
    plt.grid(True)
    
    plt.savefig('../graficos/'+qtd_usuarios+'usuarios/fig04.png', dpi=fig.dpi)
    plt.show()
   ######################################################################################################################3


    tempo_gp = 40


    lab = []
    for i in range(len(drList[tempo_gp][0])):
     lab.append('r'+ str(i))


    va_final = []
    for r in range(len(drList[tempo_gp][0])):
        variavel_auxiliar=[]
        for i in range(len(drList[tempo_gp])):
            variavel_auxiliar.append(drList[tempo_gp][i][r])
        va_final.append(variavel_auxiliar)


    tamanho = len(va_final)
    for h in range(len(va_final)):
        vetor_nanTest = np.isnan(va_final[h])
        if all(vetor_nanTest) :
            tamanho = tamanho - 1


    x1 = np.arange(len(x_index))

    for l in range(tamanho):
        lista=[]
        for j in range(len(va_final[l])):
            lista.append(va_final[l][j][0])
        plt.bar([x + 0.15 for x in x1],lista, width=0.15, label = lab[l] , color = color[l])
        x1 = [x + 0.15 for x in x1]

    plt.bar([x + 0.15 for x in x1],R_global[tempo_gp], width=0.15, label = "R" , color = 'k')




    plt.xticks([x + 0.5 for x in np.arange(len(x_index))], x_index)
    plt.xlabel('index cluster tx',fontsize=30, weight='bold')
    plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
    plt.legend(loc='upper right',fontsize=30)

    plt.title('Data rate NOMA system',fontsize=30, weight='bold')
    plt.grid(True)
    
    plt.savefig('../graficos/'+qtd_usuarios+'usuarios/fig05.png', dpi=fig.dpi)
    plt.show()



######################## Gráfico 2 --  quantidade de clusters no tempo #########################################

    label_c = []
    for i in range(len(drList[tempo_gp][0])):
        label_c.append('Cluster '+ str(i))


    ####### quantidade de clusters em cada tempo
    qtd_c_list = []
    for i in range(len(drList)):
        qtd_c_list.append(len(drList[i]))

    

    ####### número de usuários em cada cluster, em cada tempo
    qtd_clusters = []
    for i in range(len(drList)):
        aux = []
        for j in range(len(drList[i])):
            vetor_nanTest =  np.isnan(drList[i][j])
            aux.append(len(drList[i][j]) - vetor_nanTest.sum() )
        qtd_clusters.append(aux)


    # Plota as barras
    plt.figure(figsize=(25,10))


    vetorBase = np.zeros((10,len(qtd_clusters[5])))*np.NAN
    var =0
    for i in range(10):
        for j in range(len(qtd_clusters[var])):
            vetorBase[i][j] = qtd_clusters[var][j]
        var =var+5
        


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
    
    plt.savefig('../graficos/'+qtd_usuarios+'usuarios/fig06.png', dpi=fig.dpi)
    plt.show()
