try:
    #python2
    import Tkinter as tk
    import ttk
    import tkFont as tkfont
except ImportError:
    #python3
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import font  as tkfont

class Base_Form(object):
    """Base class of all forms"""

    def __init__(self, widget_class, master, action, hidden_input, kw):
        self.action = action

        if hidden_input is None:
            self.hidden_input = dict()
        else:
            if not isinstance(hidden_input, dict):
                raise ValueError("'hidden_input' should be a dict")
                
            self.hidden_input = hidden_input

        kw["class"] = "Form"
        widget_class.__init__(self, master, **kw)

class Base_SubmitButton(object):
    """Base class of submit buttons"""

    def submit(self):
        form_widget = self
        while True:
            form_widget = form_widget.master
            if form_widget is None:
                raise Exception("No form found")
            else:
                if form_widget.winfo_class() == "Form":
                    break

        if form_widget.action is None: return
        
        form_action = form_widget.action

        form_data = {}
        form_data.update(form_widget.hidden_input)

        # Applying list for python 2/3 compatibility. dict_values is a view in Python 3.
        list_of_widgets = list(form_widget.children.values())
        
        while True:
            try:
                widget = list_of_widgets.pop()
            except IndexError:
                break

            list_of_widgets.extend(list(widget.children.values()))

            if not hasattr(widget,"fieldname"): continue
            
            field_name = widget.fieldname
            Tk_class = widget.winfo_class()
            
            if Tk_class == "Entry" or Tk_class == "TEntry":
                field_value = widget.get()
            elif Tk_class == "Text":               
                field_value = widget.get("1.0",'end-1c')
            elif Tk_class == "TCombobox":
                field_value = widget.get()
            elif Tk_class == "Listbox":
                field_value = [widget.get(idx) for idx in widget.curselection()]
            elif Tk_class == "Checkbutton" or Tk_class == "TCheckbutton":
                variable_name = widget.cget("variable").string
                field_value = widget.tk.globalgetvar(variable_name)
            elif Tk_class == "Radiobutton" or Tk_class == "TRadiobutton":
                field_value = widget.tk.globalgetvar(widget.cget("variable").string)
            else:
                continue

            form_data[field_name] = field_value
            form_data["WarehouseList"] = app.frames["PageTwo"].CoordonneesWH
            form_data["stationList"] = app.frames["PageTwo"].CoordonneesDS
	
	form_data = str(form_data)	
	form_data = re.sub(r"(\\')", "'", form_data)
	form_data = re.sub(r"('\[)", "[", form_data)
	form_data = re.sub(r"(\]')", "]", form_data)
	form_data = re.sub(r"(\"\{)", "{", form_data)
	form_data = re.sub(r"(\}\")", "}", form_data)
        form_action(form_data)

	# Creating the json
        fichier = open("data.json", "w")
        fichier.write(form_data)
        fichier.close()

class Form_Frame(tk.Frame, Base_Form):
    def __init__(self, master, action=None, hidden_input=None, **kw):
        Base_Form.__init__(self, tk.Frame, master, action, hidden_input, kw)
        
class Form_TFrame(tk.Frame, Base_Form):
    def __init__(self, master, action=None, hidden_input=None, **kw):
        Base_Form.__init__(self, ttk.Frame, master, action, hidden_input, kw)
        
class Form_LabelFrame(tk.LabelFrame, Base_Form):
    def __init__(self, master, action=None, hidden_input=None, **kw):
        Base_Form.__init__(self, tk.LabelFrame, master, action, hidden_input, kw)
        
class Form_TLabelFrame(ttk.LabelFrame, Base_Form):
    def __init__(self, master, action=None, hidden_input=None, **kw):
        Base_Form.__init__(self, ttk.LabelFrame, master, action, hidden_input, kw)

Form = Form_Frame

class Submit_Button(tk.Button, Base_SubmitButton):
    def __init__(self, parent, *args, **kw):
        kw["command"] = self.submit
        tk.Button.__init__(self, parent, *args, **kw)

class Submit_TButton(ttk.Button, Base_SubmitButton):
    def __init__(self, parent, *args, **kw):
        kw["command"] = self.submit
        ttk.Button.__init__(self, parent, *args, **kw)

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PageOne")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class PageOne(tk.Frame):

    def myField(self, form, myinput, nbRow):
	tk.Label(form,text=myinput).grid(row=nbRow,column=0,sticky=E,pady=(8,0))
	entry = tk.Entry(form)
        entry.fieldname = myinput
        entry.grid(row=nbRow,column=1,sticky= E+W)

    def scriptMain(self):
        os.system('python main.py')

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
	label = tk.Label(self, text="Delivrone Configuration 1/2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

	fields = ["aerianspace", "numberDrone", "averageSpeed", "failureFrequency", "numberStation", "batteriesPerStation", "chargingTime", "changingTime", "mode", "deliveryFrequency", "consumption", "maxCycle", "startAt", "startAt", "motorsNumber", "motorPrice", "propellersNumber", "propellerPrice", "droneList"]
        count = 1
	pp = pprint.PrettyPrinter(indent=4)

        #self.title('Initialization')
        self.form = Form(self, action =lambda data: messagebox.showinfo("form data",pp.pformat(data)))
        self.form.pack(expand=True, fill="both", ipadx=10, ipady=10)

        for field in fields:
            self.myField(self.form, field, count)
            count = count + 1	

	Submit_Button(self.form, text="Submit").grid(row=count,column=1,sticky =E)
        tk.Label(self, text="BEFORE SUBMIT").pack()
	tk.Button(self, text ='Launch Simulator', command = self.scriptMain).pack(side=RIGHT,padx = 5,pady = 5)
	button = tk.Button(self, text="Go to WareHouse & Station Edition",
                           command=lambda: controller.show_frame("PageTwo"))
        button.pack(side=RIGHT,padx = 5,pady = 5)

class PageTwo(tk.Frame):
    
    def ClicWH(self, event):
        X = event.x
        Y = event.y
        r = 10
        self.CoordonneesWH.append("{'longitude':'" + str(X) + "','latitude':'" + str(Y) + "'}")
        self.Canevas.create_rectangle(X-r, Y-r, X+r, Y+r, outline='black',fill='blue', tags='WH')
        print str(self.CoordonneesWH)

    def ClicDS(self, event):
        X = event.x
        Y = event.y
        r = 10
        self.CoordonneesDS.append("{'longitude':'" + str(X) + "','latitude':'" + str(Y) + "'}")
        self.Canevas.create_rectangle(X-r, Y-r, X+r, Y+r, outline='black',fill='red', tags='DS')
        print str(self.CoordonneesDS)

    def EffacerWH(self):
        # Efface la zone graphique 
        self.CoordonneesWH[:] = []
        for WH in self.Canevas.find_withtag("WH"):
            self.Canevas.delete(WH)

    def EffacerDS(self):
        self.CoordonneesDS[:] = []
        for DS in self.Canevas.find_withtag("DS"):
            self.Canevas.delete(DS)

    def EditWH(self):
        self.Canevas.bind('<Button-1>',self.ClicWH)

    def EditDS(self):
        self.Canevas.bind('<Button-1>',self.ClicDS)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Delivrone Configuration 2/2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

	Largeur = 680
	Hauteur = 520
	self.CoordonneesWH = []
	self.CoordonneesDS = []

	tk.Label(self, text="Click on this window to place Warehouses and Drone stations").pack(anchor=W, padx=(2,0))
	self.Canevas = tk.Canvas(self, width = Largeur, height =Hauteur, bg ='white')
	self.Canevas.bind('<Button-1>',self.ClicWH)

	self.Canevas.pack(padx =5, pady =5)
	tk.Button(self, text ='Edit WareHouses', command = self.EditWH).pack(side=LEFT,padx = 5,pady = 5)
	tk.Button(self, text ='Edit Stations', command = self.EditDS).pack(side=LEFT,padx = 5,pady = 5)
	tk.Button(self, text ='Delete Warehouses', command = self.EffacerWH).pack(side=LEFT,padx = 5,pady = 5)
	tk.Button(self, text ='Delete Stations', command = self.EffacerDS).pack(side=LEFT,padx = 5,pady = 5)
	#tk.Button(self, text ='Quitter', command = self.destroy).pack(side=LEFT,padx=5,pady=5)
	#Submit_Button(SampleApp().frames["PageOne"].form, text="Submit").grid(row=count,column=1,sticky =E)

        button = tk.Button(self, text="Go Back to SUBMIT",
                           command=lambda: controller.show_frame("PageOne"))
        button.pack(side=LEFT,padx=5,pady=5)

if __name__== "__main__":
    try:
        from Tkinter import *
        import tkMessageBox as messagebox
        from ttk import Combobox
        from Tkconstants import *
    except ImportError:
        from tkinter import *
        from tkinter.ttk import Combobox
        from tkinter.constants import *

    import pprint
    import re
    import os

    """ def myField(form, myinput, nbRow):
	Label(form,text=myinput).grid(row=nbRow,column=0,sticky=E,pady=(8,0))
	entry = Entry(form)
        entry.fieldname = myinput
        entry.grid(row=nbRow,column=1,sticky= E+W)

    def ClicWH(event):
        X = event.x
        Y = event.y
        r = 10
	CoordonneesWH.append("{'longitude':'" + str(X) + "','latitude':'" + str(Y) + "'}")
        Canevas.create_rectangle(X-r, Y-r, X+r, Y+r, outline='black',fill='blue', tags='WH')
	print str(CoordonneesWH)

    def ClicDS(event):
        X = event.x
        Y = event.y
        r = 10
	CoordonneesDS.append("{'longitude':'" + str(X) + "','latitude':'" + str(Y) + "'}")
        Canevas.create_rectangle(X-r, Y-r, X+r, Y+r, outline='black',fill='blue', tags='WH')
        Canevas.create_rectangle(X-r, Y-r, X+r, Y+r, outline='black',fill='red', tags='DS')
	print str(CoordonneesDS)

    def EffacerWH():
        # Efface la zone graphique 
	print "toto"
	CoordonneesWH[:] = []
	for WH in Canevas.find_withtag("WH"):
            Canevas.delete(WH)

    def EffacerDS():
	CoordonneesDS[:] = []
	for DS in Canevas.find_withtag("DS"):
            Canevas.delete(DS)

    def EditWH():
        Canevas.bind('<Button-1>',ClicWH)

    def EditDS():
        Canevas.bind('<Button-1>',ClicDS)

    Largeur = 480
    Hauteur = 320
    CoordonneesWH = []
    CoordonneesDS = []
    pp = pprint.PrettyPrinter(indent=4)
    root= Tk()
    fields = ["aerianspace", "numberDrone", "averageSpeed", "failureFrequency", "numberStation", "batteriesPerStation", "chargingTime", "changingTime", "mode", "deliveryFrequency", "consumption", "maxCycle", "startAt", "startAt", "motorsNumber", "motorPrice", "propellersNumber", "propellerPrice", "droneList"]
    count = 1

    root.title('Initialization')

    Label(root, text="Delivrone: configuration of parameters.").pack(anchor=W, padx=(2,0))

    form = Form(root, action =lambda data: messagebox.showinfo("form data",pp.pformat(data)))
    form.pack(expand=True, fill="both", ipadx=10, ipady=10)

    for field in fields:
	myField(form, field, count)
        count = count + 1

    Label(root, text="Click on this window to place Warehouses and Drone stations").pack(anchor=W, padx=(2,0))
    Canevas = Canvas(root, width = Largeur, height =Hauteur, bg ='white')
    Canevas.bind('<Button-1>',ClicWH)
        
    Canevas.pack(padx =5, pady =5)
    Button(root, text ='Edit WareHouses', command = EditWH).pack(side=LEFT,padx = 5,pady = 5)
    Button(root, text ='Edit Stations', command = EditDS).pack(side=LEFT,padx = 5,pady = 5)
    Button(root, text ='Delete Warehouses', command = EffacerWH).pack(side=LEFT,padx = 5,pady = 5)
    Button(root, text ='Delete Stations', command = EffacerDS).pack(side=LEFT,padx = 5,pady = 5)
    Button(root, text ='Quitter', command = root.destroy).pack(side=LEFT,padx=5,pady=5)

    Submit_Button(form, text="Submit").grid(row=count,column=1,sticky =E)

    root.mainloop()"""

    app = SampleApp()
    app.mainloop()
