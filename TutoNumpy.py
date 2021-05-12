#numpy
#crear_array_con_np
import numpy as np
num=[1,2,3,4,4,5,6,7,8,9, 6, 5,4]
num2=[41,72,80,85,90,97,107,113,138,140,94,80,73]

def crear_array(x):
	array_creado=np.array(x)
	return array_creado
	
#ejemplo1:
#print((crear_array(num)>4).sum())
#resultado 7

def TamañoDeArray(x):
		#para ver las dimensiomes
		#primero pasamos a un narray
		ArrayCreado=np.array(x)
		#y luego usamos los metodos
		ArrayFilas=ArrayCreado.size
		ArrayColumnas=ArrayCreado.shape
		
#ejemplo2:
#TamañoDeArray(num)
#resultado 13    y    (13,)

def ModificarTamaño(x):
		ArrayCreado=np.array(x)
		#la primera variable es el numero de columnas y la segunda el numero de filas
		ArrayDosDim=ArrayCreado.reshape((2,13))
		print(ArrayDosDim)
		
#ejemplo3:
	#imaginemos que nuestra array num es la edad de nuestros sobrinos, y la nueva array num2 son sus estaturas en cms
	#ahora tenemos dos arrays que podemos combinar
#sobrinos=num+num2
	#el array sobrinos tiene 26 filas y 1 columna, ahora con reshape podemos tener un array de 2 dimensiones
#ModificarTamaño(sobrinos)
#resultado
#[[  1   2   3   4   4   5   6   7   8   9   6   5   4]
# [ 41  72  80  85  90  97 107 113 138 140  94  80  73]]

def Seleccion(x):
	ArrayCreado=np.array(x)
	ArrayDosDim=ArrayCreado.reshape((2,13))
	#suponiendo que queremos saber la edad y el tamaño de nuestro 4° sobrino
	print(ArrayDosDim[0,3])
	print(ArrayDosDim[1,3])
	#podriamos hacer lo mismo con este codigo, pero nos daria un 'Slicing' del array
	print(ArrayDosDim[:,3])
	#si quisieramos saber el tamaño de los primeros 4 sobrinos usariamos
	print(ArrayDosDim[1,0:3])


#ejemplo4: 
#sobrinos=num+num2
#Seleccion(sobrinos)
#respuesta 4   85 [4,85]   [41 72 80]

def Remplazar(x,y):
	x[0]=y

#ejemplo5
#el sobrino de la posicion 0 acaba de cumplir 2 años
#Remplazar(num,2)
#print(num)
#resultado [2, 2, 3, 4, 4, 5, 6, 7, 8, 9, 6, 5, 4]

def RemplazarVarios(x):
	Nnum=[1,1,1]
	x[-3:]=Nnum

#ejemplo6
#RemplazarVarios(num)
#print(num)
#Resultado [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 1, 1, 1]

def JuntarArrays(x,y,D):
	x1=np.array(x)
	y1=np.array(y)
	if D=="h":
		xReshape1=x1.reshape(13,1)
		yReshape1=y1.reshape(13,1)
		x_y=np.hstack((xReshape1,yReshape1))
	if D=="v":
		xReshape2=x1.reshape(1,13)
		yReshape2=y1.reshape(1,13)
		x_y=np.vstack((xReshape2,yReshape2))
	return x_y
	

def mat(x,y,z):
	x1=np.array(x)
	if z=="+":
		return x1[:]+y
	if z=="-":
		return x1[:]-y
	if z=="/":
		return x1[:]/y
	if z=="**":
		return x1[:]**y
	if z=="*":
		return x1[:]*y
	#si multiplicas directamente estarias duplicando el array, es necesario especificar el tramo que vas a alterar

#ejemplo8
#print(mat(num,12,"*"))
#resultado [ 12  24  36  48  48  60  72  84  96 108  72  60  48]

def MasMet(x,y,z,w):
	x_y=JuntarArrays(x,y,w)
	if z==1:
		xymet=x_y.sum(0)
	if z==2:
		xymet=x_y.min(0)
	if z==3:
		xymet=x_y.max(0)
	if z==4:
		xymet=x_y.mean(0)
	print(xymet)		

#ejemplo9								
#MasMet(num,num2,2,"h")
#resultado 1,41

def comparacion(x,y,z):
	#comparar y seleccionar
	x1=np.array(x)
	if z==1:
		xB=x1[:]>y
	if z==2:
		xB=x1[:]<y
	if z==3:
		xB=x1[:]>=y
	if z==4:
		xB=x1[:]<=y
	if z==5:
		xB=x1[:]==y
	print(xB)
	print(xB.sum())
	#para seleccionar los que necesitas se usa esta sintaxis array[arrayboleanos]
	print(x1[xB])	
	
	
#ejemplo10
#comparacion(num,5,3)
#resultado boleano   ,    7   y   segmento

#ejemplo11 en dos dimensiones
#x_y=JuntarArrays(num,num2,"h")
#x_yB=x_y[:,1]>80
#print(x_y[x_yB])

#ejemplo11 criterio multiple
#x_y=JuntarArrays(num,num2,"h")
#x_yB=(x_y[:,1]>80) & (x_y[:,0]<7)
#print(x_y[x_yB])