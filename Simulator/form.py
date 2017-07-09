try:
    import Tkinter as tk
    import ttk
except ImportError:
    import tkinter as tk
    import tkinter.ttk as ttk

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

    def __str__(self):
        sb = []
        for key in self.__dict__:
            sb.append("{key}='{value}'".format(key=key, value=self.__dict__[key])) 
        return ', '.join(sb)

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
            form_data["WarehouseList"] = CoordonneesWH
            form_data["stationList"] = CoordonneesDS
	
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

    def myField(form, myinput, nbRow):
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

    def EditWH(val):
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

    root.mainloop()
