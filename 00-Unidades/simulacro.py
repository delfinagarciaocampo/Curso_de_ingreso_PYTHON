import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Simulacro Turno Tarde
Nombre: Delfina García Ocampo

Un gimnasio quiere medir el progreso de sus clientes, para ello se debe ingresar:

Nombre
Edad (debe ser mayor a 12)
Altura (no debe ser negativa)
Días que asiste a la semana (1, 3, 5)
Kilos que levanta en peso muerto (no debe ser cero, ni negativo)

No sabemos cuántos clientes serán consultados.
Se debe informar al usuario:
    # 1) El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.
    # 2) El porcentaje de clientes que asiste solo 1 día a la semana.
    # 3) Nombre y edad del cliente con más altura.
    # 4) Determinar si los clientes eligen más ir 1, 3 o 5 días
    # 5)Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        seguir = True
        bandera_altura = True
        bandera_edad = True

        cont_dia_tres = 0
        acum_kilos = 0

        cont_dia_uno = 0
        cont_dia_cinco = 0

        while seguir:
            # Ingreso datos
            nombre = prompt("Nombre", "Ingrese el nombre")

            edad = int(prompt("Edad", "Ingrese la edad"))
            while edad < 12:
                edad = int(prompt("Error", "Reingrese la edad"))

            altura = int(prompt("Altura", "Ingrese su altura (en cm)"))
            while altura < 0:
                altura = int(prompt("Error", "Reingrese la altura"))

            dias_asistidos = int(prompt("Días asistidos", "Ingrese los días que asiste a la semana"))
            while dias_asistidos != 1 and dias_asistidos != 3 and dias_asistidos != 5:
                dias_asistidos = int(prompt("Error", "Reingrese los días"))

            kilos = int(prompt("Kilos", "Ingrese los kilos que levanta en peso muerto"))
            while kilos < 1:
                kilos = int(prompt("Error", "Reingresar"))

            #Punto 1 (Promedio kilos que levantan las personas 3d/sem)
            match dias_asistidos:
                case 1:
                    #Punto 2 (Porcentaje que asiste 1 dia x sem)
                    cont_dia_uno += 1
                case 3:
                    cont_dia_tres += 1
                    acum_kilos = acum_kilos + kilos
                case 5:
                    cont_dia_cinco += 1
                    #Punto 5 (Nombre y kilos de la persona más joven)
                    if bandera_edad == True:
                        menor_edad = edad
                        menor_e_kilos = kilos
                        bandera_edad = False
                    else:
                        if menor_edad > edad:
                            menor_edad = edad
                            menor_e_kilos = kilos

            #Punto 3 (Nombre y edad del cliente con más altura)
            if bandera_altura == True:
                mayor_altura = altura
                mayor_a_nombre = nombre
                mayor_a_edad = edad
                bandera_altura = False
            else:
                if mayor_altura < altura:
                    mayor_altura = altura
                    mayor_a_nombre = nombre
                    mayor_a_edad = edad

            seguir = question("Continuar", "¿Seguir ingresando?")

        #P1
        if cont_dia_tres == 0:
            promedio_kilos = 0
        else:
            promedio_kilos = acum_kilos / cont_dia_tres

        #P2
        total_clientes = cont_dia_uno + cont_dia_tres + cont_dia_cinco
        promedio_dia_uno = cont_dia_uno * 100 / total_clientes
        promedio_dia_uno = int(promedio_dia_uno)

        #P4
        if cont_dia_uno > cont_dia_tres and cont_dia_uno > cont_dia_cinco:
            mensaje = "Los clientes prefieren ir 1 día"

        if cont_dia_tres > cont_dia_uno and cont_dia_tres > cont_dia_cinco:
            mensaje = "Los clientes prefieren ir 3 días"
        
        if cont_dia_cinco > cont_dia_uno and cont_dia_cinco > cont_dia_tres:
            mensaje = "Los clientes prefieren ir 5 días"

        print(f"1. Las personas que van 3 veces por semana levantan un promedio de: {promedio_kilos}")
        print(f"2. Un {promedio_dia_uno}% asiste 1 vez por semana")
        print(f"3. El cliente más alto es:\n\tNombre: {mayor_a_nombre}\n\tEdad: {mayor_a_edad}")
        print(mensaje)
        print(f"5. De quienes van 5 veces por semana, el más joven tiene {menor_edad} años y levanta {menor_e_kilos} kg en peso muerto")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()