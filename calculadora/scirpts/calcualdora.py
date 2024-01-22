import random
from tkinter import *
from tkinter import Tk
import time
import os
import requests
#===========================================================================================================
#cores

cnz = "#424242"
cnz2 = "#141313"
pret = "#3b3b3b"
branc = "#feffff"
azul = "#38576b"
cinz = "#ECEFF1"
larng = '#FFAB40'







#===========================================================================================================
def calculadoraPROG():
    while True:
        try:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            operador = input("Digite o operador: ")

            if operador in ('+', '-', '', '/'):
                resultado = eval(f"{n1} {operador} {n2}")
                if operador == '/' and n2 == 0:
                    raise ZeroDivisionError("Erro: Divisão por zero não é permitida.")
                print(f"O resultado da operação é: {resultado}")
            else:
                raise ValueError("Operador inválido. Por favor, use '+', '-', '' ou '/'.")

            continuar = input("Deseja fazer outra operação? (S/N): ").lower()
            if continuar != 's':
                break

        except Exception as e:
            print(f"Erro: {e}. Por favor, tente novamente.")


def calcular():
    expressao = app_label.cget("text")
    resultado = eval(expressao)
    app_label.config(text=str(resultado))


def adicionar_caracter(caracter):
    expressao_atual = app_label.cget("text")
    app_label.config(text=expressao_atual + str(caracter))


def limpar_tela():
    app_label.config(text="")


#===========================================================================================================
#Tk
calculadora = Tk()
calculadora.title("Calculadora")
li = 350
ai = 552
calculadora.geometry(f"{li}x{ai}")
calculadora.config(bg=branc)
#===========================================================================================================
#frames
frame_tela = Frame(calculadora,width= 350, height= 130, bg= pret)
frame_tela.grid(column= 0, row= 0)


frame_corpo = Frame(calculadora,width= 350, height= 450, bg= pret)
frame_corpo.grid(column= 0, row= 1)


#===========================================================================================================
#label
app_label = Label(frame_tela, width=7, height=5, padx=7, relief=FLAT,justify=LEFT,font="Ivy 30 bold",bg=pret,fg=branc)
app_label.place(x=170,y=-15)


#===========================================================================================================
#botoes
b_clear = Button(frame_corpo,text= "C", width= 20, height= 5, bg= cinz, font=("Ivy 9 bold"),relief=RAISED,overrelief= RIDGE, command=limpar_tela)
b_clear.place(x=0,y=0)

b_porcentage = Button(frame_corpo,text= "%", width= 15, height= 5, bg= cinz, font=("Ivy 9"),relief=RAISED,overrelief= RIDGE,command=lambda: adicionar_caracter("%"))
b_porcentage.place(x=143,y=0)

b_division = Button(frame_corpo,text= "/", width= 12, height= 5,bg= larng, font=("Ivy 9 bold"), fg= branc,relief=RAISED,overrelief= RIDGE,command=lambda: adicionar_caracter('/'))
b_division.place(x=256,y=0)



b_7 = Button(frame_corpo,text= "7", width= 11, height= 5, bg= cinz, font=("Ivy 9 bold"),relief=RAISED,overrelief= RIDGE, command=lambda: adicionar_caracter(7))
b_7.place(x=0,y=85)

b_8 = Button(frame_corpo,text= "8", width= 11, height= 5, bg= cinz, font=("Ivy 9 bold"),relief=RAISED,overrelief= RIDGE, command=lambda: adicionar_caracter(8))
b_8.place(x=86,y=85)

b_9 = Button(frame_corpo,text= "9", width= 11, height= 5, bg= cinz, font=("Ivy 9 bold"),relief=RAISED,overrelief= RIDGE, command=lambda: adicionar_caracter(9))
b_9.place(x=172,y=85)

b_multiplicacao = Button(frame_corpo,text= "X", width= 12, height= 5,bg= larng, font=("Ivy 9 bold"), fg= branc,relief=RAISED,overrelief= RIDGE, command=lambda: adicionar_caracter("*"))
b_multiplicacao.place(x=256,y=85)


#coluna 3
b_4 = Button(frame_corpo,text= "4", width= 11, height= 5, bg= cinz, font=("Ivy 9 bold"),relief=RAISED,overrelief= RIDGE, command=lambda: adicionar_caracter(4))
b_4.place(x=0,y=170)

b_5 = Button(frame_corpo,text= "5", width= 11, height= 5, bg= cinz, font=("Ivy 9 bold"),relief=RAISED,overrelief= RIDGE, command=lambda: adicionar_caracter(5))
b_5.place(x=86,y=170)

b_6 = Button(frame_corpo,text= "6", width= 11, height= 5, bg= cinz, font=("Ivy 9 bold"),relief=RAISED,overrelief= RIDGE, command=lambda: adicionar_caracter(6))
b_6.place(x=172,y=170)

b_multiplicacao = Button(frame_corpo,text= " - ", width= 12, height= 5,bg= larng, font=("Ivy 9 bold"), fg= branc,relief=RAISED,overrelief= RIDGE, command=lambda: adicionar_caracter("-"))
b_multiplicacao.place(x=256,y=170)


#coluna 3
b_1 = Button(frame_corpo,text= "1", width= 11, height= 5, bg= cinz, font=("Ivy 9 bold"),relief=RAISED,overrelief= RIDGE, command=lambda: adicionar_caracter(1))
b_1.place(x=0,y=255)

b_2 = Button(frame_corpo,text= "2", width= 11, height= 5, bg= cinz, font=("Ivy 9 bold"),relief=RAISED,overrelief= RIDGE, command=lambda: adicionar_caracter(2))
b_2.place(x=86,y=255)

b_3 = Button(frame_corpo,text= "3", width= 11, height= 5, bg= cinz, font=("Ivy 9 bold"),relief=RAISED,overrelief= RIDGE, command=lambda: adicionar_caracter(3))
b_3.place(x=172,y=255)

b_multiplicacao = Button(frame_corpo,text= " + ", width= 12, height= 5,bg= larng, font=("Ivy 9 bold"), fg= branc,relief=RAISED,overrelief= RIDGE, command=lambda: adicionar_caracter("+"))
b_multiplicacao.place(x=256,y=255)


#coluna 4
b_0 = Button(frame_corpo,text= "0", width= 20, height= 5, bg= cinz, font=("Ivy 9 bold"),relief=RAISED,overrelief= RIDGE,command=lambda: adicionar_caracter(0))
b_0.place(x=0,y=340)

b_dot = Button(frame_corpo,text= ".", width= 15, height= 5, bg= cinz, font=("Ivy 9 bold"),relief=RAISED,overrelief= RIDGE,command=lambda: adicionar_caracter("."))
b_dot.place(x=143,y=340)

b_division = Button(frame_corpo,text= "=", width= 12, height= 5,bg= larng, font=("Ivy 9 bold"), fg= branc,relief=RAISED,overrelief= RIDGE, command=calcular)
b_division.place(x=256,y=340)


#===========================================================================================================

def fechar_programa():
    calculadora.destroy()

b_sair=Button(frame_tela,text= "SAIR",fg=branc, bg= pret,font=("Ivy 10"),command= fechar_programa )
b_sair.place(x=0,y=0)


#===========================================================================================================
calculadora.mainloop()





