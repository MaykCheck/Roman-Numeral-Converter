from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import *

window = Tk()
window.title("Roman Numeral Converter")
window.config(padx=50, pady=75)

RomanNumeralMap = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
    }

SayıDeğeri = 0

def Dönüştür():
    sayı = SayıGirişi.get()
    if sayı == "":
        SonuçBaşlığı.config(text="Lütfen bir sayı giriniz!")
    elif sayı not in RomanNumeralMap:
        SonuçBaşlığı.config(text="Lütfen bir uygun bir sayı giriniz!")
    else:
        SonuçBaşlığı.config(text=f"Sonuç: {RomanNumeralMap[sayı]}")

def ToplamalıDönüştürme():
    sayı = SayıGirişi.get()
    if sayı == "":
        SonuçBaşlığı.config(text="Lütfen bir sayı giriniz!")
    else:
        try:
            for i in range(len(sayı)):
                if sayı[i] in RomanNumeralMap:
                    if i+1 < len(sayı) and RomanNumeralMap[sayı[i]] < RomanNumeralMap[sayı[i + 1]]:
                        SayıDeğeri -= RomanNumeralMap[sayı[i]]
                    else:
                        SayıDeğeri += RomanNumeralMap[sayı[i]]
            SonuçBaşlığı.config(text=f"{sayı}")
        except:
            SonuçBaşlığı.config(text="Lütfen uygun bir sayı giriniz!")



SayıGirişiBaşlığı = Label(text="Lütfen Sayınızı Giriniz.")
SayıGirişiBaşlığı.pack()

SayıGirişi = Entry()
SayıGirişi.pack()

HesaplaButonu = Button(text="Hesapla", command=ToplamalıDönüştürme)
HesaplaButonu.pack()

SonuçBaşlığı = Label()
SonuçBaşlığı.pack()


window.mainloop()