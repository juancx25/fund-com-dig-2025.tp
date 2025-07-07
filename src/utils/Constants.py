DATA_SIZE: int = 20                     # Cantidad de bits enviados
Tb: float = 0.01                        # Tiempo entre bits de información
fs: float = 1000                        # Frecuencia de muestreo
SAMPLE_RESOLUTION = int(Tb * fs)        # Cantidad de muestras totales (fs muestras en Tb segundos)

fc: float = 100                         # Frecuencia de la señal portadora (para ondas moduladas)

M = 4                                   # Multiplicidad de la señal. Debe respetar M = 2^k, con k entero positivo