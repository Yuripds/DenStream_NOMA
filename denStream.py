import sys
import numpy as np
from sklearn.utils import check_array
from copy import copy ,deepcopy
from microCluster import *
from math import ceil
from sklearn.cluster import DBSCAN
import cmath
import desempenho as dsp
from statistics import pstdev
import main_oma as oma
import metodo_padrao as mpad
import pandas as pd

class DenStream:

    def __init__(self, lambd=1, beta=2, mu=2, zeta=5,p_tol=10,alpha=0.2,N0=10**-10,B=20*(10**6), Pt = ((10**(4.6))*(10**-3)),sd_out=10**4):
   
        self.lambd = lambd
        self.beta = beta
        self.mu = mu
        self.t = 0
        self.p_micro_clusters = []
        self.o_micro_clusters = []
        self.zeta = zeta
        self.newUsers = {}
        self.estimacao_tempo_newUsers = []
        self.p_tol =p_tol
        self.alpha = alpha
        self.N0 = N0
        self.B = B
        self.sd_out= sd_out
        self.Pt = Pt
        ###### configuração pre-definida
        self.cluster_id_mt={'0':[],'1':[],'2':[],'3':[],'4':[],'5':[]}
        self.flag_end = True
        
       

        if lambd > 0:
            self.tp = ceil((1 / lambd) * np.log((beta * mu) / (beta * mu - 1)))
        else:
            self.tp = sys.maxsize

    def _addUsers(self, X, y=None, y_old=None, estimacao_tempo=[], novos_users=[], estimacao_tempo_novosUsers=[], sample_weight=None, ad_users=False, time_param=500,sd_param=500):
            
            x_id = X.index
            novos_users_id = novos_users.index

            X = check_array(X, dtype=np.float64, order="C")

            n_samples, _ = X.shape

            sample_weight = self._validate_sample_weight(
                sample_weight, n_samples)

            estimacaoGanhoCanal = estimacao_tempo

            ##### transformar o X e o x_id em dicionário
            x_dic = {}
            for i,value in enumerate(X):
                x_dic[str(x_id[i])] = value
                

            #################################################### tratamento dos dados de novos usuários e guardando em variáveis ##########
            user_nlist = novos_users.to_numpy(dtype='float32')

            for i, users in enumerate(user_nlist):
                self.newUsers[str(novos_users_id[i])] = users
                self.estimacao_tempo_newUsers.append(
                         estimacao_tempo_novosUsers[i])
                
            ############################################################### metodo parão ##################################################

            self.formar_grupopadrao(x_dic)


            ###############################################################################################################################

            indx = 0
            ############ entrada das primeiras amostras
            for sample_id, weight in zip(x_dic, sample_weight):
                self._partial_fit(x_dic[sample_id], estimacaoGanhoCanal[indx], weight,sd_param,sample_id)
                indx = indx+1


            y_tempo = []
            contador = 0
            
            while contador < time_param:

                self.manutencao()

                y_old = []
                fixSamples = []
                for p_micro_cluster in self.p_micro_clusters:
                    if len(p_micro_cluster.getSample())!= 0:
                        samples_in_pmc = p_micro_cluster.getSample()
                        for i in samples_in_pmc:
                             fixSamples.append(i)

                for sample in fixSamples:
                    index = self._get_group_index(sample,self.p_micro_clusters)
                    y_old.append(index)

                if ad_users == True:
                        y = []
                        usuarios_f = []
                        for i, users_id in enumerate(self.newUsers):
                            # add estimacao_tempo_novosUsers junto a fila de novos usuários
                            nova_amostra = self.newUsers[users_id]
                            nova_amostra_id = users_id
                            new_sample_weight = np.ones(
                                1, dtype=np.float32, order='C')[0]
                            ############# Entrada das novas amostras e de amostras que o canal variou 
                            if i==3:
                                self.flag_end=False
                            self._partial_fit(nova_amostra, self.estimacao_tempo_newUsers[i], new_sample_weight,sd_param,nova_amostra_id)
                        
                        
                        for i,mc in enumerate(self.p_micro_clusters):
                            for valor in mc.getGainChannel():
                                y.append(i)
                                usuarios_f.append(valor)

                        
                        y_tempo.append(y)


                else:
                    y_tempo.append(y_old)
                    usuarios_f = fixSamples
                
                y_tempo =[]
                self.newUsers = {}
                contador = contador+10
                self.t += 1  

            return y_tempo          
                       

            


    def formar_grupopadrao(self,x_dic):

        copia_x_dic = x_dic
        copia_newusers = self.newUsers
        copia_x_dic.update(copia_newusers)

        self.cluster_id_mt = {}
        #############################  reafatorando e ordenando o dicionário #####################################################
        x_dic_ref =[]
        for i in x_dic:
            x_dic_ref.append([i,copia_x_dic[i][0]])
        
        x_dic_ref_ord = sorted(x_dic_ref, key = lambda x: x[1],reverse=True)
        #############################################################################################################
    
        pares = []
        aux = 1
        for i in range(int(len(x_dic_ref_ord)/2)):
            pares.append([x_dic_ref_ord[i], x_dic_ref_ord[len(x_dic_ref_ord)-aux]])
            aux =aux+1

    
        for i,par in enumerate(pares):
            self.cluster_id_mt[str(i)]=[int(par[0][0]),int(par[1][0])]


        #############################################################################################################

   



               

    def _get_group_index(self,sample,micro_clusters):
        indice = -1
        flag=0
        for idx,mc in enumerate(micro_clusters):
            list_cg = mc.getGainChannel()
            for i in list_cg:
                if sample[0] == i:
                    indice=idx
                    flag=1
                    break
            if flag==1:
                break
        
        return indice
                
        

                      
    

    def _get_nearest_micro_cluster(self,sample, micro_clusters,sd_param):
        smaller_size = 100
        best_micro_cluster = None
        best_micro_cluster_index = -1
        
        for i, micro_cluster in enumerate(micro_clusters):
            size_mc = len(micro_cluster.getGainChannel())
            if size_mc < smaller_size:
                smaller_size = size_mc

        candidatos =[]
        for i, micro_cluster in enumerate(micro_clusters):
            lista_aux =deepcopy(micro_cluster.getGainChannel()) 
            if len(micro_cluster.getGainChannel())==1:
                antigo_std = micro_cluster.getGainChannel()[0]
                sd_param_n =sd_param
            else:
                antigo_std = np.std(micro_cluster.getGainChannel())
                ### lembrando que isso é em porcentagem
                sd_param_n=5

            crescimento_pct = ((self.sandard_d_(lista_aux,sample[0]) - antigo_std)/ antigo_std)*100
            if abs(crescimento_pct)>= sd_param_n:
                candidatos.append(micro_cluster)

        
        for i, micro_cluster in enumerate(candidatos):
            if len(micro_cluster.getGainChannel()) ==smaller_size:
                best_micro_cluster = micro_cluster
                break
        
        for i, micro_cluster in enumerate(micro_clusters):
            if micro_cluster == best_micro_cluster:
                best_micro_cluster_index = i

        return best_micro_cluster_index, best_micro_cluster




    def _try_merge(self, sample,eu_id,estimacaoGanhoCanal, weight, micro_cluster):
       
        
        if micro_cluster is not None:
            micro_cluster_copy = deepcopy(micro_cluster)
            micro_cluster_copy.insert_sample(sample,estimacaoGanhoCanal, eu_id ,weight)
            lista_aux = micro_cluster_copy.getGainChannel()

            if len(micro_cluster.getGainChannel())==1:
                antigo_std = micro_cluster.getGainChannel()[0]

            else:
                antigo_std = np.std(micro_cluster.getGainChannel())
    

            sd_param_outlier =self.sd_out
            crescimento_pct = ((np.std(lista_aux)- antigo_std)/ antigo_std)*100

            is_not_outlier = True
            if abs(crescimento_pct)>= sd_param_outlier:
                is_not_outlier = False



            if self._restricao_sic(micro_cluster_copy) &  is_not_outlier :
                micro_cluster.insert_sample(sample, estimacaoGanhoCanal, eu_id ,weight)
                return True
                
        return False




    def _merging(self, sample,estimacaoGanhoCanal, weight,sd_param,eu_id):
        _, nearest_p_micro_cluster = \
            self._get_nearest_micro_cluster(sample,self.p_micro_clusters,sd_param)

        success = self._try_merge(sample,eu_id,estimacaoGanhoCanal, weight, nearest_p_micro_cluster)


        if not success:
            index, nearest_o_micro_cluster = \
                self._get_nearest_micro_cluster(sample,self.o_micro_clusters,sd_param)
            success = self._try_merge(sample,eu_id,estimacaoGanhoCanal, weight, nearest_o_micro_cluster)


            
            if success:

                if nearest_o_micro_cluster.weight() > self.beta * self.mu:
                    del self.o_micro_clusters[index]
                    
                    self.p_micro_clusters.append(nearest_o_micro_cluster)
            else:
                qtd_clusters = len(self.p_micro_clusters) + len(self.o_micro_clusters)
                micro_cluster = MicroCluster(self.lambd, self.t,c_id =qtd_clusters)
                micro_cluster.insert_sample(sample,estimacaoGanhoCanal, eu_id ,weight)
                self.o_micro_clusters.append(micro_cluster)


    def _decay_function(self, t):
        return 2 ** ((-self.lambd) * (t))



    def manutencao(self):
            for i,p_micro_cluster in enumerate(self.p_micro_clusters):
                gainList = p_micro_cluster.getGainChannel()
                
                ganhoTempoList = p_micro_cluster.getGanhoTempo()

                users_id = p_micro_cluster.getusers_ids()
                
                tam_init = len(gainList)
                idx=0
                while(tam_init>idx):
                    diff_pct = ((abs(ganhoTempoList[idx][self.t])  - abs(gainList[idx]))/abs(gainList[idx]))*100
                    ######### zeta é dado em porcentagem #############
                    if abs(diff_pct) >= self.zeta:
                        self.newUsers[str(users_id[idx])] = np.array([abs(ganhoTempoList[idx][self.t]),cmath.phase(ganhoTempoList[idx][self.t])])
                        self.estimacao_tempo_newUsers.append(ganhoTempoList[idx])
                        #### aqui passar o id do usuário que foi removido
                        p_micro_cluster.delete_sample(idx)
                        tam_init = tam_init-1
                    else:
                        idx = idx +1
                    
                if len(gainList)==0:
                    self.p_micro_clusters.pop(i)


            for op,o_micro_cluster in enumerate(self.o_micro_clusters):
                gainList_outL = o_micro_cluster.getGainChannel()
                ganhoTempoList_out = o_micro_cluster.getGanhoTempo()
                sampleList = o_micro_cluster.getSample()
                users_id_out = o_micro_cluster.getusers_ids()
                tam_init = len(gainList_outL)
                idx=0
                while(tam_init>idx):
                    self.newUsers[str(users_id_out[idx])] = sampleList[idx]
                    self.estimacao_tempo_newUsers.append(ganhoTempoList_out[idx])
                    o_micro_cluster.delete_sample(idx)
                    tam_init =tam_init-1
                if len(gainList_outL)==0:
                    self.o_micro_clusters.pop(op)




    def _partial_fit(self, sample,estimacaoGanhoCanal, weight,sd_param,eu_id):

        self._merging(sample, estimacaoGanhoCanal, weight,sd_param,eu_id)

        if len(self.p_micro_clusters)!=0:
            cluster_id = []
            usuarios_gc = []
            usuario_id = []
            for idx,mc in enumerate(self.p_micro_clusters):
                cluster_id.append(mc.getcluster_id())
                usuarios_gc.append(mc.getGainChannel())
                usuario_id.append(mc.getusers_ids())

            for idx,omc in enumerate(self.o_micro_clusters):
                cluster_id.append(-1)
                usuarios_gc.append(omc.getGainChannel())
                usuario_id.append(omc.getusers_ids())
            
        
            ##### calculando desempenho do meu método
                # aqui o calculo de desempenho inclui usuários de o-mc para serem transmitidos por OMA   
            drglobal_mp,drusuarios_mp = dsp.resultado(usuarios_gc,cluster_id,self.t,self.alpha,self.B,self.N0,self.Pt,self.t)

            ##### calculando desempenho do método tradicional
                # aqui o calculo de desempenho inclui usuários de o-mc para serem transmitidos por OMA  
            drglobal_t,drusuarios_t = mpad.mp_resultado(usuarios_gc,usuario_id,self.cluster_id_mt,self.alpha,self.B,self.N0,self.Pt)

            ##### calculando desempenho do meu método OMA
            drglobal_oma,drusuarios_oma = oma.simulacao_OMA(usuarios_gc,cluster_id,self.B,self.N0,self.Pt) 

            ############################################### salvar dados em csv
                # concatenar os 3 resultados 
            desempenhos_dos_metodos = [drglobal_mp[0],drglobal_t[0],drglobal_oma[0]]
            tam_ref = 0
            for metodo in desempenhos_dos_metodos:
                if len(metodo)>tam_ref:
                    tam_ref = len(metodo)

            desempenhos_dos_metodos_ref = np.zeros((tam_ref,3))*np.NAN
            for i_metodo, metodo in enumerate(desempenhos_dos_metodos):
                for idx_ele in range(len(metodo)):
                    if type(metodo[idx_ele]) == type(desempenhos_dos_metodos):
                        desempenhos_dos_metodos_ref[idx_ele,i_metodo] = metodo[idx_ele][0]
                    else:
                        desempenhos_dos_metodos_ref[idx_ele,i_metodo] = metodo[idx_ele]

            desempenhos_dos_metodos_ref_list = desempenhos_dos_metodos_ref.tolist()
            desempenho_df = pd.DataFrame(data=desempenhos_dos_metodos_ref_list,columns=['R_DS','R_tradicional','R_OMA'])

            #desempenho_df.to_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho/desempenho_df'+ str(self.t) +'_.csv')

            ############################################### gerar csv para plotar o desempenho individual de cada usuário do método proposto
            desempenhos_dos_usuarios_ref_2 = np.zeros((12,len(drusuarios_mp[0])))*np.NAN
            for i_grupo, grupo in enumerate(drusuarios_mp[0]):
                for idx_ele_grupo in range(len(grupo)):
                        desempenhos_dos_usuarios_ref_2[idx_ele_grupo,i_grupo] = grupo[idx_ele_grupo]

            desempenhos_dos_usuarios_ref_list_2 = desempenhos_dos_usuarios_ref_2.tolist()
            desempenho_usuarios_df = pd.DataFrame(data=desempenhos_dos_usuarios_ref_list_2)


            #desempenho_usuarios_df.to_csv('/home/yuripedro/Documentos/Git hub/DenStream_NOMA/desempenho_individual_DS/desempenho_usuario_df'+ str(self.t) +'_.csv')
            
           

        if self.t % self.tp == 0 & self.t !=0:  
            self.manutencao()

        self.t += 1

    def update_cluster_id_mt(self,usuario_id,cluster_id):
        
        if len(self.cluster_id_mt)>0:
            for i,eu_id in enumerate(usuario_id):
                ### if para testar se o cluster existe
                if str(cluster_id[i]) in self.cluster_id_mt:
                    ### loop dentro do bloco eu_id
                    for eu_do_bloco in eu_id:
                        add1 = True
                        # comparar com cada elemento do bloco
                        for key in self.cluster_id_mt:
                            if int(eu_do_bloco) in self.cluster_id_mt[key]:
                                add1 = False
                        if add1:
                             # add novo elemento usando append
                            self.cluster_id_mt[str(cluster_id[i])].append(int(eu_do_bloco))
                                
                               
                                
                else:
                    self.cluster_id_mt[str(cluster_id[i])]=[]
                    ### loop dentro do bloco eu_id
                    for eu_do_bloco in eu_id:
                        add2 = True
                        # comparar com cada elemento do bloco
                        for key in self.cluster_id_mt:
                            if int(eu_do_bloco) in self.cluster_id_mt[key]:
                                add2=False
                        if add2:
                            # add novo elemento usando append
                            self.cluster_id_mt[str(cluster_id[i])].append(int(eu_do_bloco))
        else:
            self.cluster_id_mt[str(cluster_id[0])]=[]
            for i,eu_id in enumerate(usuario_id):
                for eu_do_bloco in eu_id:
                    self.cluster_id_mt[str(cluster_id[i])].append(int(eu_do_bloco))



    def _validate_sample_weight(self, sample_weight, n_samples):
        """Set the sample weight array."""
        if sample_weight is None:
            # uniform sample weights
            sample_weight = np.ones(n_samples, dtype=np.float64, order='C')
        else:
            # user-provided array
            sample_weight = np.asarray(sample_weight, dtype=np.float64,
                                       order="C")
        if sample_weight.shape[0] != n_samples:
            raise ValueError("Shapes of X and sample_weight do not match.")
        return sample_weight 



    def _restricao_sic(self,micro_cluster):
                
        gamaL = micro_cluster.getGainChannel()

        #### ordem crescente
        gamaL.sort()
        p_list = dsp.alloc_power(gamaL,self.alpha)

        ### p_list esta do menor ganho para o maior
        sucesso =[]
        
        param=1
        for receptor in range(len(gamaL)-1):
            diff = p_list[receptor]*self.Pt*(gamaL[receptor+1])

            aux = sum(p_list[param:])

            diff = diff-(aux*self.Pt*(gamaL[receptor+1]))
            if diff >=self.p_tol:
                sucesso.append(True)
            else:
                sucesso.append(False)
            param=param+1

           

        if sum(sucesso) == len(sucesso):
            return True

        
        return False


    def sandard_d_(self,list_gc,sample):
        sample_=sample
        nova_lista=list_gc
        nova_lista.append(sample_)
        sd_novo = np.std(nova_lista)
        
        
        return sd_novo
    
  