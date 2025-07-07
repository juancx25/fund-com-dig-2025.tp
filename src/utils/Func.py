import numpy as np
from scipy.special import erfc

""" Funciones utilitarias que no pertenecen a ninguna abstracción específica
"""

# Convierte una secuencia de bits en símbolos de tamaño K
def bits2sym(bits, K):
    pad = (-len(bits)) % K
    if pad:
        bits = np.concatenate([bits, np.zeros(pad, int)])
    return bits.reshape(-1, K).dot(1 << np.arange(K)[::-1])

# Genera una entrada aleatoria de ceros y unos, dado el tamaño especificado.
def generateInputData(DATA_SIZE):
    return np.random.randint(2, size = DATA_SIZE)

def Q(x) -> list[float]:
    return 0.5 * erfc(x / np.sqrt(2))

def isLog2Integer(value) -> bool:
    return np.log2(value).is_integer()

