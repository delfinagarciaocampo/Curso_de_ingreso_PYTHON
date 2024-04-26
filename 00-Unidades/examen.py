import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Fecha: 01/03/2024
Nombre: Delfina
Apellido: García Ocampo
División: TT-E
DNI: 47203284

De los 50 participantes del torneo de UTN-TETRIS, se debe ingresar los siguientes datos:
· Nombre
· Categoría (Principiante - Intermedio - Avanzado)
· Edad (entre 18 y 99 inclusive)
· Score (mayor que 0)
· Nivel alcanzado (1 , 2 o 3)

Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál es la categoría que tiene menos participantes.
Informe B- El Porcentaje de jugadores de la categoría intermedios sobre el total
Informe C- La categoría del participante de mayor Score
Informe D- El score y nombre del intermedios con menor score
Informe E- Promedio de score de los participantes avanzados.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        bandera_mayor_score = True
        bandera_inter_menor_score = True

        participantes = 0

        cont_principiante = 0
        cont_intermedio = 0
        cont_avanzado = 0

        acum_score_avanzado = 0

        while participantes < 50:
            #Ingreso datos
            nombre = prompt("Nombre", "Ingrese el nombre")

            categoria = prompt("Categoría", "Ingrese la categoría")
            while categoria != "Principiante" and categoria != "Intermedio" and categoria != "Avanzado":
                categoria = prompt("Error", "Reingrese categoría")

            edad = int(prompt("Edad", "Ingrese la edad"))
            while edad < 18 or edad > 99:
                edad = prompt("Error", "Reingrese la edad")
                edad = int(edad)

            score = int(prompt("Score", "Ingrese puntaje"))
            while score <= 0:
                score = int(prompt("Error", "Reingrese el puntaje"))

            nivel_alcanzado = int(prompt("Nivel", "Ingrese el nivel alcanzado"))
            while nivel_alcanzado != 1 and nivel_alcanzado != 2 and nivel_alcanzado != 3:
                nivel_alcanzado = prompt("Error", "Reingrese nivel")

            # Informe A- Cuál es la categoría que tiene menos participantes.
            match categoria:
                case "Principiante":
                    cont_principiante += 1
                case "Intermedio":
                    cont_intermedio += 1
                    # Informe D- El score y nombre del intermedios con menor score
                    if bandera_inter_menor_score == True:
                        inter_menor_score = score
                        nombre_inter_menor_score = nombre
                        bandera_inter_menor_score = False
                    else:
                        if inter_menor_score > score:
                            inter_menor_score = score
                            nombre_inter_menor_score = nombre
                case "Avanzado":
                    cont_avanzado += 1
                    # Informe E- Promedio de score de los participantes avanzados.
                    acum_score_avanzado = acum_score_avanzado + score

            # Informe C- La categoría del participante de mayor Score
            if bandera_mayor_score == True:
                categoria_mayor_score = categoria
                mayor_score = score
                bandera_mayor_score == False
            else:
                if mayor_score < score:
                    categoria_mayor_score = categoria
                    mayor_score = score

            participantes += 1

        #Inf A
        if cont_principiante < cont_intermedio and cont_principiante < cont_avanzado:
            mensaje = "A) La categoría Principiante tiene menos participantes"

        if cont_intermedio < cont_principiante and cont_intermedio < cont_avanzado:
            mensaje = "A) La categoría Intermedio tiene menos participantes"
        
        if cont_avanzado < cont_principiante and cont_avanzado < cont_intermedio:
            mensaje = "A) La categoría Avanzado tiene menos participantes"

        # Informe B- El Porcentaje de jugadores de la categoría intermedios sobre el total
        porcentaje_intermedio = cont_intermedio * 100 / participantes

        # Inf E
        promedio_score_avanzado = acum_score_avanzado / cont_avanzado

        #Mensajes
        print(mensaje)
        print(f"B) El porcentaje de jugadores intermedios es de {porcentaje_intermedio}%")
        print(f"C) La categoría del participante con mayor score es: {categoria_mayor_score}")
        print(f"D) El Intermedio con menor score es {nombre_inter_menor_score} con un puntaje de {inter_menor_score}")
        print(f"E) El promedio de score de los participantes Avanzados es de: {promedio_score_avanzado}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()