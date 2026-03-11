
print("Sistema de Empleados")
nombre_empleado = input("Ingrese el nombre del empleado: ")
edad_empleado = int(input("Ingrese la edad del empleado: "))
salario_empleado = float(input("Ingrese el salario del empleado: "))
es_jefe_departamento = input("¿Es jefe de departamento? (si/no): ")

# convertir a bool el es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == "si"

print(f"\nDatos del Empleado:\nNombre: {nombre_empleado}\nEdad: {edad_empleado} años\nSalario: ${salario_empleado:.2f}\nJefe de Departamento: {'Sí' if es_jefe_departamento else 'No'}")
