import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sympy.combinatorics.graycode import random_bitstring

sns.set()

def gray_decode(n):
    m = n >> 1
    while m:
        n ^= m
        m >>= 1
    return n

def plot_M_QAM(M, N=1000):
    # Parâmetros da modulação
    k = int(np.log2(M))    # Número de bits por símbolo
    M_sqrt = int(np.sqrt(M))
    if M_sqrt ** 2 != M:
        raise ValueError("M must be a perfect square.")
    Eb = 1     # Energia média por bit
   
    # Gerar símbolos da modulação
    bits = np.random.randint(0, 2, N*k)
    bits_reshape = np.reshape(bits, (len(bits)//k,k))
    symbols = np.zeros(N, dtype=np.complex64)
    for i in range(0, N):
        row_idx = gray_decode(int(''.join(map(str, bits_reshape[i][0:(len(bits_reshape[0])//2)])), 2))
        col_idx = gray_decode(int(''.join(map(str, bits_reshape[i][(len(bits_reshape[0])//2):len(bits_reshape)+1] )), 2))

        symbols[i] = (row_idx + 1j * col_idx) / np.sqrt(Eb)

    return symbols


def add_ruido(symbols, SNR_dB=25):
    Eb = 1 
    # Adicionar ruído gaussiano branco ao sinal
    SNR = 10**(SNR_dB/10)
    sigma = np.sqrt(Eb/(2*SNR))
    noise = sigma * (np.random.randn(len(symbols)) + 1j*np.random.randn(len(symbols)))
    received_symbols = symbols + noise

    # Plotar constelação dos símbolos
 #   plt.figure(figsize=(6, 6))
 #   plt.scatter(received_symbols.real, received_symbols.imag, marker='.', color='blue')
 #   plt.grid(True)
 #   plt.title(f'Constelação dos símbolos {M}-QAM')
 #   plt.show()

    return received_symbols

# teste
a=plot_M_QAM(M=4, N=1000)
print(a)