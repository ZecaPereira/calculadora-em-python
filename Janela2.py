from tkinter import *
root = Tk()
root.title("Calculadora do Zeca")
root.geometry("340x380")
root.configure(background="black")

#DISPLAY:
display = Label(root, width=10, font=("Arial", 24), bd=5, bg="black", fg="white", justify='right')
display.grid(row=0, column=1, columnspan=4, padx=5, pady=5)

#LISTA GLOBAL PRA CONTA:
memoria = []

#FUNÇÕES DOS BOTÕES:
'ALOCANDO NUMEROS NO DISPLAY E NA MEMORIA'
def adicionar_numero(numero):
    global memoria
    memoria.append(numero)
    display.config(text=memoria)
    return memoria, display

'APAGANDO TUDO DO DISPLAY E DA MEMORIA'
def apagar_tudo():
    global memoria
    memoria = []
    display.config(text="")
    return memoria, display

'APAGANDO O ÚLTIMO NÚMERO DO DISPLAY E DA MEMORIA'
def apagar_ultimo():
    global memoria
    if memoria:
        memoria.pop()
        display.config(text=memoria)
    return memoria, display

'FAZENDO A CONTA E MOSTRANDO O RESULTADO NO DISPLAY' #tem que corrigir essa função depois:
def calcular_resultado():
    global memoria
    expressao = ''.join(memoria)
    try:
        resultado = str(eval(expressao))
        display.config(text=resultado)
        memoria = [resultado]
    except:
        pass
    return memoria, display

#BOTÕES:
'''mano pq eu to usando um dicionário????
to com preguiça de corrigir o dicionário pra uma lista com tuplas, vai ficar assim mesmo kkkk
To com preguiça de criar uma classe pra os botões, então vai ficar assim mesmo kkkk'''

'BOTÃO DE NÚMEROS E OPERAÇÕES'
botoes = {
    '7': (1, 1, "7"), '8': (1, 2, "8"), '9': (1, 3, "9"), '/': (1, 4, "/"),
    '4': (2, 1, "4"), '5': (2, 2, "5"), '6': (2, 3, "6"), '*': (2, 4, "*"),
    '1': (3, 1, "1"), '2': (3, 2, "2"), '3': (3, 3, "3"), '-': (3, 4, "-"),
    '0': (4, 1, "0"), '.': (4, 2, "."), '=': (4, 3, "="), '+': (4, 4, "+"),
}
for texto, (linha, coluna, valor) in botoes.items():
    botao = Button(root, text=texto, width=10, height=3, bg="white", fg="black")
    botao.grid(row=linha, column=coluna, padx=2, pady=2)
    botao.config(command=lambda v=valor: adicionar_numero(v))

'DELETAR'
botao = Button(root, text="Del", width=10, height=3, bg="white", fg="black")
botao.grid(row=4, column=4, padx=2, pady=2)
botao.config(command=apagar_ultimo)

'AC'
botao = Button(root, text="AC", width=22, height=3, bg="white", fg="black")
botao.grid(row=5, column=3,columnspan = 2,  padx=2, pady=2)
botao.config(command=apagar_tudo)

'RESULTADO'

root.mainloop()