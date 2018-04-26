from tkinter import *
import sqlite3

#janela
root = Tk()
root.title("My favourite journal @ Zotero")
root.resizable(0, 0)

#conexao com o banco de dados
db = sqlite3.connect('zotero.sqlite')
cursor = db.cursor()
cursor.execute('''SELECT * FROM itemData INNER JOIN itemDataValues ON itemData.valueID=itemDataValues.valueID WHERE fieldID=12 ORDER BY value''' )

#variaveis basicas
all_rows = cursor.fetchall()
n=0
t=0

#label com o total
lab1 = Label(root, text = str(len(all_rows)) + " papers considered.", height=2)
lab1.pack()

#elemento lista pra mostrar os resultados
mylist = Listbox(root)
mylist.config(width=100, height=20)

#percorrendo os resultados e contando repeticoes
while n<len(all_rows):
    title = all_rows[n][4]
    i=0
    while (n+1+i)<len(all_rows) and title.upper() == all_rows[n+1+i][4].upper():
        i=i+1
    mylist.insert(END, str(i+1) + " - " + title)
    n=n+1+i
    t=t+1

#label com total de journals diferentes
lab2 = Label(root, text = str(t) + " different journals identified.", height=2)
lab2.pack()

#exibir lista
mylist.pack(side = LEFT)
#barra de rolagem
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
scrollbar.config( command = mylist.yview )
mylist.config(yscrollcommand=scrollbar.set)

#finalizando
db.close()
root.mainloop()
