import numpy as np

def calcular_bin_frequencia(frecuencia_hz, espectrograma, tasa_muestreo):
    '''Función que transforma una frecuencia en Hz en su respectivo bin de 
    frecuencia. Requiere como entrada el espectrograma de la señal que se 
    quiere analizar'''
    
    rango_total_frecuencia=tasa_muestreo/2
    
    # Se calcula el delta de frecuencia de cada bin del espectrograma, es
    # decir la distancia entre un bin y otro (en hz).
    frequency_delta_por_bin=rango_total_frecuencia/ espectrograma.shape[0]
    
    # Se calcula el bin de frecuencia y se retorna el mismo como resultado de la
    # función.
    frecuencia_bin=np.floor(frecuencia_hz/frequency_delta_por_bin)
    return int(frecuencia_bin)

def calcular_band_energy_ratio(espectrograma, inicio_band_1, fin_band_1,
                               inicio_band_2, fin_band_2,tasa_muestreo):
    '''Función que calcula la "Relación de Energía entre Bandas" o "Band Energy 
    Ratio". Requiere como entrada el espectrograma de la señal que se quiere
    analizar'''
    
    # Calcular el bin de cada una de las frecuencias que se le pasaron a la
    # función como parámetros de entrada.
    frecuencia_bin_inicio_band_1=calcular_bin_frequencia(espectrograma, 
                                                         inicio_band_1, 
                                                         tasa_muestreo)
    frecuencia_bin_fin_band_1=calcular_bin_frequencia(espectrograma, 
                                                      fin_band_1, 
                                                      tasa_muestreo)
    frecuencia_bin_inicio_band_2=calcular_bin_frequencia(espectrograma, 
                                                         inicio_band_2, 
                                                         tasa_muestreo)
    frecuencia_bin_fin_band_2=calcular_bin_frequencia(espectrograma, 
                                                      fin_band_2, 
                                                      tasa_muestreo)
    # Calcular potencia del espectrograma
    power_spec=np.abs(espectrograma)**2
    power_spec=power_spec.T
    
    # Calcular la band energy ratio para cada ventana/frame del espectrograma
    # El resultado es un array con los valores de BER para cada frame,
    # la longitud del array esta definido por el número de frames/ventanas
    # totales de la señal.
    band_energy_ratio = []
    for frequencies_in_frame in power_spec:
        sum_power_band1_frequencies=np.sum(frequencies_in_frame
                                           [frecuencia_bin_inicio_band_1:
                                            frecuencia_bin_fin_band_1])
        sum_power_band2_frequencies=np.sum(frequencies_in_frame
                                           [frecuencia_bin_inicio_band_2:
                                            frecuencia_bin_fin_band_2])
        ber_frame_actual=sum_power_band1_frequencies/ sum_power_band2_frequencies
        band_energy_ratio.append(ber_frame_actual)
        
    # La función retorna el array numpy con los valores de la característica BER
    # por cada frame de una señal.
    return np.array(band_energy_ratio)