from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
import sqlite3 

def mesaj(titx, msj):
    msg = messagebox.showinfo(titx, msj)

try:
    conn = sqlite3.connect("E:\Project\WebSite\GelecekMaker\VeritabanıEğitimleri\Library5.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (Id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, \
    adi TEXT, email TEXT, role TEXT)")
    conn.commit()
    conn.close()
    print("Connection is success..")
except Exception as e:
    print("Error :", e)

def kaydet():
    try:
        conn = sqlite3.connect("E:\Project\WebSite\GelecekMaker\VeritabanıEğitimleri\Library5.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO users (adi, email, role) VALUES ('%s', '%s', '%s')" \
                   %(EntryAdi.get(), EntryMail.get(), EntryRol.get() ))
        conn.commit()
        conn.close()
        msg = mesaj("Information", "Record was success")
        # msg = messagebox.showinfo("Information", "Kayıt işlemi başarılı-Record is success")
        # print("Kayıt işlemi başarı ile yapıldı.- Record is success..")
    except Exception as x:
        msg = mesaj("Hata", "Kaydet bölümü hatası")
    
def listele_print():
    try:
        conn = sqlite3.connect("E:\Project\WebSite\GelecekMaker\VeritabanıEğitimleri\Library5.db")
        cur = conn.cursor()
        resultx = cur.execute("SELECT * FROM users")
        for i in resultx:
            print(i)         
        msg = mesaj("Bilgi", "Print işlemi başarı ile yapıldı")
    except Exception as e:
        msg = mesaj("Hata", "Print işlemi yapılamadı")

# EKRAN TASARIMI
form = Tk() # Pencereyi tanımladık.
form.geometry('800x600') #Pencere boyutunu tanımladık.

LabelAdi = Label(form, text="Adı Soyadı")
LabelAdi.place(x=10, y=10 )
EntryAdi = Entry(form, bd= 1)
EntryAdi.place(x= 100, y=10, width=200)

LabelId = Label(form, text="Id No:")
LabelId.place(x=320, y=10)
EntryId = Entry(form, bd=1)
EntryId.place(x=370, y=10, width=40)


LabelMail = Label(form, text="E-Mail")
LabelMail.place(x=10, y=40)
EntryMail=Entry(form, bd = 1)
EntryMail.place(x=100, y=40, width=250)

LabelRol = Label(form, text="Rolü")
LabelRol.place(x=10, y = 70)
EntryRol = ttk.Combobox(form)
EntryRol['values'] = ('Admin', 'User', 'Student', 'Guest', 'Superuser')
EntryRol.place(x=100, y=70)

Kaydet = Button(form, text='KAYDET', command = kaydet)
Kaydet.place(x= 50, y = 110)

ListelePrint = Button(form, text="Print Listele", command = listele_print)
ListelePrint.place(x = 120, y = 110)

liste = ttk.Treeview(form)
liste["columns"] = ("Sut1", "Sut2", "Sut3")
liste.place(x=0, y=140)

form.mainloop()
