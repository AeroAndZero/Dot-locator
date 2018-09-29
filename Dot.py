#from PIL import ImageTk
from tkinter import *
import sys
#from tkinter import messagebox
""" Save Function Under Progress """

#window
window = Tk()
window.title("Dot Locater v2.0")
window.geometry("200x280")

win2 = Tk()
win2.title("ToolBox")
#msgbox = messagebox.showinfo("Attention !", "This is a beta version and have some bugs, So don't Add Too Many Dots")

viewmode = False
drewline = False

yrecords = []
xrecords = []

# Re generating The Coordinates
def regen():
    print("Regenerated")
    global viewmode
    global canvasline

    canvas.destroy()
    graph()
    window.geometry("250x270")
    if drewline == True:
        canvasline()

"""  FOR ADDING A POINT """
def add_point():
    global xvar
    global yvar
    xvar = xinput.get()
    yvar = yinput.get()
    yrecords.append(int(yvar))
    xrecords.append(int(xvar))

"""For Removing a Point  """
def clear():
    global xvar
    global yvar
    xvar = xinput.get()
    yvar = yinput.get()
    yrecords.remove(int(yvar))
    xrecords.remove(int(xvar))

    xvar = 0
    yvar = 0

def allclear():
    global canvas
    global xrecords
    global yrecords
    global linerecordsx1
    global linerecordsy1
    global linerecordsx2
    global linerecordsy2

    canvas.destroy()
    xrecords = []
    yrecords = []
    linerecordsx1 = []
    linerecordsy1 = []
    linerecordsx2 = []
    linerecordsy2 = []
    graph()
    print("All Clear")

def graph():
    # Its Important To Be Socialized
    global canvas
    global viewmode
    global cor
    global yvar
    global xvar
    global y_graphdict
    global x_graphdict
    global canvas

    y = 15
    x = 5
    mkdot = 5
    window.geometry("250x270")

    y_graphdict = {
        5 : 12,
        4 : 36,
        3 : 60,
        2 : 84,
        1 : 108,
        0 : 132,
        -1 : 156,
        -2 : 180,
        -3 : 204,
        -4 : 228,
        -5 : 252
    }

    x_graphdict = {
        -5 : 2,
        -4 : 26,
        -3 : 50,
        -2 : 74,
        -1 : 98,
        0 : 122,
        1 : 146,
        2 : 170,
        3 : 194,
        4 : 218,
        5 : 242
    }

    # Setting Up Everything
    if viewmode == False:
        viewmode = True
    def makecanvas():
        global canvas
        canvas = Canvas(window, width=250, height=270)
        canvas.pack()
    makecanvas()

    # Being Picasso Here
    line = canvas.create_line(125,0,125,270, width=2)
    line2 = canvas.create_line(0,135,300,135, width=2)

    #print(yrecords)
    #print(len(yrecords))

    #dot = canvas.create_oval(276.5,82,276.5+mkdot,82+mkdot,fill="black")
    for dotx,doty in zip(xrecords,yrecords):
        print(dotx,doty)
        dot = canvas.create_oval(x_graphdict[int(dotx)],y_graphdict[int(doty)],x_graphdict[int(dotx)]+mkdot,y_graphdict[int(doty)]+mkdot, fill="black")

    """
    for i in cor:
        for j in i:
            if j == i[5]:
                text = canvas.create_text(120,y,text=str(j))
            y+=2

    for a in cor:
        for b in a:
            if b == a[5]:
                xtext = canvas.create_text(x,143,text=str(b))
            x+=2
    """
    numline = ['5','4','3','2','1','0','1','2','3','4','5']

    for i in numline:
        text = canvas.create_text(120,y,text=str(i))
        y+=24

    for j in numline:
        text2 = canvas.create_text(x,143,text=str(j))
        x+=24

    print("Graph Created") # Important For Debugging

linerecordsx1 = []
linerecordsy1 = []
linerecordsx2 = []
linerecordsy2 = []

def drwline():
    global x1entry
    global y1entry
    global x2entry
    global y2entry
    global drewline

    x1val = x1entry.get()
    y1val = y1entry.get()
    x2val = x2entry.get()
    y2val = y2entry.get()

    linerecordsx1.append(int(x1val))
    linerecordsy1.append(int(y1val))
    linerecordsx2.append(int(x2val))
    linerecordsy2.append(int(y2val))

    drewline = True

    y_graphdict = {
        5 : 12,
        4 : 36,
        3 : 60,
        2 : 84,
        1 : 108,
        0 : 132,
        -1 : 156,
        -2 : 180,
        -3 : 204,
        -4 : 228,
        -5 : 252
    }

    x_graphdict = {
        -5 : 2,
        -4 : 26,
        -3 : 50,
        -2 : 74,
        -1 : 98,
        0 : 122,
        1 : 146,
        2 : 170,
        3 : 194,
        4 : 218,
        5 : 242
    }

    linediff = 2.5

    global canvasline
    def canvasline():
        global linerecordsx1
        global linerecordsy1
        global linerecordsx2
        global linerecordsy2

        for x1,y1,x2,y2 in zip(linerecordsx1, linerecordsy1, linerecordsx2, linerecordsy2):
            canvasline = canvas.create_line(x_graphdict[x1] + linediff,
                                            y_graphdict[y1] + linediff,
                                            x_graphdict[x2] + linediff,
                                            y_graphdict[y2] + linediff,
                                            width=2)
    canvasline()
    print("It Works")

def line():
    global x1entry
    global y1entry
    global x2entry
    global y2entry

    linewin = Tk()
    linewin.title("Make Line")
    linewin.geometry("310x100")

    linelabel = Label(linewin,text="Make Line Between :").grid(row=0,columnspan=4)
    xlbl = Label(linewin,text="X(1) : ").grid(row=1,column=0, padx=10)
    ylbl = Label(linewin,text="Y(1) : ").grid(row=2,column=0, padx=10)

    x1entry = StringVar(linewin)
    y1entry = StringVar(linewin)
    xlbl2 = Entry(linewin, textvariable=x1entry, width=15).grid(row=1,column=1)
    ylbl2 = Entry(linewin, textvariable=y1entry, width=15).grid(row=2,column=1)
    mkbtn = Button(linewin,text="Draw Line", command=drwline).grid(row=3,columnspan=4)

    x2lbl = Label(linewin, text="X(2) : ").grid(row=1,column=2, padx=10)
    y2lbl = Label(linewin, text="Y(2) : ").grid(row=2,column=2, padx=10)

    x2entry = StringVar(linewin)
    y2entry = StringVar(linewin)
    x_entry = Entry(linewin, textvariable=x2entry, width=15).grid(row=1,column=3)
    y_entry = Entry(linewin, textvariable=y2entry, width=15).grid(row=2,column=3)

    linewin.mainloop()

def closethewindow():
    sys.exit()

# Elements
""" Window Elements """
graph()

""" Win 2 Elements """
# Labels
lbl_x = Label(win2, text="X Value : ").grid(row=0)
lbl_y = Label(win2, text="Y Value : ").grid(row=1)
credit = Label(win2, text="Created By Ayush Thakur").grid(row=5, columnspan=2)
warning = Label(win2, text="**Contains Bugs**").grid(row=6,columnspan=2)

# Entries
xinput = StringVar(win2)
xin = Entry(win2, textvariable=xinput).grid(row=0,column=1)
yinput = StringVar(win2)
yin = Entry(win2, textvariable=yinput).grid(row=1,column=1)

# Butt ons
btn_add = Button(win2, text="Add Point",width = 10 ,command=lambda:[add_point(),regen()]).grid(row=2, columnspan=2)
btn_remove = Button(win2, text="Delete Point",width=10,command=lambda:[clear(),regen()]).grid(row=3, columnspan=2)
close = Button(win2, text="Exit",width = 10,command=closethewindow).grid(row=4, columnspan=2)

# File Menu
menu = Menu(win2)  # Menu Created
win2.config(menu=menu)  # Configuring
FileMenu = Menu(menu, tearoff=0)  # SubMenu on Menu Bar
menu.add_cascade(label="Options", menu=FileMenu)  # Adding SubMenu On Menu Bar
FileMenu.add_command(label="Clear", command=allclear)  # Adding Menus In Submenu.. DONE
FileMenu.add_command(label="Draw Line", command=line) #For Drawing A Line
#FileMenu.add_command(label="Save", command=save)  # Saving FILEs
#FileMenu.add_command(label="Open Last Save",command=openfile)

window.mainloop()
win2.mainloop()
keep_it_running = input("DONT QUIT")
