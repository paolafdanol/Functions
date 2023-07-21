print("     Calculo de Salario")
print("Tarifa por Hora: 10")
print("Tarifa de horas extras: 15\n")

tarifa_nor=10
tarifa_ext=15
horas_norm=40

horas=int(input("Introduzca horas trabajadas: "))
tarifa=int(input("Introduzca la tarifa por hora: "))

def calculo_salario():
    if horas <= 40:
        salario = (horas * tarifa_nor)
        print("Su salario total es: ", salario)
    elif horas > 40:
        horas_extras=(horas-40)
        print("Horas extras trabajadas: ",horas_extras)
        salario=(horas_extras*tarifa_ext+(horas_norm * tarifa_nor))
        print("Su salario total es: ", salario)

calculo_salario()

