"""
Título: Generación de Señal CMOS con Ruido de Alta Frecuencia

Descripción: Este programa genera una señal CMOS y le añade ruido de alta frecuencia. 
El nivel de ruido y la frecuencia del ruido se pueden ajustar mediante variables configurables. 
La señal resultante se guarda en un archivo CSV y se muestra en una gráfica.

Autor: ChatGPT con prompts de Alejandro Alonso Puig
Fecha: 17 de julio de 2024
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parámetros de la señal
num_points = 2047  # número de puntos en la señal
fs = 1000  # frecuencia de muestreo (Hz)
f_cmos = 5  # frecuencia de la señal CMOS (Hz)
factor_ruido = 0.15  # factor de ruido (porcentaje de la amplitud de la onda original)
f_ruido_factor = 40  # factor de la frecuencia del ruido en relación a la frecuencia de la señal CMOS

# Amplitud de la señal CMOS ajustada
amplitud_ruido = factor_ruido
amplitud_cmos_alta = 1 - amplitud_ruido
amplitud_cmos_baja = 0

# Generar un ciclo de la señal CMOS
t = np.linspace(0, 1 / f_cmos, num_points, endpoint=False)  # vector de tiempo para un ciclo
cmos_signal = amplitud_cmos_baja + (amplitud_cmos_alta - amplitud_cmos_baja) * ((np.sign(np.sin(2 * np.pi * f_cmos * t)) + 1) / 2)  # señal CMOS

# Generar ruido de alta frecuencia
f_ruido = f_ruido_factor * f_cmos  # frecuencia del ruido, al menos 10 veces la frecuencia de la onda original
ruido = amplitud_ruido * np.sin(2 * np.pi * f_ruido * t)  # ruido ajustado por el factor de ruido

# Sumar ruido a la señal CMOS
señal_con_ruido = cmos_signal + ruido

# Limitar la señal para que no supere la amplitud de 1
señal_con_ruido = np.clip(señal_con_ruido, -1, 1)

# Convertir los valores de la señal para usar coma como separador decimal
señal_con_ruido_coma = [str(value).replace('.', ',') for value in señal_con_ruido]

# Crear un DataFrame con los valores modificados
señal_df_coma = pd.DataFrame(señal_con_ruido_coma)

# Guardar el DataFrame en un archivo CSV con coma como separador decimal y sin encabezado ni comillas
file_path_comma = "cmos_con_ruido.csv"
señal_df_coma.to_csv(file_path_comma, index=False, header=False, quoting=3, sep=' ')

# Graficar la señal generada
plt.plot(t, señal_con_ruido, label="Señal CMOS con Ruido")
plt.plot(t, cmos_signal, label="Señal CMOS Original", linestyle='--')
plt.title("Señal CMOS con Ruido de Alta Frecuencia")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)
plt.show()

print(f"Archivo guardado en {file_path_comma}")
