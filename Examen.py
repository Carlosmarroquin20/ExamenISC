
#Importando el TK inter
from tkinter import ttk
from tkinter import *
import math
import datetime
class Desk:
    def __init__(self, window,):
#Ventana del programa
        ancho1 = 400
        altura1 = 200
        self.wind = window
        self.wind.geometry(str(ancho1)+'x'+str(altura1))
        #TITULO
        self.wind.columnconfigure(0, weight=1)
        self.wind.title('EXAMEN ISC')
        #ENTRADA
        frame = LabelFrame(self.wind, text = 'Bienvenido!!! rellene lo que se le solicita')
        frame.grid(row = 0, column = 2, columnspan = 20, pady = 20)
        #NOMBRE DEL USUARIO
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.p1 = Entry(frame)
        self.p1.focus()
        self.p1.grid(row = 1, columnspan = 6)
        #APELLIDO DEL USUARIO
        Label(frame, text = 'Apellido.: ').grid(row = 2, column = 0)
        self.op2 = Entry(frame)
        self.op2.grid(row = 2, columnspan = 6)
        #Day
        Label(frame, text = 'Día: ').grid(row = 3, column = 0)
        self.pp3 = Entry(frame)
        self.pp3.grid(row = 3, columnspan = 6)
        #month
        Label(frame, text = 'Mes: ').grid(row = 4, column = 0)
        self.pes4 = Entry(frame)
        self.pes4.grid(row = 4, columnspan = 6)
        #year
        Label(frame, text = 'Año: ').grid(row = 5, column = 0)
        self.pap5 = Entry(frame)
        self.pap5.grid(row = 5, columnspan = 6)
        #Colocacion de botones y posicion
        Button(frame, text = 'Función 1', command = self.funcion1).grid(row = 6, column = 0 , sticky = W + E)
        Button(frame, text = 'Función 2', command = self.funcion2).grid(row = 6, column = 1 , sticky = W + E)
        Button(frame, text = 'Función 3', command = self.funcion3).grid(row = 6, column = 2 , sticky = W + E)
        Button(frame, text = 'Función 4', command = self.funcion4).grid(row = 6, column = 3 , sticky = W + E)
        Button(frame, text = 'Función 5', command = self.funcion5).grid(row = 6, column = 4 , sticky = W + E)
        #Resutado:
        self.message = Label(text = '', fg = 'Black')
        self.message.grid(row = 3, column = 1, columnspan = 2, sticky = W + E)

    #1. Letras a numeros Hexadecimales
    def funcion1(self):
        day=int(self.pp3.get())
        month=int(self.pes4.get())
        year=int(self.pap5.get())
        hexadecimalday=format(day, 'x')
        hexadecimalmonth=format(month, 'x')
        hexadecimalyear=format(year, 'x')
        self.message['text'] = '{}/{}/{}, Convertido a hexadecimal es: {}/{}/{}'.format(day,month,year,hexadecimalday,hexadecimalmonth,hexadecimalyear)
    #2. HOras
    def funcion2(self):   
        day=int(self.pp3.get())
        month=int(self.pes4.get())
        year=int(self.pap5.get())
        fecha_de_nacimiento = datetime.datetime(year, month, day)
        fecha_de_hoy = datetime.datetime.now()
        dias_vividos = fecha_de_hoy - fecha_de_nacimiento
        horas = dias_vividos * 24
        hv = horas.days
        self.message['text'] = 'Usted nacio el: {}/{}/{},su total de horas vividas es {}'.format(day,month,year,hv)   
    #3. Par o impar
    def funcion3(self):
        name=str(self.p1.get())
        last=str(self.op2.get())
        nr_nombre=int(len(name))
        nr_apellido=int(len(last))
        if nr_nombre%2==0 and nr_apellido %2==0 :
            self.message['text'] = '{} {}, Su Nombre es par y Su Apellido es par'.format(name,last)
        elif nr_nombre%2==0 and nr_apellido %2==1:
            self.message['text'] = '{} {}, Su nombre es par y tu Apellido es impar'.format(name,last)
        elif nr_nombre%2==1 and nr_apellido %2==0:
            self.message['text'] = '{} {}, Su nombre es impar y tu Apellido es par'.format(name,last)
        else:
            self.message['text'] = '{} {}, Su nombre es impar y tu Apellido es impar'.format(name,last)   
    #4. Vocales, consonantes
    def funcion4(self):
        nr=str(self.p1.get())
        apd=str(self.op2.get())
        cuenta = 0
        for carac in nr:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
        for carac in apd:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
        cud=len(nr)
        cudd=len(apd)
        consonante=cud+cudd-cuenta
        self.message['text'] = 'Su nombre y apellido tienen {} vocales y {} consonantes'.format(cuenta,consonante)
        #5.inverso
    def funcion5(self):
        em=str(self.p1.get())
        nu=str(self.op2.get())
        cadena_invertida = ""
        cadena_invertida1= ""
        for letra in em:
            cadena_invertida = letra + cadena_invertida
        for letra1 in nu:
            cadena_invertida1 = letra1 + cadena_invertida1
        self.message['text'] = '{} {}, al reves es: {} {}'.format(em,nu,cadena_invertida,cadena_invertida1)
if __name__ == '__main__':
    window = Tk()
    app = Desk(window)
    window.mainloop()