#CLUSTERING
#unsupervised
#agrupa objetos similares que estan relacionados entre si

'''algoritmos tipicos
Basado en centro (Cebtroid based model)
basado en la conectividad(connectivity based model)
basado en la distribucion(distributiom based model)
basado en la densidad(density based model)
'''
'''K-mean
suponiendo k puntos el funciona asi
1° elije k centros para los clusters llamados centroides
2° asigna cada punto al centroide mas cercano en funcion a la distancia
3° actualoza los centriodes, para los nuevos grupos calcula el centroide tomandonel profemedio de cada punto asignado
4° repita los pasos 2 y 3 hasta que se llegue a un equilibrio o se llegue al maximo de iteraciones
'''
#la distancia entre los puntos se puede calcular de varias formas
import numpy as np
def distancia():
	x1=np.array([1,-1])
	x2=np.array([4,3])
	print(np.sqrt(((x1-x2)**2).sum()))
#distancia()
#R 2.2360

#DATOS DE VINOS
""" Se cargaran datos de vino con 13 dimensiones, para tratar de reducir las dimensiones y trabajar con datos mas manejables"""

from sklearn.datasets import load_wine
import pandas as pd

data = load_wine()
wine = pd.DataFrame(data.data, columns=data.feature_names)
#miranmos miramos las estadisticas de los datos que nos proporcionan
#print(wine.shape)
#R (178, 13)
#print(wine.columns)
""" R   Index(['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium',
       'total_phenols', 'flavanoids', 'nonflavanoid_phenols',
       'proanthocyanins', 'color_intensity', 'hue',
       'od280/od315_of_diluted_wines', 'proline'],
      dtype='object') """
#print(wine.iloc[:,0:3].describe())

##GRAFICAR
#ploteamos los datos para entenderlos
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
#scatter_matrix(wine.iloc[:,[0,2]]) #mostrar 2 componentes
##scatter_matrix(wine.iloc[:,:5]) #motrar varios componentes
##plt.show()


#PREPROCESAR

# ahora que consideramos que los datos podrian tener 3 polos distintos, preprocesaremos los datos, debido a que el modelo que usaremos trabaja mejor con datos que fluctuan en las mismas escalas

"""X = wine[['alcohol', 'total_phenols']]

from sklearn.preprocessing import StandardScaler
# instanciamos el escalador
scale = StandardScaler()
# Calculamos la media y la desviacion estandar necesaria para calcular luego
scale.fit(X)
# StandardScaler(copy=True, with_mean=True, with_std=True)

X_scaled = scale.transform (X)"""

"""a =wine.iloc[:,0]
b =wine.iloc[:,5]
plt.scatter(a,b)
plt.scatter(X_scaled[:,0],X_scaled[:,1])
plt.show()"""

#UTILIZACION DEL MODELO INSTANCIAR -> ENTRENAR -> PREDECIR

"""from sklearn.cluster import KMeans
# instantiate the model
kmeans = KMeans(n_clusters=3)
# fit the model
kmeans.fit(X_scaled)
# make predictions
y_pred = kmeans.predict(X_scaled)"""

"""# Graficar los centroides (visualizar es la mejor manera de entender en estos casos)
# plot the scaled data
plt.scatter(X_scaled[:,0], 
            X_scaled[:,1],
            c= y_pred)
# identify the centroids
plt.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1], 
            marker="*",
            s = 250, 
            c = [0,1,2], 
            edgecolors='k')
plt.xlabel('alcohol'); plt.ylabel('total phenols')
plt.title('k-means (k=3)')
plt.show()"""

#Predecir
"""
X_new = np.array([[13, 2.5]])
X_new_scaled = scale.transform(X_new)

print(kmeans.predict(X_new_scaled))"""
#optimizar la variable K
#para ajustar este valor utilizamos el concepto de inercia_, que se entiende como la distancia de los puntos a su centroide, de esta manera la idea seria reducir la inercia hasta llegar a un punto optimo
#por lo que nos conviene analizarla en cada caso graficando todos los casos posibles

"""# calculate distortion for a range of number of cluster
inertia = []
for i in np.arange(1, 11):
    km = KMeans(n_clusters=i)
    km.fit(X_scaled)
    inertia.append(km.inertia_)

# plot
plt.plot(np.arange(1, 11), inertia, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()"""

# como vemos en la figura, 3 parece ser un buen candidato a optimo, debido a que en este punto la inercia comienza a bajar lentamente.

#MODELAR CON TODAS LAS CARACTERISTICAS
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

X = wine

scale = StandardScaler() 
scale.fit(X)
X_scaled = scale.transform(X)

inertia = [] 
for i in np.arange(1, 11):
    km = KMeans(n_clusters=i)
    
    km.fit(X_scaled) 
    inertia.append(km.inertia_)
    
plt.plot(np.arange(1, 11), inertia, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title("all feature")
plt.show()


"""
import numpy as np

p0=np.array([0,0])
p2=np.array([2,2])

n = (int(input())-1)
n1= input()
n1=(int(n1[0]),int(n1[2]))
Arr=np.array([n1])



for x in range(n):
    n2= input()
    
    try:
       n3=(int(n2[0]),int(n2[2]))
    except:
        n3=(int(n2[0]),(float(n2[3])/10))

    Arr2=np.array([n3])
    Arr=np.append(Arr, Arr2 , axis=0)
 
#Arr Tiene los datos listos
for x in Arr:
    a=np.sqrt(((x-[0,0])**2).sum())
    b=np.sqrt(((x-[2,2])**2).sum())
    if a>b: 
        p2=np.append(p2,x , axis=0)
    if a<=b: 
        p0=np.append(p0,x , axis=0)

p0=p0.reshape(-1,2)
p2=p2.reshape(-1,2)

#Calcular los centros

for x in p0:
    cx=x[0]
    cy=x[1]
    


    
"""





























