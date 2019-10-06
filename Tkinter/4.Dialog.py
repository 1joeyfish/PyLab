
# https://tkdocs.com/tutorial/index.html
# https://www.python-course.eu/python_tkinter.php
# https://www.tutorialspoint.com/python3/python_gui_programming.htm
# https://www.python-course.eu/
# http://effbot.org/tkinterbook/

# import Libs
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import commondialog
from tkinter import filedialog
from tkinter import colorchooser

# Create main GUI in memory
root = Tk()

#window position
# The "x" (horizontal position) is specified with a leading plus or minus, 
# "+25" means the left edge of the window should be 25 pixels from the left edge of the screen, 
# "-50" means the right edge of the window should be 50 pixels from the right edge of the screen. 
# Similarly, a "y" (vertical) position of "+10" means the top edge of the window should be ten pixels below the top of the screen, 
# "-100" y means the bottom edge of the window should be 100 pixels above the bottom of the screen.
#root.geometry("800x600")         # widthxheight±x±y

# Add a label
LabelUserName = Label(root, text = "Python Table Test")
LabelUserName.grid(row=1,column=1,columnspan=2)

# Add a label
LabelUserName = Label(root, text = "User Name:")
LabelUserName.grid(row=2,column=1)
# Add a ebtry box
name = Entry(root, bd = 5)
name.grid(row=2,column=2)

# Add a label
LabelUserName = Label(root, text = "Password:")
LabelUserName.grid(row=3,column=1)
# Add a ebtry box
passwd = Entry(root, bd = 5, show ="*")
passwd.grid(row=3,column=2)

def ShowPwd(event):
    passwd["show"]=""
def HidePwd(event):
    passwd["show"]="*"

EyeImageFile = PhotoImage(file='eye.png')
SeeBtn = ttk.Button(root,image=EyeImageFile)
SeeBtn.bind('<ButtonPress-1>',ShowPwd)
SeeBtn.bind('<ButtonRelease-1>', HidePwd)
SeeBtn.grid(row=3, column=3)


# Add a button and callback functions
def BtnOKCallBack():
    if (name.get()=="Joe") and (passwd.get()=="Joey"):
        messagebox.showinfo( "Hello Python", "Good Boy:-)")
    else:
        #messagebox.showinfo( "Hello Python", "Bad Guy!!!")
        NoteWindow=Toplevel()
        NoteWindow.geometry("800x600")
        
        textNote = Text(NoteWindow)
        textNote.grid(row=1,column=1,rowspan=5,columnspan=5)
        textNote.insert("1.0","Please type in what you want..")

        def BtnSaveClicked():
          filename = filedialog.asksaveasfilename()  # modal dialogs-the commands(and hence your program) will not continue  until the user submits the dialog
          fo=open(filename,"w+")
          fo.write(textNote.get("1.0","end"))
          fo.close()

        def BtnOpenFileClicked():
          filename = filedialog.askopenfilename()   # filedialog.askdirectory()
          fo=open(filename,"r+")
          fo.seek(0, 0)
          str=fo.read()
          textNote.insert("1.0",str)
          fo.close()
        
        def BtnColorClicked():
          # return a tuple(triple, color), triple is a tuple (R, G, B), color is a regular Tkinter color object.
          clr=colorchooser.askcolor(initialcolor='#ff0000')   # filedialog.askdirectory()
          textNote["foreground"]=clr[1] 

        BtnOpenFile = ttk.Button(NoteWindow, text = "Open...", width=10,command=BtnOpenFileClicked)
        BtnOpenFile.grid(row=6,column=1)
        BtnOpenSave = ttk.Button(NoteWindow, text = "Save...", width=10,command=BtnSaveClicked)
        BtnOpenSave.grid(row=6,column=2)
        BtnOpenSave = ttk.Button(NoteWindow, text = "Color...", width=10,command=BtnColorClicked)
        BtnOpenSave.grid(row=6,column=3)

        def BtnExitCallBack():
          exit()
        BtnOpenExit = Button(NoteWindow, text = "Exit", width=10,command=BtnExitCallBack)
        BtnOpenExit.grid(row=6,column=5)

        # Check if the window isabove another one. use "isbelow" if want to check it is below.
        # if (Tk.eval('wm stackorder '+str(NoteWindow)+' isabove '+str(root))=='1'):    
        NoteWindow.lower(root)
          #NoteWindow.lift()
        
        NoteWindow.minsize(200,100)
        NoteWindow.maxsize(800,600)
        NoteWindow.resizable(TRUE,FALSE)  # width,height
        
        # You can query or set the current window state, 
        # and there are also the methods "iconify" and "deiconify" which are shortcuts for setting the "iconic" or "normal" states respectively.
        thestate = NoteWindow.state()
        NoteWindow.state('normal')
        NoteWindow.iconify()
        NoteWindow.deiconify()
        


   
BtnHello = Button(root, text = "Login", width=10, command = BtnOKCallBack)
BtnHello.grid(row=4,column=1)

def BtnExitCallBack():
  exit()
BtnHello = Button(root, text = "STOP",  width=20, command = BtnExitCallBack)
BtnHello.grid(row=4,column=2)




# Run main loop and show the window
root.mainloop()