import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
import statistics

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

    ganhos.append(g_aux)
    potencias.append(alloc_power(g_aux,0.2))
    
    var_aux=var_aux+1
    if var_aux > len(indices_list)-1:
        var_aux = 0

        

############################################ Implementar sinal recebido #######################################################

### gerando simbolos
def gerar_sinais_function(potencias, SNR_dB):
    
    conjunto_de_sinais = []
    conjunto_de_sinais_ruido = []
    conjunto_de_simbolos =[]

    for indice_i,i in enumerate(potencias):
        #### gerar simbolos para cada usuario
        simbolos_aux = []
        for usuarios in range(len(i[0])):
            simbolos_aux.append(mgraf.plot_M_QAM(M=4, N=1000))
        
        for simb_l in simbolos_aux:
            conjunto_de_simbolos.append(simb_l)


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


        sinal_tx_ruido= mgraf.add_ruido(sinal_sup, SNR_dB)

        conjunto_de_sinais.append(sinal_sup)
        conjunto_de_sinais_ruido.append(sinal_tx_ruido)

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

    parte_real = np.real(sinal)
    parte_imaginaria= np.imag(sinal)

    sinal_demodulado = []
    for i in range(len(sinal)):
        if parte_real[i]<0 and parte_imaginaria[i]< 0 :
            sinal_demodulado.append((-1 + 1j *-1))
        if parte_real[i]>=0 and parte_imaginaria[i]> 0 :
            sinal_demodulado.append((1 + 1j *1))
        if parte_real[i]<0 and parte_imaginaria[i]>= 0 :
            sinal_demodulado.append((-1 + 1j *1))
        if parte_real[i]>= 0 and parte_imaginaria[i]< 0 :
            sinal_demodulado.append((1 + 1j *-1))

    return sinal_demodulado


def sic(sinal,potencia):
     
    sinal_separado = []
    for idx in range(len(potencia)):
        if idx == 0:
            sinal_separado.append(demodulador(divisao_elemt_list(sinal,np.sqrt(potencia[idx]))))

        if idx == 1:
            sinal_01 = subtracao_listas(sinal,(np.array(sinal_separado[0])*np.sqrt(potencia[idx-1])).tolist())
            sinal_separado.append(demodulador(divisao_elemt_list(sinal_01,np.sqrt(potencia[idx]))))               

        if idx ==2 and potencia[idx]>0:
            sinal_02_aux = subtracao_listas(sinal,(np.array(sinal_separado[0])*np.sqrt(potencia[idx-2])).tolist())
            sinal_02 = subtracao_listas(sinal_02_aux,(np.array(sinal_separado[1])*np.sqrt(potencia[idx-1])).tolist())
            sinal_separado.append(demodulador(divisao_elemt_list(sinal_02,np.sqrt(potencia[idx]))))         

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

snr_vect = [5,10,15]
erro_p_snr = []

for snr in snr_vect:
    conjunto_de_sinais,conjunto_de_sinais_ruido,conjunto_de_simbolos = gerar_sinais_function(potencias, SNR_dB=snr)

    sinais_pos_sic = []
    for i in range(len(conjunto_de_sinais)):  
        sinais_pos_sic.append(sic(conjunto_de_sinais_ruido[i],potencias[i][0]))

    vetor_erro = []
    ##################################################### verificar a partir daqui
    for i_c_simbolos,c_simbolos in enumerate(conjunto_de_simbolos):
        erro_aux = np.zeros((1,3))*np.NAN
        for sinal_id,sinal in enumerate(c_simbolos):
           erro_aux[0][sinal_id] = SER(sinais_pos_sic[i_c_simbolos][sinal_id],sinal)
        vetor_erro.append(erro_aux[0].tolist())

    erro_p_snr.append(vetor_erro)


################################################ Gráficos ####################################################################
########################### criar varios vetores por faixa de potencia 
#### calculando a média
erro_media = []
faixa_potencias = []
for id,erros_c in enumerate(snr_vect):
    erro_media_aux = []
    faixa_potencias_aux =[]

    erro_pot_aux = []
    for j in range(len(erros_c)):
        erro_pot_aux.append([erros_c[j][0],erros_c[j][1],erros_c[j][2],potencias[j][0],potencias[j][1],potencias[j][2]])
    
    erro_pot_aux.sort(key = lambda k: k[3])
    
    erro_aux_split = []
    for x in erro_aux:
        erro_aux_split.append(np.split(erro_pot_aux,3))
    ####
   ############################# corrigir isso

    for spt in erro_aux_split:
        
        aux_p1 = []
        for j in spt:
            aux_p1.append([min(j[int(len(j)/2):len(j)]),max(j[int(len(j)/2):len(j)])])
        
        aux_e2 =[]
        for col in range(len(spt[0])):
            aux_e1 =[]
            for linha in range(len(spt)):
                aux_e1.append(spt[linha][col])
            aux_e2.append(statistics.mean(aux_e1))
        erro_media_aux.append(aux_e2)
        faixa_potencias_aux.append(aux_p1)
   
    faixa_potencias.append(faixa_potencias_aux)
    erro_media.append(erro_media_aux) 


curvas=[]
for faixa in range(3):
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
    


################### corrigir esse gráfico em seguida

eu_label = ['EU_01_f0','EU_02_f0','EU_03_f0','EU_01_f1','EU_02_f1','EU_03_f1','EU_01_f2','EU_02_f2','EU_03_f2']

for curva_id,curva in enumerate(curvas) :
    plt.plot(snr_vect, curva, label = eu_label[curva_id], linestyle="-") 

plt.legend() 
plt.show()

















################ Próximos passos 
#    1-  Gerar csv com ganho complexo e coeficiente de potencia dos usuários do cluster 0  ------------------ Feito
#    2-  Implementar modulação 4-QAM ------------------------------------------------------------------------ Feito
#    3-  Implentar o sinal recebido para diferentes valores de SINR (0 a 25 dB) ----------------------------- Feito
#    4-  Calculo da BER (tem que implementar o SIC) --------------------------------------------------------- Feito
#    5-  2 Gráficos 2D do meu método e do método tradicional.  BER x SINR ----------------------------------- Fazendo
