import random
import csv

sueldo_trabajador = {}

def sueldos_aleatorio(trabajadores):
    for trabajador in trabajadores:
        if trabajador == 10:
            return {
                trabajador : random.randint(300000,2500000)
            }
    

def calsificar_sueldo(trabajadores,sueldo_trabajadores):
    sueldo_trabajador = {"menor a 800000":[],"entre 800000 y 2000000":[],"mayor a 2000000":[]}

    for sueldo_trabajador in sueldo_trabajadores.item:
        if sueldo_trabajador < 800000:
            sueldo_trabajador = {"menor_800000"}.append[trabajadores, sueldo_trabajadores]
        elif sueldo_trabajador <= 2000000:
            sueldo_trabajador = {"entre_800000_2000000"}.append[trabajadores, sueldo_trabajadores]
        elif sueldo_trabajador > 2000000:
            sueldo_trabajador = {"mayor_2000000"}.append[trabajadores, sueldo_trabajadores]
        

def estadistica(trabajadores):
    print()

def reporte_sueldo(trabajadores):
    with open("reprte_sueldo.csv","w") as archivo:
        print
