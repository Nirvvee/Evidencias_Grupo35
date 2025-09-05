def ejemplo_diccionarios():
    alumno = {
        "nombre": "María",
        "edad": 18,
        "grupo": "5A",
        "materias": ["Español", "Inglés", "Física"]
    }
    print("Alumno:", alumno)

    print("Nombre:", alumno["nombre"])
    alumno["edad"] = 19
    print("Edad actualizada:", alumno["edad"])

    alumno["promedio"] = 9.2
    print("Con promedio:", alumno)

    for clave, valor in alumno.items():
        print(f"{clave}: {valor}")

    # Diccionario de calificaciones
    califs = {"Español": 8, "Inglés": 9, "Física": 10}
    print("Calificaciones:", califs)

    print("Materias y califs:")
    for mat, cal in califs.items():
        print(f"{mat}: {cal}")

if __name__ == "__main__":
    ejemplo_diccionarios()