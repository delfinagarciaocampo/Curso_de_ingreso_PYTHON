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

        bandera = True

        contador_masc_IOT_IA = 0

        contador_IOT = 0
        contador_RV_RA = 0
        contador_IA = 0

        contador_masc = 0
        contador_fem = 0
        contador_otro = 0

        votaron_IOT_edad = 0

        cont_fem_edad = 0
        acum_fem_edad = 0

        while seguir:
            #Ingreso de datos
            nombre = prompt("Nombre", "Ingrese el nombre")

            edad = int(prompt("Edad", "Ingrese la edad"))
            while edad < 18:
                edad = int(prompt("Error", "No puede ser menor a 18, reingrese la edad"))

            genero = prompt("Género", "Ingrese el género")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("Error", "Reingrese el género")

            tecno = prompt("Tecnología", "Ingrese la tecnología")
            while tecno != "IA" and tecno != "RV/RA" and tecno != "IOT":
                tecno = prompt("Error", "Tecnología no válida, reingresar")

            #Punto 1 (Cantidad de masc que votaron por IOT o IA entre 25/50 años) // Punto 3 (Porcentaje de empleados por cada género)
            match genero:
                case "Masculino":
                    if (tecno == "IOT" or tecno == "IA") and 25 <= edad and edad <= 50:
                        contador_masc_IOT_IA += 1
                    contador_masc += 1
                case "Femenino":
                    contador_fem += 1
                    #Punto 5 (Prom de edad femenino que votó por IA)
                    if tecno == "IA":
                        cont_fem_edad += 1
                        acum_fem_edad = acum_fem_edad + edad
                case "Otro":
                    contador_otro += 1

            #Punto 2 (Tecnología más votada)
            match tecno:
                case "IOT":
                    contador_IOT += 1
                    #Punto 4 (Porcentaje que votó IOT entre 18/25 y 33/42)
                    if (edad >= 18 and edad <= 25) or (edad >= 33 and edad <= 42):
                        votaron_IOT_edad += 1
                case "IA":
                    contador_IA += 1
                case "RV/RA":
                    contador_RV_RA += 1
                    #Punto 6 (Nombre y género del empleado que votó por RV/RA con menor edad)
                    if bandera == True:
                        menor_edad = edad
                        menor_nombre = nombre
                        menor_genero = genero
                        bandera = False
                    else:
                        if menor_edad > edad:
                            menor_edad = edad
                            menor_nombre = nombre
                            menor_genero = genero

            seguir = question("Continuar", "¿Ingresar otro?")
        
        #Punto 2
        if contador_IA > contador_IOT and contador_IA > contador_RV_RA:
            mas_votada = "La tecnología más votada es la IA"
        
        if contador_RV_RA > contador_IOT and contador_RV_RA > contador_IA:
            mas_votada = "La tecnología más votada es la RV/RA"
        
        if contador_IOT > contador_IA and contador_IOT > contador_RV_RA:
            mas_votada = "La tecnología más votada es la IOT"

        #Punto 3
        empleados = contador_masc + contador_fem + contador_otro
        porc_masc = contador_masc * 100 / empleados
        porc_fem = contador_fem * 100/ empleados
        porc_otro = contador_otro * 100 / empleados

        #Punto 4
        porc_IOT_edad = votaron_IOT_edad * 100 / empleados

        #Punto 5
        prom_fem_IA = acum_fem_edad / cont_fem_edad


        #MENSAJES
        '''P1'''
        print(f"La cantidad de empleados masculinos entre 25 y 50 años que votaron por IOT o IA es de: {contador_masc_IOT_IA}")
        '''P2'''
        print(mas_votada)
        '''P3'''
        print(f"Promedio empleados:\n\tMasculino: {porc_masc}%\n\tFemenino: {porc_fem}%\n\tOtro: {porc_otro}%")
        '''P4'''
        print(f"Porcentaje de empleados que votaron por IOT entre 18/25 y 33/42 años: {porc_IOT_edad}%")
        '''P5'''
        print(f"El promedio de edad de los empleados de genero femenino que votaron por IA es de {prom_fem_IA}")
        '''P6'''
        print(f"El empleado más jóven que votó por RV/RA es:\n\tNombre: {menor_nombre}\n\tGénero: {menor_genero}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()