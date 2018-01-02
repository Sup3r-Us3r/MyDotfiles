#!/usr/bin/env python3.5
#coding: utf-8

from tkinter import *

def Run():


	def Autenticador():
		guardar_user = open("login.txt", "w")
		guardar_user.write(ed1.get())
		guardar_pass = open("senha.txt", "w")
		guardar_pass.write(ed2.get())
		janela.quit()

	janela = Tk()
	Label(janela, text="Autenticação", width=80, height=2, bg="#161616", fg="green").pack()
	janela.title("SpyQuiz")

	lb1 = Label(janela, text="LOGIN: ", font="Helvetica 13 bold")
	lb2 = Label(janela, text="SENHA: ", font="Helvetica 13 bold")

	ed1 = Entry(janela, bg="#161616", fg="green")
	ed2 = Entry(janela, bg="#161616", fg="green", show="|")

	bt1 = Button(janela, text="Confirmar", bg="#161616", fg="green", command=Autenticador)

	lb1.place(x=10, y=53, height=30)
	lb2.place(x=10, y=93, height=30)

	ed1.place(x=85, y=49, height=30)
	ed2.place(x=85, y=90, height=30)

	bt1.place(x=100, y=150)

	janela.geometry("300x200")
	janela.mainloop()

Run()