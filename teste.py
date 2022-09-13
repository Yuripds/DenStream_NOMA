import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import cmath
from multiprocessing import Pool, freeze_support, cpu_count
from coeficienteDesvanecimento_GlobalLib import coeficiente_desvanecimento

from denStream import *

sns.set()


def desvanecimentoGlobal_usuarios(qtd_usuarios):
  cg_obj = coeficiente_desvanecimento.Coeficiente_de_Desvanecimento()
  d=np.random.uniform(500,2000,qtd_usuarios)
  dGlobal = np.zeros((qtd_usuarios,10**3),dtype=complex)
  for i in range(qtd_usuarios):
    dGlobal[i,:] = cg_obj.desvanecimentoGlobal(d=d[i],LOS=False,NN=20,tamanho=10**3,seed=i,fc=2.0*(10**9))

  return d,dGlobal


B = 180*(10**3)
N0 = 10**(-17.3)

cena_01 = np.multiply([10**40,10**39.5,10**14.5,10**14,10**13.5,10**13,10**12.5,10**12,10**11.5,10**11,10**10.5,10**10], N0*B).tolist()
cena_02 = np.multiply([10**40,10**39.5,10**15,10**14.5,10**14,10**13.5,10**13,10**12.5,10**12,10**11.5,10**11,10**10.5], N0*B).tolist()
cena_03 = np.multiply([10**40,10**39.5,10**39,10**15,10**14.5,10**14,10**13.5,10**13,10**12.5,10**12,10**11.5,10**11], N0*B).tolist()
cena_04 = np.multiply([10**40,10**39.5,10**39,10**38.5,10**15,10**14.5,10**14,10**13.5,10**13,10**12.5,10**12,10**11.5], N0*B).tolist()
cena_05 = np.multiply([10**40,10**39.5,10**39,10**38.5,10**38,10**15,10**14.5,10**14,10**13.5,10**13,10**12.5,10**12], N0*B).tolist()
cena_06 = np.multiply([10**40,10**39.5,10**39,10**38.5,10**38,10**37.5,10**15,10**14.5,10**14,10**13.5,10**13,10**12.5], N0*B).tolist()
cena_07 = np.multiply([10**40,10**39.5,10**39,10**38.5,10**38,10**37.5,10**37,10**15,10**14.5,10**14,10**13.5,10**13], N0*B).tolist()
cena_08 = np.multiply([10**40,10**39.5,10**39,10**38.5,10**38,10**37.5,10**37,10**36.5,10**15,10**14.5,10**14,10**13.5], N0*B).tolist()
cena_09 = np.multiply([10**40,10**39.5,10**39,10**38.5,10**38,10**37.5,10**37,10**36.5,10**36,10**15,10**14.5,10**14], N0*B).tolist()
cena_10 = np.multiply([10**40,10**39.5,10**39,10**38.5,10**38,10**37.5,10**37,10**36.5,10**36,10**35.5,10**15,10**14.5], N0*B).tolist()
cena_11 = np.multiply([10**40,10**39.5,10**39,10**38.5,10**38,10**37.5,10**37,10**36.5,10**36,10**35.5,10**35,10**15], N0*B).tolist()
cena_12 = np.multiply([10**40,10**39.5,10**39,10**38.5,10**38,10**37.5,10**37,10**36.5,10**36,10**35.5,10**35,10**34.5], N0*B).tolist()
cena_13 = np.multiply([10**40,10**37,10**34,10**31,10**28,10**25,10**22,10**19,10**16,10**13,10**10,10**7], N0*B).tolist()
cena_14 = np.multiply([10**11,10**10.5,10**10,10**9.5,10**9,10**8.5,10**8,10**7.5,10**7,10**6.5,10**6,10**5.5], N0*B).tolist()



def allocPower(gamaL,alpha):
  p_list = []

  den = 0
  for i in range(len(gamaL)):
    den = den + ((abs(gamaL[-1])/abs(gamaL[i]))**(alpha))

  for i in range(len(gamaL)):
    p = ((abs(gamaL[-1])/abs(gamaL[i]))**(alpha)) / den
    p_list.append(p)

  return p_list

def dataRate(w,B,Pt,gamaUser,N0,p_list,index):
 
  num = p_list[index]*Pt*gamaUser

  p_list = p_list[index+1:]
  p_array = np.array(p_list)
  den_list = p_array*Pt*gamaUser

  den = np.sum(den_list)
  den = den+(w*(N0*B))
  r = w*B*np.log2(1+(num/den))

  return r

def sumDataRate(w,B,Pt,N0,gamaL,alpha):
  gamaL.sort()
  p_list = allocPower(gamaL,alpha)
  print("p_list: ",p_list)
 
  r_array = np.ones((7,1))
  r_array[:] = float(np.NaN)
  
  for ind in range(len(gamaL)):
    gamaUser = gamaL[ind]
    r = dataRate(w,B,Pt,gamaUser,N0,p_list,ind)
    print("r_teste: ", r)
    r_array[ind] = r

  output = r_array[np.isfinite(r_array)]
  R_global = np.sum(output)

  return r_array,R_global


def get_index_vc(vect):
  index =[]
  for i in range(len(vect)-1):
    if vect[i]-vect[i+1] != 0:
      index.append(i+1)

  return index


def simulacao(dados,modelo,w,B,N0,alpha,etNU_list,nU_list,eT_list):

  saida = modelo._addUsers(X=dados,estimacao_tempo=eT_list,novos_users =nU_list,estimacao_tempo_novosUsers = etNU_list, ad_users=True,time_param=100)
  
  
  for idx in range(len(saida)):
    print("rotulos:" ,len(saida[idx]))

  for idx in range(len(saida)):
    print("rotulos:" ,saida[idx])

  usuarioRotulos = np.zeros((12,3))


  drList_final = []
  dr_global_final = []
  for tempo in range(len(saida)):
    usuarioRotulos[:,0] = saida[tempo]
    usuarioRotulos[:,1] = h[0:12, 0]
    usuarioRotulos[:,2] = h[0:12, 1]

    rotulo = saida[tempo]
    unique, counts = np.unique(rotulo, return_counts=True)
    n_clusters = len(unique)
    Pt = (((10**(4.6))*(10**-3)))/n_clusters

    usuarioRotulos_sort = usuarioRotulos[np.argsort(usuarioRotulos[:, 0])]
    index = get_index_vc(usuarioRotulos_sort[:, 0])
    usuarioRotulos_sort_split = np.split(usuarioRotulos_sort,index)
    print("usuarioRotulos_sort_split: ",usuarioRotulos_sort_split)

    drList = []
    dr_global = []
    for i in range(len(usuarioRotulos_sort_split)):
      gamaL = []
      cluster = usuarioRotulos_sort_split[i]
      for m in range(len(cluster)):
        gamaL.append(cluster[m][1])
      r,R_global = sumDataRate(w,B,Pt,N0,gamaL,alpha)
      dr_global.append(R_global)

      drList.append(r)

    dr_global_final.append(dr_global)
    drList_final.append(drList)
    
  return drList_final,dr_global_final
  




############################################################################################
qtd_usuarios = 12
d,dGlobal = desvanecimentoGlobal_usuarios(qtd_usuarios)


#### replicar informaçoes do vetor 
dGlobal = list(np.array(cena_10, dtype = 'complex'))
dGlobal_prolongado = np.array([dGlobal]*1000)
dGlobal_p_transposto = dGlobal_prolongado.T 


h=np.zeros((2,qtd_usuarios))
for i in range(qtd_usuarios):
  h[0][i] = abs(dGlobal_p_transposto[i][0])    
  h[1][i] = cmath.phase(dGlobal_p_transposto[i][0])
  
h=h.T

######### ver onde coletar as metricas de desempenho e colocar para rodar


train = pd.DataFrame(data=h,columns=['0','1'])
train = train.sample(frac = 1)


modelo = DenStream(lambd=0.5, eps=0.5, beta=0.4, mu=3, eps_dbscan = 1.0 , min_samples_dbscan = 1,zeta = 10.0)


df_dGlobal = pd.DataFrame(dGlobal_p_transposto)
df_dGlobal = abs(df_dGlobal)

w =100
B = 180*(10**3)
N0 = 10**(-17.3)
alpha_= 0.3

dados = train[0:10]
nU_list= train[10:12]

etNU_list = df_dGlobal.iloc[nU_list.index.values.astype(int)].values.tolist()


eT_list =  df_dGlobal.iloc[dados.index.values.astype(int)].values.tolist()



drList,R_global = simulacao(dados=dados,modelo = modelo,w=w,B=B,N0=N0,alpha=alpha_,etNU_list=etNU_list,nU_list = nU_list,eT_list=eT_list)


print("cenário 01: ",R_global)

'''
######################## Gráfico #########################################
tempo_gp = 0

x_index = range(len(drList[tempo_gp]))
color = ['#0000CD','#0000FF','#6495ED','#4169E1','#87CEFA','#B0C4DE']



plt.rcParams['xtick.labelsize'] = 30
plt.rcParams['ytick.labelsize'] = 30

plt.figure(figsize=(10,8))


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


##### mudar aqui #########################
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
plt.show()



######################## Gráfico #########################################
tempo_gp = 10

x_index = range(len(drList[tempo_gp]))
color = ['#0000CD','#0000FF','#6495ED','#4169E1','#87CEFA','#B0C4DE']



plt.rcParams['xtick.labelsize'] = 30
plt.rcParams['ytick.labelsize'] = 30

plt.figure(figsize=(10,8))


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


##### mudar aqui #########################
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
plt.show()


######################## Gráfico #########################################
tempo_gp = 20

x_index = range(len(drList[tempo_gp]))
color = ['#0000CD','#0000FF','#6495ED','#4169E1','#87CEFA','#B0C4DE']



plt.rcParams['xtick.labelsize'] = 30
plt.rcParams['ytick.labelsize'] = 30

plt.figure(figsize=(10,8))


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


##### mudar aqui #########################
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
plt.show()


######################## Gráfico #########################################
tempo_gp = 30

x_index = range(len(drList[tempo_gp]))
color = ['#0000CD','#0000FF','#6495ED','#4169E1','#87CEFA','#B0C4DE']



plt.rcParams['xtick.labelsize'] = 30
plt.rcParams['ytick.labelsize'] = 30

plt.figure(figsize=(10,8))


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


##### mudar aqui #########################
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
plt.show()




######################## Gráfico #########################################
tempo_gp = 40

x_index = range(len(drList[tempo_gp]))
color = ['#0000CD','#0000FF','#6495ED','#4169E1','#87CEFA','#B0C4DE']



plt.rcParams['xtick.labelsize'] = 30
plt.rcParams['ytick.labelsize'] = 30

plt.figure(figsize=(10,8))


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


##### mudar aqui #########################
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
plt.show()




######################## Gráfico 2 --  quantidade de clusters no tempo #########################################


# Plota as barras
#plt.figure(figsize=(25,10))
color = ['#00008B','#0000FF','#4169E1','#87CEFA','#B0C4DE']

label_c = []
for i in range(len(drList[tempo_gp][0])):
  label_c.append('Cluster '+ str(i))


####### quantidade de clusters em cada tempo
qtd_c_list = []
for i in range(len(drList)):
  qtd_c_list.append(len(drList[i]))

qtd_cMAX = max(qtd_c_list)

####### número de usuários em cada cluster, em cada tempo
qtd_clusters = []
for i in range(len(drList)):
  aux = []
  for j in range(len(drList[i])):
    vetor_nanTest =  np.isnan(drList[i][j])
    aux.append(len(drList[i][j]) - vetor_nanTest.sum() )
  qtd_clusters.append(aux)



plt.rcParams['xtick.labelsize'] = 30
plt.rcParams['ytick.labelsize'] = 30
# Plota as barras
plt.figure(figsize=(25,10))


vetorBase = np.zeros((10,len(qtd_clusters[0])))*np.NAN
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
plt.show()

'''