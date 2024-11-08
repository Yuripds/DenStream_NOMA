import numpy as np
import seaborn as sns

sns.set()

def get_index_vc(vect):
  roturlos = vect[:,1]
  index =[]
  for i in range(len(roturlos)-1):
    if roturlos[i]-roturlos[i+1] != 0:
      index.append(i+1)

  return index

def alloc_power(gamaL,alpha):
  p_list = []

  den = 0
  for i in range(len(gamaL)):
    den = den + ((abs(gamaL[-1])/abs(gamaL[i]))**(alpha))

  for i in range(len(gamaL)):
    p = ((abs(gamaL[-1])/abs(gamaL[i]))**(alpha)) / den
    p_list.append(p)

  return p_list


def data_rate(w,B,Pt,gamaUser,N0,p_list,index):
 
  num = p_list[index]*Pt*(gamaUser**2)

  p_list = p_list[index+1:]
  p_array = np.array(p_list)
  den_list = p_array*Pt*(gamaUser**2)

  den = np.sum(den_list)
  den = den+(w*(N0*B))
  r = w*B*np.log2(1+(num/den))

  return r


def sum_data_rate(gamaL,alpha,B,N0,Pt):
    w =100
    gamaL.sort()
    p_list = alloc_power(gamaL,alpha)
    #print("p_list: ",p_list)
    
    r_array = np.ones((12,1))
    r_array[:] = float(np.NaN)
    
    for ind in range(len(gamaL)):
        gamaUser = gamaL[ind]
        r = data_rate(w,B,Pt,gamaUser,N0,p_list,ind)
        #print("r_teste: ", r)
        r_array[ind] = r

    output = r_array[np.isfinite(r_array)]
    R_global = np.sum(output)

    return r_array,R_global


def oma_data_rate(g_canal,n_usuarios,B,N0,Pt):
  w =100
  num = Pt*(g_canal**2)
  den = N0*B*w

  d_rate = (1/n_usuarios)*B*w*np.log2(1+(num/den))

  return d_rate


def oma_sum_data_rate(g_canal,B,N0,Pt):
    g_canal_list = []
    for i in g_canal:
      g_canal_list.append(i)

    sum_dr_list = []
    for i in g_canal_list:
        sum_dr_list.append(oma_data_rate(i,len(g_canal_list),B,N0,Pt))
    sum_dr =sum(sum_dr_list)

    return sum_dr,sum_dr_list


def mp_resultado(usuarios_gc,usuario_id,cluster_id_mt,alpha,B, N0,Pt):
    
    usuarios_f=[]
    usuario_id_ref = []
    id_aux=0
    for bloco_ue in usuarios_gc:
      for ue in range(len(bloco_ue)):
        usuarios_f.append(bloco_ue[ue])
        usuario_id_ref.append(int(usuario_id[id_aux][ue]))
      id_aux = id_aux+1


    #### consultar a configuração padrão cluster_id_mt
    y_tempo=[]
    for uid in usuario_id_ref:
      for i,key in enumerate(cluster_id_mt):
        if uid in cluster_id_mt[key]:
          y_tempo.append(int(key))


    if -1 in y_tempo:
      flag_oma = True
    else:
      flag_oma = False
    
    usuarioRotulos = np.zeros((len(usuarios_f),2))    
    idx =0 
    for valor in usuarios_f:
        usuarioRotulos[idx,0] = valor
        usuarioRotulos[idx,1] = y_tempo[idx]
        idx= idx+1
    
    usuarioRotulos_sort = usuarioRotulos[np.argsort(usuarioRotulos[:, 1])]

    index = get_index_vc(usuarioRotulos_sort)

    gama_aux = usuarioRotulos_sort[:,0]
    usuarioRotulos_sort_split = np.split(gama_aux,index)

    drList_final = []
    dr_global_final = []
    drList = []
    dr_global = []
    for i in range(len(usuarioRotulos_sort_split)):
      gamaL = []
      cluster = usuarioRotulos_sort_split[i]
      if (i==0) & flag_oma | len(cluster)==1:
        for m in range(len(cluster)):
            gamaL.append(cluster[m])
        r,R_global = oma_sum_data_rate(gamaL,B,N0,Pt)
        dr_global.append(R_global)

        drList.append(r)

      else:
        for m in range(len(cluster)):
            gamaL.append(cluster[m])
        r,R_global = sum_data_rate(gamaL,alpha,B,N0,Pt)
        dr_global.append(R_global)

        drList.append(r)
 

    dr_global_final.append(dr_global)
    drList_final.append(drList)

    return dr_global_final,drList_final