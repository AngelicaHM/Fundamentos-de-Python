#Crear una función para el comando print, ya que es repetitivo.
def nuevo_tema(tema:str): #En esta función se indido el tipo de variable con fines informativos, ya que no la está definiendo como tal. Esto se concidera buenas prácticas de programación, nada más.
    print("\n----- ", tema, " -----\n") # forma 1 con caracteres de escape.
def nuevoTema2(tema):
    print("\n----- "  + tema +  " -----\n") # forma 2 concatenando.
def nuevoTema3(tema):
    print(f"\n-----   {tema}  -----\n") # forma 3 con formato (con más estilo Python)también llamada "cadena formateada".
def nuevoTema4(tema):
    print(f"\n-----   {tema}  -----\n")
    llave_a = "{" #Se pueden crear variables para signos que podrían confuncdirse con los comandos del lenguaje.
    llave_c = "}" #Por ejemplo llaves de apertura y de cierre.
    print(f"\n----- {llave_a} {tema} {llave_c} -----\n")

if __name__ == "__main__":# esto se utiliza para indicar qué línea inicia primero, ya que Python no usa main. No es obligatorio para todo solo cuando es necesario indicar un orden de inicio.

    print("-----Operadores aritméticos-----")#Para incluir las líneas dentro del if debemos darle espacio con el tabulador y mantener la misma distancia para las líneas que pertenezcan al Código.
    print("Operador suma, 7 + 10 =",7 + 10)
    print("Operador resta, 7 - 10 =",7 - 10)
    print("Operador multiplicación, 7 * 10 =",7 * 10)
    print("Operador división, 7 / 10 =",7 / 10)
    print("Operador división entera, 7 // 10 =",7 // 10)
    print("Operador módulo, 7 % 10 =",7 % 10)
    print("Operador exponente, 7 ** 10 =",7 ** 10)
    print("Operador identidad, + 7  =",+ 7 )
    print("Operador cambio de signo -7 =",-7)

    #Este es un comentario de una sola línea
    '''Este es un comentario
    de varias líneas'''
    print("-----Operadores lógicos-----")
    print("  ---Operador NOT---") # Comprobación de tabla de verdad de NOT
    print("not True: ", not True )
    print("not False: ", not False )
    print("  ---Operador AND---") # Comprobación de tabla de verdad de AND
    print("True and True:", True and True)
    print("True and False:", True and False)
    print("False and True:", False and True)
    print("False and False:", False and False)
    print("  ---Operador OR---") # Comprobación de tabla de verdad de OR
    print("True or True:", True or True)
    print("True or False:", True or False)
    print("False or True:", False or True)
    print("False or False:", False or False)
    print("-----Operadores de comparación-----")
    print("Operador 'igual que', 7 == 10:", 7 == 10)
    print("Operador 'distinto de', 7 != 10:", 7 != 10)
    print("Operador 'menor que', 7 < 10:", 7 < 10)
    print("Operador 'menor o igual que', 7 <= 10:", 7 <= 10)
    print("Operador 'mayor que', 7 > 10:", 7 > 10)
    print("Operador 'mayor o igual que', 7 >= 10:", 7 >= 10)

#06/06/2025 VARIABLES
#Crear Funciones
nuevo_tema("Operadores aritméticos") 
nuevoTema2("Operadores aritméticos") 
nuevoTema3("Operadores aritméticos") 
nuevoTema4("Operadores aritméticos") 
if __name__ == "__main__":

    nuevo_tema("Operadores aritméticos") #llamamos a la función "nuevoTema"
    print("Operador suma, 7 + 10 =",7 + 10)
    print("Operador resta, 7 - 10 =",7 - 10)
    print("Operador multiplicación, 7 * 10 =",7 * 10)
    print("Operador división, 7 / 10 =",7 / 10)
    print("Operador división entera, 7 // 10 =",7 // 10)
    print("Operador módulo, 7 % 10 =",7 % 10)
    print("Operador exponente, 7 ** 10 =",7 ** 10)
    print("Operador identidad, + 7  =",+ 7 )
    print("Operador cambio de signo -7 =",-7)

    nuevo_tema("Operadores lógicos") #llamamos a la función "nuevoTema"
    print("  ---Operador NOT---") # Comprobación de tabla de verdad de NOT
    print("not True: ", not True )
    print("not False: ", not False )
    print("  ---Operador AND---") # Comprobación de tabla de verdad de AND
    print("True and True:", True and True)
    print("True and False:", True and False)
    print("False and True:", False and True)
    print("False and False:", False and False)
    print("  ---Operador OR---") # Comprobación de tabla de verdad de OR
    print("True or True:", True or True)
    print("True or False:", True or False)
    print("False or True:", False or True)
    print("False or False:", False or False)
    nuevo_tema("Operadores de comparación") #llamamos a la función "nuevoTema"
    print("Operador 'igual que', 7 == 10:", 7 == 10)
    print("Operador 'distinto de', 7 != 10:", 7 != 10)
    print("Operador 'menor que', 7 < 10:", 7 < 10)
    print("Operador 'menor o igual que', 7 <= 10:", 7 <= 10)
    print("Operador 'mayor que', 7 > 10:", 7 > 10)
    print("Operador 'mayor o igual que', 7 >= 10:", 7 >= 10)

    #Ejemplo de variable dinámica
    mensaje="Hola bebe"
    print(mensaje)
    mensaje=10
    print(mensaje)
    
    print("--------------------------")
    # Ejemplos con Números 
    nuevo_tema("Enteros")
    w = 105
    x = 12345678987654321
    y = -58
    z = 0b0011011 #el prefijo "0b" (cero be) denota que el numero es binario.
    h = 0xFF #el prefijo "0x" (cero equis) denota que el numero esta en hexadecimal.

    print(w, type(w))
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(h, type(h))

    print("--------------------------")
    nuevo_tema("Flotantes")
    x = 1234.56
    print(x, type(x))
    y = -0.2584
    print(y, type(y))

    print("--------------------------")
    nuevo_tema("Número complejos")
    x = -46j
    y = 12 + 45j
    z = 2j 
    c = y + z
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(c, type(c))

    print("--------------------------")
    nuevo_tema("Booleanos")
    x = True
    print(x, type(x))
    y = False
    print(y, type(y))

    print("--------------------------")
    nuevo_tema("Listas")
    lista=[10, 20.5, "Lista de Python"]
    print(lista)
    print(lista[0])
    print(lista[1])
    print(lista[2])
    lista[0]="Hola"
    lista.append(34)
    lista.insert(0,1.1)
    print(lista)
    lista.append([3,4,5,6,7,8])
    print(lista)
    print(lista[5])
    print(lista[5][4])

    print("--------------------------")
    nuevo_tema("Tupla")
    tupla=(25, "Tupla", 1+10j)
    print(tupla)
    print(tupla[1])
    #tupla[0]=0   'tuple' object does not support item assignment, no es un peración valida para tuplas.
    #print(tupla)
    tupla=(25, "Tupla", 1 + 10j, "Otro")
    print(tupla)

    print("--------------------------")
    nuevo_tema("Sets") #Conjuntos
    conjunto={10, 20, 30, 40, 50, 20}# muestra un error por duplicar el 20, aún así imprime el conjunto.
    print(conjunto)
    #print(conjunto[1]) no estan iterados (ordenados) es un conjunto desordenado ('set' object is not subscriptable).
    conjunto.add(80) #Añadir elementos
    print(conjunto)
    print(50 in conjunto)#para saber si existe un elemeto específico en el set, salida:Tueo or False.

    print("--------------------------")
    nuevo_tema("Diccionarios")
    diccionario={"Nombre": "Conrado", 
                 "Edad": 41,
                 "Teléfono":12345789,
                 90:4+3j}
    print(diccionario)
    print(diccionario["Teléfono"])
    print(diccionario[90])

    print("--------------------------")
    nuevo_tema("Cadenas")
    cadena1="Esto es una cadena"
    cadena2= 'Esto es una cadena'
    cadena_multilinea='''Esto es una cadena con
    de varias líneas con tabuladores 
    y saltos
    de 
    línea'''
    print(cadena1, type(cadena1))
    print(cadena2, type(cadena2))
    print(cadena_multilinea, type(cadena_multilinea))

    cadena3=("Hola") *5
    print(cadena3)
    cadena3=("Hola\n") *5
    print(cadena3)
    cadena3=("Hola\t") *5
    print(cadena3)
    print(cadena1[2])
    print(cadena1[2:10])
    print(cadena1[ :5])
    print(cadena1[5:])
    print(cadena1[ :-5])
    print(cadena1[5:-5])
    print(cadena1[::-1])   
    







