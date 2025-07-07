# fund-com-dig-2025.tp
[ES] Trabajo Práctico de Fundamentos de Comunicaciones Digitales, correspondiente al 4to año de la carrera de Ingeniería en Computación en la UNMdP

## Cómo usar
Al ejecutar el programa, se nos presentan dos opciones en un menú, una para cada tipo de ejercicio:

En la opción número 1, podremos elegir una opción para cada pulso a simular, de los cuales tenemos, en orden:
*Unipolar NRZ*, *Unipolar RZ*, *Polar NRZ*, *Polar RZ* y *Manchester*.

En la opción número 2, podremos elegir una opción para cada pulso a simular, las cuales son, en orden:
*2-ASK*, *M-ASK*, *2-PSK*, *M-PSK*

Cada codificación graficará:
- Señal de entrada
- Señal de salida
- Densidad espectral de potencia de la señal
- Tasa de error por bit asociada al código, en función de γ$_{b}$

Para seleccionar una opción en el menú o submenú, ingrese el número correspondiente a cada sección y presione ENTER. La opción 'Volver' regresará al menú anterior o cerrará la aplicación (en caso de encontrarse en el menú principal).

Al seleccionar una opción correspondiente a una codificación, se abrirá una ventana con los gráficos asociados. Para volver, cierre la ventana y se encontrará nuevamente en el submenú.

### Señal de entrada
La señal de entrada se genera automáticamente a la hora de ejecutar de forma distinta para cada una de las señales presentes. Esto quiere decir que, para cada ejecución nueva de la aplicación, cada código dispondrá de una señal diferente y, de necesitarse cambiar la señal de entrada para ese código específico, se requerirá un reinicio del programa.

### ¿Cómo cambio las constantes asociadas?
Existe un archivo Constants.py en la carpeta *utils/* que contiene:

- DATA_SIZE: Tamaño del paquete de bits enviados.
- Tb: Período de duración de cada bit.
- fs: Frecuencia de muestreo.

Onda modulada:
- fc: Frecuencia de la onda portadora.

Codificaciones M-arias:
M: Multiplicidad de la codificación. 

## ¿Cómo funciona?

### Señales
Una clase abstracta Signal (en *classes/Signal.py*) implementa las funciones generales de toda señal, y define aquellos métodos que serán típicos de cada señal, para poder ser implementado en cada una.
Cada clase heredada de Signal (en *classes/Signals.py*) implementa los comportamientos de cada señal. Se puede agregar una nueva señal fácilmente respetando esos lineamientos.

### Utils

En */utils* se encuentran:

**Menú:** Un menú genérico invocable y con la posibilidad de generar submenús llamándose a sí mismo.
**Func:** Funciones genéricas como la distribución de probabilidad (Q).
**Constants:** Explicado arriba. Tantas ganas de escribir no tengo, je

## Consignas

### FUNDAMENTOS DE COMUNICACIONES DIGITALES. TRABAJO PRÁCTICO.

El trabajo práctico consiste en la simulación de sistemas de transmisión digital, utilizando preferentemente Python, o bien Matlab o ‘C/C++` en el desarrollo de dos ejercicios, uno relativo a la primera parte de la materia, sobre transmisión Banda Base, y otro relacionado con la temática de los últimos capítulos de la misma, sobre el tema transmisión digital modulada.

**Ejercicio 1.** Simulación de sistemas de transmisión digital en Banda Base.

El ejercicio tiene tres niveles de desarrollo, que tienen una complejidad creciente.

**Nivel 1:**
Se propone una simulación de formas de onda en el tiempo, y densidades espectrales correspondientes, de al menos dos formatos de transmisión, uno de cada uno de los dos siguientes grupos de formatos: 

**Grupo a:** Formatos de pulso rectangular Unipolar NRZ, Unipolar RZ, Polar NRZ, Polar RZ
**Grupo b:** Formatos de pulso rectangular Mánchester, AMI y formato M-ario.

También simular que es lo que sucede en los casos UNRZ y PNRZ si en lugar del formato rectangular se utiliza un pulso de Nyquist, incluyendo el extremo del pulso sinc(rt).

**Nivel 2:**
Se propone una simulación de formas de onda en el tiempo, y densidades espectrales correspondientes de los formatos de los grupos anteriormente mencionados, planteado como un script genérico donde se pueda elegir que formato se desea simular, para luego mostrar sus características en el tiempo y la frecuencia. También simular que es lo que sucede en los casos UNRZ, PNRZ y M-ario si en lugar del formato rectangular se utiliza un pulso de Nyquist, incluyendo el extremo del pulso sinc(rt).

**Nivel 3:**
Completar alguno de los dos niveles 1 o 2 con una de las siguientes opciones:
**a.** Una simulación de la tasa de error que presenta el sistema, como probabilidad de error en función del parámetro γb.
**b.** A través de un ejemplo por simulación, mostrar el efecto de la Interferencia Inter simbólica (ISI).

**Ejercicio 2.** Simulación de sistemas de transmisión digital modulada y control de errores.

El ejercicio tiene tres niveles de desarrollo, que tienen una complejidad creciente.

**Nivel 1:**
Se propone una simulación de formas de onda en el tiempo, y densidades espectrales correspondientes, de al menos dos formatos de transmisión
pasabanda, uno de cada uno de los dos siguientes grupos de formatos:
**Grupo a:** Modulaciones binarias como 2ASK, 2FSK, 2PSK
**Grupo b:** Modulaciones M-arias MASK, MPSK, con valor de M a adoptar M ≥ 4, M = 2^n.

**Nivel 2:**
Se propone una simulación de formas de onda en el tiempo, y densidades espectrales correspondientes de las modulaciones digitales de los grupos anteriormente mencionados, planteado como un script genérico donde se pueda elegir que modulación se desea simular, para luego mostrar sus características en el tiempo y la frecuencia.

**Nivel 3:**
Completar alguno de los dos niveles 1 o 2 con una de las siguientes opciones:
**a.** Una simulación de la tasa de error que presenta el sistema, como probabilidad de error en función del parámetro γb.
**b.** Aplicar a un caso como el inciso anterior algún tipo de control de error.

## ¿Qué hay hecho?

- Simulación de todas las señales del grupo **a** del **Ejercicio 1**.
- Simulación de señal Manchester del grupo **b** del **Ejercicio 1**.
- Menú genérico
- Simulación de señales 2ASK, 2PSK del grupo **a** del **Ejercicio 2**.
- Ambas señales del grupo **b** del **Ejercicio 2**.

## ¿Qué quedó por hacer?

- Simulación de señales AMI y M-Arias del grupo **b** del **Ejercicio 1**
- Simulación de UNRZ y PNRZ con pulso de Nyquist en el **Ejercicio 1**
- Efecto de la Interferencia Inter Simbólica en el **Nivel 3** del **Ejercicio 1**
- Control de error en el **Nivel 3** del **Ejercicio 2**

## ¿Qué más podría agregarse?

- Funcionalidad de comparación de señales que permita elegir un grupo y compararlo en los mismos gráficos para detectar diferencias fácilmente
