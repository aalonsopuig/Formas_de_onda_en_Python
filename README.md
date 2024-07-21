# Formas_de_onda_en_Python
Generación de formas de onda en pantalla y CSV para carga en generadores de funciones.
Se trata de una serie de programas en Python, realizados con la ayuda de ChatGPT 4o para generar formas de onda en fichero CSV que se pueden cargar en muchos generadores de funciones. Las formas de onda se han realizado no superando una amplitud de 1 y con 2047 puntos en eje X. Esto es posible modificarlo en los parámetros del inicio del programa. También se incluyen los ficheros CSV generados por si son de interes para la carga directa en generadores de funciones.

Los programas requieren varias librerías que se pueden instalar desde el propio terminal del IDE ejecutando: pip install numpy pandas matplotlib


**Generación de señal cardiaca (ECG)**

Este programa simula una señal de electrocardiograma (ECG) utilizando funciones gaussianas para representar las diferentes ondas del ciclo cardíaco. Las ondas P, Q, R, S y T se generan con funciones gaussianas ajustadas, mientras que los segmentos PR y ST se representan como segmentos de voltaje constante para mayor realismo. La señal generada incluye 2047 puntos para un ciclo completo del ECG, asegurando una alta resolución.

La señal resultante se guarda en un archivo CSV, utilizando comas como separadores decimales y sin encabezados, para facilitar su uso en otras aplicaciones y análisis. Además, el programa visualiza la señal ECG generada en una gráfica, proporcionando una representación visual inmediata del resultado. Este programa es útil para estudios y demostraciones relacionadas con la biomedicina y la instrumentación médica.

![image](https://github.com/user-attachments/assets/93b28b33-8eca-433a-a280-f2022423d258)

**Generación de ciclo de señal AM**

Este programa genera una señal de modulación de amplitud (AM) utilizando una onda portadora senoidal y una onda moduladora senoidal, desfasada 180 grados. La modulación se realiza con una profundidad del 80%, y se asegura que la amplitud máxima de la señal modulada no supere el valor de 1. La señal se genera con 2047 puntos para un ciclo completo, proporcionando una alta resolución.

El resultado de la señal AM se guarda en un archivo CSV, utilizando comas como separadores decimales y sin encabezados, facilitando su uso en otras aplicaciones y análisis. Además, el programa visualiza la señal AM generada en una gráfica, ofreciendo una representación visual inmediata del resultado. Este programa es útil para estudios y demostraciones en telecomunicaciones, procesamiento de señales y aplicaciones educativas.

![image](https://github.com/user-attachments/assets/1e5a1e46-fc72-4f85-9a56-883dceed196f)

