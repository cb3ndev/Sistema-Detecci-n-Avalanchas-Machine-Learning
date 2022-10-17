import numpy as np

# El path es la carpeta donde el archivo csv será almacenado (para la primera función)
# o de donde será cargado (para la segunda función).
# El nombre del archivo csv debe llevar la extension csv, por ejemplo:
# "ejemplo_archivo.csv", esto debe ser así para ambas funciones.

def guardar_array_en_csv(path, nombre_archivo_csv, array_señal):
    np.savetxt(path+nombre_archivo_csv, array_señal, delimiter=',')
    
def cargar_csv_en_array(path, nombre_archivo_csv):
    array_señal = np.genfromtxt(path+nombre_archivo_csv, 
                                delimiter=',')
    # Esta función retorna un array numpy a partir de un archivo csv.
    return array_señal