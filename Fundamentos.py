#Crear una función para el comando print, ya que es repetitivo.
def nuevoTema(tema:str): #En esta función se indido el tipo de variable con fines informativos, ya que no la está definiendo como tal. Esto se concidera buenas prácticas de programación, nada más.
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
nuevoTema("Operadores aritméticos") 
nuevoTema2("Operadores aritméticos") 
nuevoTema3("Operadores aritméticos") 
nuevoTema4("Operadores aritméticos") 
if __name__ == "__main__":

    nuevoTema("Operadores aritméticos") #llamamos a la función "nuevoTema"
    print("Operador suma, 7 + 10 =",7 + 10)
    print("Operador resta, 7 - 10 =",7 - 10)
    print("Operador multiplicación, 7 * 10 =",7 * 10)
    print("Operador división, 7 / 10 =",7 / 10)
    print("Operador división entera, 7 // 10 =",7 // 10)
    print("Operador módulo, 7 % 10 =",7 % 10)
    print("Operador exponente, 7 ** 10 =",7 ** 10)
    print("Operador identidad, + 7  =",+ 7 )
    print("Operador cambio de signo -7 =",-7)

    nuevoTema("Operadores lógicos") #llamamos a la función "nuevoTema"
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
    nuevoTema("Operadores de comparación") #llamamos a la función "nuevoTema"
    print("Operador 'igual que', 7 == 10:", 7 == 10)
    print("Operador 'distinto de', 7 != 10:", 7 != 10)
    print("Operador 'menor que', 7 < 10:", 7 < 10)
    print("Operador 'menor o igual que', 7 <= 10:", 7 <= 10)
    print("Operador 'mayor que', 7 > 10:", 7 > 10)
    print("Operador 'mayor o igual que', 7 >= 10:", 7 >= 10)