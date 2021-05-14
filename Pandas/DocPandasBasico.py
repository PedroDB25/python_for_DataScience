#Import y alias
import pandas as pd

#Los Datos de pandas se llaman si son de varias dimensiones DataFrame o Series si es una dimension.
#Y son similares a los arrays en numpy pero estos pueden tener mas cosas ademas de numeros, y sobre todo tienen un indice.

#Como crear series en pandas.
def Hseries(x,y):
	datos=pd.Series(x,index= y)
	return datos

#Como crear DataFrames en pandas.
def HDataFrame(x,y):
	datos = pd.DataFrame(x,index= y)
	return datos

#si quieres eleminar una columna o una fila puedes usar el metodo drop()
#iris.drop('id', axis=1, inplace=True)
	
#Funcion para obtener las dimensiones
def TamañoDF(x):
	print(x.shape) #dimensiones
	print(x.shape[0]) #filas
	print(x.shape[1]) #Columnas
	print(x.size) #Campos (Total de datos introducidos.)

#Si tenemos un dataFrame en internet podemos descargarlo directamente con esta linea.
def DatosDeInternet(x):
	df_Descargada = x
	return df_Descargada

#Como obtener los n primeros o los n ultimos valores de un Dataframe, mientras que info nos da informacion acerca de los datos.
def VistazoDF(x,y):
	print(x.head(n=y))
	print(x.tail(n=y))
	print(x.info())

#Localizar un dato por su valor index
def Encontrar(x,y):
	print(x.loc[y])

def Encontrarvarios(x,y,z):
	print(x.loc[y:z])
	

#Localizar datos por su posicion.
def EncontrarPorPosicion(x,y):
	print(x.iloc[y])

	
#Seleccionar columnas
def SelColum(x,y):
	#mirar todas las columnas
	print(x.columns)
	#elegir una comuna
	print(x[y].head(3))
	
#utilizar las estadisticas de localizar por index y luego ver los primeros 3 valores.
def SelComum(x,y,z):
	print(x.loc[:,y:z].head(3))
	

#Calcular las estadisticas basicas.
def CalEsta(x):
	print(x.min()) #Minimo
	print(x.max()) #Maximo
	print(x.mean()) #Media
	print(x['edades'].quantile([0.25, 0.5, 0.75, 1])) #cuantiles 25, 50 , 75 y 100
	print(x.var()) #varianza
	print(x.std()) #Desviacion estandar

#una forma resumida de obtener las estadisticas basicas.
def descripcion(x):
	print(x.describe())

# es posible que en los valores tengamos datos no numericos, la forma de obtener datos sobre ellos es usar
def VNN(x,y):
	print(x[y].value_counts())
	print(x[y].describe())


#si necesitamos grupos separados por categorias usamos, aunque esto nos limita a solo mirar 2 parametros.
def agruparpor(x,y):
	print(x.groupby(y).mean())



#pero podemos agregar mas parametros con el metodo .agg
def agruparpormas(x,y,z):
	print(x.groupby(y)[z].agg(['min', np.median, max]))
