# попытки создать GUI версию чеснока
import tkinter
from tkinter import * 
from PIL import Image, ImageTk
import os
import time 
import subprocess

print("загрузка файлов чеснока...") 
os.system('curl -O https://www.myinstants.com/media/sounds/misha-idi-nakh-i.mp3')
os.system('curl -O https://zvukipro.com/uploads/files/2020-12/1609052060_elevator-music-vanoss-gaming-background-music.mp3') 
os.system('mv 1609052060_elevator-music-vanoss-gaming-background-music.mp3 waiting.mp3')  
print("готово") 
root=Tk() 
root.geometry('520x500')

img = ImageTk.PhotoImage(Image.open("chesnok.png"))
panel = Label(root, image = img) 
panel.pack(side = "bottom", fill = "both", expand = "yes") 

a = Label(root, text="скачать чеснок") 

a.pack() 
def op3n():
    os.system('mpv music.mp3 &') 
    while True:
        time.sleep(0.5) 
        os.system('feh -F chesnoeb.png &') 

def ska4at(): 
    print("закачка чеснока...") 
    subprocess.Popen( 
                     ['mpv', 'waiting.mp3'],
                     stdout=subprocess.DEVNULL,
                     stderr=subprocess.DEVNULL,
)
    os.system('curl -O https://i.imgur.com/zWphWZ6.png') 
    os.system('mv zWphWZ6.png chesnoeb.png') 
    os.system('curl -O https://ia601209.us.archive.org/1/items/OMFGHello_20150908/OMFG%20-%20Hello.mp3') 
    os.system('mv OMFG%20-%20Hello.mp3 music.mp3') 
    os.system('killall mpv') 
 
    a.destroy()
    B.destroy()
    panel.destroy() 
    B2.destroy()
    B3.destroy()

    text = Label(root, text="чеснок был успешно скачан!")
    text.pack() 
    ending = Button(root, text ="открыть чеснок", command=op3n)
    ending.pack() 

B = Button(root, text ="скачать чеснтного чеснака", command=ska4at) 
B.place(x=50,y=50)

def misha(): 
    os.system('mpv misha-idi-nakh-i.mp3 &')
    time.sleep(18) 
    os.system('killall mpv') 
    root.destroy() 

B2 = Button(root, text="нахуй", command=misha) 
B2.place(x=300, y=50) 

B3 = Button(root, text="выйти", command=root.destroy)
B3.place(x=425, y=50) 

root.mainloop()
