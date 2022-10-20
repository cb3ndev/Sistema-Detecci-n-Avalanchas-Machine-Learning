from tsfel import time_series_features_extractor
from tsfel import load_json
from librosa import stft
import pandas as pd

def modulo_extraccion_caracteristicas(señal, tasa_muestreo, archivo_JSON, 
                                      FRAME_LENGTH, HOP_LENGTH):
    '''Módulo de extracción de características para una señal segmentada en frames.
    Calcula un vector que es la unión de todos los vectores de características de 
    cada frame'''
    
    # Carga del archivo JSON por su nombre, este debe encontrarse en la misma
    # carpeta del script.
    JSON_características = load_json(archivo_JSON)
    
    # Obtención del espectrograma de la señal, este se utilizará en la extracción
    # de las características de tipo BER.
    espectrograma=stft(señal, n_fft=FRAME_LENGTH, hop_length=HOP_LENGTH, center=False)
    
    # Extracción de las 8 primeras características con TSFEL, notar que en el
    # parámetro "overlap" se le pasa un porcentaje de solapamiento con respecto
    # al tamaño total del frame. El resultado es un Dataframe de pandas que en este 
    # caso corresponde a una matriz (de tamaño: n° frames X 8 características).
    matriz_caracteristicas=time_series_features_extractor(JSON_características, 
                                                          señal, fs=tasa_muestreo,
                                                          window_size=FRAME_LENGTH, 
                                                          overlap=
                                                          (FRAME_LENGTH-HOP_LENGTH)/
                                                          FRAME_LENGTH)
    
    # Extracción de las 6 características de tipo BER. Cada una de estas
    # instrucciones genera un array de tamaño igual al n° de frames 
    # (1 característica por cada frame).
    ber_signal_band_to_band1=calcular_band_energy_ratio(espectrograma,
                                                        6,8,0,50, tasa_muestreo)
    ber_signal_band_to_band2=calcular_band_energy_ratio(espectrograma,
                                                        26,35,0,50, tasa_muestreo)
    ber_signal_band_to_band3=calcular_band_energy_ratio(espectrograma,
                                                        7,16,16,37, tasa_muestreo)
    ber_signal_band_to_band4=calcular_band_energy_ratio(espectrograma,
                                                        5,11,0,50, tasa_muestreo)
    ber_signal_band_to_band5=calcular_band_energy_ratio(espectrograma,
                                                        11,35,0,50, tasa_muestreo)
    ber_signal_band_to_band6=calcular_band_energy_ratio(espectrograma,
                                                        0,5,5,50, tasa_muestreo)
    
    # Se concatena el grupo de características BER al de TSFEL utilizando 
    # librería pandas. El resultado será un dataframe de pandas que corresponde 
    # a una matriz (de tamaño: n° frames X 14 características).
    matriz_caracteristicas["BER band/band1"]=ber_signal_band_to_band1
    matriz_caracteristicas["BER band/band2"]=ber_signal_band_to_band2
    matriz_caracteristicas["BER band/band3"]=ber_signal_band_to_band3
    matriz_caracteristicas["BER band/band4"]=ber_signal_band_to_band4
    matriz_caracteristicas["BER band/band5"]=ber_signal_band_to_band5
    matriz_caracteristicas["BER band/band6"]=ber_signal_band_to_band6
    
    # El dataframe de la matriz se convierte a un array y se realiza el flattening.
    vector_caracteristicas=matriz_caracteristicas.values.flatten()
    
    # El resultado del módulo es un vector unidimensional (numpy array).
    # El tamaño del array esta determinado por el número de frames, cuya
    # cantidad esta determinada a su vez por el tamaño de los Frames y su
    # solapamiento (FRAME_LENGTH y HOP_LENGTH). 
    return vector_caracteristicas