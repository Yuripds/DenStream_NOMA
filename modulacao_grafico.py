import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

def plot_M_QAM(M, N=1000, SNR_dB=25):
    # Parâmetros da modulação
    k = int(np.log2(M))    # Número de bits por símbolo
    M_sqrt = int(np.sqrt(M))
    if M_sqrt ** 2 != M:
        raise ValueError("M must be a perfect square.")
    Eb = 1     # Energia média por bit
    T = 1      # Duração do bit

    # Gerar símbolos da modulação
    bits = np.random.randint(0, 2, N*k)
    bits_reshape = np.reshape(bits, (len(bits)//k,k))
    symbols = np.zeros(N, dtype=np.complex64)
    for i in range(0, N, k):
        row_idx = int(''.join(map(str, bits_reshape[i][0:(len(bits_reshape[0])//2)])), 2)
        col_idx = int(''.join(map(str, bits_reshape[i][(len(bits_reshape[0])//2):len(bits_reshape)+1] )), 2)
        symbols[i] = (row_idx + 1j * col_idx) / np.sqrt(Eb)

    # Adicionar ruído gaussiano branco ao sinal
    SNR = 10**(SNR_dB/10)
    sigma = np.sqrt(Eb/(2*SNR))
    noise = sigma * (np.random.randn(N) + 1j*np.random.randn(N))
    received_symbols = symbols + noise

    # Plotar constelação dos símbolos
  #  plt.figure(figsize=(6, 6))
  #  plt.scatter(received_symbols.real, received_symbols.imag, marker='.', color='blue')
  #  plt.grid(True)
  #  plt.title(f'Constelação dos símbolos {M}-QAM')
  #  plt.show()


    return received_symbols


#received_symbols = plot_M_QAM(64,N=1000,SNR_dB=15)  # Gera e plota um sinal 16-QAM
# print(received_symbols)