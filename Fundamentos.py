#Crear una función para el comando print, ya que es repetitivo
def nuevoTema(tema):
    print("\n----- ", tema, " -----\n")# forma 1 con caracteres de escape
def nuevoTema2(tema):
    print("\n----- " + tema + " -----\n")# forma 2 concatenando

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
    print("  ---Operador NOT---")
    print("not True: ", not True )
    print("not False: ", not False )
    print("  ---Operador AND---")
    print("True and True:", True and True)
    print("True and False:", True and False)
    print("False and True:", False and True)
    print("False and False:", False and False)
    print("  ---Operador OR---")
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
nuevoTema("Operadores aritméticos") #usando caracteres de escape
nuevoTema2("Operadores aritméticos") # usando concatenación
