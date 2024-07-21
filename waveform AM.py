"""
Título: Generación de Señal AM con Onda Moduladora Desfasada 180 Grados

Descripción: Este programa genera una señal de modulación de amplitud (AM) utilizando una
onda portadora senoidal y una onda moduladora senoidal, modulando con una profundidad del 80%.
La onda moduladora está desfasada 180 grados. El resultado se guarda en un archivo CSV y se
muestra en una gráfica.

Autor: ChatGPT con prompts de Alejandro Alonso Puig
Fecha: 17 de julio de 2024
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parámetros de la señal
num_points = 2047  # número de puntos en el eje x
fc = 500  # frecuencia de la portadora
fm = 50  # frecuencia de la moduladora
Ac = 0.5  # amplitud de la portadora
Am = 0.5  # amplitud de la moduladora (100% de profundidad de modulación)

# Duración de un ciclo de la onda moduladora
T = 1 / fm
t = np.linspace(0, T, num_points, endpoint=False)  # vector de tiempo para un ciclo

# Generar la onda portadora en fase normal
carrier = Ac * np.cos(2 * np.pi * fc * t)

# Generar la onda moduladora desfasada 180 grados
modulator = Am * np.cos(2 * np.pi * fm * t + np.pi)

# Generar la señal AM
am_signal = (1 + modulator) * carrier

# Normalizar la señal AM para que la amplitud máxima sea 1
am_signal = am_signal / np.max(np.abs(am_signal))

# Convertir los valores de la señal AM para usar coma como separador decimal
am_signal_comma = [str(value).replace('.', ',') for value in am_signal]

# Crear un DataFrame con los valores modificados
am_df_comma = pd.DataFrame(am_signal_comma)

# Guardar el DataFrame en un archivo CSV con coma como separador decimal y sin encabezado ni comillas
file_path_comma = "am_signal.csv"
am_df_comma.to_csv(file_path_comma, index=False, header=False, quoting=3, sep=' ')

# Graficar la señal AM generada
plt.plot(t, am_signal)
plt.title("Señal AM con Onda Moduladora Desfasada 180 Grados (un ciclo)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

print(f"Archivo guardado en {file_path_comma}")
