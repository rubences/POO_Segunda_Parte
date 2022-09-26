from introducir import solicitar_introducir_numero_extremo
from introducir import solicitar_introducir_numero2

class Matriz:
    def __init__(self, matriz):
        self.matriz = matriz

    def condicionmatriz(lista):
        for elemento in lista:
            sum = 0
            for i in range(len(elemento)):
                if i == 3 and elemento[i] != sum:
                    elemento[i] = sum
                    print("Matriz corregida")
                    print(lista)
                else:
                    sum+=int(elemento[i])
        print("Matriz correcta")
        return lista

    def suma(lista):
        sum = 0
        for elemento in lista:
            for i in elemento:
                sum+=int(i)
        return sum

    def construirmatriz(matriz=[[], [], [], []], suma=0, i=0):
        if len(matriz[3]) < 3:
            if len(matriz[i]) < 3:
                pregunta = int(solicitar_introducir_numero2("Introduce un elemento de la matriz: "))
                matriz[i].append(pregunta)
                suma+=pregunta
                print(matriz)
                Matriz.construirmatriz(matriz, suma, i)
            elif len(matriz[i]) == 3:
                elemento4 = (matriz[i][0]+matriz[i][1]+matriz[i][2])
                matriz[i].append(elemento4)
                suma+=elemento4
                print(matriz)
                i+=1
                Matriz.construirmatriz(matriz, suma, i)
        else:
            elemento4 = (matriz[i][0]+matriz[i][1]+matriz[i][2])
            matriz[i].append(elemento4)
            suma+=elemento4
            print(matriz)
            print(matriz)
            print(f"La suma de los elementos de la matriz es {suma}")

class Cadenatexto:
    def __init__(self, texto):
        self.texto = texto

    def comprobarlonguitud(cadena):
        if 3 <= len(cadena) <= 10:
            print("La cadena está entre 3 y 10 caracteres.")
            return True
        else:
            print("La cadena no está entre los 3 y 10 caracteres.")
            return False

class Generadorlista:
    def __init__(self) -> None:
        pass

    def generarlista():
        lista1 = []
        lista2 = []
        lista3 = []
        lista4 = []
        lista5 = []
        for i in range(11):
            lista1.append(i)
        for i in range(-10,1,1):
            lista2.append(i)
        for i in range(0,21,2):
            lista3.append(i)
        for i in range(-19,0,2):
            lista4.append(i)
        for i in range(0,51,5):
            lista5.append(i)
        return lista1, lista2, lista3, lista4, lista5

    def generarnumero(n, lista1, condicion, sumatorio):
        if n!=condicion:
            lista1.append(n)
            n+=sumatorio
            Generadorlista.generarnumero(n, lista1, condicion, sumatorio)
        else:
            print(lista1)


class ScriptTabla:
    def __init__(self) -> None:
        pass

    def scripttabla():
        f = solicitar_introducir_numero_extremo("Introduzca un argumento",1,9)
        c = solicitar_introducir_numero_extremo("Introduzca otro argumento",1,9)
        for i in range(f):
            for i in range(c):
                print(" * ", end='')
        print(""); print("_________________________________")
        print("Ahora la parte modificada para que salga una tabla de fxc")
        print("_________________________________")
        for i in range(f):
            for i in range(c):
                if i == c-1:
                    print(" * ")
                else:
                    print(" * ", end='')

class Codewars:
    def string_to_array(s):
        if s == '' or "":
            return [""]
        else:
            return s.split()