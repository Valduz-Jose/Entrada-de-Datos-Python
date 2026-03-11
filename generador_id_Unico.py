# Solicitar nombre apellido y a*o
# Generar un ID unico con las primeras 2 letras del nombre, las primeras 2 letras del apellido y los dos ultimos digitos del a*o, mas cuatro digitos aleatorios al final

from random import randint

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
anio = input("Ingrese su anio de nacimiento (YYYY): ")

# Normalizar
nombre_2 = nombre.strip().upper()[0:2]
apellido_2 = apellido.strip().upper()[0:2]
anio_2 = anio[-2:]  # Tomar los dos últimos dígitos

# Generar cuatro dígitos aleatorios
aleatorio = randint(1000, 9999)

# Generar ID único
id_unico = f"{nombre_2}{apellido_2}{anio_2}{aleatorio}"
print(f"Su ID único es: {id_unico}")