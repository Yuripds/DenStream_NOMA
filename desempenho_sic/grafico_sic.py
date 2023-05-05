import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns


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

  return p_list


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

    for indice_i,i in enumerate(potencias):
        #### gerar simbolos para cada usuario
        simbolos_aux = []
        for usuarios in range(len(i)):
            simbolos_aux.append(mgraf.plot_M_QAM(M=4, N=1000))

        #### realiza a multiplicação da potencia com o simbolo
        sinal_aux = []
        for sinal in range(len(i)):
            sinal_aux.append(simbolos_aux[sinal]*np.sqrt(potencias[indice_i][sinal]))
        
        #### sobrepoe os sinais gerados na etapa anterior
        sinal_sup = []
        for coluna in range(len(sinal_aux[0])):
            mult_aux = []
            for linha in range(len(sinal_aux)):
                mult_aux.append(sinal_aux[linha][coluna])
            sinal_sup.append(sum(mult_aux))


        sinal_tx_ruido=[]
        for j in sinal_sup:
            sinal_tx_ruido.append(mgraf.add_ruido(j, SNR_dB))

        conjunto_de_sinais.append(sinal_sup)
        conjunto_de_sinais_ruido.append(sinal_tx_ruido)

    return conjunto_de_sinais,conjunto_de_sinais_ruido


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



def sic(sinais,potencia):
     
    sinal_separado = []
    for idx,y in enumerate(sinais):
        if idx == 0:
            sinal_separado.append(divisao_elemt_list(y,np.sqrt(potencia[idx])))

        if idx == 1:
            sinal_01 = subtracao_listas(y,sinal_separado[0]*np.sqrt(potencia[idx-1]))
            sinal_separado.append(divisao_elemt_list(sinal_01,np.sqrt(potencia[idx])))               

        if idx ==2:
            sinal_02_aux = subtracao_listas(y,sinal_separado[0]*np.sqrt(potencia[idx-2]))
            sinal_02 = subtracao_listas(sinal_02_aux,sinal_separado[1]*np.sqrt(potencia[idx-1]))
            sinal_separado.append(divisao_elemt_list(sinal_02,np.sqrt(potencia[idx])))         

    return sinal_separado

def demodulador(sinal):

    parte_real = np.real(sinal)
    parte_imaginaria= np.imag(sinal)

    sinal_demodulado = []
    for i in range(len(sinal)):
        if parte_real[i]<0 & parte_imaginaria[i]< 0 :
            sinal_demodulado ==  (-1 + 1j *-1)
        if parte_real[i]>=0 & parte_imaginaria[i]> 0 :
            sinal_demodulado ==  (1 + 1j *1)
        if parte_real[i]<0 & parte_imaginaria[i]>= 0 :
            sinal_demodulado ==  (-1 + 1j *1)
        if parte_real[i]>= 0 & parte_imaginaria[i]< 0 :
            sinal_demodulado ==  (1 + 1j *-1)

    return sinal_demodulado





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




conjunto_de_sinais,conjunto_de_sinais_ruido = gerar_sinais_function(ganhos,potencias, SNR_dB=100)




#sinais_pos_sic = []
#for i in range(len(conjunto_de_sinais)):  
#    sinais_pos_sic.append(sic(conjunto_de_sinais_ruido[i],ganhos[i],potencias[i]))


print("AQUI")








################################################ Gráficos ####################################################################










################ Próximos passos 
#    1-  Gerar csv com ganho complexo e coeficiente de potencia dos usuários do cluster 0  ------------------ Feito
#    2-  Implementar modulação 4-QAM ------------------------------------------------------------------------ Feito
#    3-  Implentar o sinal recebido para diferentes valores de SINR (0 a 25 dB) ----------------------------- Feito
#    4-  Calculo da BER (tem que implementar o SIC) --------------------------------------------------------- Feito
#    5-  2 Gráficos 2D do meu método e do método tradicional.  BER x SINR ----------------------------------- Fazendo
