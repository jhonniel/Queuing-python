import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import *
import time



mydb=mysql.connector.connect(host="10.9.14.103",user="python",passwd="python101",database="queing")




main = tk.Tk()
main.title("Queing System")
main.geometry("1000x500+200+150")
main.configure(background="black")

lbl = Label(main, text="", font=("Arial Bold", 10), bg="black", fg="white")
lbl.grid(column=20, row=20)
lbl.place(width="200", height="50", x="40", y="400")

def evtCashier():

    lbl.configure(text="CASHIER Printing ......")
    mycursor=mydb.cursor()

    mycursor.execute(" INSERT INTO queing.cashier(DateIssue, Status) VALUES (NOW(), 1)" )
    mydb.commit()
    lbl.configure(text="DONE Printing ......")


cashier = Button(main, text="CASHIER", font=("Arial Bold", 40), bg="#26D744", fg="white", command=evtCashier)
cashier.place(width="250", height="100", x="20", y="30")


def evtSAO():
    lbl.configure(text="SAO Printing ......")
    mycursor = mydb.cursor()

    mycursor.execute(" INSERT INTO queing.sao(DateIssue, Status) VALUES (NOW(), 1)")
    mydb.commit()
    lbl.configure(text="DONE Printing ......")

sao = Button(main, text="SAO", font=("Arial Bold", 50), bg="#D8D805", fg="white", command=evtSAO)
sao.place(width="250", height="100", x="20", y="300")

main.mainloop()