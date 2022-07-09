from tkinter import *
from math import *
import sys

fonte1=('Verdana','10')

class App:
	def __init__(self,x):
		
		x.title("Aplication")#window title
		x.geometry("400x400")#window size
		
		#frame for space below top
		self.frame1 = Frame(x,pady=10)
		self.frame1.pack()
		#box for input
		self.frame2 = Frame(x,pady=10)
		self.frame2.pack()
		#calculate button
		self.frame3 = Frame(x,pady=10)
		self.frame3.pack()
		#frame with message to user
		self.frame4 = Frame(x,pady=10)
		self.frame4.pack()
		#frame which shows the answer
		self.frame5 = Frame(x,pady=10)
		self.frame5.pack()
		#exit and clean buttons
		self.frame6 = Frame(x,pady=10)
		self.frame6.pack()
		
		#set space below top
		Label(self.frame1,text=' ',fg='black',font=fonte1,height=1).pack()
		        		
		#input entry
		Label(self.frame2,text='n :', font=fonte1,width=5).pack(side=LEFT)
		self.valor1=Entry(self.frame2,width=5,font=fonte1)
		self.valor1.focus_force()
		self.valor1.pack(side=LEFT)
		
		#caling the calculate function
		calculate=Button(self.frame3,font=fonte1, text='Calculate',command=self.calculate)
		calculate.pack(side=LEFT)
		
		#message to the user
		Label(self.frame4,text='Probability of among n persons \n at least 2 have the same \n birthday =',font=fonte1,width=75).pack(side=LEFT)
		self.msg=Label(self.frame5,width=10,font=fonte1)
		self.msg.pack(side=LEFT)
		
		#calling the limpar e sair functions
		limpar=Button(self.frame6, font=fonte1, text= 'Clean', command=self.limpar)
		limpar.pack(side=LEFT)
		sair=Button(self.frame6, font=fonte1, text= 'Exit', command=self.sair)
		sair.pack(side=LEFT)
		
		
	def calculate(self):
		'''
		this function calculates the probability p, of none person have 
		the same birthday and then return the the desire probability
		1-p
		'''
		valor1 = self.valor1.get()
		i=int(valor1)
		p=1.0
		for j in range(i):
			p*=(365-j)/365
		self.msg['text']= '%f' %(1-p)
		
	def limpar(self):
		self.valor1.delete('0 ', END)
		self.msg.delete('0 ', END)
		
	def sair(self):
		app.destroy()


app = Tk()
App(app)
app.mainloop()
