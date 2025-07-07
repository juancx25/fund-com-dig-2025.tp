from enum import Enum
from scipy.signal import welch
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
import numpy as np
from utils.Constants import *

""" Modulación de la señal

    Enumeración que define el tipo de señal con respecto a su modulación. Es implementado en cada señal.
"""
class SignalModulation(Enum):
    BASE_BAND = 1,
    MODULATED = 2

""" Señal estándar: clase abstracta que define los comportamientos genéricos de una señal.

    Atributos:
        input:      Secuencia de bits con los datos de entrada. Debe ser de tamaño DATA_SIZE
        amplitude:  Amplitud de la señal.
        M:          Multiplicidad de la señal.
"""
class Signal(ABC):
    def __init__(self, input, amplitude, M = 2):

        self.bits = input
        self.upscaledInput = np.repeat(input, SAMPLE_RESOLUTION)    # Señal de entrada ajustada a la resolución de muestreo
        self.modulation = self.setModulation()                      # Tipo de modulación. Definido en cada señal
        self.M = M
        self.K = int(np.log2(M))                                    # Bits por símbolo
        self.amplitude = amplitude
        self.clk = self.generateClk()                               # Señal de reloj
        
        self.x = np.linspace(0, Tb * DATA_SIZE, DATA_SIZE * SAMPLE_RESOLUTION, endpoint=False)  # Función lineal del tiempo
        self.y = self.generateSignal()
        
        return
    
    """ Establecer modulación

        Definido en cada clase hija.
    """
    @abstractmethod
    def setModulation(self) -> SignalModulation:
        pass

    """ Genera la señal de salida para la entrada proporcionada.

        Definido en cada clase hija de forma independiente.
    """
    @abstractmethod
    def generateSignal(self) -> list[float]:
        pass

    """ Calcula el error para todos los valores de Yb

        Definido en cada clase hija.
    """
    @abstractmethod
    def calculateError(self, Yb) -> list[float]:
        pass

    """ Devuelve el nombre de la señal

        Definido en cada clase hija.
    """
    @abstractmethod
    def getName() -> str:
        pass
    
    def generateClk(self) -> list[float]:
        return np.repeat(np.tile([0, 1], DATA_SIZE), SAMPLE_RESOLUTION // 2)

    def spectralDensity(self):
        return welch(self.y, fs=1/Tb, return_onesided = True)

    def plotAll(self):
        fig, axes = plt.subplots(2, 2, constrained_layout = True)
        fig.suptitle("Señal tipo " + self.getName(), fontsize=14)

        axes[0, 0].plot(self.x, self.upscaledInput)
        axes[0, 0].set_title("Origen")
        axes[0, 0].set_xlabel("[s]")
        axes[0, 0].set_ylabel("[V]")
        axes[0, 0].grid(True)
        
        axes[1, 0].plot(self.x, self.y)
        axes[1, 0].set_title("Señal codificada")
        axes[1, 0].set_xlabel("[s]")
        axes[1, 0].set_ylabel("[V]")
        axes[1, 0].grid(True)

        [x, Pxx] = self.spectralDensity()
        axes[0, 1].semilogy(x, Pxx)
        axes[0, 1].set_title("Densidad espectral")
        axes[0, 1].set_xlabel("[Hz]")
        axes[0, 1].set_ylabel("[V²/Hz]")
        axes[0, 1].grid(True)

        Yb_db = np.linspace(0, 10, 100)
        Yb = 10**(Yb_db / 10)
        error = self.calculateError(Yb)
        axes[1, 1].semilogy(Yb_db, error)
        axes[1, 1].set_title("Tasa de error")
        axes[1, 1].set_xlabel("γb[dB]")
        axes[1, 1].grid(True)

        plt.show()
        return