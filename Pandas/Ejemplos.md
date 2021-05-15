# Ejemplos de pandas#

    import pandas as pd

Datos con los que trabajaremos

    Vedad=[1,2,3,4,4,5,6,7,8,9, 6, 5,4]
    Vestatura=[41,72,80,85,90,97,107,113,138,140,94,80,73]
    Vgenero=[1,1,0,0,0,1,0,1,1,0,0,1,0]
    Vnombres=['dante','gusti','anahi','antutu','Claudia','pato','pamela','aceituna','pedro','rabito','javiera','cristobal','soraya']

Y una base de datos que usaremos en algunos ejemplos

    #presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')


### ejemplo1: Crear una serie con las listas de edades y nombres, con nombres como index.###
    
    serie=pd.Series(Vedad,index= Vnombres)
    print(serie)
    #resultado
    dante        1
    gusti        2
    anahi        3
    ...


### ejemplo2: Crear un dataFrame con todos los datos que nos dan, con los nombres como indice.###

    DicSobrinos = {'edades': Vedad,'estatura':Vestatura,'genero':Vgenero}
    DFSobrinos=HDataFrame(DicSobrinos,Vnombres)
    print(DFSobrinos)
    #resultado
                edades  estatura  genero
    dante           1        41       1
    gusti           2        72       1
    anahi           3        80       0
    antutu          4        85       0
    ...


### ejemplo3: Obtener las dimensiones del DataFrame.###

	DicSobrinos = {'edades': Vedad,'estatura':Vestatura,'genero':Vgenero}
	DFSobrinos=HDataFrame(DicSobrinos,Vnombres)
	print(DFSobrinos.shape) #(13, 3) dimensiones
	print(DFSobrinos.shape[0]) #13 filas
	print(DFSobrinos.shape[1]) #3 columnas
	print(DFSobrinos.size) #39 campos


### ejemplo4: extraerCSV desde internet###

	presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
	TamañoDF(presidents_df)


### ejemplo5: Obtener algunos datos de la parte superior o inferior.###

	presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
	print(presidents_df.head(1))
	print(presidents_df.tail(1))
	#resultado
			order  age  height partyname
	George Washington      1   57     189  none
			order  age  height       partyname
	Donald J. Trump     45   70     191  republican

	...muchos datos sobre el dataframe

### ejemplo6: seleccionar varios por su index desde un nombre hasta otro.###

	DicSobrinos = {'edades': Vedad,'estatura':Vestatura,'genero':Vgenero}
	DFSobrinos=HDataFrame(DicSobrinos,Vnombres)
	nom1='dante'
	nom2='pato'
	print(DFSobrinos.loc[nom1:nom2])

### ejemplo7: buscar por la posicion del dato###

	DicSobrinos = {'edades': Vedad,'estatura':Vestatura,'genero':Vgenero}
	DFSobrinos=HDataFrame(DicSobrinos,Vnombres)
	posicion=3
	print(DFSobrinos.iloc[posicion])
	#resultado
	edades       4
	estatura    85
	genero       0
	Name antutu

### ejemplo8 Mostrar todas las columna###

	DicSobrinos = {'edades': Vedad,'estatura':Vestatura,'genero':Vgenero}
	DFSobrinos=HDataFrame(DicSobrinos,Vnombres)
	print(DFSobrinos.columns)


### ejemplo9 Utiliza la seleccion por index y muestra las tres primeras linea###

	DicSobrinos = {'edades': Vedad,'estatura':Vestatura,'genero':Vgenero}
	DFSobrinos=HDataFrame(DicSobrinos,Vnombres)
	print(DFSobrinos.loc[:,y:z].head(3))
	#resultado
	edades  estatura
	dante       1        41
	gusti       2        72
	anahi       3        80

### ejemplo10 Mostrar estadisticas basicas###

	DicSobrinos = {'edades': Vedad,'estatura':Vestatura,'genero':Vgenero}
	DFSobrinos=HDataFrame(DicSobrinos,Vnombres)
	print(x.min()) #Minimo
	print(x.max()) #Maximo
	print(x.mean()) #Media
	print(x['edades'].quantile([0.25, 0.5, 0.75, 1])) #cuantiles 25, 50 , 75 y 100
	print(x.var()) #varianza
	print(x.std()) #Desviacion estandar
	
	#resultados
	#min
	edades       1
	estatura    41
	genero       0

	#max
	edades        9
	estatura    140
	genero        1

	#mean
	edades       4.923077
	estatura    93.076923
	genero       0.461538

	#cuantiles
	#0.25    4.0
	#0.50    5.0
	#0.75    6.0
	#1.00    9.0

	#varianza
	edades        5.243590
	estatura    733.576923
	genero        0.269231

	#desviancion estandar
	edades       2.289889
	estatura    27.084625
	genero       0.518875



### ejemplo11 Usa el metodo .describe() para extraer estadistica basicas.###

	DicSobrinos = {'edades': Vedad,'estatura':Vestatura,'genero':Vgenero}
	DFSobrinos=HDataFrame(DicSobrinos,Vnombres)
	print(DFSobrinos.describe())
	
	#resultado
		edades    estatura     genero
	count  13.000000   13.000000  13.000000
	mean    4.923077   93.076923   0.461538
	std     2.289889   27.084625   0.518875
	min     1.000000   41.000000   0.000000
	25%     4.000000   80.000000   0.000000
	50%     5.000000   90.000000   0.000000
	75%     6.000000  107.000000   1.000000
	max     9.000000  140.000000   1.000000

### ejemplo 12 Obten las estadisticas de los datos no numericos.###

	print(presidents_df[party].value_counts())
	print(presidents_df[party].describe())

	#resultado
	republican               19
	democratic               15
	democratic-republican     4
	whig                      4
	none                      1
	federalist                1
	national union            1

	count             45
	unique             7
	top       republican
	freq              19

### ejercicio13: Mirar la media de los datos por genero.###

	DicSobrinos = {'edades': Vedad,'estatura':Vestatura,'genero':Vgenero}
	DFSobrinos=HDataFrame(DicSobrinos,Vnombres)
	print(DFSobrinos.groupby('genero').mean())
	#resultado
		edades   estatura
	genero
	0       5.142857  95.571429
	1       4.666667  90.166667

### ejemplo14: Agregar por genero y mirar las edades, calculando su minimo, maximo y media###

	DicSobrinos = {'edades': Vedad,'estatura':Vestatura,'genero':Vgenero}
	DFSobrinos=HDataFrame(DicSobrinos,Vnombres)
	print(DFSobrinos.groupby('genero')['edades'].agg(['min', np.median, max]))
	#resultados
	
		min  median  max
	genero
	0         3       4    9
	1         1       5    8


### ejemplo 15: Agrupar los datos por genero, sobre la edad obtener la mediana y la media, mientras que, sobre la estatura obtener  el minimo y el maximo. ###
	
	print(DF.groupby('genero').agg({'edades': [np.median, np.mean],'estatura':    [min, max]}))
	#resultado
		    edades           	estatura
	       median      mean     	min  max
	genero
	0           4  	5.142857       73  140
	1           5  	4.666667       41  138
