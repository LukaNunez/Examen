import Funcion as fn

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]

sueldo_trabajador = {}

while True:
    try:
        print("------Menu------")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas.")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            fn.sueldos_aleatorio(trabajadores)
        elif opcion == 2:
            fn.calsificar_sueldo(trabajadores)
        elif opcion == 3:
            fn.estadistica(trabajadores)
        elif opcion == 4:
            fn.reporte_sueldo(trabajadores)
        elif opcion == 5:
            print("Finalizando programa . . .")
            print("Desarrollado por luka nuñez")
            print("Rut: 21.433.339-2")
            break
    except:
        print("ingrese una opcion valida")