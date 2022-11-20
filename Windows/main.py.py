import tempfile
import os
import tkinter as tk
import tkinter.font as tkFont
import re

class App:
    def __init__(self, root):
        self.count = 0
        #setting title
        root.title("Lick_it")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # global GButton_135
        GButton_135=tk.Button(root)
        GButton_135["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=9)
        GButton_135["font"] = ft
        GButton_135["fg"] = "#000000"
        GButton_135["justify"] = "center"
        GButton_135["text"] = "LOOK_SLAVE"
        GButton_135.place(x=480,y=20,width=83,height=35)
        GButton_135["command"] = self.GButton_135_command

        self.GLabel_16=tk.Label(root,justify="center",padx=10,pady=10)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_16["font"] = ft
        self.GLabel_16["fg"] = "#333333"
        self.GLabel_16["justify"] = "center"
        self.GLabel_16["text"] = "Lick_it"
        # self.GLabel_16.justify = LEFT
        self.GLabel_16.place(x=10,y=30,width=410,height=428)

        GButton_61=tk.Button(root)
        GButton_61["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=8)
        GButton_61["font"] = ft
        GButton_61["fg"] = "#000000"
        GButton_61["justify"] = "center"
        GButton_61["text"] = "WAKE SLAVE"
        GButton_61.place(x=480,y=100,width=83,height=36)
        GButton_61["command"] = self.GButton_61_command

        GButton_62=tk.Button(root)
        GButton_62["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_62["font"] = ft
        GButton_62["fg"] = "#000000"
        GButton_62["justify"] = "center"
        GButton_62["text"] = "VOL_UP"
        GButton_62.place(x=480,y=200,width=81,height=38)
        GButton_62["command"] = self.GButton_62_command

        GButton_833=tk.Button(root)
        GButton_833["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_833["font"] = ft
        GButton_833["fg"] = "#000000"
        GButton_833["justify"] = "center"
        GButton_833["text"] = "Enter"
        GButton_833.place(x=470,y=420,width=81,height=34)
        GButton_833["command"] = self.GButton_833_command

        GButton_15=tk.Button(root)
        GButton_15["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=9)
        GButton_15["font"] = ft
        GButton_15["fg"] = "#000000"
        GButton_15["justify"] = "center"
        GButton_15["text"] = "SLAVE_SLEEP"
        GButton_15.place(x=480,y=140,width=82,height=45)
        GButton_15["command"] = self.GButton_15_command

        
        GButton_575=tk.Button(root)
        GButton_575["bg"] = "#f0f0f0"
        # GButton_575["cursor"] = "tcross"
        ft = tkFont.Font(family='Times',size=10)
        GButton_575["font"] = ft
        GButton_575["fg"] = "#000000"
        GButton_575["justify"] = "center"
        GButton_575["text"] = "VOL_DOWN"
        GButton_575.place(x=480,y=250,width=81,height=39)
        GButton_575["command"] = self.GButton_575_command


        GButton_422=tk.Button(root)
        GButton_422["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_422["font"] = ft
        GButton_422["fg"] = "#000000"
        GButton_422["justify"] = "center"
        GButton_422["text"] = "REBOOT"
        GButton_422.place(x=480,y=310,width=80,height=39)
        GButton_422["command"] = self.GButton_422_command

        self.GLineEdit_971=tk.Entry(root)
        self.GLineEdit_971["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_971["font"] = ft
        self.GLineEdit_971["fg"] = "#333333"
        self.GLineEdit_971["justify"] = "center"
        self.GLineEdit_971["text"] = "Target text"
        self.GLineEdit_971.place(x=440,y=370,width=144,height=34)

        
        GButton_107=tk.Button(root)
        GButton_107["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_107["font"] = ft
        GButton_107["fg"] = "#000000"
        GButton_107["justify"] = "center"
        GButton_107["text"] = "<"
        GButton_107.place(x=480,y=62,width=30,height=30)
        GButton_107["command"] = self.GButton_107_command

        GButton_777=tk.Button(root)
        GButton_777["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_777["font"] = ft
        GButton_777["fg"] = "#000000"
        GButton_777["justify"] = "center"
        GButton_777["text"] = "O"
        GButton_777.place(x=510,y=62,width=30,height=30)
        GButton_777["command"] = self.GButton_777_command

        GButton_786=tk.Button(root)
        GButton_786["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=23)
        GButton_786["font"] = ft
        GButton_786["fg"] = "#000000"
        GButton_786["justify"] = "center"
        GButton_786["text"] = "□"
        GButton_786.place(x=540,y=62,width=30,height=30)
        GButton_786["command"] = self.GButton_786_command


    def GButton_107_command(self):

        ss = os.system("adb shell input keyevent 4") # Back btn
        print(ss)


    def GButton_777_command(self):
        ss = os.system("adb shell input keyevent 3") # Home btn
        print(ss)


    def GButton_786_command(self):
        if self.count <10:
            ss = os.system("adb shell input keyevent 220") # Menu btn
            self.count+=1
        elif self.count == 20:
            self.count = 0
        else:
            ss = os.system("adb shell input keyevent 221") # Menu btn
            self.count+=1
            
        print(ss)



    def GButton_135_command(self):
        ss = readcmd("adb devices -l")
        self.GLabel_16.configure(text=ss)
        # print(ss)


    def GButton_61_command(self):
        ss=os.system("adb shell input keyevent KEYCODE_WAKEUP")
        print(ss)


    def GButton_62_command(self):
        ss=os.system("adb shell media volume --show --adj raise")
        print(ss)


    def GButton_833_command(self):
        data=str(self.GLineEdit_971.get())
        # replace white space with % in string
        data = data.replace(" ", "%s")
        data = "adb shell input text "+data
        print(data)
        ss=os.system(data)
        # print(ss)
          
    def GButton_15_command(self):
        ss=os.system("adb shell input keyevent SLEEP")
        print(ss)
    
    def GButton_575_command(self):
        ss=os.system("adb shell media volume --show --adj lower")
        print(ss)

    def GButton_422_command(self):
        ss=os.system("adb shell reboot")
        print(ss)


def readcmd(cmd):
    ftmp = tempfile.NamedTemporaryFile(suffix='.out', prefix='tmp', delete=False)
    fpath = ftmp.name
    if os.name=="nt":
        fpath = fpath.replace("/","\\") # forwin
    ftmp.close()
    os.system(cmd + " > " + fpath)
    data = ""
    with open(fpath, 'r') as file:
        data = file.read()
        file.close()
    os.remove(fpath)
    return data



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.config(bg="#d9d9d9")
    root.mainloop()
