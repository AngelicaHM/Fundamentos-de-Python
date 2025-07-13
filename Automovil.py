class Automovil:
    def __init__(self, marca, color):
    #Definir atributos de clase    
    #Solo los que empiezan con "self"
        self.marca = marca
        self.color = color

    def avanzar(self):
         print(f"El coche avanza y es un: {self.marca}")

    def retroceder(self):
        print(f"El coche retrocede y es de color {self.color}")

if __name__ == "__main__":
    auto = Automovil("BMW", "Azul")
    auto.avanzar()
    auto.retroceder()

    auto = Automovil("Honda", "Gris")
    auto.retroceder()
    auto.avanzar()
    


