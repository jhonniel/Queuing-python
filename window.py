from tkinter import *
import tkinter
import mysql.connector
from mysql.connector.constants import ClientFlag
import random

config = {
    'user': 'python',
    'password': 'python101',
    'host': '10.9.14.103',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': '/opt/mysql/ssl/ca.pem',
    'ssl_cert': '/opt/mysql/ssl/client-cert.pem',
    'ssl_key': '/opt/mysql/ssl/client-key.pem',
}

cnx = mysql.connector.connect(**config)
#name =["OFFLINE","NOW SERVING # 3","NOW SERVING # 2","NOW SERVING # 1"

def evtwin():
     mycursor = mydb.cursor()

     mycursor.execute(" UPDATE queing.cashier SET Status = 2 WHERE Status=1 LIMIT 1")
     mydb.commit()

     mycursor.execute("select No from cashier WHERE status = 2 LIMIT 1 ")

     for i in mycursor:
          Label.configure(text=i)




kui = tkinter.Tk()

kui.title("QUE SYSTEM")
kui.geometry("450x100")
kui.configure(bg='gray')


Label = tkinter.Label(kui, text="ONLINE",bg='black',fg='pink', font=('Italic', 20))
Label.pack(padx=50, pady=5)
Grid()

pickButton1 = tkinter.Button(text="NEXT",command=evtwin,bg='pink',fg='black',font=('Italic', 20))
pickButton1.pack()
pickButton1.place(bordermode=OUTSIDE,height=100, width= 95)


kui.mainloop()