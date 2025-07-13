file = open("EjemploArchivo.txt", "w")
file.write("Este es el contenido del archivo.")
file.close()

lista= ["Fresa", "Mango", "Papaya"]  

with open("EjemploArchivo.txt", "a") as file:    #La instrucción with junto con un recurso, se crea un contexto de uso o de aplicación del recurso, cierra el archivo al finalizar las instrucciones.
    for e in lista:
        file.write(e + "\n")                      #Añade la informaicón de lista al archivo existente.

print("Lista escrita en el archivo")

lista2 = ["Honda", "Suzuki", "BMW"]

with open("EjemploArchivo.txt", "a") as file:
    file.writelines(lista2)

print("Lista escrita con writelines")

print("Imprimir todo el contenido del archivo")

with open("EjemploArchivo.txt", "r") as file:
    print(file.read())

print("Leer dos líneas y posteriormente 5 caracteres")
with open("EjemploArchivo.txt", "r") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline(5))

print("Almacenar el contenido de una lista y mostrar el último elemento")
with open("EjemploArchivo.txt", "r") as file:
    contenido = file.readlines()
    print (contenido[-1])



