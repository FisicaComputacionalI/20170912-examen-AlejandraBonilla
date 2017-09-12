import numpy as np 
import matplotlib.pyplot as plt 
#declaramos la funcion que nos devuelva f(x)= 2014*cos(3*x) donde 2014 es el año en el que entre y multiplica a cos(3*t) y 3 es la cantidad de años que llevo en la universidad y en una constante que multiplica a la variable t del argumento del cos
def f(t):
  return (2014)*np.cos(3*t)

#definimos el rango de la variable 
t1= np.arange(0.0,5.0,0.09)

plt.plot(t1, f(t1))

plt.savefig('ejercicio2.png')

