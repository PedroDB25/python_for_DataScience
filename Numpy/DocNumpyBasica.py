#import y alias
import numpy as np

#funcion para crear arrayas
def crear_array(x):
	array_creado=np.array(x)
	return array_creado
	

#funcion para ver las dimensiones del array
def TamañoDeArray(x):
		ArrayCreado=np.array(x)
		ArrayFilas=ArrayCreado.size
		ArrayColumnas=ArrayCreado.shape

#funcion para modificar las dimensiones de un array
def ModificarTamaño(x):
		ArrayCreado=np.array(x)
		#(columnas,filas)
		ArrayDosDim=ArrayCreado.reshape((2,13))
		print(ArrayDosDim)

		
#Unir arrays
#Para esto hay varias formas
#1 unir las listas antes, formar un array y luego un resharpe
def unirListas(x,y):
	return np.array(x+y).reshape(2,-1)

#2 si ya tenemos los arrays, podemos concatenarlos y luego usar resharpe
def unirArray(x,y):
	return np.concatenate((x,y)).resharpe(2,-1)

#3 Usar vstack o hstack (para estos tenemos que tenerlos en las mismas dimensiones desde antes)
def unirArrayAlLado():
	return np.hstack((x,y))

def unirArrayAbajo():
	return np.vstack((x,y))


#Seleccionar 
#Para seleccionar simplemente llamamos las posiciones del array
def Seleccion(x,n):
	return x[n]


#modificar valores unicos o multiples.
def Remplazar(x,y):
	x[0]=y

def RemplazarVarios(x):
	Nnum=[1,1,1]
	x[-3:]=Nnum

#Operaciones basicas con arrays
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


#Metricas basicas.
def MasMet(x,y,z,w):
	x_y=JuntarArrays(x,y,w)
	if z==1:
		xymet=x_y.sum()
	if z==2:
		xymet=x_y.min()
	if z==3:
		xymet=x_y.max()
	if z==4:
		xymet=x_y.mean()
	print(xymet)		


#Comparaciones
def comparacion(x,y,z):

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
