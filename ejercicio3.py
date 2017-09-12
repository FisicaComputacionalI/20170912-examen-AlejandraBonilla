import numpy as np 
import matplotlib.pyplot as plt 

#definimos la primera funcion que corresponde a la funcion del ejercicio1
def f(t):
  return t+(1996)
#definimos la segunda funcion que corresponde a la funcion del ejercicio2 
def g(t):
   return (2014)*np.cos(3*t)

# definimos el rango de dos variables y el intervalo en el que cambiann
t1= np.arange(0,21,1)
t2= np.arange(0,21,0.09)

# crea el grupo de graficas. 
plt.figure(1)
# crea el lienzo con dos renglones, una culumna y entra a la primera seccion de esta division. 
plt.subplot(211)
#grafica la variable t1 contra la funcion f(t1)con estrellas negras y grafica la variable t2 contra la fucnion g(t2). 
plt.plot(t1, f(t1),'k*', t2, g(t2))

# entra a la segunda seccion del lienzo dividido
plt.subplot(212)
# grafica la variable t2 contra la funcion g(t) con una linea punteada roja
plt.plot(t2, g(t2), 'r--')

# guarda la grafica
plt.savefig('ejercicio3.png')
