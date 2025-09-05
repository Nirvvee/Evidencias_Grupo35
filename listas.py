def ejemplo_listas():
    materias = ["Matemáticas", "Español", "Historia", "Biología"]
    print("Materias:", materias)

    materias.append("Programación")
    print("Después de agregar:", materias)

    materias.remove("Historia")
    print("Después de eliminar Historia:", materias)

    print("Primera materia:", materias[0])
    print("Última materia:", materias[-1])

    # Lista de calificaciones
    califs = [9, 7, 10, 8, 6]
    print("Calificaciones:", califs)
    print("Promedio:", sum(califs)/len(califs))

    aprobados = [c for c in califs if c >= 7]
    print("Aprobados:", aprobados)

    print("Ordenadas:", sorted(califs))
    print("Reprobados:", [c for c in califs if c < 7])

if __name__ == "__main__":
    ejemplo_listas()