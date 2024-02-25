import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Se nos ha solicitado desarrollar una aplicación para llevar registro de las entradas vendidas en el Estadio River 
Plate, para el concierto de Taylor Swift. Para ello, se solicitará al usuario la siguiente información al momento de 
comprar cada entrada:

Al presionar el voton se debera pedir la carga de los siguientes datos, hasta que el usuario lo desee:

Los datos que deberas pedir para los ventas son:
    * Nombre del comprador
    * Edad (no menor a 16)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Platea)
    * Medio de pago (Crédito, Efectivo, Débito) 
    * Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente.

 * Lista de precios: 
        * General: $16000
        * Campo:   $25000
        * Platea:  $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 

Al finalizar la carga, el programa debera mostrar los siguientes informes:

    #! 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    #! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
    #!          de crédito y su edad promedio.
    #! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y 
    #!          pagaron con tarjeta de débito  respecto al total de personas en la lista.
    #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de 
    #!          los aplicados a tarjetas de crédito
    #! 5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de 
    #!          tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
    #! 6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya 
    #!          edad es un número primo.
    #! 7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
    #!          pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        seguir = True
        precio_alto_bandera = False

        descuento = 0

        precio = 0

        cont_masc_campo = 0
        cont_fem_campo = 0
        cont_otro_campo = 0

        general_credito = 0
        general_credito_cont_edad = 0
        general_credito_acum_edad = 0

        cont_total_personas = 0
        cont_platea_credito = 0

        acum_descuento_credito = 0

        precio_alto = 0

        edad_primo = 0

        acum_total_platea = 0

        while seguir:
            #Ingreso de datos
            nombre = prompt("Nombre", "Ingrese el nombre")

            edad = int(prompt("Edad", "Ingrese la edad"))
            while edad < 16 or edad == None:
                edad = int(prompt("Error", "Edad no válida, reingresar"))

            genero = prompt("Género", "Ingrese género")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("Error", "Reingresar")

            tipo_entrada = prompt("Tipo de entrada", "Ingrese el tipo de entrada")
            while tipo_entrada != "General" and tipo_entrada != "Campo" and tipo_entrada != "Platea":
                tipo_entrada = prompt("Error", "Entrada no válida, reingresar")
            
            pago = prompt("Medio de pago", "Ingrese el medio de pago")
            while pago != "Crédito" and pago != "Efectivo" and pago != "Débito":
                pago = prompt("Error", "Medio de pago no válido, elija otro")

            #Descuentos
            match pago:
                case "Crédito":
                    descuento = 0.2
                    #Punto 4 (Total de descuento en pesos)
                    descuento_credito = precio * descuento
                    acum_descuento_credito = acum_descuento_credito + descuento_credito
                case "Débito":
                    descuento = 0.15
                case "Efectivo":
                    descuento = 0

            match tipo_entrada:
                case "General":
                    precio = 16000
                    #Punto 2 (Determinar cuántos pagaron con crédito y edad promedio)
                    if pago == "Crédito":
                        general_credito += 1
                        general_credito_cont_edad += 1
                        general_credito_acum_edad = general_credito_acum_edad + edad
                    #Punto 5 (Nombre y edad de la persona que pagó el precio más alto)
                    while precio_alto_bandera == True:
                        if pago == "Débito":
                            if precio_alto == 0:
                                precio_alto = precio_total
                                precio_alto_edad = edad
                                precio_alto_nombre = nombre
                            else:
                                if precio_alto > precio_total:
                                    precio_alto_edad = edad
                                    precio_alto_nombre = nombre
                                    precio_alto_bandera = False
                case "Campo":
                    precio = 25000
                    #Punto 1 (Género más frecuente)
                    match genero:
                        case "Masculino":
                            cont_masc_campo += 1
                        case "Femenino":
                            cont_fem_campo += 1
                        case "Otro":
                            cont_otro_campo += 1
                case "Platea":
                    precio = 30000
                    #Punto 3 (Calcular porcentaje que compró platea con tarjeta de débito)
                    if pago == "Crédito":
                        cont_platea_credito += 1
                    #Punto 6 (Cantidad de personas con edad numero primo)
                    for i in range(2, edad):
                        if edad % i != 0:
                            edad_primo += 1
                    #Punto 7 (Cantidad de personas con edad multiplo de 6, acumulador de precio)
                    if pago == "Débito":
                        for i in range(6, edad):
                            if edad % 6 == 0:
                                acum_total_platea = acum_total_platea + acum_total_platea

            precio_total = precio - precio * descuento
            precio_total_mssj = "El precio total es de ${0}".format(precio_total)
            alert("Precio final", precio_total_mssj)

            cont_total_personas += 1
            seguir = question("Continuar", "¿Realizar otra operación?")


        #Punto 1
        if cont_masc_campo > cont_fem_campo and cont_masc_campo > cont_otro_campo:
            mensaje = "El género más frecuente de quienes compran 'Campo' es: Masculino"
        if cont_fem_campo > cont_masc_campo and cont_fem_campo > cont_otro_campo:
            mensaje = "El género más frecuente de quienes compran 'Campo' es: Femenino"
        if cont_otro_campo > cont_masc_campo and cont_otro_campo > cont_fem_campo:
            mensaje = "El género más frecuente de quienes compran 'Campo' es: Otro"

        #Punto 2
        promedio_edad_general_credito = general_credito_acum_edad / general_credito_cont_edad

        #Punto 3
        porcentaje_platea_credito = cont_platea_credito * 100 / cont_total_personas

        print(f"1. {mensaje}")
        print(f"2. Un total de {general_credito} personas compraron 'General' con tarjeta de crédito, un promedio en edad de: {promedio_edad_general_credito}")
        print(f"3. El {porcentaje_platea_credito}% que compró 'Platea' pagó con tarjeta de crédito")
        print(f"4. El total de descuentos con tarjeta de crédito en pesos es de ${acum_descuento_credito}")
        print(f"5. Quien pagó el precio más alto por una entrada 'General' con débito fue:\n\tNombre: {precio_alto_nombre}\n\tEdad: {precio_alto_edad}")
        print(f"6. Un total de {edad_primo} personas compraron 'Platea' y su edad es un número primo")
        print(f"7. El monto total recaudado por la venta de entradas de tipo 'Platea' y pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6 es de: {acum_total_platea}")



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()