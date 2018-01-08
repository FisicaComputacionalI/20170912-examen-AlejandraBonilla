import numpy as np 
import matplotlib.pyplot as plt 
#declaramos la funcion que nos devuelva f(x)= 1996+x
def f(t):
 return t+(1996)

#definimos el rango de la variable 
t1= np.arange(0,21,1)
t2= np.arange(0,21,1)

#ponemos etiquetas
plt.xlabel('edad')
plt.ylabel('anios')
#El titulo tenía que ser tu nombre
#plt.title('AniosVsEdad')
plt.title('Alejandra Bonilla') 

#graficamos la funcion
plt.plot(t1, f(t1),'k*',t2, f(t2), 'm')


plt.savefig('ejercicio1.png')



