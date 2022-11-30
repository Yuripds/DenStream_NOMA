import sys
import numpy as np
from sklearn.utils import check_array
from copy import copy ,deepcopy
# from DenStreamLib import microCluster
from microCluster import *
from math import ceil
from sklearn.cluster import DBSCAN
import cmath
import desempenho as dsp
from statistics import pstdev

class DenStream:

    def __init__(self, lambd=1, beta=2, mu=2, zeta=5,p_tol=10,alpha=0.2,N0=10**-10,B=20*(10**6), Pt = ((10**(4.6))*(10**-3)),sd_out=10**4):
   
        self.lambd = lambd
        self.beta = beta
        self.mu = mu
        self.t = 0
        self.p_micro_clusters = []
        self.o_micro_clusters = []
        self.zeta = zeta
        self.newUsers = []
        self.estimacao_tempo_newUsers = []
        self.p_tol =p_tol
        self.alpha = alpha
        self.N0 = N0
        self.B = B
        self.sd_out= sd_out
        self.Pt = Pt
        
       

        if lambd > 0:
            self.tp = ceil((1 / lambd) * np.log((beta * mu) / (beta * mu - 1)))
        else:
            self.tp = sys.maxsize

    def _addUsers(self, X, y=None, y_old=None, estimacao_tempo=[], novos_users=[], estimacao_tempo_novosUsers=[], sample_weight=None, ad_users=False, time_param=500,sd_param=500):
            
            X = check_array(X, dtype=np.float64, order="C")

            n_samples, _ = X.shape

            sample_weight = self._validate_sample_weight(
                sample_weight, n_samples)

            estimacaoGanhoCanal = estimacao_tempo

            indx = 0
            for sample, weight in zip(X, sample_weight):
                self._partial_fit(sample, estimacaoGanhoCanal[indx], weight,sd_param)
                indx = indx+1


            #################################################### tratamento dos dados de novos usuários e guardando em variáveis ##########
            user_nlist = novos_users.to_numpy(dtype='float32')

            for i, users in enumerate(user_nlist):
                self.newUsers.append(users)
                self.estimacao_tempo_newUsers.append(
                         estimacao_tempo_novosUsers[i])
            
            ###############################################################################################################################
            y_tempo = []
            contador = 0
            
            drList_final = []
            dr_global_final=[]
            while contador < time_param:
                ################################ verificar o porque esta sendo criado grupos com apenas 1 usuário #####################
                
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

                        for i, users in enumerate(self.newUsers):
                            # add estimacao_tempo_novosUsers junto a fila de novos usuários
                            nova_amostra = users
                            new_sample_weight = np.ones(
                                1, dtype=np.float32, order='C')[0]

                            self._partial_fit(nova_amostra, self.estimacao_tempo_newUsers[i], new_sample_weight,sd_param)
                        
                        
                        for i,mc in enumerate(self.p_micro_clusters):
                            for m in range(len(mc.getGainChannel())):
                                y.append(i)
                           # index = self._get_group_index(user[1],self.p_micro_clusters)

                           
                        
                        y_tempo.append(y)


                else:
                    y_tempo.append(y_old)

                
               
                dr_global,drList = dsp.resultado(fixSamples,self.newUsers,y_tempo,self.t,self.alpha,self.B,self.N0,self.Pt)
                drList_final.append(drList)
                dr_global_final.append(dr_global)
                y_tempo =[]

                self.newUsers = []
                contador = contador+10
                self.t += 1            
                       

            
            return  drList_final,dr_global_final

               

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




    def _try_merge(self, sample,estimacaoGanhoCanal, weight, micro_cluster):
       
        
        if micro_cluster is not None:
            micro_cluster_copy = deepcopy(micro_cluster)
            micro_cluster_copy.insert_sample(sample,estimacaoGanhoCanal, weight)
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
                micro_cluster.insert_sample(sample, estimacaoGanhoCanal,weight)
                return True
                
        return False




    def _merging(self, sample,estimacaoGanhoCanal, weight,sd_param):
        _, nearest_p_micro_cluster = \
            self._get_nearest_micro_cluster(sample,self.p_micro_clusters,sd_param)

        success = self._try_merge(sample,estimacaoGanhoCanal, weight, nearest_p_micro_cluster)


        if not success:
            index, nearest_o_micro_cluster = \
                self._get_nearest_micro_cluster(sample,self.o_micro_clusters,sd_param)
            success = self._try_merge(sample,estimacaoGanhoCanal, weight, nearest_o_micro_cluster)
            
            if success:

                if nearest_o_micro_cluster.weight() > self.beta * self.mu:
                    del self.o_micro_clusters[index]
                    
                    self.p_micro_clusters.append(nearest_o_micro_cluster)
            else:
                micro_cluster = MicroCluster(self.lambd, self.t)
                micro_cluster.insert_sample(sample,estimacaoGanhoCanal, weight)
                self.o_micro_clusters.append(micro_cluster)


    def _decay_function(self, t):
        return 2 ** ((-self.lambd) * (t))



    def manutencao(self):
            for i,p_micro_cluster in enumerate(self.p_micro_clusters):
                gainList = p_micro_cluster.getGainChannel()
                
                ganhoTempoList = p_micro_cluster.getGanhoTempo()
                
                tam_init = len(gainList)
                idx=0
                while(tam_init>idx):
                    diff_pct = ((abs(ganhoTempoList[idx][self.t])  - abs(gainList[idx]))/abs(gainList[idx]))*100
                    ######### zeta é dado em porcentagem #############
                    if abs(diff_pct) >= self.zeta:
                        self.newUsers.append(np.array([abs(ganhoTempoList[idx][self.t]),cmath.phase(ganhoTempoList[idx][self.t])]))
                        self.estimacao_tempo_newUsers.append(ganhoTempoList[idx])
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
                tam_init = len(gainList_outL)
                idx=0
                while(tam_init>idx):
                    self.newUsers.append(sampleList[idx])
                    self.estimacao_tempo_newUsers.append(ganhoTempoList_out[idx])
                    o_micro_cluster.delete_sample(idx)
                    tam_init =tam_init-1
                if len(gainList_outL)==0:
                    self.o_micro_clusters.pop(op)




    def _partial_fit(self, sample,estimacaoGanhoCanal, weight,sd_param):

        self._merging(sample, estimacaoGanhoCanal, weight,sd_param)
        
        if self.t % self.tp == 0 & self.t !=0:  
            self.manutencao()

        self.t += 1

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
        for receptor in range(len(gamaL)-1):
            diff = p_list[receptor]*self.Pt*(gamaL[receptor+1])
            aux =0
            for i in range(len(gamaL)-1):
                aux = aux+p_list[i+1]*self.Pt*(gamaL[receptor+1])
            
            diff = diff-aux
            if diff >=self.p_tol:
                sucesso.append(True)
            else:
                sucesso.append(False)

        if sum(sucesso) == len(sucesso):
            return True

        
        return False


    def sandard_d_(self,list_gc,sample):
        sample_=sample
        nova_lista=list_gc
        nova_lista.append(sample_)
        sd_novo = np.std(nova_lista)
        
        
        return sd_novo