import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Delfina
apellido: García Ocampo
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        seguir = True

        bandera = True

        acumulador_edad = 0
        contador_edad = 0

        acumulador_votos = 0

        while seguir:
            #Ingreso de datos // Conf dato correcto
            nombre = prompt("Nombre", "Ingrese el nombre")

            edad = int(prompt("Edad", "Ingrese la edad"))
            while edad < 25:
                edad = int(prompt("Error", "No puede ser menor de 25, reingrese la edad"))
            #Punto 3 -> Promedio de edades
            acumulador_edad = acumulador_edad + edad
            contador_edad += 1

            votos = int(prompt("Votos","Ingrese cantidad de votos"))
            while votos < 0:
                votos = prompt("Error", "Lacantidad no puede ser negativa, reingresar")
                votos = int(votos)
            #Punto 4 -> total votos
            acumulador_votos = acumulador_votos + votos
            mensaje_total_votos = "El total de votos emitidos es {0}".format(acumulador_votos)

            #Punto 1 -> Nombre del candidato con más votos // Punto 2 -> Nombre y edad del menos votado
            if bandera == True:
                mas_votos = votos
                candidato_mas_votos = nombre
                menos_votos = votos
                candidato_menos_votos = nombre
                edad_menos_votos = edad
                bandera = False
            else:
                if votos > mas_votos:
                    mas_votos = votos
                    candidato_mas_votos = nombre
                if votos < menos_votos:
                    menos_votos = votos
                    candidato_menos_votos = nombre
                    edad_menos_votos = edad
            
            mensaje_c_mas_votos = "El candidato más votado es " + candidato_mas_votos
            mensaje_c_menos_votos = "El candidato menos votado es {0} con {1} años de edad".format(candidato_menos_votos, edad_menos_votos) #, candidato_menos_votos, "con", edad_menos_votos , "años de edad"

            seguir = question("Continuar", "¿Continuar ingresando?")
        
        #P3
        promedio = acumulador_edad / contador_edad
        mensaje_promedio = "El promedio de edad es {0}".format(promedio)

        #Mensajes
        #P1
        alert("Punto 1", mensaje_c_mas_votos)
        #P2
        alert("Punto 2", mensaje_c_menos_votos)
        #P3
        alert("Punto 3", mensaje_promedio)
        #P4
        alert("Punto 4", mensaje_total_votos)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()