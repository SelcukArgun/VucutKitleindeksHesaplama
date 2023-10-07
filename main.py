import tkinter
from tkinter import *

#pencere
window = Tk()
window.title("Vücut Kitle İndeks Hesaplama")
window.minsize(width=350, height=250,)

#KG_girişi
kg_text = tkinter.Label(text="Kilonuzun Girin (kg)", font=("Arial", 10, "italic", "bold"))
kg_text.place(x=108, y=25)

#KG_Entry
kg_entry = tkinter.Entry()
kg_entry.place(x=110, y=50)

#BOY_girişi
boy_text = tkinter.Label(text="Boyunuzu Girin (cm)", font=("Arial", 10, "italic", "bold"))
boy_text.place(x=108, y=100)

#BOY_Entry
boy_entry = tkinter.Entry()
boy_entry.place(x=110, y=125)

#Sonuç mesajı
sonuc_label = tkinter.Label(text="", font=("Arial", 10, "bold"))
sonuc_label.place(x=98, y=190)

#buton + işlev
def vki_hesaplama():
    try:
        user_input_kg = float(kg_entry.get())
        user_input_boy = float(boy_entry.get()) / 100
        #endeks = user_input_kg / (user_input_boy * 2 )
        if user_input_boy <= 0 or user_input_kg <= 0 :
            sonuc_label.config(text="Lütfen pozitif bir sayı girin")
        else:
            endeks = user_input_kg / (user_input_boy ** 2 )

            if endeks < 18.5 :
                sonuc = "Zayıfsınız"
            elif endeks >= 18.5 and endeks <= 24.9:
                sonuc = "Normal"

            elif endeks >= 25 and endeks <= 29.9:
               sonuc = "Fazla Kilolu"

            elif endeks >= 30:
                sonuc = "Obezsiniz "

            else:
                sonuc = "Hatalı bir işlem"

            sonuc_label.config(text=f"Vücut Kitle İndeksi: {round(endeks,1)}\n{sonuc}")
    except ValueError :
        sonuc_label.config(text="Lütfen sayısal değer girin!")
        sonuc_label.place(x=90, y=195)

button = Button(text="Hesapla" , command=vki_hesaplama)
button.place(x=144, y=155)


tkinter.mainloop()
