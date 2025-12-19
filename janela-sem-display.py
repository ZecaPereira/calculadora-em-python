from tkinter import *
Root = Tk()
Root.title("Calculadora do Zeca")
Root.geometry("240x228")
Root.configure(background="black")

#BUTTONS
'Numeros de 1 a 9'
for i in range(1, 10):
    'Isso foi otimizado usando matemática de linha e coluna, só deus sabe como eu pensei nisso'
    Button(Root, text=str(i), width=10, height=3, bg="white", fg="black").grid(row=(i-1)//3, column=(i-1)%3)
'Zero e 9'
Button(Root, text="0", width=10, height=3, bg="white", fg="black").grid(row=3, column=0)
Button(Root, text="=", width=21, height=3, bg="white", fg="black").grid(row=3, column=1,columnspan=2)

#FUNÇÕS DOS BOTÕES
def clicar():
    pass

Root.mainloop()