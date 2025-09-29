
# Solicitar el nombre y genero de la persona 
nombre = input("Ingresa tu nombre: ").strip().title()
sexo = input("Ingresa tu Genero (M para mujer, H para hombre): ").strip().upper()
edad_str = input("Ingresa tu edad: ").strip()

# Obtener la primera letra del nombre
pra_letra = nombre[0].upper()

# REGLA: Mujer con nombre que empiece con letra anterior a M (A-L) O Hombre con nombre que empiece con letra posterior a N (O-Z)
if (sexo == "M" and pra_letra < "M")or (sexo == "H" and pra_letra > "N"):
   # Si cumple alguna de las condiciones anteriores, asignar al grupo A
   grupo = "A"
else:
    # Si NO cumple ninguna de las condiciones, asignar al grupo B
    grupo = "B"

    # Validar la edad y determinar si es mayor de edad (18 años o más)
try:
    edad = int(edad_str)
    if edad >= 18:
        estado_edad = "Eres mayor de edad."
    else:
        estado_edad = "Eres menor de edad."
except ValueError:
    # Manejo de error si el usuario no introduce un número
    estado_edad = "No fue posible determinar tu mayoría de edad."

# Mostrar los resultados al usuario
print(f"\nHola {nombre}")
print(f"Tu genero es: {'Mujer' if sexo == 'M' else 'Hombre'}") # "Mujer" si sexo es "M", "Hombre" en cualquier otro caso
print(f"Perteneces al grupo: {grupo}")
print(estado_edad)