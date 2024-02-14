import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Delfina
apellido: García Ocampo
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        marca = self.combobox_marca.get()
        cantidad = int(self.combobox_cantidad.get())
        precio = 800

        if cantidad > 5:
            precio = precio * cantidad
            precio_descuento = precio - (precio * 0.5)
            mensaje = 'Tiene un descuento del 50%. Su importe final es de:', precio_descuento

            alert("Alert", mensaje)

            if precio_descuento > 4000:
                precio_descuento = precio_descuento - (precio_descuento * 0.05)
                mensaje = 'Tiene un descuento adicional del 5%. Su importe final es de:', precio_descuento

                alert("Descuento adicional", mensaje)
        elif cantidad == 5:
            if marca == "ArgentinaLuz":
                precio = precio * 5
                precio_descuento = precio - (precio * 0.4)
                mensaje = 'Tiene un descuento del 40%. Su importe final es de:', precio_descuento

                alert("Alert", mensaje)
            else:
                precio = precio * 5
                precio_descuento = precio - (precio * 0.3)
                mensaje = 'Tiene un descuento del 30%. Su importe final es de:', precio_descuento

                alert("Alert", mensaje)
        elif cantidad == 4:
            if marca == "ArgentinaLuz" or marca == "FelipeLamparas":
                precio = precio * 4
                precio_descuento = precio - (precio * 0.25)
                mensaje = 'Tiene un descuento del 25%. Su importe final es de:', precio_descuento

                alert("Alert", mensaje)
            else:
                precio = precio * 4
                precio_descuento = precio - (precio * 0.2)
                mensaje = 'Tiene un descuento del 20%. Su importe final es de:', precio_descuento

                alert("Alert", mensaje)
        elif cantidad == 3:
            if marca == "ArgentinaLuz":
                precio = precio * 3
                precio_descuento = precio - (precio * 0.15)
                mensaje = 'Tiene un descuento del 15%. Su importe final es de:', precio_descuento

                alert("Alert", mensaje)
            elif marca == "FelipeLamparas":
                precio = precio * 3
                precio_descuento = precio - (precio * 0.1)
                mensaje = 'Tiene un descuento del 10%. Su importe final es de:', precio_descuento

                alert("Alert", mensaje)
            else:
                precio = precio * 3
                precio_descuento = precio - (precio * 0.05)
                mensaje = 'Tiene un descuento del 5%. Su importe final es de:', precio_descuento

                alert("Alert", mensaje)
        else:
            precio = precio * cantidad
            mensaje = 'Su importe final es de:', precio

            alert("Alert", mensaje)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()