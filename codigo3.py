from scipy import signal
import noisereduce as nr

def modulo_pre_procesamiento(señal, señal_ruido, tasa_muestreo = 100):
    '''Módulo de pre-procesamiento de señales digitales,.
    Hace un filtrado de bandas no deseadas y de ruido'''
    
    #Etapa del filtro Butterworth pasabanda.
    filtro_pasabanda = signal.butter(6, [1.8,45], 'bandpass',
                                     fs=tasa_muestreo, output='sos')
    señal_filtrada_1 = signal.sosfilt(filtro_pasabanda, señal)
    
    #Etapa del filtro Butterworth rechazabanda.
    filtro_rechazabanda = signal.butter(6, [25,30], 'bandstop',
                                        fs=tasa_muestreo, output='sos')
    señal_filtrada_2 = signal.sosfilt(filtro_rechazabanda, señal_filtrada_1)
    
    #Etapa del filtro de reducción de ruido.
    señal_filtrada_3 = nr.reduce_noise(y = señal_filtrada_2, n_fft=128, 
                                       hop_length=64, sr=tasa_muestreo,
                                       n_std_thresh_stationary=1, 
                                       stationary=True,
                                       time_mask_smooth_ms=5000, 
                                       freq_mask_smooth_hz=1.8, 
                                       y_noise = señal_ruido)
    return señal_filtrada_3