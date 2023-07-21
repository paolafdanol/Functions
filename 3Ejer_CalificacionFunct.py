print("     Calificaciones")
i=0
def calcula_calificacion():
    try:
        puntos=float(input("Por favor, introduzca su puntuación entre 0.0 y 1.0: "))
        if puntos > 1.0:
            print("Puntuación incorrecta\n")
        elif puntos >= 0.9:
            print("Sobresaliente\n")
        elif puntos >= 0.8:
            print("Notable\n")
        elif puntos >= 0.7:
            print("Bien\n")
        elif puntos >= 0.6:
            print("Suficiente\n")
        else:
            print("Insuficiente\n")
    except:
        print("\nPuntuación incorrecta\n")


while i<7:
    i += 1
    calcula_calificacion()



