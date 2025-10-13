# -*- coding: utf-8 -*-

# Solicitar al usuario cuantas personas desea registrar
try:
    num_personas = int(input("Cuantas personas deseas registrar? "))
except ValueError:
    print("Por favor, ingresa un numero valido.")
    exit()

# Lista para almacenar los datos de todas las personas
personas = []

# Bucle para registrar cada persona
for i in range(num_personas):
    print(f"\n--- Registrando persona {i+1} de {num_personas} ---")
    
    # Solicitar el nombre y genero de la persona 
    nombre = input("Ingresa el nombre: ").strip().title()
    sexo = input("Ingresa el genero (M para mujer, H para hombre): ").strip().upper()
    edad_str = input("Ingresa la edad: ").strip()

    # Obtener la primera letra del nombre
    pra_letra = nombre[0].upper()

    # REGLA: Mujer con nombre que empiece con letra anterior a M (A-L) O Hombre con nombre que empiece con letra posterior a N (O-Z)
    if (sexo == "M" and pra_letra < "M") or (sexo == "H" and pra_letra > "N"):
        # Si cumple alguna de las condiciones anteriores, asignar al grupo A
        grupo = "A"
    else:
        # Si NO cumple ninguna de las condiciones, asignar al grupo B
        grupo = "B"

    # Validar la edad y determinar si es mayor de edad (18 o mas)
    try:
        edad = int(edad_str)
        if edad >= 18:
            estado_edad = "Es mayor de edad."
        else:
            estado_edad = "Es menor de edad."
    except ValueError:
        # Manejo de error si el usuario no introduce un numero
        estado_edad = "No fue posible determinar la mayoria de edad."

    # Almacenar los datos de la persona
    persona = {
        "nombre": nombre,
        "sexo": sexo,
        "edad": edad_str,
        "grupo": grupo,
        "estado_edad": estado_edad
    }
    
    personas.append(persona)

# Mostrar los resultados de todas las personas
print("\n" + "="*50)
print("RESULTADOS DE TODAS LAS PERSONAS REGISTRADAS")
print("="*50)

for i, persona in enumerate(personas, 1):
    print(f"\n--- Persona {i} ---")
    print(f"Nombre: {persona['nombre']}")
    print(f"Genero: {'Mujer' if persona['sexo'] == 'M' else 'Hombre'}")
    print(f"Pertenece al grupo: {persona['grupo']}")
    print(f"Estado de edad: {persona['estado_edad']}")

# Contadores generales
grupo_a = sum(1 for p in personas if p["grupo"] == "A")
grupo_b = sum(1 for p in personas if p["grupo"] == "B")
mayores = sum(1 for p in personas if "mayor" in p["estado_edad"])
menores = sum(1 for p in personas if "menor" in p["estado_edad"])

print("\n" + "="*50)
print("RESUMEN GENERAL")
print("="*50)
print(f"Total de personas registradas: {len(personas)}")
print(f"Personas en grupo A: {grupo_a}")
print(f"Personas en grupo B: {grupo_b}")
print(f"Mayores de edad: {mayores}")
print(f"Menores de edad: {menores}")

# Nueva funcionalidad: Exportar a archivo
exportar = input("\n¿Deseas exportar los resultados a un archivo? (S/N): ").strip().upper()
if exportar == "S":
    with open("resultados_personas.txt", "w", encoding="utf-8") as archivo:
        archivo.write("RESULTADOS DE REGISTRO DE PERSONAS\n")
        archivo.write("=" * 40 + "\n")
        for persona in personas:
            archivo.write(f"Nombre: {persona['nombre']}, Grupo: {persona['grupo']}, Edad: {persona['edad']}\n")
    print("Datos exportados a 'resultados_personas.txt'")
    input("Presiona Enter para continuar...")

input("\nPresiona Enter para salir...")