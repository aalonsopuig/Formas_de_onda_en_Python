import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Número de puntos en el ciclo ECG
num_points = 2047

# Tiempo simulado para un ciclo ECG
t = np.linspace(0, 1, num_points)

# Funciones gaussianas para representar las ondas
def gaussian(x, mu, sig, amplitude):
    return amplitude * np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

# Generar cada componente de la señal ECG
p_wave = gaussian(t, 0.1, 0.025, 0.1)
q_wave = gaussian(t, 0.25, 0.01, -0.15)
r_wave = gaussian(t, 0.3, 0.01, 1.0)
s_wave = gaussian(t, 0.35, 0.01, -0.2)
t_wave = gaussian(t, 0.6, 0.05, 0.25)

# Segmentos PR y ST como pausas
pr_segment = np.zeros_like(t)
st_segment = np.zeros_like(t)
pr_segment[(t >= 0.125) & (t < 0.25)] = 0.02
st_segment[(t >= 0.36) & (t < 0.45)] = -0.02

# Combinar todos los componentes para formar la señal ECG
ecg_signal = p_wave + pr_segment + q_wave + r_wave + s_wave + st_segment + t_wave

# Convertir los valores de la señal ECG para usar coma como separador decimal
ecg_signal_comma = [str(value).replace('.', ',') for value in ecg_signal]

# Crear un DataFrame con los valores modificados
ecg_df_comma = pd.DataFrame(ecg_signal_comma)

# Guardar el DataFrame en un archivo CSV con coma como separador decimal y sin encabezado
file_path_comma = "ecg_signal.csv"
ecg_df_comma.to_csv(file_path_comma, index=False, header=False, sep=' ', quoting=3)

# Graficar la señal ECG generada
plt.plot(t, ecg_signal)
plt.title("Señal ECG más realista")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.show()

print(f"Archivo guardado en {file_path_comma}")
