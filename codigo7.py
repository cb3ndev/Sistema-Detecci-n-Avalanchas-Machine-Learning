from sklearn import svm

def entrenamiento_modelo_SVM(gamma, C, dataframe_training_dataset):
    
    ''' Función encargada de entrenar un modelo de Machine Learning con el 
    algoritmo SVM a partir de un training dataset que se encuentra en una 
    estructura de tipo Dataframe (Pandas), tiene como entrada también los
    hiperparámetros de entrenamiento'''
    
    # Dataframe correspondiente a los vectores de características 
    # (Es el mismo dataframe del Training Dataset sin la columna "clase")
    dataframe_vectores_caracteristicas = dataframe_training_dataset.\
                                        loc[:,dataframe_training_dataset.\
                                            columns != 'clase']
    # Dataframe correspondiente a la columna de clase 
    # (Corresponde a un dataframe de solo la columna "clase")
    dataframe_columna_clase=dataframe_training_dataset['clase']
    
    # Eleccion de hiperparametros y entrenamiento de modelo
    modelo_SVM= svm.SVC(gamma=gamma , C=C)
    modelo_SVM.fit(dataframe_vectores_caracteristicas.values, 
                   dataframe_columna_clase.values)
    
    # esta función devuelve un objeto de tipo SVC, que es un objeto de la
    # libreria scikit-learn que representa un modelo de SVM.
    return modelo_SVM