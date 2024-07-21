"""
Título: Generación de Onda Cuadrada como Suma de Tres Ondas Senoidales Basado en Fourier

Descripción: Este programa genera una onda cuadrada utilizando la suma de tres ondas senoidales
con relaciones de frecuencia 1, 1/3 y 1/5. La señal resultante se guarda en un archivo CSV y se 
muestra en una gráfica. Este enfoque se basa en la serie de Fourier, que descompone una función 
periódica en una suma de senos y cosenos.

Autor: ChatGPT con prompts de Alejandro Alonso Puig
Fecha: 17 de julio de 2024
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parámetros de la señal
num_points = 2047  # número de puntos en la señal
fs = 1000  # frecuencia de muestreo (Hz)
f_base = 5  # frecuencia base de la onda cuadrada (Hz)

# Generar el vector de tiempo para un ciclo de la señal
t = np.linspace(0, 1 / f_base, num_points, endpoint=False)  # vector de tiempo para un ciclo

# Generar las ondas senoidales con las frecuencias 1, 1/3 y 1/5 de la frecuencia base
senoidal_1 = np.sin(2 * np.pi * f_base * t)
senoidal_3 = (1/3) * np.sin(2 * np.pi * (3 * f_base) * t)
senoidal_5 = (1/5) * np.sin(2 * np.pi * (5 * f_base) * t)

# Sumar las tres ondas senoidales para aproximar una onda cuadrada
onda_cuadrada = senoidal_1 + senoidal_3 + senoidal_5

# Normalizar la señal para que la amplitud máxima sea 1
onda_cuadrada = onda_cuadrada / np.max(np.abs(onda_cuadrada))

# Convertir los valores de la señal para usar coma como separador decimal
onda_cuadrada_coma = [str(value).replace('.', ',') for value in onda_cuadrada]

# Crear un DataFrame con los valores modificados
onda_df_coma = pd.DataFrame(onda_cuadrada_coma)

# Guardar el DataFrame en un archivo CSV con coma como separador decimal y sin encabezado ni comillas
file_path_comma = "cuadrada_fourier3.csv"
onda_df_coma.to_csv(file_path_comma, index=False, header=False, quoting=3, sep=' ')

# Graficar la señal generada
plt.plot(t, onda_cuadrada, label="Onda Cuadrada Aproximada")
plt.plot(t, senoidal_1, label="Senoidal 1", linestyle='--')
plt.plot(t, senoidal_3, label="Senoidal 1/3", linestyle='--')
plt.plot(t, senoidal_5, label="Senoidal 1/5", linestyle='--')
plt.title("Generación de Onda Cuadrada como Suma de Tres Ondas Senoidales")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)
plt.show()

print(f"Archivo guardado en {file_path_comma}")
