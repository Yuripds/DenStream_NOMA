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
  p_list = []

  den = 0
  for i in range(len(gamaL)):
    den = den + ((abs(gamaL[-1])/abs(gamaL[i]))**(alpha))

  for i in range(len(gamaL)):
    p = ((abs(gamaL[-1])/abs(gamaL[i]))**(alpha)) / den
    p_list.append(p)

  return p_list


indices_list = []
for i in range(325):
    indices_df = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_indece_grafico3/usuario_id_df'+str(i+1)+'_.csv').drop(['Unnamed: 0'], axis=1)
    indices_list.append(indices_df.iloc[0].tolist())

##### calcular potencias e ganho e salvar em uma estrutura de dados








############################################ Implementar sinal recebido #######################################################

def get_index_vc(vect):
    split_list =[]
    for i in range(len(vect)):
        if vect[i]==0:
            split_list.append(i)
    split_list.append(len(vect))
    return split_list


def gerando_sinal(dataframe,SNR_dB):
    
    simbolos_tx = []
    for i in range(len(dataframe)):
       sinal_com_ruido = mgraf.plot_M_QAM(4,N=100,SNR_dB=SNR_dB) 
       simbolos_tx.append(abs(sinal_com_ruido).tolist())

    sinal_montado = []
    for m in range(len(simbolos_tx[0])) :
        usuarios = []
        for j in simbolos_tx:
            usuarios.append(j[m])
        sinal_montado.append(dataframe.iloc[-1].ganho*sum(np.multiply(usuarios,dataframe.potencia).tolist()))

    return sinal_montado


# um simbolo por vez?
def sinal_tx(dataframe,SNR_dB):
    indices = get_index_vc(dataframe.index)

    sinal=[]
    init=0
    for i in range(len(indices)-1):
        df_split = dataframe.iloc[indices[init]:indices[init+1]]
        sinal.append(gerando_sinal(df_split,SNR_dB=SNR_dB))
        init = init + 1

    return sinal



#### de 0 até 25 db de SNR
SNR = [0,5,10,15,20,25]

##################### mudar a estrutura de dados de tx_list
tx_list = []
for i in SNR:
    tx_list.append(sinal_tx(parametros_df_geral,SNR_dB=i))

############################################## calculo da BER #################################################################

########### implementar o SIC
def sic(sinal):
    sinal_separado = 1

    return sinal_separado






################################################ Gráficos ####################################################################





################ Próximos passos 
#    1-  Gerar csv com ganho complexo e coeficiente de potencia dos usuários do cluster 0  ------------------ Feito
#    2-  Implementar modulação 4-QAM ------------------------------------------------------------------------ Feito
#    3-  Implentar o sinal recebido para diferentes valores de SINR (0 a 25 dB) ----------------------------- Feito
#    4-  Calculo da BER (tem que implementar o SIC) --------------------------------------------------------- Fazendo
#    5-  2 Gráficos 2D do meu método e do método tradicional.  BER x SINR ----------------------------------- 
