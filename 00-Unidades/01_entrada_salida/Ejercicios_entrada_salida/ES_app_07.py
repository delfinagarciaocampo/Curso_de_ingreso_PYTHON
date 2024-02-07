import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_07
---
Enunciado:
Al presionar el botón  que corresponde a cada operación (suma, resta, multiplicación, y división), 
se deberán obtener los valores contenidos en las cajas de texto (txtOperadorA y txtOperadorB), 
transformarlos en números enteros, realizar dicha operación y luego mostrar el resultado 
de la misma utilizando el Dialog Alert. Ej: "El resultado de la …… es: 755"  
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Operador A")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_operador_a = customtkinter.CTkEntry(master=self)
        self.txt_operador_a.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Operador B")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_operador_b = customtkinter.CTkEntry(master=self)
        self.txt_operador_b.grid(row=1, column=1)
        
        self.btn_sumar = customtkinter.CTkButton(master=self, text="Sumar", command=self.btn_sumar_on_click)
        self.btn_sumar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_restar = customtkinter.CTkButton(master=self, text="Restar", command=self.btn_restar_on_click)
        self.btn_restar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_multiplicar = customtkinter.CTkButton(master=self, text="Multiplicar", command=self.btn_multiplicar_on_click)
        self.btn_multiplicar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_dividir = customtkinter.CTkButton(master=self, text="Dividir", command=self.btn_dividir_on_click)
        self.btn_dividir.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_sumar_on_click(self):
        op_A = int(self.txt_operador_a.get())
        op_B = int(self.txt_operador_b.get())

        suma_op = op_A + op_B
        sum_conver = str(suma_op)
        resultado_op = "El resultado de la suma es: " + sum_conver

        alert("Ejercicio", resultado_op)

    def btn_restar_on_click(self):
        op_A = int(self.txt_operador_a.get())
        op_B = int(self.txt_operador_b.get())

        resta_op = op_A - op_B
        res_conver = str(resta_op)
        resultado_op = "El resultado de la resta es: " + res_conver

        alert("Ejercicio", resultado_op)

    def btn_multiplicar_on_click(self):
        op_A = int(self.txt_operador_a.get())
        op_B = int(self.txt_operador_b.get())

        multi_op = op_A * op_B
        mul_conver = str(multi_op)
        resultado_op = "El resultado de la multiplicación es: " + mul_conver

        alert("Ejercicio", resultado_op)

    def btn_dividir_on_click(self):
        op_A = int(self.txt_operador_a.get())
        op_B = int(self.txt_operador_b.get())

        div_op = op_A / op_B
        div_conver = str(div_op)
        resultado_op = "El resultado de la división es: " + div_conver

        alert("Ejercicio", resultado_op)
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()