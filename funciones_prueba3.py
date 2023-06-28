import os
import time
import msvcrt
import numpy

casitas =numpy.zeros((2,5), int)

def menu():
    os.system("cls")
    print("""MENÚ Mascota Segura:
    1-GRABAR
    2-BUSCAR
    3-RETIRARSE
    4-SALIR""")

def validar_opcion():
    while True:
        opcion = int(input("ingrese la opción deseada: "))
        try:
            if opcion in(1,2,3,4):
                return opcion
            else:
                print("opción inválida!")
                time.sleep(1)
                os.sistem("cls")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
            time.sleep(1)
            os.sistem("cls")

def validar_rut():
    while True:
        rut = int(input("ingrese su rut del dueño(sin puntos, sin guión y sin dígito verificador): "))
        try:
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("rut inválido")            
                time.sleep(1)
                os.sistem("cls")
        except:
            print("ERROR! INGRESE UN NÚMERO ENTERO!!")
            time.sleep(1)
            os.sistem("cls")
            

def validar_nombre():
    nombre = input("porfavor ingrese su nombre(mínimo debe tener 3 letras): ")
    if len(nombre.strip()) >= 3 and nombre.isalpha():
        return nombre
    else:
        print("ERROR! NOMBRE INVÁLIDO!")
        time.sleep(1)
        os.sistem("cls")
    
def validar_nombre_mascota():
    nombre_mascota = input("porfavor ingrese el nombre de la mascota(mínimo debe tener 3 letras): ")
    if len(nombre_mascota.strip()) >= 3 and nombre_mascota.isalpha():
        return nombre_mascota
    else:
        print("ERROR! NOMBRE inválido!")
        time.sleep(1)
        os.sistem("cls")

def validar_dinero():
    while True:
        dinero = int(input("ingrese el dinero: "))
        try:
            if dinero >= 1:
                return dinero
            else:
                print("ERROR!! NO PUEDE COMPRAR CON MENOS DE 1 PESO")
                time.sleep(1)
                os.sistem("cls")
        except:
            print("ERROR!! INGRESE UN NÚMERO ENTERO!") 
            time.sleep(1)
            os.sistem("cls")      

def validar_dias():
    while True:
        dias=int(input("ingrese la cantidad de días que se quedará su mascota($15000 * dia): "))
        try:
            if dias > 0 :
                return dias
            else:
                print("ERROR! SU MASCOTA NO PUEDE QUEDARSE MENOS DE 1 DÍA!")
                time.sleep(1)
                os.sistem("cls")
        except:
            print("ERROR! INGRESE UN NÚMERO ENTERO!!")
            time.sleep(1)
            os.sistem("cls")

def validar_fila():
    while True:
        fila = int(input("elija la fila: "))
        try:
            if fila in(1,2):
                return fila
            else:
                print("ERROR! FILA INVÁLIDA")
        except:
            print("ERROR! indique un número entero!")


def validar_columna():
    while True:
        columna = int(input("elija la columna: "))
        try:
            if columna in(1,2,3,4,5):
                return columna
            else:
                print("ERROR! columna INVÁLIDA")
        except:
            print("ERROR! indique un número entero!")

def mostrar_guarderia():
    print("GUARDERÍA \t")
    print("       1 2 3 4 5")
    for x in range(2):
        print("fila",x+1, end=" ")
        for y in range(5):
            print( casitas[x][y], end=" " )
        print()
    print("presione un botón para continur la reserva")
    msvcrt.getch()
            
def validar_id_mascota():
    for x in range(len(casitas)):
        casitas = 1 + x
        return


lista_rut=[]
lista_nombre=[]
lista_id_mascota =[]
lista_nombre_mascota=[]
lista_cantidad_dias=[]
lista_fila=[]
lista_columna=[]
lista_dias =[]



def grabar():
    if 1 in casitas:
        print("No hay alojamiento disponible para su mascota😢, vuelva otro día")

    rut = validar_rut()
    nombre = validar_nombre()
    id_mascota = validar_id_mascota()
    nombre_mascota = validar_nombre_mascota()
    dias=validar_dias()
    while True:
        mostrar_guarderia()
        fila= validar_fila()
        columna = validar_columna()
        elec_fila = fila - 1
        elec_columna= columna - 1
        
        if casitas[elec_fila][elec_columna]== 0:
            casitas[elec_fila][elec_columna]=1
            lista_rut.append(rut)
            lista_nombre.append(nombre)
            lista_id_mascota.append(id_mascota)
            lista_nombre_mascota.append(nombre_mascota)
            lista_dias.append(dias)
            lista_fila.append(elec_fila)
            lista_columna.append(elec_columna)
            print("su mascota ya tiene su lugar en la guardería!!💕")
            return
        else:
            print("lo siento este lugar no está disponible😢")
            time.sleep(1)
            os.sistem("cls")

def buscar():
    rut = validar_rut()
    if rut in len(lista_rut):
        fila = lista_fila.index(rut)
        columna = lista_columna.index(rut)
        print(f"la ubicación de su mascota es: fila:{fila} columna: {columna}")
        print("oprima una tecla para continuar")
        msvcrt.getch()
        return
    else:
        print("su rut no se encuentra registrado!")
        time.sleep(1)
        os.sistem("cls")

def retirarse():
    
    rut = validar_rut()
    if rut in lista_rut:
        total_pago= lista_dias.index(rut) * 15000
        print(f"su total a pagar es: ${total_pago}")
        dinero = validar_dinero()
        if dinero == total_pago:
            fila=lista_fila.index(rut)
            columna= lista_columna.index(rut)

            casitas[fila][columna]=0
            lista_rut.pop(lista_dias.index(rut))
            lista_nombre.pop(lista_nombre.index(rut))
            lista_id_mascota.pop( lista_id_mascota.index(rut))
            lista_nombre_mascota.pop(lista_nombre_mascota.index(rut))
            lista_dias.pop(lista_dias.index(rut))
            lista_fila.pop(lista_fila.index(rut))
            lista_columna.pop(lista_columna.index(rut))
            return
        else:
            print("dinero insuficiente!! guardias!")
            time.sleep(1)
            os.sistem("cls")
    else:
        print("no está registrada su mascota en la guarde´ría")  
        time.sleep(1)
        os.sistem("cls")     

def salir():
    print("ADIOS!!")
    return

    
        
         

    

