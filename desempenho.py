import numpy as np

def get_index_vc(vect):
  index =[]
  for i in range(len(vect)-1):
    if vect[i]-vect[i+1] != 0:
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
 
  num = p_list[index]*Pt*gamaUser

  p_list = p_list[index+1:]
  p_array = np.array(p_list)
  den_list = p_array*Pt*gamaUser

  den = np.sum(den_list)
  den = den+(w*(N0*B))
  r = w*B*np.log2(1+(num/den))

  return r


def sum_data_rate(gamaL):
    w =100
    B = 180*(10**3)
    N0 = 10**(-17.3)
    alpha= 0.2
    Pt = ((10**(4.6))*(10**-3))

    gamaL.sort()
    p_list = alloc_power(gamaL,alpha)
    #print("p_list: ",p_list)
    
    r_array = np.ones((24,1))
    r_array[:] = float(np.NaN)
    
    for ind in range(len(gamaL)):
        gamaUser = gamaL[ind]
        r = data_rate(w,B,Pt,gamaUser,N0,p_list,ind)
        #print("r_teste: ", r)
        r_array[ind] = r

    output = r_array[np.isfinite(r_array)]
    R_global = np.sum(output)

    return r_array,R_global


def resultado(var_aux,var_aux_outlier,y_tempo):

    usuarioRotulos = np.zeros((12,2))

    lista_refatorada= []

    for i in var_aux:
        if len(i) != 0:
            for j in i:
                lista_refatorada.append(j)

    if len(var_aux_outlier)!= 0:
      for i in var_aux_outlier:
          if len(i) != 0:
              for j in i:
                  lista_refatorada.append(j)
    
    idx =0 
    for valor in lista_refatorada:
        usuarioRotulos[idx,0] = valor
        usuarioRotulos[idx,1] = y_tempo[0][idx]
        idx= idx+1
    
    usuarioRotulos_sort = usuarioRotulos[np.argsort(usuarioRotulos[:, 0])]
   
    index = get_index_vc(usuarioRotulos_sort[:, 0])

    usuarioRotulos_sort_split = np.split(usuarioRotulos_sort,index)
    print("usuarioRotulos_sort_split: ",usuarioRotulos_sort_split)

    drList_final = []
    dr_global_final = []
    drList = []
    dr_global = []
    for i in range(len(usuarioRotulos_sort_split)):
      gamaL = []
      cluster = usuarioRotulos_sort_split[i]
      for m in range(len(cluster)):
          gamaL.append(cluster[m][0])
      r,R_global = sum_data_rate(gamaL)
      dr_global.append(R_global)

    drList.append(r)

    dr_global_final.append(dr_global)
    drList_final.append(drList)

    return dr_global_final,drList_final