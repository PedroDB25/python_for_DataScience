import matplotlib.pyplot as plt
import numpy as np
import tutopandas
DF=tutopandas.DFsobrinos2()

#ARMADO BASICO

def FiguraVacia():
	fig=plt.figure()
	ax=plt.axes()
	plt.show()

def FiguraConGrafico():
	fig=plt.figure()
	ax=plt.axes()
	#datos del ploteo
	x=np.linspace(0,10,100)
	y=np.sin(x)
	ax.plot(x,y)
	
	plt.show()

def FiguraConTitulos():
	fig=plt.figure()
	ax=plt.axes()
	#datos del ploteo
	x=np.linspace(0,10,100)
	y=np.sin(x)
	ax.plot(x,y)
	#limitar ejes
	plt.ylim(0.75)
	plt.xlim(4)
	#titulos
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('fun sin')
	#mostrar todo
	plt.show()

def FiguraConVariosTrazosYLeyenda():		
	fig=plt.figure()
	ax=plt.axes()
	#datos del ploteo
	x=np.linspace(0,10,100)
	ax.plot(x,np.cos(x),color='b',label='cos(x)')	
	ax.plot(x,np.sin(x),linestyle='--',label='sin(x)')	
	#mostrar todo
	plt.legend()
	plt.show()

#PLOTEO SCATTER

def scatterplot():
	fig=plt.figure()
	plt.scatter(DF['edades'],DF['estatura'])
	#titulos
	plt.xlabel('edades')
	plt.ylabel('estaturas')
	plt.title('Sobrinos')
	plt.show()
	
def PloteoDirecto(a,b,c,d,e):
	a.plot(kind=b,x=c,y=d,title=e)
	plt.show()

#ejemplo1
#PloteoDirecto(DF,'scatter','edades','estatura','sobrino')

#HISTOGRAMAS

#DF['estatura'].plot(kind='hist',bins=10)
#plt.show()

#BOXPLOT

#DF.boxplot(column='estatura')
#plt.show()

#BARPLOT

#DF['genero'].plot(kind='bar')
#NG=DF['genero'].value_counts()
#NG.plot(kind='bar')
#plt.show()

'''histograma representa datos numericos, muentras que un grafico de barras muesta la categoria de loa datos'''