file = open("EjemploArchivo.txt", "w")
file.write("Este es el contenido del archivo.")
file.close()

lista= ["Fresa", "Mango", "Papaya"]  
con 
with open("EjemploArchivo.txt", "a") as file:    #La instrucción with junto con un recurso, se crea un contexto de uso o de aplicación del recurso, cierra el archivo al finalizar las instrucciones.
    for e in lista:
        file.write(e + "\n")                      #Añade la informaicón de lista al archivo existente.

print("Lista escrita en el archivo")