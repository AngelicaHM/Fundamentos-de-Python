from Fundamentos import nuevo_tema                 #Importamos la funcion "nuevo_tema" del archivo "Fundamentos".
import Calc.operaciones as c                       #Importamos las funciones operaciones de la carpeta "Calc" y del archivo "operaciones"
#print(Calc.operaciones.resta(4, 1))               #El "as C" es para ahorrar el nombre del archivo de importación
#print(c.resta(4,1))                               #Uso d ela variable c para simplificar la instrucción

if __name__ == "__main__":
    nuevo_tema("Módulo y paquetes")

    print(c.resta(6,1)) 
    print(c.suma(2, 3, 4)) 
    print(c.mult(5, 6)) 
    print(c.div(11, 2.5)) 
