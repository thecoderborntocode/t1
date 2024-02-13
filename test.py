import tkinter as tk
# import tkinter as tk1
import turtle as tu
# root = tk.Tk()
from PIL import ImageTk,Image
import time
import turtle

lock = -1

def disp(clock):
    global lock
    lock = lock+1
    a = ["ram2.jpg","ram10.jpg","ram11.jpg","lord-rama-wallpapers-high-resolution.jpg","ram4.jpg","ram5.jpg","ram7.jpg","ram8.jpg","ram10.jpg", "ram14.jpg", "ram15.jpg"]
    OSCILLATE = tk.Tk()


    def dest():                                                                #BOLO SRI SIYAVAR RAMCHANDRA KI JAI
        OSCILLATE.destroy()                                                    #SRI AYODYAPATI RAMCHANDRA KI JAI
                                                                               # SRI SIYARAM KI JAI
    button = tk.Button(OSCILLATE,command=dest)                                 #SRI RADHARAMANA KI JAI
    img = Image.open(a[lock])                                                 #SRI SITARAMANA KI JAI
    imgr = ImageTk.PhotoImage(img)                                             #JAI JAI SRI RAM
    label = tk.Label(OSCILLATE,image=imgr)
    label.pack()
    OSCILLATE.after(clock,button.invoke)
    OSCILLATE.mainloop()
for i in range(0,11):
    disp(2000)

tu.bgcolor("black")
tu.pencolor("orange")
tu.write("achutam keshavam ",align="center",font=("arial",50,"normal"))
time.sleep(1.5)
tu.clear()
tu.write("ram narayanam",align="center",font=("arial",50,"normal"))
time.sleep(1.7)
tu.clear()
tu.write("krishna damodaram",align="center",font=("arial",50,"normal"))
time.sleep(1.8)
tu.clear()
tu.write("vasudevam hari",align="center",font=("arial",50,"normal"))
time.sleep(1.5)
tu.clear()
tu.write("sridharam madhavam",align="center",font=("arial",50,"normal"))
time.sleep(1.9)
tu.clear()
tu.write("gopika vallabham",align="center",font=("arial",50,"normal"))
time.sleep(1.7)
tu.clear()
tu.write("janaki nayakam",align="center",font=("arial",50,"normal"))
time.sleep(1.8)
tu.clear()
tu.write("ramchandram bhaje",align="center",font=("arial",50,"normal"))
time.sleep(1.8)
tu.clear()



tu.bye()

lock = -1
for i in range(0,11):
    disp(1000)
lock = -1
time.sleep(3)
for i in range(0,11):
    disp(500)
count = -1
def com():
    global count
    root = tk.Tk()
    def dest():
        root.destroy()
    count = count+1
    d = ["JAI","SREE","RAM","ART BY VIJAY"]
    label = tk.Label(root, text=d[count], font=("Arial", 150))
    label.pack()
    button  = tk.Button(root,command=dest)
    root.after(2000,button.invoke)
    root.mainloop()
for i in range(0,4):
    com()
tk.mainloop()
# root.mainloop()




