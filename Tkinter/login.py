#INPORT LIBRARIES

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

#create main_GUI using Tk function
main_GUI=Tk()
main_GUI.title('Login')

usernameLabel=Label(main_GUI,text="username:")
usernameLabel.grid(row=1,column=1)
passwordLabel=Label(main_GUI,text="Password:")
passwordLabel.grid(row=2,column=1)

#Create entries

usernameEntry=Entry(main_GUI)
usernameEntry.grid(row=1,column=2,columnspan=2)
passwordEntry=Entry(main_GUI,show="*")
passwordEntry.grid(row=2,column=2,columnspan=2)

#Define function for login button
def login_button_clicked():
    username=usernameEntry.get()
    password=passwordEntry.get()
    if username=="jogo" and password=="jogops007":
        messagebox.askokcancel("QUICK MESSAGE","Hi,welcome!")
        NOTE=Toplevel()
        NOTE.title('Notes')
        # Create Text input
        text=Text(NOTE)
        text.grid(row=1,column=1,rowspan=2,columnspan=3)
        
        #Create Save Button
        def SaveNote():
            OutputPath=filedialog.asksaveasfilename()
            File=open(OutputPath,'w+')
            info=text.get('1.0','end')
            File.write(info)
            File.close()

        save_BTN=Button(NOTE,text="Save...",command=SaveNote)
        save_BTN.grid(row=3,column=1)
        
        #Create Open Button
        def OpenNote():
            InputPath=filedialog.askopenfilename()
            File=open(InputPath,'r+')
            words=File.read()
            text.insert('1.0',words)
            File.close()


        open_BTN=Button(NOTE,text="Open...",command=OpenNote)
        open_BTN.grid(row=3,column=2)
        
        #Create Exit Button
        def ExitNote():
            exit()

        exit_BTN=Button(NOTE,text="Exit",command=ExitNote)
        exit_BTN.grid(row=3,column=3)

    else:
        messagebox.askokcancel("QUICK MESSAGE","ERROR!")

#Define function for cancel button
def cancel_button_clicked():
    exit()

LOGINbutton=Button(main_GUI,text="LOGIN",command=login_button_clicked)
LOGINbutton.grid(row=3,column=2)
CANCELbutton=Button(main_GUI,text="CANCEL",command=cancel_button_clicked)
CANCELbutton.grid(row=3,column=3)


#Create eye buttons
eye=PhotoImage(file="Eye.png")
EyeButton=Button(main_GUI,image=eye)
EyeButton.grid(row=2,column=4)

#define hide and show function

def ShowPWD(event):
    passwordEntry["show"]=""

def HidePWD(event):
    passwordEntry["show"]="*"


EyeButton.bind('<ButtonPress-1>',ShowPWD)
EyeButton.bind('<ButtonRelease-1>',HidePWD)


#show
main_GUI.mainloop()         