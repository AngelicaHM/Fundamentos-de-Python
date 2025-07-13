from tkinter import *                               #Se importa la paquetería de Tkinter
from tkinter import ttk                        

def ingresar (*args):                               #Defino la función que ejecuta el ingres al presionar el botón
    n1=0                                            #Le doy un acción cualquiera porque no se a dónde dirigir el ingreso

raiz= Tk()                                          #Objeto ventana, raíz de todo el widget
raiz.title("Inicio de sesión")                      #Título de la ventana

marcoPrincipal = ttk.Frame(raiz, padding="3 3 12 12")            #Se le asigna un marco de separación de las orillas
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E, S))        #Orientación del componente, en este caso centrado
marcoPrincipal.columnconfigure(0, weight=1)                      #Weight e spara que este balanceado
marcoPrincipal.rowconfigure(0, weight=1)

user = StringVar()                                               #Variable para guardar el nombre de ususario
passw =StringVar()                                               #Variable para guardar la contraseña

txtUser = ttk.Entry(marcoPrincipal, width=30, textvariable=user)       #Caja de texto donde ingresa el nombre de usuario con ancho de 30
txtUser.grid(column=2, row=1, sticky=(W))                           #Ubicación del cuadro de texto (2,1) orientado a la izq

txtPassw = ttk.Entry(marcoPrincipal, width=30, textvariable=passw)     #Caja de texto donde ingresa la contraseña con ancho de 30
txtPassw.grid(column=2, row=2, sticky=(W))                          #Ubicación del cuadro de texto (2,2) orientado a la izq

ttk.Button(marcoPrincipal, text="Ingresar", command = ingresar).grid(column=2, row=3, sticky=E)   #Botón que llama a la función ingresar, con su ubicación (2,3)

ttk.Label(marcoPrincipal, text="Usuario").grid(column=1, row=1, sticky= E)           #Etiqueta de texto "Usuario", ubicación (1, 1) orientado a la der
ttk.Label(marcoPrincipal, text="Contraseña").grid(column=1, row=2, sticky= E)        #Etiqueta de texto "Contraseña", ubicación (1, 2) orientado a la der


for child in marcoPrincipal.winfo_children():           #Ciclo que asigan un distancia entre elementos 
    child.grid_configure(padx=5, pady=5)

txtPassw.focus()                      #focus envia el cursos a los cuadros de texto para que el usuario se enfoque en ellos
txtUser.focus()
raiz.bind('<Return>', ingresar)       #Habilitamos la función ingresar con la tecla Enter

raiz.mainloop()                       #Ejecución del algoritmo par los diferentes eventos