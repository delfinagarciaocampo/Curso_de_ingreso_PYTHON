import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Delfina
apellido: García Ocampo
---
TP: Iluminación
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
        cantidad = int(self.combobox_cantidad.get())
        marca = self.combobox_marca.get()
        precio = 800
        descuento = 0

        #Forma 1 (if marca, match cantidad)
        # if marca == "ArgentinaLuz":

        #     match cantidad:
        #         case 6 | 7 | 8 | 9 | 10 | 11 | 12:
        #             descuento = 0.5
        #         case 5:
        #             descuento = 0.4
        #         case 4:
        #             descuento = 0.25
        #         case 3:
        #             descuento = 0.15
        #         case _:
        #             descuento = 0
        # elif marca == "FelipeLamparas":

        #     match cantidad:
        #         case 6 | 7 | 8 | 9 | 10 | 11 | 12:
        #             descuento = 0.5
        #         case 5:
        #             descuento = 0.3
        #         case 4:
        #             descuento = 0.25
        #         case 3:
        #             descuento = 0.1
        #         case _:
        #             descuento = 0
        # else:
        #     match cantidad:
        #         case 6 | 7 | 8 | 9 | 10 | 11 | 12:
        #             descuento = 0.5
        #         case 5:
        #             descuento = 0.3
        #         case 4:
        #             descuento = 0.2
        #         case 3:
        #             descuento = 0.05
        #         case _:
        #             descuento = 0

        #Forma 2 (if cantidad, match marca)
        # if cantidad > 5:

        #     match marca:
        #         case _:
        #             descuento = 0.5
        
        # elif cantidad == 5:

        #     match marca:
        #         case "ArgentinaLuz":
        #             descuento = 0.4
        #         case _:
        #             descuento = 0.3
        
        # elif cantidad == 4:

        #     match marca:
        #         case "ArgentinaLuz" | "FelipeLamparas":
        #             descuento = 0.25
        #         case _:
        #             descuento = 0.2
        
        # elif cantidad == 3:

        #     match marca:
        #         case "ArgentinaLuz":
        #             descuento = 0.15
        #         case "FelipeLamparas":
        #             descuento = 0.1
        #         case _:
        #             descuento = 0.05
        
        # else:
        #   descuento = 0

        #Forma 3 (match marca, match cantidad)
        match marca:
            
            case "ArgentinaLuz":
                match cantidad:
                    case 6 | 7 | 8 | 9 | 10 | 11 | 12:
                        descuento = 0.5
                    case 5:
                        descuento = 0.4
                    case 4:
                        descuento = 0.25
                    case 3:
                        descuento = 0.15
                    case _:
                        descuento = 0
            
            case "FelipeLamparas":
                match cantidad:
                    case 6 | 7 | 8 | 9 | 10 | 11 | 12:
                        descuento = 0.5
                    case 5:
                        descuento = 0.3
                    case 4:
                        descuento = 0.25
                    case 3:
                        descuento = 0.1
                    case _:
                        descuento = 0
            
            case _:
                match cantidad:
                    case 6 | 7 | 8 | 9 | 10 | 11 | 12:
                        descuento = 0.5
                    case 5:
                        descuento = 0.3
                    case 4:
                        descuento = 0.2
                    case 3:
                        descuento = 0.05
                    case _:
                        descuento = 0

        precio_total = precio * cantidad - ((precio * cantidad) * descuento)
        if precio_total > 4000:
            precio_total = precio_total - precio_total * 0.05
        print(precio_total)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()