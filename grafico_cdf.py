import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns
from matplotlib import ticker


sns.set()
########################################################################## leitura de csv ########################################################


desempenho_df1 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df1_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df2 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df2_.csv').drop(['Unnamed: 0'], axis=1).mean()  
desempenho_df3 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df3_.csv').drop(['Unnamed: 0'], axis=1).mean()  
desempenho_df4 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df4_.csv').drop(['Unnamed: 0'], axis=1).mean()  
desempenho_df5 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df5_.csv').drop(['Unnamed: 0'], axis=1).mean()  
desempenho_df6 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df6_.csv').drop(['Unnamed: 0'], axis=1).mean()  
desempenho_df7 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df7_.csv').drop(['Unnamed: 0'], axis=1).mean()  
desempenho_df8 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df8_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df9 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df9_.csv').drop(['Unnamed: 0'], axis=1).mean() 

desempenho_df10 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df10_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df11 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df11_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df12 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df12_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df13 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df13_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df14 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df14_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df15 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df15_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df16 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df16_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df17 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df17_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df19 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df19_.csv').drop(['Unnamed: 0'], axis=1).mean()

desempenho_df20 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df20_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df21 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df21_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df22 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df22_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df23 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df23_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df24 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df24_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df26 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df26_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df27 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df27_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df28 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df28_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df29 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df29_.csv').drop(['Unnamed: 0'], axis=1).mean() 

desempenho_df30 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df30_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df31 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df31_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df33 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df33_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df34 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df34_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df35 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df35_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df36 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df36_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df37 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df37_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df38 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df38_.csv').drop(['Unnamed: 0'], axis=1).mean() 
 

desempenho_df40 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df40_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df41 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df41_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df42 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df42_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df43 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df43_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df44 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df44_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df45 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df45_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df47 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df47_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df48 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df48_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df49 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df49_.csv').drop(['Unnamed: 0'], axis=1).mean() 

desempenho_df50 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df50_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df51 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df51_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df52 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df52_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df53 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df53_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df55 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df55_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df56 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df56_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df57 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df57_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df58 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df58_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df59 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df59_.csv').drop(['Unnamed: 0'], axis=1).mean() 

desempenho_df60 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df60_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df62 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df62_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df63 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df63_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df64 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df64_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df65 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df65_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df66 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df66_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df67 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df67_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df68 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df68_.csv').drop(['Unnamed: 0'], axis=1).mean() 

desempenho_df70 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df70_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df71 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df71_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df72 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df72_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df73 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df73_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df74 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df74_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df75 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df75_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df77 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df77_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df78 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df78_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df79 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df79_.csv').drop(['Unnamed: 0'], axis=1).mean()  

desempenho_df80 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df80_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df81 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df81_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df83 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df83_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df85 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df85_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df86 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df86_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df87 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df87_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df88 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df88_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df89 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df89_.csv').drop(['Unnamed: 0'], axis=1).mean()


desempenho_df90 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df90_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df91 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df91_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df93 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df93_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df94 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df94_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df95 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df95_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df96 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df96_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df97 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df97_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df98 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df98_.csv').drop(['Unnamed: 0'], axis=1).mean()

##################################################################################################

desempenho_df100 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df100_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df101 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df101_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df102 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df102_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df103 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df103_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df105 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df105_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df107 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df107_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df108 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df108_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df109 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df109_.csv').drop(['Unnamed: 0'], axis=1).mean()

desempenho_df110 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df110_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df111 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df111_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df112 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df112_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df113 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df113_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df115 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df115_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df116 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df116_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df117 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df117_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df118 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df118_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df119 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df119_.csv').drop(['Unnamed: 0'], axis=1).mean()

desempenho_df120 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df120_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df122 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df122_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df123 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df123_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df124 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df124_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df125 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df125_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df126 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df126_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df127 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df127_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df128 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df128_.csv').drop(['Unnamed: 0'], axis=1).mean()

desempenho_df130 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df130_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df131 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df131_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df132 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df132_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df133 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df133_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df134 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df134_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df135 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df135_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df136 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df136_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df138 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df138_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df139 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df139_.csv').drop(['Unnamed: 0'], axis=1).mean() 


desempenho_df140 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df140_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df141 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df141_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df142 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df142_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df143 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df143_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df145 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df145_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df146 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df146_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df147 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df147_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df148 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df148_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df149 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df149_.csv').drop(['Unnamed: 0'], axis=1).mean() 


desempenho_df150 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df150_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df152 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df152_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df153 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df153_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df154 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df154_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df155 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df155_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df156 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df156_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df157 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df157_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df159 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df159_.csv').drop(['Unnamed: 0'], axis=1).mean() 

desempenho_df160 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df160_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df161 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df161_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df162 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df162_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df163 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df163_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df164 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df164_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df165 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df165_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df167 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df167_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df168 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df168_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df169 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df169_.csv').drop(['Unnamed: 0'], axis=1).mean()

desempenho_df170 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df170_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df171 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df171_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df172 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df172_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df173 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df173_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df175 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df175_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df176 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df176_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df177 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df177_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df178 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df178_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df179 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df179_.csv').drop(['Unnamed: 0'], axis=1).mean() 

desempenho_df180 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df180_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df181 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df181_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df183 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df183_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df184 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df184_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df185 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df185_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df186 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df186_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df187 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df187_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df188 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df188_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df189 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df189_.csv').drop(['Unnamed: 0'], axis=1).mean()

desempenho_df191 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df191_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df192 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df192_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df193 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df193_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df194 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df194_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df195 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df195_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df196 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df196_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df198 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df198_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df199 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df199_.csv').drop(['Unnamed: 0'], axis=1).mean()

########################################################################################

desempenho_df200 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df200_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df201 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df201_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df202 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df202_.csv').drop(['Unnamed: 0'], axis=1).mean()  
desempenho_df203 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df203_.csv').drop(['Unnamed: 0'], axis=1).mean()  
desempenho_df204 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df204_.csv').drop(['Unnamed: 0'], axis=1).mean()  
desempenho_df206 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df206_.csv').drop(['Unnamed: 0'], axis=1).mean()  
desempenho_df207 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df207_.csv').drop(['Unnamed: 0'], axis=1).mean()  
desempenho_df208 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df208_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df209 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df209_.csv').drop(['Unnamed: 0'], axis=1).mean() 
 
desempenho_df210 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df210_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df211 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df211_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df212 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df212_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df214 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df214_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df215 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df215_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df216 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df216_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df217 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df217_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df218 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df218_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df219 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df219_.csv').drop(['Unnamed: 0'], axis=1).mean()

desempenho_df221 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df221_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df222 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df222_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df223 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df223_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df224 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df224_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df225 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df225_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df226 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df226_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df228 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df228_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df229 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df229_.csv').drop(['Unnamed: 0'], axis=1).mean()


desempenho_df230 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df230_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df231 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df231_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df232 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df232_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df233 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df233_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df235 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df235_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df236 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df236_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df237 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df237_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df238 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df238_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df239 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df239_.csv').drop(['Unnamed: 0'], axis=1).mean() 
 

desempenho_df240 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df240_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df241 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df241_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df243 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df243_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df244 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df244_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df245 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df245_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df246 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df246_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df247 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df247_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df248 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df248_.csv').drop(['Unnamed: 0'], axis=1).mean() 

desempenho_df250 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df250_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df251 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df251_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df252 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df252_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df253 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df253_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df254 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df254_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df255 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df255_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df257 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df257_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df258 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df258_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df259 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df259_.csv').drop(['Unnamed: 0'], axis=1).mean()  

desempenho_df260 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df260_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df261 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df261_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df262 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df262_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df264 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df264_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df265 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df265_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df266 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df266_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df267 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df267_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df268 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df268_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df269 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df269_.csv').drop(['Unnamed: 0'], axis=1).mean() 

desempenho_df270 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df270_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df272 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df272_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df273 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df273_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df274 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df274_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df275 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df275_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df276 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df276_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df277 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df277_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df279 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df279_.csv').drop(['Unnamed: 0'], axis=1).mean() 


desempenho_df280 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df280_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df281 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df281_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df282 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df282_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df283 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df283_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df284 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df284_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df285 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df285_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df287 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df287_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df288 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df288_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df289 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df289_.csv').drop(['Unnamed: 0'], axis=1).mean()

desempenho_df290 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df290_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df291 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df291_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df292 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df292_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df293 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df293_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df295 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df295_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df296 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df296_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df297 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df297_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df298 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df298_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df299 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df299_.csv').drop(['Unnamed: 0'], axis=1).mean()  

###########################################################################################

desempenho_df300 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df300_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df301 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df301_.csv').drop(['Unnamed: 0'], axis=1).mean()  
desempenho_df302 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df302_.csv').drop(['Unnamed: 0'], axis=1).mean()  
desempenho_df304 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df304_.csv').drop(['Unnamed: 0'], axis=1).mean()  
desempenho_df305 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df305_.csv').drop(['Unnamed: 0'], axis=1).mean()  
desempenho_df306 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df306_.csv').drop(['Unnamed: 0'], axis=1).mean()  
desempenho_df307 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df307_.csv').drop(['Unnamed: 0'], axis=1).mean()  
desempenho_df308 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df308_.csv').drop(['Unnamed: 0'], axis=1).mean()  
desempenho_df309 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df309_.csv').drop(['Unnamed: 0'], axis=1).mean() 

desempenho_df311 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df311_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df312 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df312_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df313 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df313_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df314 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df314_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df315 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df315_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df316 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df316_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df317 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df317_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df319 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df319_.csv').drop(['Unnamed: 0'], axis=1).mean()

desempenho_df320 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df320_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df321 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df321_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df322 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df322_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df323 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df323_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df324 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df324_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df326 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df326_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df327 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df327_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df328 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df328_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df329 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df329_.csv').drop(['Unnamed: 0'], axis=1).mean() 

desempenho_df330 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df330_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df331 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df331_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df332 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df332_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df334 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df334_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df335 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df335_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df336 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df336_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df337 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df337_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df338 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df338_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df339 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df339_.csv').drop(['Unnamed: 0'], axis=1).mean() 
 

desempenho_df340 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df340_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df342 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df342_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df343 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df343_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df344 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df344_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df345 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df345_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df346 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df346_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df347 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df347_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df349 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df349_.csv').drop(['Unnamed: 0'], axis=1).mean() 

desempenho_df350 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df350_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df351 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df351_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df352 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df352_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df353 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df353_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df354 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df354_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df355 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df355_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df357 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df357_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df358 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df358_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df359 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df359_.csv').drop(['Unnamed: 0'], axis=1).mean() 


desempenho_df360 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df360_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df361 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df361_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df362 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df362_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df364 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df364_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df365 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df365_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df366 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df366_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df367 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df367_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df368 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df368_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df369 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df369_.csv').drop(['Unnamed: 0'], axis=1).mean() 

desempenho_df370 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df370_.csv').drop(['Unnamed: 0'], axis=1).mean()
desempenho_df372 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df372_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df373 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df373_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df374 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df374_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df375 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df375_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df376 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df376_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df377 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df377_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df379 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df379_.csv').drop(['Unnamed: 0'], axis=1).mean() 

desempenho_df380 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df380_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df381 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df381_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df382 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df382_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df383 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df383_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df384 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df384_.csv').drop(['Unnamed: 0'], axis=1).mean() 
desempenho_df385 = pd.read_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df385_.csv').drop(['Unnamed: 0'], axis=1).mean() 

########## calcular a média em cada tempo e assim plotar o grafico ######################
########################################################################## refatorando dataframe ################################################
desempenho_df_geral = pd.concat([desempenho_df1 , desempenho_df2 , desempenho_df3 , desempenho_df4 , 
                                desempenho_df5 , desempenho_df6 , desempenho_df7 , desempenho_df8 ,
                                desempenho_df9 , desempenho_df10, desempenho_df11, desempenho_df12, 
                                desempenho_df13, desempenho_df14, desempenho_df15, desempenho_df16,
                                desempenho_df17, desempenho_df19, desempenho_df20, desempenho_df21,
                                desempenho_df22, desempenho_df23, desempenho_df24, desempenho_df26, 
                                desempenho_df27, desempenho_df28, desempenho_df29, desempenho_df30 , 
                                desempenho_df31 , desempenho_df33 , desempenho_df34 , desempenho_df35,
                                desempenho_df36 ,desempenho_df37 , desempenho_df38 , desempenho_df40 , 
                                desempenho_df41 , desempenho_df42 , desempenho_df43 ,desempenho_df44 ,
                                desempenho_df45 ,desempenho_df47 ,desempenho_df48 ,desempenho_df49 ,
                                desempenho_df50 ,desempenho_df51 ,desempenho_df52 ,desempenho_df53 ,
                                desempenho_df55 ,desempenho_df56 ,desempenho_df57 ,desempenho_df58 ,
                                desempenho_df59 ,desempenho_df60 ,desempenho_df62 ,desempenho_df63 ,
                                desempenho_df64 ,desempenho_df65 ,desempenho_df66 ,desempenho_df67 ,
                                desempenho_df68 ,desempenho_df70 ,desempenho_df71 ,desempenho_df72 ,
                                desempenho_df73 ,desempenho_df74 ,desempenho_df75 ,desempenho_df77 ,
                                desempenho_df78 ,desempenho_df79 ,desempenho_df80 ,desempenho_df81 ,
                                desempenho_df83 ,desempenho_df85 ,desempenho_df86 ,desempenho_df87 ,
                                desempenho_df88 ,desempenho_df89 ,desempenho_df90 ,desempenho_df91 ,
                                desempenho_df93 ,desempenho_df94 ,desempenho_df95 ,desempenho_df96 ,
                                desempenho_df97 ,desempenho_df98 ,desempenho_df100,desempenho_df101,
                                desempenho_df102,desempenho_df103,desempenho_df105,desempenho_df107,
                                desempenho_df108,desempenho_df109,desempenho_df110,desempenho_df111,
                                desempenho_df112,desempenho_df113,desempenho_df115,desempenho_df116,
                                desempenho_df117,desempenho_df118,desempenho_df119,desempenho_df120,
                                desempenho_df122,desempenho_df123,desempenho_df124,desempenho_df125,
                                desempenho_df126,desempenho_df127,desempenho_df128,desempenho_df130,
                                desempenho_df131,desempenho_df132,desempenho_df133,desempenho_df134,
                                desempenho_df135,desempenho_df136,desempenho_df138,desempenho_df139,
                                desempenho_df140,desempenho_df141,desempenho_df142,desempenho_df143,
                                desempenho_df145,desempenho_df146,desempenho_df147,desempenho_df148,
                                desempenho_df149,desempenho_df150,desempenho_df152,desempenho_df153,
                                desempenho_df154,desempenho_df155,desempenho_df156,desempenho_df157,
                                desempenho_df159,desempenho_df160,desempenho_df161,desempenho_df162,
                                desempenho_df163,desempenho_df164,desempenho_df165,desempenho_df167,
                                desempenho_df168,desempenho_df169,desempenho_df170,desempenho_df171,
                                desempenho_df172,desempenho_df173,desempenho_df175,desempenho_df176,
                                desempenho_df177,desempenho_df178,desempenho_df179,desempenho_df180,
                                desempenho_df181,desempenho_df183,desempenho_df184,desempenho_df185,
                                desempenho_df186,desempenho_df187,desempenho_df188,desempenho_df189,
                                desempenho_df191,desempenho_df192,desempenho_df193,desempenho_df194,
                                desempenho_df195,desempenho_df196,desempenho_df198,desempenho_df199,
                                desempenho_df200,desempenho_df201,desempenho_df202,desempenho_df203,
                                desempenho_df204,desempenho_df206,desempenho_df207,desempenho_df208,
                                desempenho_df209,desempenho_df210,desempenho_df211,desempenho_df212,
                                desempenho_df214,desempenho_df215,desempenho_df216,desempenho_df217,
                                desempenho_df218,desempenho_df219,desempenho_df221,desempenho_df222,
                                desempenho_df223,desempenho_df224,desempenho_df225,desempenho_df226,
                                desempenho_df228,desempenho_df229,desempenho_df230,desempenho_df231,
                                desempenho_df232,desempenho_df233,desempenho_df235,desempenho_df236,
                                desempenho_df237,desempenho_df238,desempenho_df239,desempenho_df240,
                                desempenho_df241,desempenho_df243,desempenho_df244,desempenho_df245,
                                desempenho_df246,desempenho_df247,desempenho_df248,desempenho_df250,
                                desempenho_df251,desempenho_df252,desempenho_df253,desempenho_df254,
                                desempenho_df255,desempenho_df257,desempenho_df258,desempenho_df259,
                                desempenho_df260,desempenho_df261,desempenho_df262,desempenho_df264,
                                desempenho_df265,desempenho_df266,desempenho_df267,desempenho_df268,
                                desempenho_df269,desempenho_df270,desempenho_df272,desempenho_df273,
                                desempenho_df274,desempenho_df275,desempenho_df276,desempenho_df277,
                                desempenho_df279,desempenho_df280,desempenho_df281,desempenho_df282,
                                desempenho_df283,desempenho_df284,desempenho_df285,desempenho_df287,
                                desempenho_df288,desempenho_df289,desempenho_df290,desempenho_df291,
                                desempenho_df292,desempenho_df293,desempenho_df295,desempenho_df296,
                                desempenho_df297,desempenho_df298,desempenho_df299,desempenho_df300,
                                desempenho_df301,desempenho_df302,desempenho_df304,desempenho_df305,
                                desempenho_df306,desempenho_df307,desempenho_df308,desempenho_df309,
                                desempenho_df311,desempenho_df312,desempenho_df313,desempenho_df314,
                                desempenho_df315,desempenho_df316,desempenho_df317,desempenho_df319,
                                desempenho_df320,desempenho_df321,desempenho_df322,desempenho_df323,
                                desempenho_df324,desempenho_df326,desempenho_df327,desempenho_df328,
                                desempenho_df329,desempenho_df330,desempenho_df331,desempenho_df332,
                                desempenho_df334,desempenho_df335,desempenho_df336,desempenho_df337,
                                desempenho_df338,desempenho_df339,desempenho_df340,desempenho_df342,
                                desempenho_df343,desempenho_df344,desempenho_df345,desempenho_df346,
                                desempenho_df347,desempenho_df349,desempenho_df350,desempenho_df351,
                                desempenho_df352,desempenho_df353,desempenho_df354,desempenho_df355,
                                desempenho_df357,desempenho_df358,desempenho_df359,desempenho_df360 , 
                                desempenho_df361 , desempenho_df362 , desempenho_df364 , desempenho_df365 , 
                                desempenho_df366 , desempenho_df367 , desempenho_df368 , desempenho_df369 , 
                                desempenho_df370 ,desempenho_df372 , desempenho_df373 , desempenho_df374 ,
                                desempenho_df375 , desempenho_df376 , desempenho_df377 , desempenho_df379 , 
                                desempenho_df380 ,desempenho_df381 ,desempenho_df382 , desempenho_df383 , 
                                desempenho_df384 ,desempenho_df385])

B = 180*(10**3)*100
desempenho_DS = desempenho_df_geral.R_DS/B
desempenho_tradicional = desempenho_df_geral.R_tradicional/B
desempenho_OMA = desempenho_df_geral.R_OMA/B



############################################################################# grafico ###########################################################

 

count, bins_count = np.histogram(desempenho_DS, bins=25) 
pdf = count / sum(count) 
cdf = np.cumsum(pdf)

count2, bins_count2 = np.histogram(desempenho_tradicional, bins=25) 
pdf2 = count2 / sum(count2) 
cdf2 = np.cumsum(pdf2) 

count3, bins_count3 = np.histogram(desempenho_OMA, bins=25) 
pdf3 = count3 / sum(count3) 
cdf3 = np.cumsum(pdf3) 


plt.plot(bins_count[1:], cdf, label="CDF_DS")
plt.plot(bins_count2[1:], cdf2, label="CDF_tradicional") 
plt.plot(bins_count3[1:], cdf3, label="CDF_OMA")

plt.ylabel('F(x)',fontsize=30, weight='bold')
plt.xlabel('Spectral efficiency [bps/Hz]',fontsize=30, weight='bold')

formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1)) 
    
plt.legend() 
plt.show()