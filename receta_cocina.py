# Programa para recetas de cocina
print("-----Bienvenido al programa de recetas de cocina-----")
nombre_receta = input("Ingrese el nombre de la receta: ")
ingredientes = input("Ingrese los ingredientes (separados por comas): ")
tiempo_preparacion = int(input("Ingrese el tiempo de preparación en minutos: "))
dificultad = input("Ingrese la dificultad (fácil, media, difícil): ")

print(f"-"*40)
print(f"\nDatos de la Receta:\nNombre: {nombre_receta}\nIngredientes: {ingredientes}\nTiempo de Preparación: {tiempo_preparacion} minutos\nDificultad: {dificultad.capitalize()}")