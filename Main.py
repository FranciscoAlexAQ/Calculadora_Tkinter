# Importando módulo
from tkinter import *

# Criando instância
calculadora = Tk()


# Criando classe
class Calculadora:
    def __init__(self):
        self.configurarJanela()
        self.incrementa()
        self.criarVisor()
        self.criarBotoes()
        calculadora.mainloop()

    # Configurando janela
    def configurarJanela(self):
        calculadora.title('Calculadora')
        self.criarFrames()
        calculadora.geometry('350x500+500+40')
        calculadora.iconbitmap('calculadora.ico')

    # Criando visor
    def criarVisor(self):
        self.entryVisor = Entry(self.topFrame, border=0, bg='#FFA500',
                                font=('Arial', 16), justify=CENTER)
        self.entryVisor.place(relx=0.025, rely=0.1, relwidth=0.94, relheight=0.8)

    # Criando botões
    def criarBotoes(self):
        self.btn1 = Button(self.bottomFrame, text='1', bd=0, font=12,
                           command=lambda: self.inserirValores('1'))
        self.btn1.place(relx=0.03, rely=0.03, relwidth=0.2, relheight=0.15)

        self.btn2 = Button(self.bottomFrame, text='2', bd=0, font=12,
                           command=lambda: self.inserirValores('2'))
        self.btn2.place(relx=0.265, rely=0.03, relwidth=0.2, relheight=0.15)

        self.btn3 = Button(self.bottomFrame, text='3', bd=0,font=12,
                           command=lambda: self.inserirValores('3'))
        self.btn3.place(relx=0.5, rely=0.03, relwidth=0.2, relheight=0.15)

        self.btnCE = Button(self.bottomFrame, text='CE', bd=0, font=12, bg='darkgray',
                            command=lambda: self.limpar())
        self.btnCE.place(relx=0.76, rely=0.03, relwidth=0.2, relheight=0.15)

        self.btn4 = Button(self.bottomFrame, text='4', bd=0, font=12,
                           command=lambda: self.inserirValores('4'))
        self.btn4.place(relx=0.03, rely=0.2, relwidth=0.2, relheight=0.15)

        self.btn5 = Button(self.bottomFrame, text='5', bd=0, font=12,
                           command=lambda: self.inserirValores('5'))
        self.btn5.place(relx=0.265, rely=0.2, relwidth=0.2, relheight=0.15)

        self.btn6 = Button(self.bottomFrame, text='6', bd=0, font=12,
                           command=lambda: self.inserirValores('6'))
        self.btn6.place(relx=0.5, rely=0.2, relwidth=0.2, relheight=0.15)

        self.btnmais = Button(self.bottomFrame, text='+', bd=0, font=12, bg='darkgray',
                              command=lambda: self.inserirValores('+'))
        self.btnmais.place(relx=0.76, rely=0.2, relwidth=0.2, relheight=0.15)

        self.btn7 = Button(self.bottomFrame, text='7', bd=0, font=12,
                           command=lambda: self.inserirValores('7'))
        self.btn7.place(relx=0.03, rely=0.37, relwidth=0.2, relheight=0.15)

        self.btn8 = Button(self.bottomFrame, text='8', bd=0, font=12,
                           command=lambda: self.inserirValores('8'))
        self.btn8.place(relx=0.265, rely=0.37, relwidth=0.2, relheight=0.15)

        self.btn9 = Button(self.bottomFrame, text='9', bd=0, font=12,
                           command=lambda: self.inserirValores('9'))
        self.btn9.place(relx=0.5, rely=0.37, relwidth=0.2, relheight=0.15)

        self.btnmenos = Button(self.bottomFrame, text='-', bd=0, font=12, bg='darkgray',
                               command=lambda: self.inserirValores('-'))
        self.btnmenos.place(relx=0.76, rely=0.37, relwidth=0.2, relheight=0.15)

        self.btnmulti = Button(self.bottomFrame, text='x', bd=0, font=12, bg='darkgray',
                               command=lambda: self.inserirValores('x'))
        self.btnmulti.place(relx=0.03, rely=0.54, relwidth=0.2, relheight=0.15)

        self.btn0 = Button(self.bottomFrame, text='0', bd=0, font=12,
                           command=lambda: self.inserirValores('0'))
        self.btn0.place(relx=0.265, rely=0.54, relwidth=0.2, relheight=0.15)

        self.btndiv = Button(self.bottomFrame, text='/', bd=0, font=12, bg='darkgray',
                             command=lambda: self.inserirValores('/'))
        self.btndiv.place(relx=0.5, rely=0.54, relwidth=0.2, relheight=0.15)

        self.btnponto = Button(self.bottomFrame, text='.', bd=0, font=12, bg='darkgray',
                               command=lambda: self.inserirValores('.'))
        self.btnponto.place(relx=0.76, rely=0.54, relwidth=0.2, relheight=0.15)

        self.btnigual = Button(self.bottomFrame, text='=', bd=0, font=('bold', 12), bg='white',
                               command=lambda: self.calcular())
        self.btnigual.place(relx=0.03, rely=0.7, relwidth=0.93, relheight=0.15)

    # Criando os Frames
    def criarFrames(self):
        self.topFrame = Frame(calculadora, bg='gray')
        self.topFrame.place(relx=0, rely=0, relwidth=1, relheight=0.14)

        self.bottomFrame = Frame(calculadora, bg='#FF4500')
        self.bottomFrame.place(relx=0, rely=0.14, relwidth=1, relheight=1)

    # Variável que incrementa a cada valor inserido
    def incrementa(self):
        self.contador = 0

    # Inserindo valores no visor
    def inserirValores(self, valor):
        self.entryVisor.insert(self.contador, valor)
        self.contador += 1

    # Limpando visor
    def limpar(self):
        self.entryVisor.delete(0, END)

    # Calculando resultado
    def calcular(self):
        calculo = self.entryVisor.get()
        calculo = str(calculo).replace('x', '*')

        self.entryVisor.delete(0, END)

        try:
            self.entryVisor.insert(0, eval(calculo))
        except ZeroDivisionError:
            self.entryVisor.insert(0, 'Não se pode dividir por zero')
        except:
            self.entryVisor.insert(0, 'Houve algum erro')


# Chamando classe
Calculadora()
