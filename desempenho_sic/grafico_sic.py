import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
import statistics
import joblib
from joblib import Parallel, delayed
import multiprocessing


import sys
sys.path.insert(0, '/home/yuripedro/Documentos/Git hub/DenStream_NOMA' )
import geradorGanhoCanal as ggc


import desempenho_sic.modulacao_grafico as mgraf

sns.set()

############################################ Gerar ganho de canal #############################################################
qtd_usuarios = 12
flag ="metodo_proposto"
tamanho_v = 10**4
d,dGlobal = ggc.desvanecimento_global_usuarios(qtd_usuarios,flag,tamanho_v)

############################################ calcular potencias  ##############################################################

def alloc_power(gamaL,alpha):
  Pt = ((10**(4.6))*(10**-3))
  p_list = []

  den = 0
  for i in range(len(gamaL)):
    den = den + ((abs(gamaL[-1])/abs(gamaL[i]))**(alpha))

  for i in range(len(gamaL)):
    p = Pt* (((abs(gamaL[-1])/abs(gamaL[i]))**(alpha)) / den)
    p_list.append(p)

  aux = np.zeros((1,3))*np.NAN
  for id,valor in enumerate(p_list):
      aux[0][id] = valor

  p_list_final = aux.tolist()

  return p_list_final


indices_list = []
for i in range(325):
    indices_df = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_indece_grafico3/usuario_id_df'+str(i+1)+'_.csv').drop(['Unnamed: 0'], axis=1)
    indices_list.append(indices_df.iloc[0].tolist())

##### calcular potencias e ganho e salvar em uma estrutura de dados

ganhos = []
potencias = []
var_aux = 0
for i in range(len(dGlobal[0])):

    indice_aux = []
    for m in indices_list[var_aux]:
        indice_aux.append(m-1)

    gcanal = dGlobal[indice_aux]

    g_aux = []
    for j in gcanal:
        g_aux.append(abs(j[i]))

    g_aux.sort()
    ganhos.append(g_aux)
    potencias.append(alloc_power(g_aux,0.3))
    
    var_aux=var_aux+1
    if var_aux > len(indices_list)-1:
        var_aux = 0

        

############################################ Implementar sinal recebido #######################################################

### gerando simbolos
def gerar_sinais_function(potencias,ganhos, SNR_dB):
    
    conjunto_de_sinais = []
    conjunto_de_sinais_ruido = []
    conjunto_de_simbolos =[]

    for indice_i,i in enumerate(potencias):
        #### gerar simbolos para cada usuario
        simbolos_aux = []
        for usuarios in range(len(i[0])):
            if (i[0][usuarios]) > 0:
                simbolos_aux.append(mgraf.plot_M_QAM(M=4, N=10**3))

        conjunto_de_simbolos.append(simbolos_aux)
  
        #### realiza a multiplicação da potencia com o simbolo
        sinal_aux = []
        for sinal in range(len(i[0])):
            if (np.sqrt(potencias[indice_i][0][sinal])) > 0:
                sinal_aux.append(simbolos_aux[sinal]*np.sqrt(potencias[indice_i][0][sinal]))
                
 
        #### sobrepoe os sinais gerados na etapa anterior
        sinal_sup = []
        for coluna in range(len(sinal_aux[0])):
            mult_aux = []
            for linha in range(len(sinal_aux)):
                mult_aux.append(sinal_aux[linha][coluna])
            sinal_sup.append(sum(mult_aux))

        sinal_sup_aux  = []
        sinal_sup_aux_ruido = []
        for g in ganhos[indice_i]:
            sinal_sup_aux.append(np.multiply(sinal_sup, g).tolist())
            sinal_sup_aux_ruido.append(mgraf.add_ruido(np.multiply(sinal_sup, g).tolist(), SNR_dB))

         
        conjunto_de_sinais.append(sinal_sup_aux)
        conjunto_de_sinais_ruido.append(sinal_sup_aux_ruido)

    return conjunto_de_sinais,conjunto_de_sinais_ruido,conjunto_de_simbolos


############################################## calculo da BER #################################################################

################################################ aparentemente esta tudo certo e finalizado ##################################
def subtracao_listas(sinail_01,sinal_02):

    c=[sinail_01,sinal_02]
    sinal_subtraido = []
    for coluna in range(len(c[0])):
        sinal_subtraido.append(c[0][coluna] - c[1][coluna])

    return sinal_subtraido


def divisao_elemt_list(lista, numero):

    divisao = []
    for l in lista:
        divisao.append(l/numero)

    return divisao

def demodulador(sinal):

    sinal_demodulado = []
    
    gabarito = [1+1j , 1-1j ,-1-1j ,-1+1j  ]
    for i in range(len(sinal)):
        dist = []
        for j in range(len(gabarito)):
            dist.append(np.linalg.norm(sinal[i]-gabarito[j]))

        menor_dist_idx = 0
        for k in range(len(dist)):
            if dist[k] == min(dist):
                menor_dist_idx = k
                break
        
        sinal_demodulado.append(gabarito[menor_dist_idx])

    return sinal_demodulado



def sic(sinal,ganho,potencia):
    
    sinal_separado = []
    for idx in range(len(potencia)):
        if idx == 0:
            sinal_separado.append(demodulador(divisao_elemt_list(sinal[idx],np.sqrt(potencia[idx])*ganho[idx] )))

        if idx == 1:
            sp = demodulador(divisao_elemt_list(sinal[idx],np.sqrt(potencia[idx-1])*ganho[idx] ))
            sinal_01 = subtracao_listas(sinal[idx],(np.array(sp)*np.sqrt(potencia[idx-1])).tolist())
            sinal_separado.append(demodulador(divisao_elemt_list(sinal_01,np.sqrt(potencia[idx]))))               

        if idx ==2 and potencia[idx]>0:
            sp_1 = demodulador(divisao_elemt_list(sinal[idx],np.sqrt(potencia[idx-2])*ganho[idx]))
            sp_2 =demodulador(divisao_elemt_list(subtracao_listas(sinal[idx],(np.array(sp_1)*np.sqrt(potencia[idx-2])).tolist()),np.sqrt(potencia[idx-1])) )        
            sp_3 = subtracao_listas(subtracao_listas(sinal[idx],(np.array(sp_1)*np.sqrt(potencia[idx-1])).tolist()) , (np.array(sp_2)*np.sqrt(potencia[idx-2])).tolist())
            sinal_separado.append(demodulador(divisao_elemt_list(sp_3,np.sqrt(potencia[idx]))))
        
    return sinal_separado


def SER(sinal_recebido,sinal_enviado):

    bits_errados = []
    for i in range(len(sinal_recebido)):
        bits_errados.append(sinal_enviado[i] -sinal_recebido[i])

    erro_ = 0
    for i in bits_errados:
        if i != 0:
            erro_ = erro_+1
    
    erro_de_simbolo = erro_/len(sinal_recebido)
    
    return erro_de_simbolo


##############################################  chamada das funções #############################################################


snr_vect = [0,5,10,15,20,25]
#snr_vect = [0,5]

#erro_p_snr = []
#for snr in snr_vect:
def error_calc(snr):
    conjunto_de_sinais,conjunto_de_sinais_ruido,conjunto_de_simbolos = gerar_sinais_function(potencias,ganhos, SNR_dB=snr)

    sinais_pos_sic = []
    for i in range(len(conjunto_de_sinais)):  
        sinais_pos_sic.append(sic(conjunto_de_sinais_ruido[i],ganhos[i],potencias[i][0]))

    vetor_erro = []

    for i_c_simbolos,c_simbolos in enumerate(conjunto_de_simbolos):
        erro_aux = np.zeros((1,3))*np.NAN
        for sinal_id,sinal in enumerate(c_simbolos):
            erro_aux[0][sinal_id] = SER(sinais_pos_sic[i_c_simbolos][sinal_id],sinal)
        vetor_erro.append(erro_aux[0].tolist())

    #erro_p_snr.append(vetor_erro)
    
    return vetor_erro


pool_obj = multiprocessing.Pool()
with pool_obj:
    erro_p_snr=pool_obj.map(error_calc,snr_vect)

################################################ Gráficos ####################################################################
########################### criar varios vetores por faixa de potencia 
#### calculando a média
erro_media = []
faixa_potencias = []
for id,erros_c in enumerate(erro_p_snr):
    erro_media_aux = []
    faixa_potencias_aux =[]

    erro_pot_aux = []
    for j in range(len(erros_c)):
        erro_pot_aux.append([erro_p_snr[id][j][0],erro_p_snr[id][j][1],erro_p_snr[id][j][2],potencias[j][0][0],potencias[j][0][1],potencias[j][0][2]])
    
    erro_pot_aux.sort(key = lambda k: k[3])
    
    erro_aux_split=np.split(np.array(erro_pot_aux),4)
  

    for spt in erro_aux_split:
        
        aux_p1 = []
        for j in spt:
            aux_p1.append([min(j[int(len(j)/2):len(j)]),max(j[int(len(j)/2):len(j)])])
        
        aux_e2 =[]
        for col in range(int(len(spt[0])/2)):
            aux_e1 =[]
            for linha in range(len(spt)):
                aux_e1.append(spt[linha][col])
            if np.isnan(aux_e1).any():
                aux_e1_array = np.array(aux_e1)
                aux_e1_no_nan = aux_e1_array[np.logical_not(np.isnan(aux_e1))]
                aux_e1_no_nan = aux_e1_no_nan.tolist()
                if len(aux_e1_no_nan)>0:
                    aux_e2.append(statistics.mean(aux_e1_no_nan))
                else:
                    aux_e2.append(np.NaN)
            else:
                aux_e2.append(statistics.mean(aux_e1))
        erro_media_aux.append(aux_e2)
        faixa_potencias_aux.append(aux_p1)
   
    faixa_potencias.append(faixa_potencias_aux)
    erro_media.append(erro_media_aux) 


curvas=[]
for faixa in range(4):
    curvas_aux=[]
    for i_snr,valor_snr in enumerate(erro_media):
        curvas_aux.append(valor_snr[faixa][0])
    curvas.append(curvas_aux)
    
    curvas_aux=[]
    for i_snr,valor_snr in enumerate(erro_media):
        curvas_aux.append(valor_snr[faixa][1])
    curvas.append(curvas_aux)

    curvas_aux=[]
    for i_snr,valor_snr in enumerate(erro_media):
        curvas_aux.append(valor_snr[faixa][2])
    curvas.append(curvas_aux)

eu_label = ['EU_01_f0','EU_02_f0','EU_03_f0','EU_01_f1','EU_02_f1','EU_03_f1','EU_01_f2','EU_02_f2','EU_03_f2','EU_01_f3','EU_02_f3','EU_03_f3']
curvas_array = np.array(curvas).T
curvas_df = pd.DataFrame(data=curvas_array,columns=eu_label)
curvas_df.to_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/curvas_df.csv')


marcadores = ["o","v","P","*","X","D","d","^","<",">","1","4"]


for curva_id,curva in enumerate(curvas) :
    if (curva_id not in [2,5,8,11] ):
        if len(curva)>0:
            plt.yscale("log",base=10)
            plt.plot(snr_vect, curva, label = eu_label[curva_id], linestyle="--",marker=marcadores[curva_id]) 
        else:
            continue
    else:
        continue 
    
plt.xticks(snr_vect)
plt.ylabel('Symbol Error Rate',fontsize=30, weight='bold')
plt.xlabel('Es/No, dB',fontsize=30, weight='bold')

plt.legend() 
plt.show()




