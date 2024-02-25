import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Delfina
apellido: García Ocampo
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        bandera = True
        numero = int(prompt("", "Ingrese un número"))

        for i in range(2, numero+1):
            for j in range(2, i):
                if i % j == 0:
                    bandera = False
                    break

            if bandera:
                print(i)
            bandera = True
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()