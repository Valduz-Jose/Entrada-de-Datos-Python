# SOlicitar nombres,apellidos,nombre empresa, extension dominio
# el resultaod debe ser: nombres.apellidos@empresa.dominio

print(f"{'-'*5}Generador de Emails{'-'*5}")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido:")
empresa = input("Ingrese su empresa:")
extension_dominio = input("Ingrese su extension de dominio:")

# Normalizar los datos
nombre = nombre.strip().lower().replace(" ", ".")
apellido = apellido.strip().lower().replace(" ", ".")
empresa = empresa.strip().lower().replace(" ", "")

# generar el email
email = f"{nombre}.{apellido}@{empresa}{extension_dominio}"
print(f"Su email generado es: \n{email}")