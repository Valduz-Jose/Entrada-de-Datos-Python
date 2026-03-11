respuesta_usuario = "False"

es_verdad = bool(respuesta_usuario)

print(f"El valor es: {es_verdad}")
# Devuelve True porque cualquier cadena de texto no vacía se considera verdadera en Python.

# Forma correcta
texto_vacio = ""
es_verdad = bool(texto_vacio)
print(f"El valor es: {es_verdad}")