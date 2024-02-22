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
        bandera = True
        contador = 0
        acum_edad = 0

        while True:
            nom = prompt("Nombre", "Ingrese el nombre del candidato")
            edad = int(prompt("Edad", "Ingrese la edad del candidato"))

            if edad < 25:
                edad = int(prompt("Error", "La edad no puede ser menor a 25. Ingrese la edad nuevamente"))
            
            votos = int(prompt("Votos", "Ingrese la cantidad de votos"))

            if votos < 0:
                votos = int(prompt("Error", "La cantidad de votos no puede ser un número negativo. Ingrese nuevamente"))
            
            candidato = "{0}, {1} años, {2} votos".format(nom, edad, votos)

            if bandera == True:
                mayor_votos = votos
                menor_votos = votos
                bandera = False
            else:
                if mayor_votos < votos:
                    mayor_votos = votos
                    nom_mayor = nom
                    candidato_mas_votos = "Con {0} cantidad de votos, {1} tiene más votos".format(mayor_votos, nom_mayor)
                if menor_votos > votos:
                    menor_votos = votos
                    nom_menor = nom
                    candidato_menos_votos = "Con {0} cantidad de votos, {1} tiene menos votos".format(menor_votos, nom_menor)
            
            contador += 1
            acum_edad = acum_edad + edad
        


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
