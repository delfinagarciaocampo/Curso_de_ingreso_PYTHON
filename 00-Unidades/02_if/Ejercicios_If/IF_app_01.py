import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Delfina
apellido: García Ocampo
---
Ejercicio: if_01
---
Enunciado:
Al presionar el botón 'Mostrar', se deberá obtener el contenido de la caja de texto txt_edad,
transformarlo en número, si coincide con el valor 18, mostrar el mensaje “Usted tiene 18 años” utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        edad_get = int(self.txt_edad.get())
        if edad_get == 18:
            alert("TIENE 18!!!!","Usted tiene 18 años")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

'''
NOTAS

Tipos de datos:
string -> texto
int -> nº enteros
float -> nº decimales
bool -> true/false

Operadores:
== un dato es igual a otro

'''