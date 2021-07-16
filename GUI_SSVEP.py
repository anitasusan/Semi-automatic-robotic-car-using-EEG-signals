import tkinter as tk
from tkinter import LEFT, RIGHT, TOP, BOTTOM,RAISED,CENTER

class MainGUI():
    def __init__(self, master):
        self.master = master
        self.backgroundColor = "pink"
        master.title("A simple GUI.")

        self.leftbutton = tk.Button(master, text="LEFT", width=10, height=10,relief=RAISED,background="black", foreground="white")
        self.leftbutton.pack(side=LEFT)
  
        self.rightbutton = tk.Button(master, text="RIGHT", width=10, height=10,relief=RAISED, background="black", foreground="white")
        self.rightbutton.pack(side=RIGHT)

        
        self.topbutton = tk.Button(master, text="TOP", width=10, height=10,relief=RAISED, background="black", foreground="white")
        self.topbutton.pack(side=TOP,padx=10)

        self.bottombutton = tk.Button(master, text="BOTTOM", width=10, height=10,relief=RAISED, background="black", foreground="white")
        self.bottombutton.pack(side=BOTTOM)

        self.stopbutton = tk.Button(master, text="STOP", width=10, height=10,relief=RAISED, background="black", foreground="white")
        self.stopbutton.pack(pady=100,side=BOTTOM)

        self.frame = tk.Frame(master, width=300, height=700)
        self.frame.bind('<KeyRelease>',self.keyPressed)
        self.frame.pack()
        self.frame.focus()
        self.flash_left()
        self.flash_right()
        self.flash_front()
        self.flash_back()
        self.flash_stop()

    def flash_left(self):
        leftbg = self.leftbutton.cget("background")
        leftfg = self.leftbutton.cget("foreground")
        self.leftbutton.configure(background=leftfg, foreground=leftbg)
        self.leftbutton.after(100, self.flash_left) #10 Hz
    def flash_right(self):
        rightbg = self.rightbutton.cget("background")
        rightfg = self.rightbutton.cget("foreground")
        self.rightbutton.configure(background=rightfg, foreground=rightbg)
        self.rightbutton.after(62, self.flash_right) #16 Hz
    def flash_front(self):
        topbg = self.topbutton.cget("background")
        topfg = self.topbutton.cget("foreground")
        self.topbutton.configure(background=topfg, foreground=topbg)
        self.topbutton.after(125, self.flash_front) #8 Hz
    def flash_back(self):
        bottombg = self.bottombutton.cget("background")
        bottomfg = self.bottombutton.cget("foreground")
        self.bottombutton.configure(background=bottomfg, foreground=bottombg)
        self.bottombutton.after(83, self.flash_back) #12 Hz
    def flash_stop(self):
        stopbg = self.stopbutton.cget("background")
        stopfg = self.stopbutton.cget("foreground")
        self.stopbutton.configure(background=stopfg, foreground=stopbg)
        self.stopbutton.after(72, self.flash_stop) # 14 Hz
        
    def keyPressed(self, event):
        sendDatatoArduino(event.char)
        return
    
def sendDatatoArduino(var):
    import serial
    ser= serial.Serial('COM3',9600,timeout=2)
    if var == "a" or  var == "A":
        ser.write(bytes("L",'utf-8'))  
    elif var == "s" or  var == "S":
        ser.write(bytes("B",'utf-8'))  
    elif var == "d" or var == "D":
        ser.write(bytes("R",'utf-8')) 
    elif var == "w" or var == "W":
        ser.write(bytes("F",'utf-8')) 
    elif var == "x" or  var == "X":
        ser.write(bytes("S",'utf-8')) 
        



root = tk.Tk()
gui = MainGUI(root)
root.mainloop()
