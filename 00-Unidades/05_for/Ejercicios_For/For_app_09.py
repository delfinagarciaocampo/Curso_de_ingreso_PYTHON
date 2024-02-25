import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
from random import randint
import customtkinter

'''
nombre: Delfina
apellido: García Ocampo
---
Ejercicio: for_09
---
Enunciado:
Al comenzar el juego generamos un número secreto del 1 al 100, se pedira al usuario el ingreso de un numero por prompt y si el número ingresado es el mismo que el número secreto se dará por terminado el juego con un mensaje similar a este: 

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “Usted es un psíquico”.
	2° intento: “Excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	7 intentos: “Perdiste, suerte para la próxima”.

de no ser igual se debe informar si 
“Falta…”  para llegar al número secreto  o si 
“Se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        bandera = False
        numero = randint(1,100)
        num_juego = int(prompt("", "Ingrese un número"))
        intento = 0

        for num_juego in range(0, numero+1):
            if num_juego < numero:
                pista = numero - num_juego
                ayuda = "Faltan {0} para llegar al número secreto".format(pista)
                alert("", ayuda)
                intento += 1
            if numero < num_juego:
                pista = num_juego - numero
                ayuda = "Se pasó {0} del número secreto".format(pista)
                alert("", ayuda)
                intento += 1
            num_juego = int(prompt("", "Ingrese un número"))



















        #         match intento:
        #             case 1:
        #                 mensaje = "Usted es un psíquico"
        #             case 2:
        #                 mensaje = "Excelente percepción"
        #             case 3:
        #                 mensaje = "Eso es suerte"
        #             case 4 | 5 | 6:
        #                 mensaje = "Excelente técnica"

        
        # print(numero)



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()