from sklearn import neighbors

def entrenamiento_modelo_KNN(n_neighbors, weights, metric, 
                             dataframe_training_dataset):
    
    ''' Función encargada de entrenar un modelo de Machine Learning con el 
    algoritmo KNN a partir de un training dataset que se encuentra en una 
    estructura de tipo Dataframe (Pandas), tiene como entrada también los
    hiperparámetros de entrenamiento'''
    
    # Dataframe correspondiente a los vectores de caracteristicas 
    # (Es el mismo dataframe del Training Dataset sin la columna "clase")
    dataframe_vectores_caracteristicas = dataframe_training_dataset.\
                                        loc[:,dataframe_training_dataset.\
                                            columns != 'clase']
    # Dataframe correspondiente a la columna de clase 
    # (Corresponde a un dataframe de solo la columna "clase")
    dataframe_columna_clase=dataframe_training_dataset['clase']
    
    # Eleccion de hiperparametros y entrenamiento de modelo
    modelo_KNN= neighbors.KNeighborsClassifier(n_neighbors=n_neighbors,
                                               weights=weights,
                                               metric=metric)
    modelo_KNN.fit(dataframe_vectores_caracteristicas.values, 
                   dataframe_columna_clase.values)
    
    # esta función devuelve un objeto de tipo KNeighborsClassifier, que
    # es un objeto de la libreria scikit-learn que representa un modelo 
    # de KNN.
    return modelo_KNN