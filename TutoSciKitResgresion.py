'''Modelos supervisados
un tipico ejercicio es usar los datos de valor de propiedades en boston'''
#Modelo Regresion Lineal

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#cargar los datos
boston_dataset = load_boston()

#crear el DF
boston = pd.DataFrame(boston_dataset.data, 
columns=boston_dataset.feature_names)
boston['MEDV'] = boston_dataset.target

'''para saber las columnas que se van a manejar
print(boston.columns)
resultado
Index(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
       'PTRATIO', 'B', 'LSTAT'],
      dtype='object')
'''
''' siempre que cargamos un DF es normal chequear las primeras lineas con el metodo
.head() y las ultimas con .tail()
pero este al tener 13 columnas es mejor limitar el numero de columna a mostrar
'''
#print(boston[['CRIM', 'RM', 'AGE', 'TAX']].head(n=2))

'''tambien conviene tener un resumen de los datos antes de trabajar por eso se usa el metodo .describe()'''
#boston.hist(column='CRIM')
#plt.show()

#MATRIZ DE CORRELACION
#matriz para correlacionar .corr()
#print(boston.corr().round(2))

#se puede expresar graficamente para que se entienda mejor
#boston.plot(kind='scatter',x='RM',y='MEDV',figsize=(8,6))
#plt.show()

#debido a esto se elegira el valor RM para intentsr determinar el valor de MEDV, aunque existen otros utiles este parece el mejor linealmente hablando
#asi que definimos un valor X que sera un valor de 2 dimensiones que querramos aportar y un valor Y de 1 dimension que querramos descubrir.
#X=boston[['RM']] #com doble corchete nos da un DF
#Y=boston['MEDV'] #con corchete simple nos da una serie

#INSTANCIAR EL MODELO
#recuerda importar el modelo arriba

#model = LinearRegression()

#ahora usamos el metodo train_test_split para dividir los datos en datos de entrenamiento y datos test

#X_train, X_test, Y_train, Y_test = train_test_split(X, Y,test_size = 0.3,random_state=1)

#ahora con los datos separados podemos usar el modelo, para entrenar usamos el metodo .fit()

#model.fit(X_train, Y_train)

#ejemplo
def EjemModel():
	#primero miramos la correlacion entre los datos para saber cuales elegir
	X=boston[['RM']]
	Y=boston['MEDV']
	#con los datos elegidos decidimos el modelo
	model = LinearRegression()
	#con el modelo listo separamos los datos
	X_train, X_test, Y_train, Y_test=train_test_split(X, Y,test_size = 0.3,random_state=1)
	#y ahora con los datos separados entrenamos el modelo
	model.fit(X_train, Y_train)
	
#con el modelo entrenado podemos mirar los parametros que determino, que para el modelo lineal es el intercepto y la pendiente.

#print(model.intercept_.round(2))
#resultado -30.57
#print(model.coef_.round(2))
#resultado 8.46

#por convencion los parsmetros de scikit-learn usan _ al final de los parametros

#con estos datos sabemos que para nuestro modelo podemoa decir que 
#MEDV=-30.57+8.46×RM

#HACER PREDICCIONES
#con el modelo ya entrenado podemos hacer predicciones con el metodo .predict el cual requiere un array de 2 dimensiones

#new_RM = np.array([6.5]).reshape(-1,1)
#print(model.predict(new_RM))

#con esto ya creado nos ahorrsremos lineas y trabajo escribiendo el codigo base fuera de funcion


X=boston[['RM']]
Y=boston['MEDV']
model = LinearRegression()
X_train, X_test, Y_train, Y_test=train_test_split(X, Y,test_size = 0.3,random_state=1)
model.fit(X_train, Y_train)
y_test_predicted = model.predict(X_test)


def MostrarModelo():
	#grafico
	plt.scatter(X_test, Y_test,label='testing data');
	plt.plot(X_test, y_test_predicted,label='prediction', linewidth=3)
	#plt.xlabel('RM'); plt.ylabel('MEDV')
	#plt.legend(loc='upper left')
	plt.show()

#ejemplo
#MostrarModelo()

def MostrarResi():
	#residuo
	residuals = Y_test - y_test_predicted
	# plot residuo
	plt.scatter(X_test, residuals)
	# plot a horizontal line at y = 0
	plt.hlines(y = 0,xmin = X_test.min(), xmax=X_test.max(),linestyle='--')
	# set xlim
	plt.xlim((4, 9))
	plt.xlabel('RM'); plt.ylabel('residuals')
	plt.show()
#MostrarResi()

#METRICAS PARA EVALUAR RESULTADO

'''Para analizar nuestro residuo es conveniente usar la media del error al cuadrado
	print((residuals**2).mean())
o se puede usar
from sklearn.metrics import mean_squared_error
print(mean_squared_error(Y_test, y_test_predicted))
comando que ea el mismo resultado'''
def metricas():
	residuals = Y_test - y_test_predicted
	from sklearn.metrics import mean_squared_error
	print('media del residuo al cuadrado')
	print(mean_squared_error(Y_test, y_test_predicted))
	print('R cuadrado')
	print(model.score(X_test, Y_test))
#metricas()
#R:0,60...
#por esto se entiende que el modelo explica el 60% de la variabilidad en nuestros datos
#para r cradrsdo 0 es que el modelo no explica nada  de la variacion en Y, y 100 es que explica todo

#REGRESION LINEAL MULTIVARIABLE

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

## data preparation
X2 = boston[['RM', 'LSTAT']]
Y = boston['MEDV']
## train test split
## same random_state to ensure the same splits
X2_train, X2_test, Y_train, Y_test = train_test_split(X2, Y, test_size = 0.3, random_state=1)
model2 = LinearRegression()
model2.fit(X2_train, Y_train)

#conocer sus coeficientes
#print(model2.intercept_)
#print(model2.coef_)
y_test_predicted2 = model2.predict(X2_test)

#podemos comparar loa modelos con su metrica media del error al cuadrado y el que tenga menos sera un mejor modelo(para el caso de regresiones lineales)

'''
asi el primer modelo tiene:
	36,52
mientras que el segundo tiene:
	28,93
por lo que el segundo modelo es un 21% mejor.

por lo general mientras mas caracteristicas incluyas mejor sera el modelo, pero algunas caracterisitcas pueden no ser utiles y dañar el modelo
'''