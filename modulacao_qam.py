import numpy as np

def generate_qam_symbols(M):
    if M % 4 != 0:
        raise ValueError("O valor de M deve ser um múltiplo de 4.")
    const_size = int(np.sqrt(M))
    if const_size ** 2 != M:
        raise ValueError("O valor de M deve ser um quadrado perfeito.")
    symbol_values = np.linspace(-const_size + 1, const_size - 1, const_size)
    real_part, imag_part = np.meshgrid(symbol_values, symbol_values)
    symbols = np.vectorize(complex)(real_part, imag_part)
    return symbols.reshape(-1)

# Exemplo de uso
#M = 256 # Modulação 16-QAM
#constellation = generate_qam_symbols(M)
#print(constellation)
