# Formas de onda en Python
Generación de formas de onda en pantalla y CSV para carga en generadores de funciones.
Se trata de una serie de programas en Python, realizados con la ayuda de ChatGPT 4o para generar formas de onda en fichero CSV que se pueden cargar en muchos generadores de funciones. Las formas de onda se han realizado no superando una amplitud de 1 y con 2047 puntos en eje X. Esto es posible modificarlo en los parámetros del inicio del programa. También se incluyen los ficheros CSV generados por si son de interes para la carga directa en generadores de funciones.

Los programas requieren varias librerías que se pueden instalar desde el propio terminal del IDE ejecutando: pip install numpy pandas matplotlib


## Generación de señal cardiaca (ECG)

Programa: waveform ECG.py<br>
Fichero CSV: ecg_signal.csv<br>

Este programa simula una señal de electrocardiograma (ECG) utilizando funciones gaussianas para representar las diferentes ondas del ciclo cardíaco. Las ondas P, Q, R, S y T se generan con funciones gaussianas ajustadas, mientras que los segmentos PR y ST se representan como segmentos de voltaje constante para mayor realismo. La señal generada incluye 2047 puntos para un ciclo completo del ECG, asegurando una alta resolución.

La señal resultante se guarda en un archivo CSV, utilizando comas como separadores decimales y sin encabezados, para facilitar su uso en otras aplicaciones y análisis. Además, el programa visualiza la señal ECG generada en una gráfica, proporcionando una representación visual inmediata del resultado. Este programa es útil para estudios y demostraciones relacionadas con la biomedicina y la instrumentación médica.

![image](https://github.com/user-attachments/assets/93b28b33-8eca-433a-a280-f2022423d258)

---

## Generación de ciclo de señal AM

Programa: waveform AM.py<br>
Fichero CSV: am_signal.csv<br>

Este programa genera una señal de modulación de amplitud (AM) utilizando una onda portadora senoidal y una onda moduladora senoidal, desfasada 180 grados. La modulación se realiza con una profundidad del 80%, y se asegura que la amplitud máxima de la señal modulada no supere el valor de 1. La señal se genera con 2047 puntos para un ciclo completo, proporcionando una alta resolución.

El resultado de la señal AM se guarda en un archivo CSV, utilizando comas como separadores decimales y sin encabezados, facilitando su uso en otras aplicaciones y análisis. Además, el programa visualiza la señal AM generada en una gráfica, ofreciendo una representación visual inmediata del resultado. Este programa es útil para estudios y demostraciones en telecomunicaciones, procesamiento de señales y aplicaciones educativas.

![image](https://github.com/user-attachments/assets/1e5a1e46-fc72-4f85-9a56-883dceed196f)

---
## Generación de Onda Senoidal con Ruido de Alta Frecuencia

Programa: waveform Seno con ruido.py<br>
Fichero CSV: seno_con_ruido.csv<br>

Este programa genera un ciclo de una onda senoidal y le añade ruido de alta frecuencia, asegurando que la amplitud máxima de la señal resultante no supere 1. El nivel de ruido y la frecuencia del ruido son ajustables mediante variables. La señal resultante se guarda en un archivo CSV llamado seno_con_ruido.csv y se muestra en una gráfica. Las variables de configuración principales incluyen el número de puntos en la señal (num_points), la frecuencia de la onda senoidal (f_seno), el factor de ruido (factor_ruido), que determina el porcentaje de la amplitud original que representa el ruido, y el factor de la frecuencia del ruido (f_ruido_factor), que ajusta la frecuencia del ruido en relación a la frecuencia de la onda senoidal.

![image](https://github.com/user-attachments/assets/ac1aa39c-c4f3-45fd-9a1a-4d504de3aba9)

---
## Generación de Señal CMOS con Ruido

Programa: waveform waveform CMOS con ruido.py<br>
Fichero CSV: cmos_con_ruido.csv<br>

Este programa genera una señal CMOS con ruido de alta frecuencia. La señal resultante se guarda en un archivo CSV llamado cmos_con_ruido.csv y se muestra en una gráfica. El programa permite ajustar el nivel de ruido y la frecuencia del ruido mediante variables configurables. 

![image](https://github.com/user-attachments/assets/427f5d48-f251-4e26-bd00-b80dcb2413a9)

