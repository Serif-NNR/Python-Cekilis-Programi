##
##  Çekiliş-LAP - Çekiliş Programı
##
##  Copyright (C) 2017 - Şerif İnanır
##
##  Çekiliş-LAP is free software: you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by the
## Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## Çekiliş-LAP is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
## See the GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License along
## with this program.  If not, see <http://www.gnu.org/licenses/>.
#####################################################################################




#   PROGRAM AÇIKLAMASI
#
#   Elinizdeki her satırda bir ismin bulunduğu
#   .txt uzantılı dosyayı açar ve içerisinden
#   rasgele bir satır (isim) seçer.



#-*- coding: utf-8 -*-
from tkinter import*
from tkinter import font
import random
from tkinter import filedialog

# GENEL ARAYÜZ FONKSİYONLARI
pnc=Tk()
pnc.title("Çekiliş | LapRooz")
pnc.geometry("600x315+330+150")
pnc.resizable(False,False)
slinder1=PhotoImage(file="çekiliş.png")
slinder=Label(image=slinder1,cursor="hand2")
slinder.place(x=-2,y=-2)


# DOSYAYI AÇAR VE İÇERİSİNDEN RASGELE KİŞİ SEÇER
def dosyaİşlem():
    opn=open(uzantı["text"])
    opn_lines=opn.readlines()
    liste=[]
    for satır in opn_lines:
        liste.append(satır)
    kazanan_kişi=random.choice(liste)
    opn.close()
    kazanan["text"]=kazanan_kişi

# DOSYAYI KULLANICININ SEÇMESİNİ SAĞLAR
def dosyaSec():
    dsy=filedialog.askopenfilename()
    uzantı["text"]=dsy
    seç=Button(text="Kazanan Belirle",height=4,bg="black",fg="red",font="Forte",cursor="hand2",command=dosyaİşlem)
    seç.place(x=5,y=195)


kişi=Label(text="Yarışmacı İsim Listesinin Bulunduğu Dosya: ")
kişi.place(x=5,y=130)

uzantı=Label(text="Dosya Seçilmedi")
uzantı.place(x=75,y=162)

dosya=Button(text="Dosya Seç",cursor="hand2",command=dosyaSec,bg="black",fg="white")
dosya.place(x=5,y=160)

açık=Label(text="Kazanan:",font="Algerian",fg="red")
açık.place(x=140,y=220)

kazanan=Label(text="Henüz Belirlenmedi")
kazanan.place(x=240,y=221)


author=Label(text="Kişi listesi içerisinden rasgele bir isim seçer. Program .txt dosyalarında sorunsuz çalışmaktadır.\nYazan: AlavereVintage")
author.place(x=50,y=280)

mainloop()
