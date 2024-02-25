import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la bolsa de 
valores:

Para ello deberás programar el botón  para poder cargar 10 operaciones de compra con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    
Realizar los siguientes informes:
    #! 1) - Tipo de instrumento que menos se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50 y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion del usuario que invirtio menos dinero
    #! 6) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 7) - Promedio de cantidad de instrumentos  MEP vendidos en total

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        seguir = 0

        cont_CEDEAR = 0
        cont_BONOS = 0
        cont_MEP = 0

        cont_usuarios_MEP = 0

        primer_CEDEAR_BONO = False

        menor_inversión = 0

        acumulador_dinero_CEDEAR = 0

        acumulador_MEP = 0

        while seguir < 10:
            #Ingreso de datos
            nombre = prompt("Nombre", "Ingrese el nombre")

            monto = int(prompt("Monto", "Ingrese monto"))
            while monto < 10000:
                monto = int(prompt("Error", "El monto no puede ser menor a $10000, vuelva a ingresar"))

            tipo_instr = prompt("Instrumento", "Igrese tipo de instrumento")
            while tipo_instr != "CEDEAR" and tipo_instr != "BONOS" and tipo_instr != "MEP":
                tipo_instr = prompt("Error", "Instrumento no válido, vuelva a ingresar")

            cant_instr = int(prompt("Cantidad instrumentos", "Ingrese la cantidad de instrumentos"))
            while cant_instr < 0:
                cant_instr = int(prompt("Error", "La cantidad no puede ser menor a cero, reingresar"))

            #Punto 1 (Tipo de instr. que menos se operó)
            match tipo_instr:
                case "CEDEAR":
                    cont_CEDEAR += 1
                    #Punto 6 (Promedio dinero CEDEAR)
                    acumulador_dinero_CEDEAR = acumulador_dinero_CEDEAR + monto
                    #Punto 4
                    if primer_CEDEAR_BONO == False:
                        nombre_CEDEAR_BONO = nombre
                        cantidad_CEDEAR_BONO = cant_instr
                        primer_CEDEAR_BONO = True
                case "BONOS":
                    cont_BONOS += 1
                    #Punto 4 (Nombre y cantidad del primer usuario que compró BONOS / CEDEAR)
                    if primer_CEDEAR_BONO == False:
                        nombre_CEDEAR_BONO = nombre
                        cantidad_CEDEAR_BONO = cant_instr
                        primer_CEDEAR_BONO = True
                case "MEP":
                    cont_MEP += 1
                    #Punto 2 (Cantidad de usuarios que compraron entre 50 y 200 MEP)
                    if cant_instr > 50 and cant_instr < 200:
                        cont_usuarios_MEP += 1
                    #Punto 7 (Promedio cantidad de instrumentos MEP)
                    acumulador_MEP = acumulador_MEP + cant_instr

            #Punto 5 (Persona que menos invirtió)
            if menor_inversión == 0:
                menor_inversión = monto
                menor_inversión_nombre = nombre
                menor_inversión_posicion = tipo_instr
            else:
                if menor_inversión > monto:
                    menor_inversión = monto
                    menor_inversión_nombre = nombre
                    menor_inversión_posicion = tipo_instr

            seguir += 1

        #Punto 1
        if cont_CEDEAR < cont_BONOS and cont_CEDEAR < cont_MEP:
            mensaje = "CEDEAR fue el instrumento menos operado"
        
        if cont_BONOS < cont_CEDEAR and cont_BONOS < cont_MEP:
            mensaje = "BONOS fue el instrumento menos operado"
        
        if cont_MEP < cont_CEDEAR and cont_MEP < cont_BONOS:
            mensaje = "MEP fue el instrumento menos operado"
        
        # if (cont_CEDEAR == cont_BONOS) < cont_MEP or (cont_CEDEAR == cont_MEP) < cont_BONOS or (cont_BONOS == cont_MEP) < cont_CEDEAR or cont_MEP == cont_BONOS == cont_CEDEAR:
        #     mensaje = " "

        #Punto 3
        no_compraron_CEDEAR = cont_BONOS + cont_MEP

        #Punto 6
        if cont_CEDEAR == 0:
            promedio_dinero_CEDEAR = 0
        else:
            promedio_dinero_CEDEAR = acumulador_dinero_CEDEAR / cont_CEDEAR

        #Punto 7
        promedio_MEP = acumulador_MEP / cont_MEP

        print(f"1. {mensaje}")
        print(f"2. {cont_usuarios_MEP} usuarios compraron entre 50 y 200 MEP")
        print(f"3. {no_compraron_CEDEAR} usuarios no compraron CEDEAR")
        print(f"4. El primer usuario que compró CEDEAR ó BONOS:\n\tNombre: {nombre_CEDEAR_BONO}\n\tCantidad: {cantidad_CEDEAR_BONO}")
        print(f"5. La persona que menos invirtió fue:\n\tNombre: {menor_inversión_nombre}\n\tPosición: {menor_inversión_posicion}")
        print(f"6. El promedio de dinero invertido en CEDEAR es de: {promedio_dinero_CEDEAR}")
        print(f"7. El promedio de instrumentos MEP es de: {promedio_MEP}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()