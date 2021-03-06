# Ejemplos de uso de la libreria Numpy
En este texto trataremos algunos ejemplos de las funciones basicas de numpy  
para empezar siempre debes importar numpy y por convencion le agregamos el alias np

	import numpy as np

Mientras que para estos ejercicios trabajaremos con estas listas.  
Que representan la edad de unos niños y sus tamaños.

	num=[1,2,3,4,4,5,6,7,8,9, 6, 5,4]
	num2=[41,72,80,85,90,97,107,113,138,140,94,80,73]

### Ejemplo 1: Crear un array y ver cuantos tienen mas de 4 años.

R:
1. Creamos el array con las edades.
2. Comparar cada valor y ver si nos da true o false.
3. Sumar los true.
4. Un print mostrar valores.
~~~
ArrayDeEdades=np.array(num)
ArrayDeBooleanos=ArrayDeEdades>4
suma=ArrayDeBooleanos.sum()
print(suma)
#resultado 7
~~~

### Ejemplo 2: Obtener las dimensiones del array

R:
1. Creamos el array de edades.
2. Utilizamos los metodos .size y .shape
3. Mostramos los resultados.

~~~
ArrayDeEdades=np.array(num)
print(ArrayDeEdades.size)
print(ArrayDeEdades.shape)
#resultado 13    y    (13,)
~~~

### Ejemplo 3: unir arrays de las 3 formas.

#### a) Unir listas

1. Concatenamos ambas listas.
2. Creamos el array
3. usamos reshape para tener 2 filas
4. Imprimimos los resultados
~~~
sobrinos=num+num2
arrayS=np.array(sobrinos)
array2D=arrayS.reshape(2,-1)
print(array2D)
#resultado
#[[1 2 3 4 4 5 6 7 8 6 5 4]
# [41 72 80 85 90 97 107 113 138 140  94  80  73]]
~~~

#### b) Unir Arrays
~~~	
arraynum=np.array(num)
arraynum2=np.array(num2)
arrayS=np.concatenate((arraynum,arraynum2))
array2D=arrayS.reshape(2,-1)
print(array2D)
#resultado
#[[1 2 3 4 4 5 6 7 8 6 5 4]
# [41 72 80 85 90 97 107 113 138 140  94  80  73]]
~~~

#### c) UnirAbajo
~~~
arraynum=np.array(num)
arraynum2=np.array(num2)
arrayS=np.vstack((arraynum,arraynum2))
print(arrayS)
#resultado
#[[1 2 3 4 4 5 6 7 8 6 5 4]
# [41 72 80 85 90 97 107 113 138 140  94  80  73]]
~~~

### Ejemplo 4: Seleccionar valores de algun sobrino.
~~~
sobrinos=num+num2
arrayS=np.array(sobrinos)
array2D=arrayS.reshape(2,-1)
print(array2D[0,1])
#resultado 2
~~~
### Ejemplo 5: Modificar parametros, el sobrino en la posicion 0 ha cumplido 2 años.
~~~
arraynum=np.array(num)
arraynum[0]=2
print(arraynum)
#resultado [2, 2, 3, 4, 4, 5, 6, 7, 8, 9, 6, 5, 4]
~~~
### Ejemplo 6: Los gemelos en las posiciones 0 y 1, tienen enrealidad 5 años.
~~~	
arraynum=np.array(num)
ListaAux=[5,5]
arraynum[0:2]=ListaAux
print(arraynum)
#resultado [5 5 3 4 4 5 6 7 8 9 6 5 4]
~~~
### Ejemplo 7: Matematica basica en arrays, multiplicar un array por 2.
~~~
arraynum=np.array(num)
print(arraynum[:]*2)
#resultado [2, 4, 6, 8, 8, 10, 12, 14, 16, 18, 12, 10, 8]
~~~
### Ejemplo 8: Obtener la media de edades
~~~
arraynum=np.array(num)
print(arraynum.mean())
#resultado 4.923
~~~
### Ejemplo 9: Usar comparaciones de edad.
~~~
arraynum=np.array(num)
print((arraynum[:]>7).sum())
#resultado: 2
~~~
