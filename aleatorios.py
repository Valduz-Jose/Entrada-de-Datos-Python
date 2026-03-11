# funcion randint() para generar numeros aleatorios enteros
# randint(a,b) 

# import random
from random import randint

# generar numero aleatorio entre 1 - 10
numero = randint(1,10)
print(f"El numero aleatorio generado es: {numero}")

# simular dado de seis caras
dado = randint(1,6)
print(f"El resultado del dado es: {dado}")
