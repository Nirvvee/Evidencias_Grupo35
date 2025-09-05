def ejemplo_tuplas():
    alumno = ("Carlos", 17, "4B")
    print("Alumno:", alumno)

    nombre, edad, grupo = alumno
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Grupo:", grupo)

    materias = [
        ("Matemáticas", "Profa. Ana"),
        ("Español", "Profa. Laura"),
        ("Historia", "Profe. José")
    ]
    for mat, prof in materias:
        print(f"{mat} -> {prof}")

    salon = (2, 15)
    print("Ubicación del salón:", salon)

if __name__ == "__main__":
    ejemplo_tuplas()