import pandas as pd
Vedad=[1,2,3,4,4,5,6,7,8,9, 6, 5,4]
Vestatura=[41,72,80,85,90,97,107,113,138,140,94,80,73]
Vgenero=[1,1,0,0,0,1,0,1,1,0,0,1,0]
Vnombres=['dante','gusti','anahi','antutu','Claudia','pato','pamela','caca','pedro','cacas','javiera','cristobal','soraya']

presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')

def Hseries(x,y):
	datos=pd.Series(x,index= y)
	return datos
	
#ejemplo1
#data=Hseries(Vedad,Vnombres)
#print(data)
#resultado
#dante        1
#gusti        2
#anahi        3
#...

def HDataFrame(x,y):
	datos = pd.DataFrame(x,index= y)
	return datos
	
def DFsobrinos2():
	DicSobrinos = {'edades': Vedad,'estatura':Vestatura,'genero':Vgenero}
	DFSobrinos=HDataFrame(DicSobrinos,Vnombres)
	return DFSobrinos
	
#ejemplo2:	
#DicSobrinos = {'edades': Vedad,'estatura':Vestatura,'genero':Vgenero}
#DFSobrinos=HDataFrame(DicSobrinos,Vnombres)
#print(DFSobrinos)
#resultado
#edades  estatura  genero
#dante           1        41       1
#gusti           2        72       1
#anahi           3        80       0
#antutu          4        85       0
#...


def TamañoDF(x):
	print('dimensiones')
	print(x.shape)
	print('filas')
	print(x.shape[0])
	print('colummas')
	print(x.shape[1])
	print('campos')
	print(x.size)
#ejemplo3	
#DicSobrinos = {'edades': Vedad,'estatura':Vestatura,'genero':Vgenero}
#DFSobrinos=HDataFrame(DicSobrinos,Vnombres)
#TamañoDF(DFSobrinos)
#resultado
#dimensiones
#(13, 3)
#filas
#13
#colummas
#3
#campos
#39




#ejemplo4 extraerCSV desde internet
#presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
#TamañoDF(presidents_df)

def VistazoDF(x,y):
	print(x.head(n=y))
	print(x.tail(n=y))
	print(x.info())

#ejemplo5	

#VistazoDF(presidents_df,1)
#resultado
#						order  age  height partyname
#George Washington      1   57     189  none
#						order  age  height       partyname
#Donald J. Trump     45   70     191  republican

#muchos datos sobre el dataframe

def Encontrar(x,y):
	print(x.loc[y])

#ejemplo6
#DF=DFsobrinos2()
#nom='dante'
#Encontrar(DF,nom)
#resultado
#edades       1
#estatura    41
#genero       1
#Name: dante


def Encontrarvarios(x,y,z):
	print(x.loc[y:z])
#ejemplo7 seleccionar varios
#DF=DFsobrinos2()
#nom1='dante'
#nom2='pato'
#Encontrarvarios(DF,nom1,nom2)

def EncontrarPorPosicion(x,y):
	print(x.iloc[y])

#ejemplo8
#en caso que sepas la posicion
#DF=DFsobrinos2()
#posicion=3
#EncontrarPorPosicion(DF,posicion)
#resultado
#edades       4
#estatura    85
#genero       0
#Name: antutu

def SelColum(x,y):
	#mirar todas las columnas
	print(x.columns)
	#elegir una comuna
	print(x[y].head(3))
	
#ejemplo9
#DF=DFsobrinos2()
#SelColum(DF,'edades')
#Resultado
#Index(['edades', 'estatura', 'genero'], dtype='object')
#dante    1
#gusti    2
#anahi    3
#Name: edades

def SelComum(x,y,z):
	print(x.loc[:,y:z].head(3))
	
#ejemplo10
DF=DFsobrinos2()
#SelComum(DF,'edades','estatura')
#resultado
#edades  estatura
#dante       1        41
#gusti       2        72
#anahi       3        80

def CalEsta(x):
	print('min')
	print(x.min())
	print('max')
	print(x.max())
	print('mean')
	print(x.mean())
	print('cuantiles')
	print(x['edades'].quantile([0.25, 0.5, 0.75, 1]))
	print('varianza')
	print(x.var())
	print('desviancion estandar')
	print(x.std())

#ejemplo11
#DF=DFsobrinos2()
#CalEsta(DF)
#resultados
#min
#edades       1
#estatura    41
#genero       0

#max
#edades        9
#estatura    140
#genero        1

#mean
#edades       4.923077
#estatura    93.076923
#genero       0.461538

#cuantiles
#0.25    4.0
#0.50    5.0
#0.75    6.0
#1.00    9.0

#varianza
#edades        5.243590
#estatura    733.576923
#genero        0.269231

#desviancion estandar
#edades       2.289889
#estatura    27.084625
#genero       0.518875

#otra forma de obtener estos datos es con el metodo .describe()
def descripcion(x):
	print(x.describe())

#ejemplo12
#DF=DFsobrinos2()
#descripcion(DF)
#resultado
				#edades    estatura     genero
#count  13.000000   13.000000  13.000000
#mean    4.923077   93.076923   0.461538
#std     2.289889   27.084625   0.518875
#min     1.000000   41.000000   0.000000
#25%     4.000000   80.000000   0.000000
#50%     5.000000   90.000000   0.000000
#75%     6.000000  107.000000   1.000000
#max     9.000000  140.000000   1.000000

#valores no numericos
def VNN(x,y):
	print(x[y].value_counts())
	print(x[y].describe())

#ejemplo 13
#VNN(presidents_df,'party')

#resultado
#republican               19
#democratic               15
#democratic-republican     4
#whig                      4
#none                      1
#federalist                1
#national union            1

#count             45
#unique             7
#top       republican
#freq              19
	
#si necesitamos grupos separados por categorias usammo
def agruparpor(x,y):
	print(x.groupby(y).mean())

#ejercicio14
#DF=DFsobrinos2()
#agruparpor(DF,'genero')
#resultado
			#edades   estatura
#genero
#0       5.142857  95.571429
#1       4.666667  90.166667

#pero podemos agregar mas parametros con el metodo .agg
def agruparpormas(x,y,z):
	print(x.groupby(y)[z].agg(['min', np.median, max]))

#ejemplo 15
import numpy as np
DF=DFsobrinos2()
#agruparpormas(DF,'genero','edades')
#resultados
		#min  median  max
#genero
#0         3       4    9
#1         1       5    8

#el metodo agg nos entrega mucha flexibilidad en como entregar los datos por ejemplo
#print(DF.groupby('genero').agg({'edades': [np.median, np.mean],'estatura':    [min, max]}))
#resultado
		#edades           estatura
#       median      mean      min  max
#genero
#0           4  		5.142857       73  140
#1           5  		4.666667       41  138


#si quieres eleminar una columna o una fila puedes usar el metodo drop()
#iris.drop('id', axis=1, inplace=True)