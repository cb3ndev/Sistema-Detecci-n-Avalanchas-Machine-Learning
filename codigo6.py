import pandas as pd

def convert_training_dataset_to_dataframe(array_train_dataset, tasa_muestreo,
                                          longitud_señal, FRAME_LENGTH, HOP_LENGTH,
                                          lista_caracteristicas):
    # Se define los headers o encabezados para las caracteristicas del Dataframe.
    header_caracteristicas=lista_caracteristicas
    
    num_ventanas_señal=int((((longitud_señal*tasa_muestreo)-FRAME_LENGTH)/
                            HOP_LENGTH)+1)
    
    # Se repite varias veces el mismo conjunto de headers, ya definidos en la
    # anterior instrucción. Esto se realiza según el número de ventanas/frames.
    header_caracteristicas=header_caracteristicas * num_ventanas_señal
    
    # Se coloca un header extra en la última columna que corresponde a las
    # etiquetas de ''clase''.
    header_caracteristicas.append('clase')
    
    # Se crea el dataframe indicadole los headers/encabezados de las demás 
    # columnas a partir de la lista_caracteristicas que es entrada de la función.
    dframe_train_dataset = pd.DataFrame(array_train_dataset,
                                        columns=header_caracteristicas)
    
    # El resultado es el dataframe del array del training Dataset, este dataframe
    # tiene headers incluidos que ayudaran para un análisis visual mas eficiente.
    return dframe_train_dataset