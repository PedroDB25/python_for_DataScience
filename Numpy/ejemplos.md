import numpy
num=[1,2,3,4,4,5,6,7,8,9, 6, 5,4]
num2=[41,72,80,85,90,97,107,113,138,140,94,80,73]

#ejemplo1:
#print((crear_array(num)>4).sum())
#resultado 7	
	
#ejemplo2:
#TamañoDeArray(num)
#resultado 13    y    (13,)

#ejemplo3:
	#imaginemos que nuestra array num es la edad de nuestros sobrinos, y la nueva array num2 son sus estaturas en cms
	#ahora tenemos dos arrays que podemos combinar
#sobrinos=num+num2
	#el array sobrinos tiene 26 filas y 1 columna, ahora con reshape podemos tener un array de 2 dimensiones
#ModificarTamaño(sobrinos)
#resultado
#[[  1   2   3   4   4   5   6   7   8   9   6   5   4]
# [ 41  72  80  85  90  97 107 113 138 140  94  80  73]]

#ejemplo4: 
#sobrinos=num+num2
#Seleccion(sobrinos)
#respuesta 4   85 [4,85]   [41 72 80]

#ejemplo5
#el sobrino de la posicion 0 acaba de cumplir 2 años
#Remplazar(num,2)
#print(num)
#resultado [2, 2, 3, 4, 4, 5, 6, 7, 8, 9, 6, 5, 4]

#ejemplo6
#RemplazarVarios(num)
#print(num)
#Resultado [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 1, 1, 1]

#ejemplo8
#print(mat(num,12,"*"))
#resultado [ 12  24  36  48  48  60  72  84  96 108  72  60  48]

#ejemplo9								
#MasMet(num,num2,2,"h")
#resultado 1,41


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
