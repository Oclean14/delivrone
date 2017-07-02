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

        form_action(form_data)

        fichier = open("data.json", "a")
        fichier.write(str(form_data))
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
        from Tkinter import Frame, Entry, Radiobutton, Checkbutton, Text, Listbox, Tk, Label, StringVar
        import tkMessageBox as messagebox
        from ttk import Combobox
        from Tkconstants import *
    except ImportError:
        from tkinter import Frame, Entry, Radiobutton, Checkbutton, Text, Listbox, Tk, Label, messagebox, StringVar
        from tkinter.ttk import Combobox
        from tkinter.constants import *

    import pprint

    def myField(form, myinput, nbRow):
	Label(form, text=myinput).grid(row=nbRow,column=0, sticky=E, pady=(8,0))
	entry = Entry(form)
        entry.fieldname = myinput
        entry.grid(row=nbRow,column=1, sticky =E+W)
    
    pp = pprint.PrettyPrinter(indent=4)

    root= Tk()

    Label(root, text="Delivrone: configuration des parametres.").pack(anchor=W, padx=(2,0))

    form = Form(root, action =lambda data: messagebox.showinfo("form data",pp.pformat(data)))
    form.pack(expand=True, fill="both", ipadx=10, ipady=10)

    fields = ["aerianspace", "numberDrone", "averageSpeed", "failureFrequency", "numberStation", "batteriesPerStation", "chargingTime", "changingTime", "mode", "deliveryFrequency", "consumption", "maxCycle", "startAt", "startAt", "motorsNumber", "motorPrice", "propellersNumber", "propellerPrice", "stationList", "droneList", "WarehouseList"]
    count = 1

    for field in fields:
	myField(form, field, count)
        count = count + 1

    Submit_Button(form, text="Submit").grid(row=count,column=1,sticky =E)

    # It's possible to provide hidden data
    """form.hidden_input["hidden_var1"] = "value1"
    form.hidden_input["hidden_var2"] = "value2" """

    # The fieldname attribute is necessary to provide data to action
    """Label(form, text="Entry:").grid(row=2,column=0, sticky=E, pady=(8,0))
    entry = Entry(form)
    entry.fieldname = "entry"
    entry.grid(row=2,column=1, sticky =E+W)
    
    Label(form, text="Checkbuttons:").grid(row=2,column=0, sticky=E, pady=(8,0))
    column = Frame(form)
    column.grid(row=3,column=1, sticky =E+W)

    checkbutton0 = Checkbutton(column, text="Option 0")
    checkbutton0.fieldname = "checkbutton0"
    checkbutton0.pack(side=LEFT)

    checkbutton1 = Checkbutton(column, text="Option 1")
    checkbutton1.fieldname = "checkbutton1"
    checkbutton1.pack(side=LEFT)
    
    checkbutton2 = Checkbutton(column, text="Option 2")
    checkbutton2.fieldname = "checkbutton2"
    checkbutton2.pack(side=LEFT)
    
    Label(form, text="Radiobuttons:").grid(row=4,column=0, sticky=E, pady=(8,0))
    column = Frame(form)
    column.grid(row=5,column=1, sticky =E+W)

    # All radiobuttons require a variable
    variable = StringVar()
    radiobutton0 = Radiobutton(column, variable = variable, value="value0", text="Selection 0")
    radiobutton0.fieldname = "radiobutton"
    radiobutton0.pack(side=LEFT)
    
    radiobutton1 = Radiobutton(column, variable = variable, value="value1", text="Selection 1")
    radiobutton0.fieldname = "radiobutton"
    radiobutton1.pack(side=LEFT)
    
    Label(form, text="Text area:").grid(row=6,column=0, sticky=E, pady=(8,0))

    text = Text(form, height=5)
    text.fieldname = "text"
    text.grid(row=7,column=1, sticky =E+W)

    Label(form, text="Listbox:").grid(row=8,column=0, sticky=E, pady=(8,0))

    listbox = Listbox(form)
    listbox.fieldname = "listbox"
    listbox.grid(row=9,column=1, sticky=W)

    for item in ["one", "two", "three", "four"]:
        listbox.insert("end", item)

    Label(form, text="Combobox:").grid(row=10,column=0, sticky=E, pady=(8,0))

    combobox = Combobox(form, values = ('X', 'Y', 'Z'), width=5)
    combobox.fieldname = "combobox"
    combobox.grid(row=11,column=1, sticky=W)"""
    
    root.mainloop()
