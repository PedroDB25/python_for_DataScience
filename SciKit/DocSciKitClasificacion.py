#ahora usaremos problemas con valores discretos
#un problema de solo dos caracteristicas discretas es un problema de clasificacion binario, mientras que un problema de mas caravteristicas es un problema multi-class
'''
los algoritmos comunes para clasifiacion son:
-regresion logica
-k vecinos cercanos (usaremos este modelo para el ejemplo)
-arbol de decisiones
-naive bayes
-suport vector machine
-neural network
etc... 
'''
#dejaremoa cargado la base de datos como iris
import pandas as pd
import numpy as np
iris = pd.read_csv('https://sololearn.com/uploads/files/iris.csv')

#print(iris.columns)
#R: Index(['id', 'sepal_len', 'sepal_wd', 'petal_len', 'petal_wd', 'species'], dtype='object'

#print(iris.shape)
#R (150,6)

#siempre es importante mirar los datos antes de trabajar con ellos
#print(iris.head())
#print(iris.tail())
#para ver un dato solo
#print(iris.iloc[0])

#al mirar los datos venos que hay 2 columnas que seria ID, por lo que podriamos quitar una
iris.drop('id', axis=1, inplace=True)
#print(iris.iloc[0])

#una forma de mirar loa datos es con .describe()
#print(iris.describe())
#es importante mirar que todas las columnas tengan la misma cantidad de valores
#si los datos presentan diferentes magnitudes es muy importante normalizarlos (scaling).

#al seguir analizando los datos podemoa ver que los 150 datos se agrupan en 3 especies.
#print(iris.groupby('species').size())

#ahora sabemos que los datos estan equilibrados, es muy importante este analisis debido a que en datos desequilibrados podriamos llegar a falsas afirmaciones.

#VISUALIZACION DE DATOS
import matplotlib.pyplot as plt

#iris.hist()
#plt.show()
#podemos ver en los 4 graficos de histogramas que la distrubucion normal se da en dos de ellos y una distribuciom distinta en los otros


##hacemos un diccionario para colorear
#inv_name_dict = {'iris-setosa': 0,  'iris-versicolor': 1, 'iris-virginica': 2}

##coloreamos los items
#colors = [inv_name_dict[item] for item in iris['species']] 

## ploteamos
#scatter = plt.scatter(iris['sepal_len'], iris['sepal_wd'], c = colors)

#plt.show()

#podenos ver que variando las caracterosticas a ploteat podemos distinguir las distintas especies.

#IMPLEMENTAR ALGORITMO Y PREPARAR DATOS

X = iris[['petal_len', 'petal_wd']]

y = iris['species']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=1, stratify=y)

from sklearn.neighbors import KNeighborsClassifier

#knn = KNeighborsClassifier(n_neighbors=5)
#knn.fit(X_train, y_train)
#pred = knn.predict(X_test)

#un metodo adicional para las predicciones es usar la probabilidad de prediccion, la que nos dice que probabilidad existe de que cada punto nuevo sea clasificado en su set correspondiente
#y_pred_prob = knn.predict_proba(X_test)

#ejemplo
#print(y_pred_prob[10:12])

#EVALUAR MODELO

#Precision(accuracy) proporcion de valores correctamente clasificados
#y_pred = knn.predict(X_test)

#comparar valores
#print((y_pred==y_test.values).sum())

#total de valores
#print(y_test.size)

#para verlo en %
#print(knn.score(X_test,y_test))
#R: 0,97777

#Matriz de confusion
#la precision sola puede ser engañosa
#la matriz de confusion desglosa el conteo para los casos separados, es conveniente usarlo cusndo hay datos desequilibrados o cuando hay mas de 2 categorias para clasificar

#y_pred = knn.predict(X_test)
#from sklearn.metrics import confusion_matrix 
#print(confusion_matrix(y_test, y_pred))

''' resultado
[[15  0  0]
 [ 0 15  0]
 [ 0  1 14]]'''
 
# si quisieras graficarlo prodrias usar
'''
from sklearn.metrics import plot_confusion_matrix

plot_confusion_matrix(knn, X_test, y_test, cmap=plt.cm.Blues);
'''

#validacion por k-fold cross validation
''' es un metódo que usa todos los datos pars evaluar y testear.
'''
 
#from sklearn.model_selection import cross_val_score

# create a new KNN model

#knn_cv = KNeighborsClassifier(n_neighbors=3)
#cv_scores = cross_val_score(knn_cv, X, y, cv=5)
#print(cv_scores)
#print(cv_scores.mean())

#DETERMINAR EL K MAS OPTIMO

'''
from sklearn.model_selection import GridSearchCV


knn2 = KNeighborsClassifier()

# create a dict of all values we want to test for n_neighbors

param_grid = {'n_neighbors': np.arange(2, 10)}

# use gridsearch to test all values for n_neighbors

knn_gscv = GridSearchCV(knn2, param_grid, cv=5)

#fit model to data

knn_gscv.fit(X, y)

#print(knn_gscv.best_params_)
##Respuesta       {'n_neighbors': 4}
#print(knn_gscv.best_score_)
## Respuesta       0.9666666666666668
'''
##CONSTRUIR EL MODELO CON LOS PARAMETROS DESCUBIERTOS

knn_final = KNeighborsClassifier(n_neighbors=4)
knn_final.fit(X, y)

y_pred = knn_final.predict(X)
#print(knn_final.score(X, y))

##PREDECIR CON EL MODELO
''' prediccion simple

new_data = np.array([3.76, 1.20])
new_data = new_data.reshape(1, -1)
print(knn_final.predict(np.array(new_data)))
'''
''' prediccion multiple y matrix de confusion
new_data = np.array([[3.76, 1.2], 
                     [5.25, 1.2],
                     [1.58, 1.2]])
print(knn_final.predict(new_data))
print(knn_final.predict_proba(new_data))
'''
