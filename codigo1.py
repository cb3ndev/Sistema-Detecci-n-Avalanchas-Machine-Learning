from obspy import read
from obspy.core import UTCDateTime

# La entrada de fecha_inicio_señal debe ser de tipo string (texto) con el
# siguiente formato: "2022-05-12T15:43:19", la duración_señal debe ser un
# número de tipo entero y su cantidad debe representarse en segundos. 
# La entrada de archivo_miniSEED es el nombre del archivo miniSEED que
# contiene la señal, es decir, debe ser un archivo del día que contiene a la señal
# que se quiere obtener.

def obtener_señal_de_archivo_miniSEED(fecha_inicio_señal, duracion_señal,
                                     archivo_miniSEED):
    """Obtiene una señal de infrasonido en forma de array numpy a partir
    de un archivo miniSEED que lo contiene"""
    
    #Convertir la fecha de string a formato UTCDateTime
    fecha_inicio_señal = UTCDateTime(fecha_inicio_señal)
    
    # Para poder cargar el archivo miniseed este debe estar en la misma carpeta
    señal = read(archivo_miniSEED, starttime=fecha_inicio_señal,
                 endtime=fecha_inicio_señal+duracion_señal)
    # La función retorna el array numpy de la señal indicada, según la fecha de 
    # inicio y su duración indicada
    return señal[0].data