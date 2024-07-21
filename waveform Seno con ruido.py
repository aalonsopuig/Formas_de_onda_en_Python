"""
Título: Generación de Onda Senoidal con Ruido de Alta Frecuencia

Descripción: Este programa genera un ciclo de una onda senoidal y le suma ruido de alta frecuencia.
El nivel de ruido y la frecuencia del ruido se pueden ajustar mediante variables. La señal 
resultante se guarda en un archivo CSV y se muestra en una gráfica. La amplitud máxima de la señal 
resultante no supera 1.

Autor: ChatGPT con prompts de Alejandro Alonso Puig
Fecha: 17 de julio de 2024
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parámetros de la señal
num_points = 2047  # número de puntos en la señal
fs = 1000  # frecuencia de muestreo (Hz)
f_seno = 5  # frecuencia de la onda senoidal (Hz)
factor_ruido = 0.25  # factor de ruido (porcentaje de la amplitud de la onda original)
f_ruido_factor = 20  # factor de la frecuencia del ruido en relación a la frecuencia de la onda senoidal

# Amplitud de la señal senoidal ajustada
amplitud = 1 - factor_ruido

# Generar un ciclo de la onda senoidal
t = np.linspace(0, 1 / f_seno, num_points, endpoint=False)  # vector de tiempo para un ciclo
seno = amplitud * np.sin(2 * np.pi * f_seno * t)

# Generar ruido de alta frecuencia
f_ruido = f_ruido_factor * f_seno  # frecuencia del ruido, al menos 10 veces la frecuencia de la onda original
ruido = factor_ruido * np.sin(2 * np.pi * f_ruido * t)  # ruido ajustado por el factor de ruido

# Sumar ruido a la onda senoidal
señal_con_ruido = seno + ruido

# Convertir los valores de la señal para usar coma como separador decimal
señal_con_ruido_coma = [str(value).replace('.', ',') for value in señal_con_ruido]

# Crear un DataFrame con los valores modificados
señal_df_coma = pd.DataFrame(señal_con_ruido_coma)

# Guardar el DataFrame en un archivo CSV con coma como separador decimal y sin encabezado ni comillas
file_path_comma = "seno_con_ruido.csv"
señal_df_coma.to_csv(file_path_comma, index=False, header=False, quoting=3, sep=' ')

# Graficar la señal generada
plt.plot(t, señal_con_ruido, label="Señal con Ruido")
plt.plot(t, seno, label="Señal Senoidal Original", linestyle='--')
plt.title("Onda Senoidal con Ruido de Alta Frecuencia")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)
plt.show()

print(f"Archivo guardado en {file_path_comma}")
