from cgitb import html
from tkinter import *
from npr import NotacaoPolonesaReversa
root = Tk()
root.title("calculador")

font_utilizada = "Helvetica 44 bold"

input = Entry(root, font=font_utilizada, width=30)
input.grid(row=0,column=0, columnspan=4, padx=20, pady=20)

def adiciona_equacao(elemento):
    equacao = input.get()
    input.delete(0, END)
    equacao = input.insert(0, equacao +elemento)

def apagar():
    input.delete(0, END)

def resultado():
    equacao_normal = input.get()
    p = NotacaoPolonesaReversa()
    equacao_npr = p.converte_para_npr(equacao_normal)
    print(equacao_npr)
    resultado = p.resolve_npr(equacao_npr)
    print(resultado)
    input.delete(0, END)
    input.insert(0, resultado)


# Botoes

botao_7 = Button(root, font=font_utilizada, padx=100, pady=20,
                text="7", command=lambda: adiciona_equacao("7"))
botao_8 = Button(root, font=font_utilizada, padx=100, pady=20,
                text="8", command=lambda: adiciona_equacao("8"))
botao_9 = Button(root, font=font_utilizada, padx=100, pady=20,
                text="9", command=lambda: adiciona_equacao("9"))

                
botao_4 = Button(root, font=font_utilizada, padx=100, pady=20,
                text="4", command=lambda: adiciona_equacao("4"))
botao_5 = Button(root, font=font_utilizada, padx=100, pady=20,
                text="5", command=lambda: adiciona_equacao("5"))
botao_6 = Button(root, font=font_utilizada, padx=100, pady=20,
                text="6", command=lambda: adiciona_equacao("6"))


botao_1 = Button(root, font=font_utilizada, padx=100, pady=20,
                text="1", command=lambda: adiciona_equacao("1"))
botao_2 = Button(root, font=font_utilizada, padx=100, pady=20,
                text="2", command=lambda: adiciona_equacao("2"))
botao_3 = Button(root, font=font_utilizada, padx=100, pady=20,
                text="3", command=lambda: adiciona_equacao("3"))
botao_0 = Button(root, font=font_utilizada, padx=100, pady=20,
                text="0", command=lambda: adiciona_equacao("0"))
botao_ponto = Button(root, font=font_utilizada, padx=100, pady=20,
                text=".", command=lambda: adiciona_equacao("."))



botao_soma = Button(root, font=font_utilizada, padx=100, pady=20,
                text="+", command=lambda: adiciona_equacao("+"))
botao_sub = Button(root, font=font_utilizada, padx=100, pady=20,
                text="-", command=lambda: adiciona_equacao("-"))
botao_multi = Button(root, font=font_utilizada, padx=100, pady=20,
                text="*", command=lambda: adiciona_equacao("*"))
botao_div = Button(root, font=font_utilizada, padx=100, pady=20,
                text="/", command=lambda: adiciona_equacao("/"))
botao_pot = Button(root, font=font_utilizada, padx=100, pady=20,
                text="^", command=lambda: adiciona_equacao("^"))
botao_apagar = Button(root, font=font_utilizada, padx=19, pady=20,
                text="apagar", command=apagar)
botao_resultado = Button(root, font=font_utilizada, padx=19, pady=20,
                text="resultado", command=resultado)


# Adiciona os botoes na grid
botao_7.grid(row=1, column=0)
botao_8.grid(row=1, column=1)
botao_9.grid(row=1, column=2)

botao_4.grid(row=2, column=0)
botao_5.grid(row=2, column=1)
botao_6.grid(row=2, column=2)

botao_1.grid(row=3, column=0)
botao_2.grid(row=3, column=1)
botao_3.grid(row=3, column=2)

botao_0.grid(row=4, column=0)
botao_ponto.grid(row=4, column=1)
botao_apagar.grid(row=4, column=2)
botao_resultado.grid(row=5, column=0, columnspan=2)

botao_soma.grid(row=1, column=3)
botao_sub.grid(row=2, column=3)
botao_multi.grid(row=3, column=3)
botao_div.grid(row=4, column=3)
botao_pot.grid(row=5, column=3)




root.mainloop()