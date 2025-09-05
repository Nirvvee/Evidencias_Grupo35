def ejemplo_conjuntos():
    grupo_A = {"Ana", "Luis", "Carlos", "María"}
    grupo_B = {"Pedro", "Ana", "María", "Sofía"}

    print("Grupo A:", grupo_A)
    print("Grupo B:", grupo_B)

    print("Unión (todos los alumnos):", grupo_A | grupo_B)
    print("Intersección (comparten grupos):", grupo_A & grupo_B)
    print("Solo en A:", grupo_A - grupo_B)
    print("Solo en B:", grupo_B - grupo_A)
    print("Diferencia simétrica:", grupo_A ^ grupo_B)

    grupo_A.add("Jorge")
    print("Grupo A actualizado:", grupo_A)

if __name__ == "__main__":
    ejemplo_conjuntos()