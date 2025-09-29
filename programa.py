
# Solicitar el nombre y genero de la persona 
nombre = input("Ingresa tu nombre: ").strip().title()
sexo = input("Ingresa tu Genero (M para mujer, H para hombre): ").strip().upper()

# Obtener la primera letra del nombre
pra_letra = nombre[0].upper()

# REGLA: Mujer con nombre que empiece con letra anterior a M (A-L) O Hombre con nombre que empiece con letra posterior a N (O-Z)
if (sexo == "M" and pra_letra < "M")or (sexo == "H" and pra_letra > "N"):
   # Si cumple alguna de las condiciones anteriores, asignar al grupo A
   grupo = "A"
else:
    # Si NO cumple ninguna de las condiciones, asignar al grupo B
    grupo = "B"

# Mostrar los resultados al usuario
print(f"\nHola {nombre}")
print(f"Tu genero es: {'Mujer' if sexo == 'M' else 'Hombre'}") # "Mujer" si sexo es "M", "Hombre" en cualquier otro caso
print(f"Perteneces al grupo: {grupo}")