import numpy as np
from classes.abstract.Signal import SignalModulation, Signal
from utils.Constants import *
from utils import Func

"""
    Aquí se definen todas las señales particulares en base a su abstracción genérica.
    Cada clase implementará los métodos definidos por Signal
"""


class PolarNRZ(Signal):

    def getName(self) -> str:
        return "Polar, NRZ"
    
    def setModulation(self) -> SignalModulation:
        return SignalModulation.BASE_BAND
        
    def generateSignal(self) -> list[float]:
        return np.repeat(np.where(self.bits == 1, self.amplitude/2, -self.amplitude/2), SAMPLE_RESOLUTION)
    
    def calculateError(self, Yb) -> list[float]:
        return [Func.Q(np.sqrt(2*i)) for i in Yb]
    


class UnipolarNRZ(Signal):

    def getName(self) -> str:
        return "Unipolar, NRZ"
    
    def setModulation(self) -> SignalModulation:
        return SignalModulation.BASE_BAND
        
    def generateSignal(self):
        return np.repeat(np.where(self.bits == 1, self.amplitude, 0), SAMPLE_RESOLUTION)
    
    def calculateError(self, Yb) -> list[float]:
        return [Func.Q(np.sqrt(2*i)) for i in Yb]
    


class PolarRZ(Signal):

    def getName(self) -> str:
        return "Polar, RZ"
    
    def setModulation(self) -> SignalModulation:
        return SignalModulation.BASE_BAND
        
    def generateSignal(self):
        signal = np.zeros_like(np.repeat(np.where(self.bits == 1, self.amplitude, -self.amplitude), SAMPLE_RESOLUTION))
        for i, bit in enumerate(self.bits):
            start = i * SAMPLE_RESOLUTION
            mid = start + SAMPLE_RESOLUTION // 2
            if bit == 1:
                signal[start:mid] = self.amplitude/2
            else:
                signal[start:mid] = -self.amplitude/2
        return signal
    
    def calculateError(self, Yb) -> list[float]:
        return [Func.Q(np.sqrt(i)) for i in Yb]
        


class UnipolarRZ(Signal):

    def getName(self) -> str:
        return "Unipolar, RZ"
    
    def setModulation(self) -> SignalModulation:
        return SignalModulation.BASE_BAND
        
    def generateSignal(self):
        signal = np.zeros_like(np.repeat(np.where(self.bits == 1, self.amplitude, -self.amplitude), SAMPLE_RESOLUTION))
        for i, bit in enumerate(self.bits):
            start = i * SAMPLE_RESOLUTION
            mid = start + SAMPLE_RESOLUTION // 2
            if bit == 1:
                signal[start:mid] = self.amplitude
            else:
                signal[start:mid] = 0
        return signal
    
    def calculateError(self, Yb) -> list[float]:
        return [Func.Q(np.sqrt(i)) for i in Yb]



class Manchester(Signal):

    def getName(self) -> str:
        return "Manchester"
    
    def setModulation(self) -> SignalModulation:
        return SignalModulation.BASE_BAND

    def generateSignal(self):
        return self.amplitude * (2 * np.logical_xor(np.repeat(self.bits, SAMPLE_RESOLUTION), self.clk).astype(int) - 1)

    def calculateError(self, Yb) -> list[float]:
        return [Func.Q(np.sqrt(i)) for i in Yb]



class MASK(Signal):

    def getName(self) -> str:
        return "ASK"
    
    def setModulation(self) -> SignalModulation:
        return SignalModulation.MODULATED

    def generateSignal(self):
        amplitudes = Func.bits2sym(self.bits, self.K) * (self.amplitude/(self.M-1))
        return np.repeat(amplitudes, SAMPLE_RESOLUTION * self.K) * np.cos(2*np.pi * fc * self.x)

    def calculateError(self, Yb) -> list[float]:
        return [(2*(self.M-1)/(self.M*self.K)) * Func.Q(np.sqrt(6*self.K* i /(self.M**2-1))) for i in Yb]
    

    
class MPSK(Signal):

    def getName(self) -> str:
        return "PSK"
    
    def setModulation(self) -> SignalModulation:
        return SignalModulation.MODULATED

    def generateSignal(self):
        phases = 2*np.pi*Func.bits2sym(self.bits, self.K) / self.M
        phasesPerSample = np.repeat(phases, SAMPLE_RESOLUTION * self.K)
        return self.amplitude * np.cos(2 * np.pi * fc * self.x + phasesPerSample)

    def calculateError(self, Yb) -> list[float]:
        return [(2/self.K)*Func.Q(np.sqrt(2*self.K* i )*np.sin(np.pi/self.M)) for i in Yb]
