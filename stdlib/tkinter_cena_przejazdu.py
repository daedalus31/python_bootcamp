import tkinter
from tkinter import messagebox


def policz_cene():
    cena = float(dystans.get()) * float(spalanie.get()) * float(
        cena_paliwa.get()) * 0.01
    tkinter.messagebox.showinfo(title='Do zapłaty', message=f'{cena} PLN')


root = tkinter.Tk()
root.title('Hello world!')
dystans_label = tkinter.Label(master=root, text='Dystans: ')
spalanie_label = tkinter.Label(master=root, text='Spalanie: ')
cena_paliwa_label = tkinter.Label(master=root, text='Cena paliwa: ')

dystans = tkinter.Entry(master=root)
spalanie = tkinter.Entry(master=root)
cena_paliwa = tkinter.Entry(master=root)

dystans_label.pack()
dystans.pack()
spalanie_label.pack()
spalanie.pack()
cena_paliwa_label.pack()
cena_paliwa.pack()
button = tkinter.Button(master=root, text="policz", command=policz_cene)
button.pack()
root.mainloop()
