import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
from matplotlib import ticker
from scipy import special

import modulacao_grafico as mgraf


sns.set()

########################################### Leitura de arquivos CSV ##########################################################
parametros_df1 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df1_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df2 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df2_.csv').drop(['Unnamed: 0'], axis=1)   
parametros_df3 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df3_.csv').drop(['Unnamed: 0'], axis=1)   
parametros_df4 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df4_.csv').drop(['Unnamed: 0'], axis=1)   
parametros_df5 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df5_.csv').drop(['Unnamed: 0'], axis=1)   
parametros_df6 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df6_.csv').drop(['Unnamed: 0'], axis=1)   
parametros_df7 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df7_.csv').drop(['Unnamed: 0'], axis=1)   
parametros_df8 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df8_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df9 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df9_.csv').drop(['Unnamed: 0'], axis=1)  

parametros_df10 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df10_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df11 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df11_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df12 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df12_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df13 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df13_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df14 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df14_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df15 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df15_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df16 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df16_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df17 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df17_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df19 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df19_.csv').drop(['Unnamed: 0'], axis=1) 

parametros_df20 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df20_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df21 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df21_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df22 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df22_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df23 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df23_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df24 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df24_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df25 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df25_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df27 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df27_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df28 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df28_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df29 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df29_.csv').drop(['Unnamed: 0'], axis=1)  

parametros_df30 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df30_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df31 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df31_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df32 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df32_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df34 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df34_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df35 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df35_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df36 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df36_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df37 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df37_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df38 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df38_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df39 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df39_.csv').drop(['Unnamed: 0'], axis=1)  
 

parametros_df41 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df41_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df42 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df42_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df43 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df43_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df44 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df44_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df45 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df45_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df46 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df46_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df48 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df48_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df49 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df49_.csv').drop(['Unnamed: 0'], axis=1)  

parametros_df50 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df50_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df51 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df51_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df52 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df52_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df53 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df53_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df55 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df55_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df56 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df56_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df57 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df57_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df58 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df58_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df59 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df59_.csv').drop(['Unnamed: 0'], axis=1)  

parametros_df60 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df60_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df62 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df62_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df63 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df63_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df64 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df64_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df65 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df65_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df66 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df66_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df67 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df67_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df69 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df69_.csv').drop(['Unnamed: 0'], axis=1)  

parametros_df70 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df70_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df71 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df71_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df72 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df72_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df73 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df73_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df74 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df74_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df76 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df76_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df77 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df77_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df78 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df78_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df79 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df79_.csv').drop(['Unnamed: 0'], axis=1)   

parametros_df80 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df80_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df81 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df81_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df83 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df83_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df84 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df84_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df85 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df85_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df86 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df86_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df87 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df87_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df88 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df88_.csv').drop(['Unnamed: 0'], axis=1) 


parametros_df90 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df90_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df91 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df91_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df92 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df92_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df93 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df93_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df94 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df94_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df95 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df95_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df96 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df96_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df98 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df98_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df99 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df99_.csv').drop(['Unnamed: 0'], axis=1)  
##################################################################################################

parametros_df100 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df100_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df101 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df101_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df102 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df102_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df103 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df103_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df105 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df105_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df106 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df106_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df107 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df107_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df108 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df108_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df109 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df109_.csv').drop(['Unnamed: 0'], axis=1) 

parametros_df110 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df110_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df112 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df112_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df113 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df113_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df114 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df114_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df115 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df115_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df116 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df116_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df117 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df117_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df119 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df119_.csv').drop(['Unnamed: 0'], axis=1) 

parametros_df120 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df120_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df121 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df121_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df122 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df122_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df123 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df123_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df124 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df124_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df125 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df125_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df127 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df127_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df128 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df128_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df129 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df129_.csv').drop(['Unnamed: 0'], axis=1) 

parametros_df130 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df130_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df131 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df131_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df132 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df132_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df134 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df134_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df135 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df135_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df136 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df136_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df137 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df137_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df138 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df138_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df139 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df139_.csv').drop(['Unnamed: 0'], axis=1)  


parametros_df140 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df140_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df142 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df142_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df143 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df143_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df144 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df144_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df145 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df145_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df146 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df146_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df147 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df147_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df148 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df148_.csv').drop(['Unnamed: 0'], axis=1)  


parametros_df150 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df150_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df151 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df151_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df152 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df152_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df153 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df153_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df154 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df154_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df155 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df155_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df157 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df157_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df158 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df158_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df159 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df159_.csv').drop(['Unnamed: 0'], axis=1)  

parametros_df160 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df160_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df161 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df161_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df162 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df162_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df163 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df163_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df165 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df165_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df166 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df166_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df167 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df167_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df168 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df168_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df169 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df169_.csv').drop(['Unnamed: 0'], axis=1) 

parametros_df170 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df170_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df172 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df172_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df173 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df173_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df174 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df174_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df175 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df175_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df176 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df176_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df177 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df177_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df179 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df179_.csv').drop(['Unnamed: 0'], axis=1)  

parametros_df180 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df180_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df181 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df181_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df182 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df182_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df183 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df183_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df184 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df184_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df186 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df186_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df187 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df187_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df188 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df188_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df189 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df189_.csv').drop(['Unnamed: 0'], axis=1) 

parametros_df190 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df190_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df191 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df191_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df193 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df193_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df194 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df194_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df195 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df195_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df196 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df196_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df197 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df197_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df198 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df198_.csv').drop(['Unnamed: 0'], axis=1) 
 


########################################################################################

parametros_df200 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df200_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df201 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df201_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df202 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df202_.csv').drop(['Unnamed: 0'], axis=1)   
parametros_df203 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df203_.csv').drop(['Unnamed: 0'], axis=1)   
parametros_df204 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df204_.csv').drop(['Unnamed: 0'], axis=1)   
parametros_df205 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df205_.csv').drop(['Unnamed: 0'], axis=1)   
parametros_df207 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df207_.csv').drop(['Unnamed: 0'], axis=1)   
parametros_df208 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df208_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df209 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df209_.csv').drop(['Unnamed: 0'], axis=1)  
 
parametros_df210 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df210_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df211 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df211_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df212 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df212_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df213 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df213_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df215 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df215_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df216 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df216_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df217 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df217_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df218 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df218_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df219 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df219_.csv').drop(['Unnamed: 0'], axis=1) 

parametros_df220 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df220_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df221 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df221_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df223 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df223_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df224 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df224_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df225 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df225_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df226 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df226_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df227 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df227_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df228 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df228_.csv').drop(['Unnamed: 0'], axis=1) 


parametros_df230 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df230_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df231 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df231_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df232 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df232_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df233 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df233_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df234 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df234_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df235 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df235_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df237 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df237_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df238 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df238_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df239 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df239_.csv').drop(['Unnamed: 0'], axis=1)  
 

parametros_df240 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df240_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df241 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df241_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df242 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df242_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df244 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df244_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df245 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df245_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df246 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df246_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df247 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df247_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df248 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df248_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df249 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df249_.csv').drop(['Unnamed: 0'], axis=1) 

parametros_df250 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df250_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df252 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df252_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df253 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df253_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df254 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df254_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df255 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df255_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df256 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df256_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df257 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df257_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df259 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df259_.csv').drop(['Unnamed: 0'], axis=1)   

parametros_df260 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df260_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df261 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df261_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df262 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df262_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df263 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df263_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df264 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df264_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df266 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df266_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df267 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df267_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df268 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df268_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df269 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df269_.csv').drop(['Unnamed: 0'], axis=1)  

parametros_df270 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df270_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df271 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df271_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df273 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df273_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df274 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df274_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df275 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df275_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df276 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df276_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df277 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df277_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df278 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df278_.csv').drop(['Unnamed: 0'], axis=1)  
  

parametros_df280 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df280_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df281 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df281_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df282 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df282_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df283 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df283_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df284 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df284_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df285 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df285_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df287 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df287_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df288 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df288_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df289 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df289_.csv').drop(['Unnamed: 0'], axis=1) 

parametros_df290 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df290_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df291 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df291_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df292 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df292_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df294 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df294_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df295 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df295_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df296 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df296_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df297 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df297_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df298 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df298_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df299 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df299_.csv').drop(['Unnamed: 0'], axis=1)   

###########################################################################################

parametros_df300 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df300_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df302 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df302_.csv').drop(['Unnamed: 0'], axis=1)   
parametros_df303 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df303_.csv').drop(['Unnamed: 0'], axis=1)   
parametros_df304 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df304_.csv').drop(['Unnamed: 0'], axis=1)   
parametros_df305 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df305_.csv').drop(['Unnamed: 0'], axis=1)   
parametros_df306 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df306_.csv').drop(['Unnamed: 0'], axis=1)   
parametros_df307 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df307_.csv').drop(['Unnamed: 0'], axis=1)   
parametros_df309 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df309_.csv').drop(['Unnamed: 0'], axis=1)  

parametros_df310 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df310_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df311 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df311_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df312 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df312_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df313 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df313_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df314 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df314_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df316 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df316_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df317 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df317_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df318 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df318_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df319 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df319_.csv').drop(['Unnamed: 0'], axis=1) 

parametros_df320 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df320_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df321 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df321_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df322 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df322_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df324 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df324_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df325 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df325_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df326 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df326_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df327 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df327_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df328 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df328_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df329 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df329_.csv').drop(['Unnamed: 0'], axis=1)  

parametros_df331 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df331_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df332 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df332_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df333 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df333_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df334 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df334_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df335 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df335_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df336 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df336_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df337 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df337_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df339 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df339_.csv').drop(['Unnamed: 0'], axis=1)  
 

parametros_df340 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df340_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df341 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df341_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df342 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df342_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df343 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df343_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df344 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df344_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df346 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df346_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df347 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df347_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df348 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df348_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df349 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df349_.csv').drop(['Unnamed: 0'], axis=1)  

parametros_df350 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df350_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df351 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df351_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df352 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df352_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df354 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df354_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df355 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df355_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df356 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df356_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df357 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df357_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df358 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df358_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df359 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df359_.csv').drop(['Unnamed: 0'], axis=1)  


parametros_df361 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df361_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df362 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df362_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df363 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df363_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df364 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df364_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df365 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df365_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df366 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df366_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df368 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df368_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df369 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df369_.csv').drop(['Unnamed: 0'], axis=1)  

parametros_df370 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df370_.csv').drop(['Unnamed: 0'], axis=1) 
parametros_df371 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df371_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df372 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df372_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df373 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df373_.csv').drop(['Unnamed: 0'], axis=1)  
parametros_df374 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/observacao_cluster_grafico3/obs_cluster0_df374_.csv').drop(['Unnamed: 0'], axis=1)  
  
##################################################
parametros_df_geral = pd.concat([ parametros_df1,  parametros_df2, parametros_df3, parametros_df4, parametros_df5,
                                  parametros_df6,  parametros_df7, parametros_df8, parametros_df9, parametros_df10,
                                  parametros_df11,  parametros_df12, parametros_df13, parametros_df14, parametros_df15,
                                  parametros_df16,  parametros_df17, parametros_df19, parametros_df20,
                                  parametros_df21,  parametros_df22, parametros_df23, parametros_df24, parametros_df25,
                                  parametros_df27, parametros_df28, parametros_df29, parametros_df30,
                                  parametros_df31,  parametros_df32, parametros_df34, parametros_df35,
                                  parametros_df36,  parametros_df37, parametros_df38, parametros_df39,
                                  parametros_df41,  parametros_df42, parametros_df43, parametros_df44, parametros_df45,
                                  parametros_df46, parametros_df48, parametros_df49, parametros_df50,
                                  parametros_df51,  parametros_df52, parametros_df53, parametros_df55,
                                  parametros_df56,  parametros_df57, parametros_df58, parametros_df59, parametros_df60,
                                  parametros_df62, parametros_df63, parametros_df64, parametros_df65,
                                  parametros_df66,  parametros_df67, parametros_df69, parametros_df70,
                                  parametros_df71,  parametros_df72, parametros_df73, parametros_df74,
                                  parametros_df76,  parametros_df77, parametros_df78, parametros_df79, parametros_df80,
                                  parametros_df81, parametros_df83, parametros_df84, parametros_df85,
                                  parametros_df86,  parametros_df87, parametros_df88, parametros_df90,
                                  parametros_df91,  parametros_df92, parametros_df93, parametros_df94, parametros_df95,
                                  parametros_df96, parametros_df98, parametros_df99, parametros_df100,
                                  parametros_df101,  parametros_df102, parametros_df103, parametros_df105,
                                  parametros_df106,  parametros_df107, parametros_df108, parametros_df109, parametros_df110,
                                  parametros_df112, parametros_df113, parametros_df114, parametros_df115,
                                  parametros_df116,  parametros_df117, parametros_df119, parametros_df120,
                                  parametros_df121,  parametros_df122, parametros_df123, parametros_df124, parametros_df125,
                                  parametros_df127, parametros_df128, parametros_df129, parametros_df130,
                                  parametros_df131,  parametros_df132, parametros_df134, parametros_df135,
                                  parametros_df136,  parametros_df137, parametros_df138, parametros_df139, parametros_df140,
                                  parametros_df142, parametros_df143, parametros_df144, parametros_df145,
                                  parametros_df146,  parametros_df147, parametros_df148, parametros_df150,
                                  parametros_df151,  parametros_df152, parametros_df153, parametros_df154, parametros_df155,
                                  parametros_df157, parametros_df158, parametros_df159, parametros_df160,
                                  parametros_df161,  parametros_df162, parametros_df163, parametros_df165,
                                  parametros_df166,  parametros_df167, parametros_df168, parametros_df169, parametros_df170,
                                  parametros_df172, parametros_df173, parametros_df174, parametros_df175,
                                  parametros_df176,  parametros_df177, parametros_df179, parametros_df180,
                                  parametros_df181,  parametros_df182, parametros_df183, parametros_df184,
                                  parametros_df186,  parametros_df187, parametros_df188, parametros_df189, parametros_df190,
                                  parametros_df191,  parametros_df193, parametros_df194, parametros_df195,
                                  parametros_df196,  parametros_df197, parametros_df198, parametros_df200,
                                  parametros_df201,  parametros_df202, parametros_df203, parametros_df204, parametros_df205,
                                  parametros_df207, parametros_df208, parametros_df209, parametros_df210,
                                  parametros_df211,  parametros_df212, parametros_df213, parametros_df215,
                                  parametros_df216,  parametros_df217, parametros_df218, parametros_df219, parametros_df220,
                                  parametros_df221,  parametros_df223, parametros_df224, parametros_df225,
                                  parametros_df226,  parametros_df227, parametros_df228, parametros_df230,
                                  parametros_df231,  parametros_df232, parametros_df233, parametros_df234, parametros_df235,
                                  parametros_df237, parametros_df238, parametros_df239, parametros_df240,
                                  parametros_df241,  parametros_df242, parametros_df244, parametros_df245,
                                  parametros_df246,  parametros_df247, parametros_df248, parametros_df249, parametros_df250,
                                  parametros_df252, parametros_df253, parametros_df254, parametros_df255,
                                  parametros_df256,  parametros_df257, parametros_df259, parametros_df260,
                                  parametros_df261,  parametros_df262, parametros_df263, parametros_df264,
                                  parametros_df266,  parametros_df267, parametros_df268, parametros_df269, parametros_df270,
                                  parametros_df271,  parametros_df273, parametros_df274, parametros_df275,
                                  parametros_df276,  parametros_df277, parametros_df278, parametros_df280,
                                  parametros_df281,  parametros_df282, parametros_df283, parametros_df284, parametros_df285,
                                  parametros_df287, parametros_df288, parametros_df289, parametros_df290,
                                  parametros_df291,  parametros_df292, parametros_df294, parametros_df295,
                                  parametros_df296,  parametros_df297, parametros_df298, parametros_df299, parametros_df300,
                                  parametros_df302, parametros_df303, parametros_df304, parametros_df305,
                                  parametros_df306,  parametros_df307, parametros_df309, parametros_df310,
                                  parametros_df311,  parametros_df312, parametros_df313, parametros_df314,
                                  parametros_df316,  parametros_df317, parametros_df318, parametros_df319, parametros_df320,
                                  parametros_df321,  parametros_df322, parametros_df324, parametros_df325,
                                  parametros_df326,  parametros_df327, parametros_df328, parametros_df329,
                                  parametros_df331,  parametros_df332, parametros_df333, parametros_df334, parametros_df335,
                                  parametros_df336,  parametros_df337, parametros_df339, parametros_df340,
                                  parametros_df341,  parametros_df342, parametros_df343, parametros_df344,
                                  parametros_df346,  parametros_df347, parametros_df348, parametros_df349, parametros_df350,
                                  parametros_df351,  parametros_df352, parametros_df354, parametros_df355,
                                  parametros_df356,  parametros_df357, parametros_df358, parametros_df359,
                                  parametros_df361,  parametros_df362, parametros_df363, parametros_df364, parametros_df365,
                                  parametros_df366,  parametros_df368, parametros_df369, parametros_df370,
                                  parametros_df371,  parametros_df372, parametros_df373, parametros_df374])

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
