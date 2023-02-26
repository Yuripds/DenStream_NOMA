import numpy as np
import pandas as pd
import cmath
import geradorGanhoCanal as ggc
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

def alloc_power(gamaL,alpha):
  p_list = []

  den = 0
  for i in range(len(gamaL)):
    den = den + ((abs(gamaL[-1])/abs(gamaL[i]))**(alpha))

  for i in range(len(gamaL)):
    p = ((abs(gamaL[-1])/abs(gamaL[i]))**(alpha)) / den
    p_list.append(p)

  return p_list


def data_rate(w,B,Pt,gamaUser,N0,p_list,index):
 
  num = p_list[index]*Pt*gamaUser

  p_list = p_list[index+1:]
  p_array = np.array(p_list)
  den_list = p_array*Pt*gamaUser

  den = np.sum(den_list)
  den = den+(w*(N0*B))
  r = w*B*np.log2(1+(num/den))

  return r


def sum_data_rate(gamaL,alpha,B,N0,Pt):
    w =100
    gamaL.sort()
    p_list = alloc_power(gamaL,alpha)
    #print("p_list: ",p_list)
    
    r_array = np.ones((12,1))
    r_array[:] = float(np.NaN)
    
    for ind in range(len(gamaL)):
        gamaUser = gamaL[ind]
        r = data_rate(w,B,Pt,gamaUser,N0,p_list,ind)
        #print("r_teste: ", r)
        r_array[ind] = r

    output = r_array[np.isfinite(r_array)]
    R_global = np.sum(output)

    return r_array,R_global


def formacao_de_pares(dados):
    pares = []
    aux = 1
    
    for i in range(int(len(dados)/2)):
        pares.append([dados.iloc[i].tolist(), dados.iloc[len(dados)-aux].tolist()])
        aux =aux+1

    ordem_padrao=[]
    for m in range(len(pares)):
        ordem_padrao.append([pares[m][0][0],pares[m][1][0]])

    return pares,ordem_padrao



def metodo_padrao(qtd_usuarios,seed_):

    ########################################### gerando amostras ######################################

    #### tenho que mudar o seed
    flag = "metodo_padrao"
    _d,dGlobal = ggc.desvanecimento_global_usuarios(qtd_usuarios,flag,seed_)


    h=np.zeros((3,qtd_usuarios))
    for i in range(qtd_usuarios):
        h[0][i] = i
        h[1][i] = abs(dGlobal[i][0])    
        h[2][i] = cmath.phase(dGlobal[i][0])
    
    h=h.T


    train = pd.DataFrame(data=h,columns=['index','Ganho','Fase'])
    

    df_dGlobal = pd.DataFrame(dGlobal)
    
    ############# definindo a primeira ordem, que vai permanecer até o fim do algortimo
    train = train.sort_values(by='Ganho', ascending=False)
    _,ordem_padrao = formacao_de_pares(train)

    # calulo do data rate da primeira simulação ao longo do tempo

    alpha=0.2
    N0 =10**(-17.3)
    B=180*(10**3)
    Pt = ((10**(4.6))*(10**-3))

    ####### rodar isto 100 vezes e tirar uma média, para  cada simulação eu devo gerar novos canais mudando o seed
    dr_global_final = []
    for t in range(1000):
        dr_global = []
        for i in range(len(ordem_padrao)):
            gamaL = []
            cluster = [abs(dGlobal[int(ordem_padrao[i][0])][t]),abs(dGlobal[int(ordem_padrao[i][1])][t])]
            for m in range(len(cluster)):
                gamaL.append(cluster[m])
            _r,R_global = sum_data_rate(gamaL,alpha,B,N0,Pt)
            dr_global.append(R_global)

        dr_global_final.append(np.mean(dr_global))
    

    return dr_global_final





def sim_mc():
    qtd_usuarios = 12

    dr_sim =[]
    sim=0
    seed_ =0
    while(sim<100):
        dr_sim.append(metodo_padrao(qtd_usuarios,seed_))
        sim=sim+1
        seed_ = seed_+qtd_usuarios

    return dr_sim


############## gerar grafico #######################
def media(listas):
    array_listas = []
    for i in listas:
        array_listas.append(np.array(i))

    array_listas = np.array(array_listas)

    lista_media = []
    for j in range(len(array_listas[0])):
        lista_media.append(np.mean(array_listas[:, j]))

    return lista_media

def grafico_mp():

    ########### ainda tenho que tirar a média ######################
    dr_sim = sim_mc()

    dr_sim_media =  media(dr_sim)

    plt.figure(figsize=(8,6))
    plt.xticks(rotation=45)
    plt.xlabel('time',fontsize=30, weight='bold')
    plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')

    plt.title('Data rate - standard method',fontsize=30, weight='bold')
    sns.set_theme(style="darkgrid")
    sns.lineplot(data=dr_sim_media, color='red')


    plt.show()



grafico_mp()

