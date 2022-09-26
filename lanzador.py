from codigo.code import Matriz, Cadenatexto, Generadorlista, ScriptTabla, Codewars
import sys
import time

def separador():
    print("--------------------------------------------------------")

def solicitar_introducir_numero2(invite):
    """
    Esta función verifica que tenemos un número
    """
    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        print(invite, end=": ")
        datoIntroducido = input()

        try:
            datoIntroducido = int(datoIntroducido)
        except:
            print("Solo están autorizados los caracteres 1-9.", file=sys.stderr)
        else:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return datoIntroducido

def solicitar_introducir_numero_extremo2(invite, minimum=0, maximum=100):
    """
    Esta función utiliza el anterior y añade una post-condición
    sobre los extremos del número a introducir
    """
    invite = "{}".format(invite)
    while True:
        # Entramos en un bucle infinito

        # Pedimos introducir un número
        datoIntroducido = solicitar_introducir_numero2(invite)

        if minimum <= datoIntroducido <= maximum:
            # Tenemos lo que queremos, salimos del bucle saliendo de la función
            return datoIntroducido
        else:
            print("Solo están autorizados los caracteres [1-9].")

def ejecutar():
    print("Estos son los ejercicios resueltos de forma iterativa(no los iba a borrar).\n")
    time.sleep(2)
    matriz = Matriz([[1,1,1,3],[2,2,2,7],[3,3,3,9],[4,4,4,13]]).matriz
    Matriz.condicionmatriz(matriz)
    separador()
    suma = Matriz.suma(matriz); print(f"La función suma devuelve una suma de todos los elementos de la lista, que en este caso es igual a {suma}.")
    separador()
    texto = Cadenatexto("Me llamo Javier").texto
    comprobar = Cadenatexto.comprobarlonguitud(texto)
    print(comprobar); separador()
    l1,l2,l3,l4,l5 = Generadorlista.generarlista()
    print(l1, l2, l3, l4, l5); separador()
    ScriptTabla.scripttabla()
    separador()

def ejecutar2():
    eleccion = solicitar_introducir_numero_extremo2("¿Qué ejercicio quieres runnear?", 1, 5)
    if eleccion == 3:
        Generadorlista.generarnumero(0, [], 11, 1)
        Generadorlista.generarnumero(-10, [], 1, 1)
        Generadorlista.generarnumero(0, [], 22, 2)
        Generadorlista.generarnumero(-19, [], 1, 2)
        Generadorlista.generarnumero(0, [], 55, 5)
    elif eleccion == 5:
        lista = Codewars.string_to_array(input("Introduce una cadena de texto: "))
        print(lista)
    elif eleccion == 1:
        Matriz.construirmatriz()
    elif eleccion == 2:
        texto = Cadenatexto(input("Introduce una cadena: ")).texto
        comprobar = Cadenatexto.comprobarlonguitud(texto)
        print(comprobar)
    elif eleccion == 4: #mismo code
        l1,l2,l3,l4,l5 = Generadorlista.generarlista()
        print(l1, l2, l3, l4, l5); separador()
        ScriptTabla.scripttabla()

def elegir():
    eleccion = eleccion = solicitar_introducir_numero_extremo2("¿Como quieres verlo, de forma iterativa(1), o de forma recursiva(2)?", 1, 2)
    if eleccion == 1:
        ejecutar()
    elif eleccion == 2:
        ejecutar2()