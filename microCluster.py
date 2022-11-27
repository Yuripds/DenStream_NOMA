


class MicroCluster:
    def __init__(self, lambd, creation_time):
        self.lambd = lambd
        self.decay_factor = 2 ** (-lambd)
        self.sum_of_weights = 0
        self.creation_time = creation_time
        self.gainChannel = []
        self.ganhoTempo = []
        self.sampleList = []
       

    def insert_sample(self, sample,estimacaoGanhoCanal, weight):
        # Update Ganho de canal
        gc_aux = self.gainChannel
        gc_aux.append(sample[0])
        self.gainChannel = gc_aux

        # Update Ganho no tempo

        gt_aux = self.ganhoTempo
        gt_aux.append(estimacaoGanhoCanal)
        self.ganhoTempo= gt_aux

        # Update sample list
        sample_aux = self.sampleList
        sample_aux.append(sample)
        self.sampleList = sample_aux

    

        if self.sum_of_weights != 0:
            # Update sum of weights
            old_sum_of_weights = self.sum_of_weights
            new_sum_of_weights = old_sum_of_weights * self.decay_factor + weight

            self.sum_of_weights = new_sum_of_weights

        else:

            self.sum_of_weights = weight





    def delete_sample(self,index):  
        # Update Ganho de canalnew_sample_list
        self.gainChannel.pop(index)

        # Update Ganho no tempo
        self.ganhoTempo.pop(index)

        # Update sample list
        self.sampleList.pop(index)


    def weight(self):
        return self.sum_of_weights

    def getGainChannel(self):
        return self.gainChannel
    
    def getGanhoTempo(self):
        return self.ganhoTempo
    
    
    def getSample(self):
        return self.sampleList


    

#    def __deepcopy__(self):
#        new_micro_cluster = MicroCluster(self.lambd, self.creation_time)
#        new_micro_cluster.sum_of_weights = self.sum_of_weights
#        new_micro_cluster.sampleList = self.sampleList
#        new_micro_cluster.gainChannel =self.gainChannel
#        new_micro_cluster.ganhoTempo=self.ganhoTempo
#        return new_micro_cluster

