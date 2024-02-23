import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT)  

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #! 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #! 2) - Tecnología que mas se votó.
    #! 3) - Porcentaje de empleados por cada genero
    #! 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #! 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #! 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        seguir = True
        contador_masculino_IOT_IA: 0
        contador_IOT = 0
        contador_IA = 0
        contador_RV_RA = 0

        contador_masc = 0
        contador_fem = 0
        contador_otro = 0

        contador_IOT_edad = 0
        
        contador_fem_IA = 0
        acumulador_edad_fem_IA = 0

        minimo_edad = 0

        while seguir:
            # Ingreso de datos
            nombre = prompt("", "Ingrese nombre")

            edad = prompt("", "Ingrese edad")
            edad = int(edad)
            while edad < 18:
                edad = prompt("", "No puede ser menor a 18, reingrese edad")
                edad = int(edad)
            
            genero = prompt("", "Ingrese género")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("", "Reingrese el género")
            
            tecnologia = prompt("", "Ingrese tecnología")
            while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
                tecnologia = prompt("", "Reingrese tecnología")

            # Procesamiento de datos
            if genero == "Masculino" and (tecnologia == "IA" or tecnologia == "IOT") and 25 <= edad and edad <= 50:
                contador_masculino_IOT_IA += 1

            if tecnologia == "IOT":
                contador_IOT += 1
                #P. 4
                if (edad > 18 and edad < 25) or (edad > 33 and edad < 42):
                    contador_IOT_edad += 1
            elif tecnologia == "IA":
                contador_IA += 1
            else:
                contador_RV_RA += 1
                #P. 6
                if edad < minimo_edad or contador_RV_RA == 1:
                    minimo_edad = edad
                    nombre_minimo = nombre
                    genero_minimo = genero
            '''También se puede hacer con un match'''

            match genero:
                case "Masculino":
                    contador_masc += 1
                    
                case "Femenino":
                    contador_fem += 1
                    if tecnologia == "IA":
                        contador_fem_IA += 1
                        acumulador_edad_fem_IA = acumulador_edad_fem_IA + edad
                case "Otro":
                    contador_otro += 1

            seguir = question("Seguir",  "¿Ingresar otro empleado?")

        print(f"1. Cantidad masculinos que votaron IOT/IA en el rango de edad: {contador_masculino_IOT_IA}")

        if contador_IOT > contador_IA and contador_IOT > contador_RV_RA:
            print("2. IOT fue el más votado")
        elif contador_IA > contador_IOT and contador_IA > contador_RV_RA:
            print("2. IA fue el más votado")
        else:
            print("2. RV/RA fue el más votado")

        total_empleados = contador_otro + contador_fem + contador_masc
        
        porcentaje_fem = contador_fem * 100 / total_empleados
        porcentaje_masc = contador_masc * 100 / total_empleados
        porcentaje_otro = contador_otro * 100 / total_empleados
        print(f"3. Porcentaje:\n\tMasculino: {porcentaje_masc}%\n\tFemenino: {porcentaje_fem}\n\tOtro: {porcentaje_otro}")

        porcentaje_IOT_edad = (contador_IOT_edad * 100) / total_empleados
        print(f"4. Porcentaje de empleados que votaron por IOT por edad: {porcentaje_IOT_edad}%")

        if contador_fem_IA > 0:
            promedio_edad_femenino_IA = acumulador_edad_fem_IA / contador_fem_IA
        else:
            promedio_edad_femenino_IA = "No se ingresaron femeninos que votaron IA"
        print(f"5. Promedio de edad: {promedio_edad_femenino_IA}")

        print(f"6. {minimo_edad}{nombre_minimo}{genero_minimo}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()