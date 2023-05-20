def calcular_promedio():
    quiererepetir = True
    lista = []
    while quiererepetir:
        calificacion = int(input("Enter a grade (-1 to finish):"))
        if calificacion == -1:
            quiererepetir = False
        elif calificacion < 0:
            print("Invalid grade. Please enter a positive number or -1 to finish.")
        else:
            lista.append(calificacion)

    if not lista:
        print("No grades were entered.")
        return
    resultado = sum(lista) / len(lista)
    return resultado
print(calcular_promedio())