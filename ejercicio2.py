import numpy as np 
import matplotlib.pyplot as plt 
#no se deben de poner letras con tildes o acentos ni en los comentarios. tu programa no corria por eso.
#declaramos la funcion que nos devuelva f(x)= 2014*cos(3*x) donde 2014 es el anio en el que entre y multiplica a cos(3*t) y 3 es la cantidad de anios que llevo en la universidad y en una constante que multiplica a la variable t del argumento del cos
#La constante se le suma a la funcion no se multiplica, la amplitud o magnitud es la que se multiplica. La funcion deberia de haber quedado como: 3*np.cos(2*np.pi*t)+2014 

def f(t):
  return (2014)*np.cos(3*t)

def fcorrecta(t):  
  return 3*np.cos(2*np.pi*t)+2014
#definimos el rango de la variable 
t1= np.arange(0.0,5.0,0.09)

#plt.plot(t1, f(t1))
plt.plot(t1, fcorrecta(t1))  
plt.savefig('ejercicio2_graficacorrecta.png')

