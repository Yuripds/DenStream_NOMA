import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns
from matplotlib import ticker


sns.set()

########################################################################## leitura de csv ########################################################
desempenho_df1 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df1_.csv').drop(['Unnamed: 0'], axis=1)
desempenho_df1_users = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho_individual_DS/desempenho_usuario_df1_.csv').drop(['Unnamed: 0'], axis=1)

desempenho_df74 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df74_.csv').drop(['Unnamed: 0'], axis=1)
desempenho_df74_users = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho_individual_DS/desempenho_usuario_df74_.csv').drop(['Unnamed: 0'], axis=1)

desempenho_df148 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df148_.csv').drop(['Unnamed: 0'], axis=1)
desempenho_df148_users = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho_individual_DS/desempenho_usuario_df148_.csv').drop(['Unnamed: 0'], axis=1)

desempenho_df223 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df223_.csv').drop(['Unnamed: 0'], axis=1)
desempenho_df223_users = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho_individual_DS/desempenho_usuario_df223_.csv').drop(['Unnamed: 0'], axis=1)

desempenho_df296 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df296_.csv').drop(['Unnamed: 0'], axis=1)
desempenho_df296_users = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho_individual_DS/desempenho_usuario_df296_.csv').drop(['Unnamed: 0'], axis=1)

desempenho_df370 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df370_.csv').drop(['Unnamed: 0'], axis=1)
desempenho_df370_users = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho_individual_DS/desempenho_usuario_df370_.csv').drop(['Unnamed: 0'], axis=1)

########################################################################## refatorando dataframe ################################################
desempenho_df1_r = desempenho_df1.R_DS.dropna()
cluster0_df1 = desempenho_df1_users["0"].dropna()


desempenho_df74_r = desempenho_df74.R_DS.dropna()
cluster0_df74 = desempenho_df74_users["0"].dropna()
cluster1_df74 = desempenho_df74_users["1"].dropna()
cluster2_df74 = desempenho_df74_users["2"].dropna()
cluster3_df74 = desempenho_df74_users["3"].dropna()
cluster4_df74 = desempenho_df74_users["4"].dropna()
cluster5_df74 = desempenho_df74_users["5"].dropna()

desempenho_df148_r = desempenho_df148.R_DS.dropna()
cluster0_df148 = desempenho_df148_users["0"].dropna()
cluster1_df148 = desempenho_df148_users["1"].dropna()
cluster2_df148 = desempenho_df148_users["2"].dropna()
cluster3_df148 = desempenho_df148_users["3"].dropna()
cluster4_df148 = desempenho_df148_users["4"].dropna()

desempenho_df223_r = desempenho_df223.R_DS.dropna()
cluster0_df223 = desempenho_df223_users["0"].dropna()
cluster1_df223 = desempenho_df223_users["1"].dropna()
cluster2_df223 = desempenho_df223_users["2"].dropna()
cluster3_df223 = desempenho_df223_users["3"].dropna()
cluster4_df223 = desempenho_df223_users["4"].dropna()

desempenho_df296_r = desempenho_df296.R_DS.dropna()
cluster0_df296 = desempenho_df296_users["0"].dropna()
cluster1_df296 = desempenho_df296_users["1"].dropna()
cluster2_df296 = desempenho_df296_users["2"].dropna()


desempenho_df370_r = desempenho_df370.R_DS.dropna()
cluster0_df370 = desempenho_df370_users["0"].dropna()
cluster1_df370 = desempenho_df370_users["1"].dropna()
cluster2_df370 = desempenho_df370_users["2"].dropna()
cluster3_df370 = desempenho_df370_users["3"].dropna()
cluster4_df370 = desempenho_df370_users["4"].dropna()

#####################################################################################################################################################

barWidth =0.05

x_indx = [0.1,0.1+barWidth,0.1+barWidth*2]


tempo01_df =  pd.concat([cluster0_df1,desempenho_df1_r])

plt.bar(x_indx,tempo01_df, width=barWidth, label = ['r0','r1','R'] , color = ['#03353E','#0294A5','k'])

plt.xticks([0.1+barWidth],['0'])
plt.xlabel('index cluster tx',fontsize=30, weight='bold')
plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
plt.legend(loc='best',fontsize=30)

plt.title('Data rate NOMA system',fontsize=30, weight='bold')
plt.grid(True)

plt.show()

#####################################################################################################################################################

tempo02_df = pd.concat([cluster0_df74.sort_values(),cluster1_df74.sort_values(),cluster2_df74.sort_values(),cluster3_df74.sort_values()
                        ,cluster4_df74.sort_values(),cluster5_df74.sort_values(),desempenho_df74_r],axis=1)

color = ['#03353E','#0294A5','#A79C93','#C1403D','#04060F','#F22F08']

lab = []
max =len(cluster0_df74)
for i in range(max):
    lab.append('r'+ str(i))

barWidth = 0.10
x_index = range(len(desempenho_df74_r))
x1 = np.arange(len(x_index))

for l in range(max):   
    plt.bar([x + barWidth for x in x1],tempo02_df.drop(['R_DS'],axis=1).iloc[l], width=barWidth, label = lab[l] , color = color[l])
    x1 = [x + barWidth for x in x1]
plt.bar([x + barWidth for x in x1],tempo02_df['R_DS'].dropna(), width=barWidth, label = "R" , color = 'k')

plt.xticks([x + barWidth for x in np.arange(len(desempenho_df74_r))],['0','1','2','3','4','5'])

plt.xlabel('index cluster tx',fontsize=30, weight='bold')
plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
plt.legend(loc='best',fontsize=30)

plt.title('Data rate NOMA system',fontsize=30, weight='bold')
plt.grid(True)

plt.show()




#####################################################################################################################################################
tempo03_df = pd.concat([cluster0_df148.sort_values(),cluster1_df148.sort_values(),cluster2_df148.sort_values(),
                        cluster3_df148.sort_values(),cluster4_df148.sort_values(),desempenho_df148_r],axis=1)


lab = []
max =len(cluster1_df148)
for i in range(max):
    lab.append('r'+ str(i))

barWidth = 0.10
x_index = range(len(desempenho_df148_r))
x1 = np.arange(len(x_index))

for l in range(max):   
    plt.bar([x + barWidth for x in x1],tempo03_df.drop(['R_DS'],axis=1).iloc[l], width=barWidth, label = lab[l] , color = color[l])
    x1 = [x + barWidth for x in x1]
plt.bar([x + barWidth for x in x1],tempo03_df['R_DS'].dropna(), width=barWidth, label = "R" , color = 'k')

plt.xticks([x + barWidth for x in np.arange(len(desempenho_df148_r))],['0','1','2','3','4'])

plt.xlabel('index cluster tx',fontsize=30, weight='bold')
plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
plt.legend(loc='best',fontsize=30)

plt.title('Data rate NOMA system',fontsize=30, weight='bold')
plt.grid(True)

plt.show()




#####################################################################################################################################################
tempo04_df = pd.concat([cluster0_df223.sort_values(),cluster1_df223.sort_values(),cluster2_df223.sort_values(),
                        cluster3_df223.sort_values(),cluster4_df223.sort_values(),desempenho_df223_r],axis=1)

lab = []
max =len(cluster1_df223)
for i in range(max):
    lab.append('r'+ str(i))

barWidth = 0.10
x_index = range(len(desempenho_df223_r))
x1 = np.arange(len(x_index))

for l in range(max):   
    plt.bar([x + barWidth for x in x1],tempo04_df.drop(['R_DS'],axis=1).iloc[l], width=barWidth, label = lab[l] , color = color[l])
    x1 = [x + barWidth for x in x1]
plt.bar([x + barWidth for x in x1],tempo04_df['R_DS'].dropna(), width=barWidth, label = "R" , color = 'k')

plt.xticks([x + barWidth for x in np.arange(len(desempenho_df223_r))],['0','1','2','3','4'])

plt.xlabel('index cluster tx',fontsize=30, weight='bold')
plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
plt.legend(loc='best',fontsize=30)

plt.title('Data rate NOMA system',fontsize=30, weight='bold')
plt.grid(True)

plt.show()




#####################################################################################################################################################

tempo05_df = pd.concat([cluster0_df296.sort_values(),cluster1_df296.sort_values(),cluster2_df296.sort_values(),desempenho_df296_r],axis=1)

lab = []
max =len(cluster0_df296)
for i in range(max):
    lab.append('r'+ str(i))

barWidth = 0.10
x_index = range(len(desempenho_df296_r))
x1 = np.arange(len(x_index))

for l in range(max):   
    plt.bar([x + barWidth for x in x1],tempo05_df.drop(['R_DS'],axis=1).iloc[l], width=barWidth, label = lab[l] , color = color[l])
    x1 = [x + barWidth for x in x1]
plt.bar([x + barWidth for x in x1],tempo05_df['R_DS'].dropna(), width=barWidth, label = "R" , color = 'k')

plt.xticks([x + barWidth for x in np.arange(len(desempenho_df296_r))],['0','1','2'])

plt.xlabel('index cluster tx',fontsize=30, weight='bold')
plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
plt.legend(loc='best',fontsize=30)

plt.title('Data rate NOMA system',fontsize=30, weight='bold')
plt.grid(True)

plt.show()



#####################################################################################################################################################

tempo06_df = pd.concat([cluster0_df370.sort_values(),cluster1_df370.sort_values(),cluster2_df370.sort_values(),
                        cluster3_df370.sort_values(),cluster4_df370.sort_values(),desempenho_df370_r],axis=1)


lab = []
max =len(cluster0_df370)
for i in range(max):
    lab.append('r'+ str(i))

barWidth = 0.10
x_index = range(len(desempenho_df370_r))
x1 = np.arange(len(x_index))

for l in range(max):   
    plt.bar([x + barWidth for x in x1],tempo06_df.drop(['R_DS'],axis=1).iloc[l], width=barWidth, label = lab[l] , color = color[l])
    x1 = [x + barWidth for x in x1]
plt.bar([x + barWidth for x in x1],tempo06_df['R_DS'].dropna(), width=barWidth, label = "R" , color = 'k')

plt.xticks([x + barWidth for x in np.arange(len(desempenho_df370_r))],['0','1','2','3','4'])

plt.xlabel('index cluster tx',fontsize=30, weight='bold')
plt.ylabel('Throughput (bps)',fontsize=30, weight='bold')
plt.legend(loc='best',fontsize=30)

plt.title('Data rate NOMA system',fontsize=30, weight='bold')
plt.grid(True)

plt.show()



#####################################################################################################################################################
