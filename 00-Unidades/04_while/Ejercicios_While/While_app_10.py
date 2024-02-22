import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Delfina
apellido: García Ocampo
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_p = 0
        suma_n = 0
        cont_p = 0
        cont_n = 0
        cont_ceros = 0

        while True:
            num = prompt("", "Ingrese un número")

            if num == None:
                break

            num = int(num)

            if num > 0:
                suma_p = suma_p + num
                cont_p += 1

            if num < 0:
                suma_n = suma_n + num
                cont_n +=1

            if num == 0:
                cont_ceros += 1

        if cont_n > cont_p:
            dif = cont_n - cont_p
        else:
            dif = cont_p - cont_n

        alert("Suma acumulada positivos", suma_p)
        alert("Suma acumulada negativos", suma_n)
        alert("Cantidad de numeros positivos ingresados", cont_p)
        alert("Canridad de numeros negaivos ingresados", cont_n)
        alert("Cantidad de ceros ingresados", cont_ceros)
        alert("Diferencia cantidad de numeros positivos y negativos", dif)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()