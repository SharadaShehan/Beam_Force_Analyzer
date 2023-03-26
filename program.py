#-------------------------------------------------  Developed by Sharada Shehan  ---------------------------------------------------------------------

#--------------------------------------------------------  Beam Analyser  ----------------------------------------------------------------------------


# importing modules

import tkinter as tk 
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure 
from tkinter import messagebox


#-----------------------------------------------------------------------------------------------------------------------------------------------------


# essential lists for procedure

main_dict = {
    'main_labelframes' : [], 

    'support_checkboxes' : [], 'support_checkboxes_variables' : [], 'support_labelframes' : [],
    'support_sliders' : [],'support_entries' : [],
    'support_positions' : [], 'support_values' : [],

    'load_checkboxes' : [], 'load_checkboxes_variables' : [], 'load_labelframes' : [],
    'load_sliders' : [],'load_entries' : [],
    'load_positions' : [], 'load_values' : [],

    'couple_checkboxes' : [], 'couple_checkboxes_variables' : [], 'couple_labelframes' : [],
    'couple_sliders' : [],'couple_entries' : [],
    'couple_positions' : [], 'couple_values' : [],

    'distribution_checkboxes' : [], 'distribution_checkboxes_variables' : [], 'distribution_labelframes' : [],
    'distribution_sliders' : [[],[],[]], 'distribution_entries' : [[],[],[]],
    'distribution_positions' : [[],[],[]], 'distribution_values' : [[],[],[]],

    'support_load_positions' : [], 'support_load_values' : [], 'support_load_distribution_positions' :[],
    'distribution_polynomials' : [],
}


#-----------------------------------------------------------------------------------------------------------------------------------------------------


# main window and it's frames

root = tk.Tk()

frame1 = ttk.Frame(root)
frame1.grid(row=0,column=0)
frame2 = ttk.Frame(root)
frame2.grid(row=0,column=1)
frame3 = ttk.Frame(root)
frame3.grid(row=1,column=0,columnspan=2)

#------------------------------------------------------------------------------------------------------------------------------------------------------


# waiting variable to wait for user's input

length_var = tk.DoubleVar()
length_var.set(0)
rset_var = 0

#------------------------------------------------------------------------------------------------------------------------------------------------------


# importing png images 

support_img = tk.PhotoImage(file='support.png')
length_img = tk.PhotoImage(file='length.png')
support_img = tk.PhotoImage(file='support.png')
load_img = tk.PhotoImage(file='load.png')
couple_img = tk.PhotoImage(file='couple.png')
distribution_img = tk.PhotoImage(file='Distribution.png')

#------------------------------------------------------------------------------------------------------------------------------------------------------


# inheritance from tk widgets to custom widgets

# window to take inputs from user

class settings(tk.Toplevel) :
    def __init__(self,container) :
        super().__init__()
        self.geometry('700x150+400+200')
        self.transient(container)
        self.title('Loading Configuration')
        self.resizable(False,False)

# main frames

class Frame(tk.Frame) :
    def __init__(self,container) :
        super().__init__(container)
        self.pack()

# labels

class Label(tk.Label) :
    def __init__(self,container,text,x,y,m=1) :
        super().__init__(container)
        self.configure(text=text,font=('Arial',20))
        self.grid(row=x,column=y,columnspan=m)

# internal frames

class tlFrames(tk.Frame) :
    def __init__(self,container,y) :
        super().__init__(container)
        self.grid(row=y,column=0,ipadx=0,ipady=0)


#----------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------


# more advanced custom widgets

# creating length label 

class LengthLabelFrame(tk.LabelFrame) :
    def __init__(self,container) :
        super().__init__(container)
        self.label_img = ttk.Label(self,image = length_img)
        self.label_img.grid(row=0,column=0,rowspan=3,padx=20,pady=5)
        self.label_1 = ttk.Label(self,text = "length of beam :",font=('Arial',12))
        self.label_1.grid(row=0,column=1,padx=5,pady=5)
        self.entry_1 = tk.Entry(self,width=20)
        self.entry_1.grid(row=0,column=2,padx=5,pady=3)
        self.button_1 = tk.Button(self,text='Submit',width=20,command=lambda:submit_button(self.entry_1.get()))
        self.button_1.grid(row=2,column=2,padx=10,pady=(0,8))
        self.grid(row=0,column=0,pady=(0,3))

#----------------------------------------------------------------------------------------------------------------------------------------------------------


# creating supports main

class LabelFrameChecksSupports(tk.LabelFrame) :
    def __init__(self,container,x,y) :
        super().__init__(container)
        self.label_img = ttk.Label(self,image=support_img)
        self.label_img.grid(row=0,column=0,rowspan=3,padx=10,pady=10)
        self.label_theme = ttk.Label(self,text='Select Supports :',font=('Arial',12))
        self.label_theme.grid(row=0,column=1,padx=5,pady=5,columnspan=1)
        for num in range(4) :
            if num%2 == 0 : self.col = 1
            if num%2 == 1 : self.col = 2
            if num == 0 or num == 1 : self.row = 1
            if num == 2 or num == 3 : self.row = 2
            self.check_var = tk.StringVar()
            self.check_var.set('disabled')
            main_dict['support_checkboxes_variables'].append(self.check_var)
            self.cb = ttk.Checkbutton(self,text= f'Support {num+1}',command=self.check_command,onvalue='normal',offvalue='disabled',variable=self.check_var)
            self.cb.grid(row=self.row,column=self.col,pady=2)
            main_dict['support_checkboxes'].append(self.cb)
        main_dict['main_labelframes'].append(self)
        self.grid(row=x,column=y,ipadx=5,ipady=2,padx=5,pady=5,sticky='ew')

# command for support checkbuttons

    def check_command(self) :
        for check in range(4) :
            for item in main_dict['support_labelframes'][check].winfo_children() :
                item.configure(state=main_dict['support_checkboxes_variables'][check].get())
        for check in range(4) :

            if main_dict['support_checkboxes_variables'][check].get() == 'normal' :
                main_dict['support_labelframes'][check].winfo_children()[2].configure(troughcolor="#00cc00")

            if main_dict['support_checkboxes_variables'][check].get() == 'disabled' :
                main_dict['support_labelframes'][check].winfo_children()[2].configure(troughcolor="#c1c1c1")


# creating loads main

class LabelFrameChecksLoads(tk.LabelFrame) :
    def __init__(self,container,x,y) :
        super().__init__(container)
        self.label_img = ttk.Label(self,image=load_img)
        self.label_img.grid(row=0,column=0,rowspan=3,padx=10,pady=10)
        self.label_theme = ttk.Label(self,text='Select Loads :',font=('Arial',12))
        self.label_theme.grid(row=0,column=1,padx=5,pady=5,columnspan=1)
        for num in range(4) :
            if num%2 == 0 : self.col = 1
            if num%2 == 1 : self.col = 2
            if num == 0 or num == 1 : self.row = 1
            if num == 2 or num == 3 : self.row = 2
            self.check_var = tk.StringVar()
            self.check_var.set('disabled')
            main_dict['load_checkboxes_variables'].append(self.check_var)
            self.cb = ttk.Checkbutton(self,text= f'Load {num+1}',command=self.check_command,onvalue='normal',offvalue='disabled',variable=self.check_var)
            self.cb.grid(row=self.row,column=self.col,pady=2)
            main_dict['load_checkboxes'].append(self.cb)
        main_dict['main_labelframes'].append(self)
        self.grid(row=x,column=y,ipadx=5,ipady=2,padx=5,pady=5,sticky='ew')

# command for load checkbuttons

    def check_command(self) :
        for check in range(4) :
            for item in main_dict['load_labelframes'][check].winfo_children() :
                item.configure(state=main_dict['load_checkboxes_variables'][check].get())
        for check in range(4) :

            if main_dict['load_checkboxes_variables'][check].get() == 'normal' :
                main_dict['load_labelframes'][check].winfo_children()[2].configure(troughcolor="#00cc00")

            if main_dict['load_checkboxes_variables'][check].get() == 'disabled' :
                main_dict['load_labelframes'][check].winfo_children()[2].configure(troughcolor="#c1c1c1")


# creating couples main

class LabelFrameChecksCouples(tk.LabelFrame) :
    def __init__(self,container,x,y) :
        super().__init__(container)
        self.label_img = ttk.Label(self,image=couple_img)
        self.label_img.grid(row=0,column=0,rowspan=3,padx=10,pady=10)
        self.label_theme = ttk.Label(self,text='Select Couples :',font=('Arial',12))
        self.label_theme.grid(row=0,column=1,padx=5,pady=5,columnspan=1)
        for num in range(4) :
            if num%2 == 0 : self.col = 1
            if num%2 == 1 : self.col = 2
            if num == 0 or num == 1 : self.row = 1
            if num == 2 or num == 3 : self.row = 2
            self.check_var = tk.StringVar()
            self.check_var.set('disabled')
            main_dict['couple_checkboxes_variables'].append(self.check_var)
            self.cb = ttk.Checkbutton(self,text= f'Couple {num+1}',command=self.check_command,onvalue='normal',offvalue='disabled',variable=self.check_var)
            self.cb.grid(row=self.row,column=self.col,padx=5,pady=2)
            main_dict['couple_checkboxes'].append(self.cb)
        main_dict['main_labelframes'].append(self)
        self.grid(row=x,column=y,ipadx=5,ipady=10,pady=(0,2),rowspan=1,sticky='ew')

# command for couple checkbuttons

    def check_command(self) :
        for check in range(4) :
            for item in main_dict['couple_labelframes'][check].winfo_children() :
                item.configure(state=main_dict['couple_checkboxes_variables'][check].get())
        for check in range(4) :

            if main_dict['couple_checkboxes_variables'][check].get() == 'normal' :
                main_dict['couple_labelframes'][check].winfo_children()[2].configure(troughcolor="#00cc00")

            if main_dict['couple_checkboxes_variables'][check].get() == 'disabled' :
                main_dict['couple_labelframes'][check].winfo_children()[2].configure(troughcolor="#c1c1c1")


#  creating distribution main

class LabelFrameChecksDistributions(tk.LabelFrame) :
    def __init__(self,container,x,y) :
        super().__init__(container)
        self.label_img = ttk.Label(self,image=distribution_img)
        self.label_img.grid(row=1,column=0,columnspan=1,pady=10,rowspan=3)
        self.label_theme = ttk.Label(self,text='Select Distributions :',font=('Arial',12))
        self.label_theme.grid(row=0,column=0,padx=5,pady=(10,5),columnspan=2)
        for num in range(3) :
            self.check_var = tk.StringVar()
            self.check_var.set('disabled')
            main_dict['distribution_checkboxes_variables'].append(self.check_var)
            self.cb = ttk.Checkbutton(self,text= f'Distribution {num+1}',command=self.check_command,onvalue='normal',offvalue='disabled',variable=self.check_var)
            self.cb.grid(row=num+1,column=1,padx=5,pady=3)
            main_dict['distribution_checkboxes'].append(self.cb)
        main_dict['main_labelframes'].append(self)
        self.grid(row=x,column=y,ipadx=5,ipady=5,padx=(5,20),pady=3,sticky='ew')

# command for distribution checkbuttons

    def check_command(self) :
        for check in range(3) :
            for item in main_dict['distribution_labelframes'][check].winfo_children() :
                item.configure(state=main_dict['distribution_checkboxes_variables'][check].get())
        for check in range(3) :

            if main_dict['distribution_checkboxes_variables'][check].get() == 'normal' :
                main_dict['distribution_labelframes'][check].winfo_children()[4].configure(troughcolor="#00cc00")
                main_dict['distribution_labelframes'][check].winfo_children()[6].configure(troughcolor="#00cc00")

            if main_dict['distribution_checkboxes_variables'][check].get() == 'disabled' :
                main_dict['distribution_labelframes'][check].winfo_children()[4].configure(troughcolor="#c1c1c1")
                main_dict['distribution_labelframes'][check].winfo_children()[6].configure(troughcolor="#c1c1c1")


#----------------------------------------------------------------------------------------------------------------------------------------------------------


# creating sub label frames

class LabelFrameItems(tk.LabelFrame) :
    def __init__(self,container,end,x,y,typeh,text='none',m=1) :
        super().__init__(container)
        self.slider_var = tk.DoubleVar()
        self.labeltheme = ttk.Label(self,text=text)
        self.configure(labelwidget=self.labeltheme)
        self.label1 = ttk.Label(self,text="Placement :",font=('Arial',10),anchor='w')
        self.label1.grid(row=0,column=0,padx=5,pady=(5,0),columnspan=4)
        self.slider = tk.Scale(self,from_=0,to=end) 
        self.slider.configure(orient='horizontal',variable=self.slider_var,resolution=1,length=170,troughcolor='#c1c1c1')
        self.slider.grid(row=1,column=0,padx=5,columnspan=3)
        main_dict[f'{typeh}_sliders'].append(self.slider)
        self.spinbox = ttk.Spinbox(self,width=5,values=(0.01,0.05,0.1,0.5,1,5,10))
        self.spinbox['command'] = lambda:self.spinbox_command(self.spinbox.get())
        self.spinbox['state'] = 'readonly'
        self.spinbox.grid(row=1,column=3,sticky='e',pady=(15,0))
        self.label2 = ttk.Label(self,text="Value :",font=('Arial',10),anchor='w')
        self.label2.grid(row=2,column=0,padx=5,pady=(5,5),columnspan=1)
        self.entry = tk.Entry(self,width=20)
        self.entry.grid(row=2,column=1,padx=5,pady=(0,9),columnspan=3)
        main_dict[f'{typeh}_entries'].append(self.entry)
        main_dict[f'{typeh}_labelframes'].append(self)
        for item in self.winfo_children() :
            item.configure(state='disabled')
        self.grid(row=x,column=y,rowspan=m,ipadx=5,ipady=2,padx=5,pady=5)

# command to adjust scale resolution

    def spinbox_command(self,increment) :
        self.slider['resolution'] = increment


# creating sub label frames for distributions

class LabelFrameItemsDistributions(tk.LabelFrame) :
    def __init__(self,container,end,x,y,text='none',m=1) :
        super().__init__(container)
        if y == 1 : index = 0
        if y == 2 : index = 1
        if y == 3 : index = 2
        self.slider_var1 = tk.DoubleVar()
        self.slider_var2 = tk.DoubleVar()
        self.labeltheme = ttk.Label(self,text=text)
        self.configure(labelwidget=self.labeltheme)
        self.label1 = ttk.Label(self,text="Placement :",font=('Arial',10),anchor='w')
        self.label1.grid(row=0,column=0,padx=5,pady=3,columnspan=7)
        self.label2 = ttk.Label(self,text="From :",font=('Arial',10),anchor='w')
        self.label2.grid(row=1,column=0,padx=5)
        self.label3 = ttk.Label(self,text="To :",font=('Arial',10),anchor='w')
        self.label3.grid(row=2,column=0,padx=5)
        self.slider1 = tk.Scale(self,from_=0,to=end) 
        self.slider1.configure(orient='horizontal',variable=self.slider_var1,resolution=1,length=190,troughcolor='#c1c1c1')
        self.slider1.grid(row=1,column=1,pady=(0,5),sticky='e',columnspan=5)
        main_dict['distribution_sliders'][index].append(self.slider1)
        self.spinbox1 = ttk.Spinbox(self,width=5,values=(0.01,0.05,0.1,0.5,1,5,10))
        self.spinbox1.grid(row=1,column=6,sticky='w',pady=(15,5))
        self.spinbox1['command'] = lambda:self.spinbox1_command(self.spinbox1.get())
        self.slider2 = tk.Scale(self,from_=0,to=end) 
        self.slider2.configure(orient='horizontal',variable=self.slider_var2,resolution=1,length=190,troughcolor='#c1c1c1')
        self.slider2.grid(row=2,column=1,pady=(0,5),sticky='e',columnspan=5)
        main_dict['distribution_sliders'][index].append(self.slider2)
        self.spinbox2 = ttk.Spinbox(self,width=5,values=(0.01,0.05,0.1,0.5,1,5,10))
        self.spinbox2.grid(row=2,column=6,sticky='w',pady=(15,5))
        self.spinbox2['command'] = lambda:self.spinbox2_command(self.spinbox2.get())

        self.labelwx = ttk.Label(self,text="W(x) = ",font=('Arial',10),anchor='e')
        self.labelwx.grid(row=3,column=0,padx=5,sticky='e')

        self.entry1 = tk.Entry(self,width=7)
        self.entry1.grid(row=3,column=1,padx=(3,0),pady=3,sticky='e')
        main_dict['distribution_entries'][index].append(self.entry1)
        self.label4 = ttk.Label(self,text="x\u00B2 +",font=('Arial',12),anchor='w')
        self.label4.grid(row=3,column=2,padx=(0,2),pady=3)

        self.entry2 = tk.Entry(self,width=7)
        self.entry2.grid(row=3,column=3,padx=(5,0),pady=3,sticky='e')
        main_dict['distribution_entries'][index].append(self.entry2)
        self.label5 = ttk.Label(self,text="x\u00B9 +",font=('Arial',12),anchor='w')
        self.label5.grid(row=3,column=4,padx=(0,2),pady=3)

        self.entry3 = tk.Entry(self,width=7)
        self.entry3.grid(row=3,column=5,padx=(3,0),pady=3,sticky='e')
        main_dict['distribution_entries'][index].append(self.entry3)
        self.label6 = ttk.Label(self,text="x\u2070",font=('Arial',12),anchor='w')
        self.label6.grid(row=3,column=6,padx=(0,2),pady=3,sticky='w')

        main_dict['distribution_labelframes'].append(self)

        for item in self.winfo_children() :
            item.configure(state='disabled')

        self.grid(row=x,column=y,columnspan=m,ipadx=5,ipady=5,pady=5,padx=5)

# commands to adjust scale resolution

    def spinbox1_command(self,increment) :
        self.slider1['resolution'] = increment

    def spinbox2_command(self,increment) :
        self.slider2['resolution'] = increment


#----------------------------------------------------------------------------------------------------------------------------------------------------------


# calling functions to position labelframes

# supports frame

def create_supports (row,column) :
    global length
    LabelFrameChecksSupports(tlframe2,row,column)
    LabelFrameItems(tlframe2,length,row,1,'support',' Support 1 ')
    LabelFrameItems(tlframe2,length,row,2,'support',' Support 2 ')
    LabelFrameItems(tlframe2,length,row,3,'support',' Support 3 ')
    LabelFrameItems(tlframe2,length,row,4,'support',' Support 4 ')

# loads frame

def create_loads (row,column) :
    global length
    LabelFrameChecksLoads(tlframe2,row,column)
    LabelFrameItems(tlframe2,length,row,1,'load',' Load 1 ')
    LabelFrameItems(tlframe2,length,row,2,'load',' Load 2 ')
    LabelFrameItems(tlframe2,length,row,3,'load',' Load 3 ')
    LabelFrameItems(tlframe2,length,row,4,'load',' Load 4 ')

# couples frame

def create_couples (row,column) :
    global length
    LabelFrameChecksCouples(tlframe2,row,column)
    LabelFrameItems(tlframe2,length,row,1,'couple',' Couple 1 ')
    LabelFrameItems(tlframe2,length,row,2,'couple',' Couple 2 ')
    LabelFrameItems(tlframe2,length,row,3,'couple',' Couple 3 ')
    LabelFrameItems(tlframe2,length,row,4,'couple',' Couple 4 ')

# distributions frame

def create_distributions(row,column) :
    global length
    LabelFrameChecksDistributions(tlframe3,row,column)
    LabelFrameItemsDistributions(tlframe3,length,row,1,' Distribution 1 ')
    LabelFrameItemsDistributions(tlframe3,length,row,2,' Distribution 2 ')
    LabelFrameItemsDistributions(tlframe3,length,row,3,' Distribution 3 ')


#----------------------------------------------------------------------------------------------------------------------------------------------------------


# submit button for length window

def submit_button(max) :

    if '.' in max :
        messagebox.showwarning('value error',"beam length shouldn't be a floating point number")

    elif not (max.isnumeric()) :
        messagebox.showwarning('value error','beam length must be numeric')

    else :
        global length
        global rset_var
        length = (float(max))
        length_var.set(1)
        length_frame.button_1.configure(state='disabled')

#----------------------------------------------------------------------------------------------------------------------------------------------------------


# error handling


# filling empty entries, adding '0'

def error_check0 () :
    for y in ['support','load','couple'] :
        for x in range(4) :

            if main_dict[f'{y}_checkboxes_variables'][x].get() == 'normal' :    

                if main_dict[f'{y}_entries'][x].get() == '' :
                  main_dict[f'{y}_entries'][x].insert(0,'0')

    error_check1 ()


# filling empty entries, adding '0' for distributions

def error_check1 () :
    for x in range(3) :

        if main_dict['distribution_checkboxes_variables'][x].get() == 'normal' :
            for z in range(3) :

                if main_dict['distribution_entries'][x][z].get() == '' :
                    main_dict['distribution_entries'][x][z].insert(0,'0')

    error_check2()


# refusing multiple items of same type at same point

def error_check2 () :
    for y in ['support','load','couple'] :
        error_compliment_1 = []
        for x in range(4) :

            if main_dict[f'{y}_checkboxes_variables'][x].get() == 'normal' :
                error_compliment_1.append(float(main_dict[f'{y}_sliders'][x].get()))  

        error_compliment_2 = np.array(error_compliment_1)
        error_compliment_3 = np.unique(error_compliment_2)

        if len(error_compliment_3) !=len(error_compliment_2) :
            messagebox.showwarning('position error',f'{y} positions should be unique')
            break

    else :
        error_check3 () 


# orienting distributions from left to right

def error_check3 () :
    for x in range(3) :

        if main_dict['distribution_checkboxes_variables'][x].get() == 'normal' :

            if float(main_dict['distribution_sliders'][x][0].get()) >= float(main_dict['distribution_sliders'][x][1].get()) :
                messagebox.showwarning('position error','To : position must be greater than From : position')
                break

    else :
        error_check4 ()


# refusing non-numeric inputs including + and - for supports and loads

def error_check4 () :
    error_boolean = False
    for y in ['support','load'] :
        for x in range(4) :

            if main_dict[f'{y}_checkboxes_variables'][x].get() == 'normal' :

                if '.' in main_dict[f'{y}_entries'][x].get() :
                    floatless_string = ''.join(main_dict[f'{y}_entries'][x].get().split('.',1))

                    if not (floatless_string.isnumeric()) :
                        messagebox.showwarning('value error',f'{y} value must be numeric')
                        error_boolean = True
                        break

                elif not (main_dict[f'{y}_entries'][x].get().isnumeric()) :
                    messagebox.showwarning('value error',f'{y} value must be numeric')
                    error_boolean = True
                    break

        if error_boolean == True :
            break

    else :
        error_check5 ()


# refusing non-numeric inputs excluding + and - for couples

def error_check5() :
    for x in range(4) :

        if main_dict['couple_checkboxes_variables'][x].get() == 'normal' :

            if len(main_dict['couple_entries'][x].get()) > 1 :

                if '.' in main_dict['couple_entries'][x].get() :
                    floatless_string = ''.join(main_dict['couple_entries'][x].get().split('.',1))

                    if not (((floatless_string[0] in ['+','-']) or floatless_string[0].isnumeric()) and  floatless_string[1:].isnumeric()) :
                        messagebox.showwarning('value error','couple value must be numeric')
                        break

                elif not (((main_dict['couple_entries'][x].get()[0] in ['+','-']) or main_dict['couple_entries'][x].get()[0].isnumeric()) and  main_dict['couple_entries'][x].get()[1:].isnumeric()) :
                    messagebox.showwarning('value error','couple value must be numeric')
                    break

            if len(main_dict['couple_entries'][x].get()) == 1 :

                if not(main_dict['couple_entries'][x].get().isnumeric()) :
                    messagebox.showwarning('value error','couple value must be numeric')
                    break 
    else :
        error_check6 ()


# refusing non-numeric inputs excluding + and - for distributions

def error_check6 () :
    error_boolean = False
    for x in range(3) :

        if main_dict['distribution_checkboxes_variables'][x].get() == 'normal' :
            for z in range(3) :

                if len(main_dict['distribution_entries'][x][z].get()) > 1 :

                    if '.' in main_dict['distribution_entries'][x][z].get() :
                        floatless_string = ''.join(main_dict['distribution_entries'][x][z].get().split('.',1))

                        if not (((floatless_string[0] in ['+','-']) or floatless_string[0].isnumeric()) and  floatless_string[1:].isnumeric()) :

                            messagebox.showwarning('value error','distribution value must be numeric')
                            error_boolean = True
                            break          

                    elif not (((main_dict['distribution_entries'][x][z].get()[0] in ['+','-']) or main_dict['distribution_entries'][x][z].get()[0].isnumeric()) and  main_dict['distribution_entries'][x][z].get()[1:].isnumeric()) :
                        messagebox.showwarning('value error','distribution value must be numeric')
                        error_boolean = True
                        break

                if len(main_dict['distribution_entries'][x][z].get()) == 1 :
                    if not(main_dict['distribution_entries'][x][z].get().isnumeric()) :
                        messagebox.showwarning('value error','distribution value must be numeric')
                        error_boolean = True
                        break

            if error_boolean == True :
                break

    else :
        go_to_graphs()


#-----------------------------------------------------------------------------------------------------------------------------------------------------------


# procedure after clicking on go_to_graphs button

# go_to_graphs button function

def go_to_graphs() :
    global length

    # appending sliders and entries

    for y in ['support','load','couple'] :
        for x in range(4) :

            if main_dict[f'{y}_checkboxes_variables'][x].get() == 'normal' :
                main_dict[f'{y}_positions'].append(float(main_dict[f'{y}_sliders'][x].get()))
                main_dict[f'{y}_values'].append(float(main_dict[f'{y}_entries'][x].get()))

    for x in range(3) :

        if main_dict['distribution_checkboxes_variables'][x].get() == 'normal' :
            for y in range(2) :
                main_dict['distribution_positions'][x].append(float(main_dict['distribution_sliders'][x][y].get()))
            for z in range(3) :
                main_dict['distribution_values'][x].append(-1*float(main_dict['distribution_entries'][x][z].get()))
            main_dict['distribution_values'][x].append(float(0))

    # identifying unique positions for supports and loads

    compliment1 = np.array(main_dict['support_positions'])
    compliment2 = np.array(main_dict['load_positions'])
    compliment3 = np.union1d(compliment1,compliment2)
    
    # complimentary lists

    compliment4 = [] 
    compliment5 = [] 
    compliment6 = [] 
    compliment7 = []
    compliment8 = []


    for x in compliment3 :
        main_dict['support_load_positions'].append(x)

    # keeping support values positive

    for x in main_dict['support_values'] :
        compliment6.append(x)

    # use the load values with negative sign

    for x in main_dict['load_values'] :
        compliment7.append(-1*x)

    # appending support,load values based on whether positions are unique

    for x in main_dict['support_load_positions'] :

        if x in main_dict['support_positions'] :

            # both supports and loads are availble for position

            if x in main_dict['load_positions'] :
                compliment8.append(compliment6[main_dict['support_positions'].index(x)] + compliment7[main_dict['load_positions'].index(x)])
            
            # only supports are availble for position

            else :
                compliment8.append(compliment6[main_dict['support_positions'].index(x)])
        
        # only loads are availble for position

        elif x in compliment2 :
            compliment8.append(compliment7[main_dict['load_positions'].index(x)])


    for x in compliment8 :
        main_dict['support_load_values'].append(x)

    compliment9 = np.array(main_dict['distribution_positions'],dtype=object)

    for x in compliment9 :
        for y in x :
            compliment4.append(y)
    

    # identifying unique positions for supports, loads, distributions

    compliment10 = np.union1d(compliment3,compliment4)

    for x in compliment10 :
        main_dict['support_load_distribution_positions'].append(x)

    main_list = [[] for x in main_dict['support_load_distribution_positions']]

    # creating list ( with default floating 0 ) to identify change of positional shear force value

    sub_list = [[0.0] for x in main_dict['support_load_distribution_positions']]

    # adding supports, loads values to show the change of positional shear force value

    for x in main_dict['support_load_distribution_positions'] :

        if x in main_dict['support_load_positions'] :
            for y in range(main_dict['support_load_distribution_positions'].index(x),len(main_dict['support_load_distribution_positions'])) :
                sub_list[y][0] = sub_list[y][0] + main_dict['support_load_values'][main_dict['support_load_positions'].index(x)]

    #-----------------------------------------------------------------------------------------------------------------------------------------------------


    # developing basic polynomial functions for distributions ( no accuracy for intercept )

    compliment11 = []

    for x in main_dict['distribution_values'] :
        compliment11.append(np.poly1d(x))

    compliment12 = []
    compliment13 = []

    for x in main_dict['distribution_positions'] :
        compliment12.append(x)

    # identifying the change of shear force value due to distributions, from their beginning position to ending position

    for x in range(len(compliment12)) :

        if len(compliment12[x]) > 0 :
            compliment13.append(compliment11[x](compliment12[x][1])-compliment11[x](compliment12[x][0]))

        if len(compliment12[x]) == 0 :
            compliment13.append(float(0))

    compliment14 = []

    for x in main_dict['support_load_distribution_positions'] :
        for y in main_dict['distribution_positions'] :

            if (x in y) and ( y[0] == x ) :

                # adding corresponding shear force value changes ( due to distributions ) to relevant intervals , while looping position < ending position of distribution

                i = 0
                while main_dict['support_load_distribution_positions'][main_dict['support_load_distribution_positions'].index(x)+i] < y[1] :
                    main_list[main_dict['support_load_distribution_positions'].index(x)+i].append(main_dict['distribution_values'][main_dict['distribution_positions'].index(y)])
                    i += 1    
                
                # storing complete shear force value change due to distribution, from it's beginning position to ending position 

                compliment14.append([main_dict['support_load_distribution_positions'].index(x)+i , compliment13[compliment12.index(y)]])


    # two distributions appended to same position are added together

    compliment15 = []

    for x in main_list :

        if len(x) == 2  :
            for y in range(4) :
                compliment15.append(x[0][y]+x[1][y])
            main_list[main_list.index(x)] = compliment15
            compliment15 = []

    # three distributions appended to same position are added together

    compliment18 = []

    for x in main_list :

        if len(x) == 3  :
            for y in range(4) :
                compliment18.append( x[0][y] + x[1][y] + x[2][y] )
            main_list[main_list.index(x)] = compliment18
            compliment18 = []

    compliment16 = []

    # taking out internal lists appended into main_list values lists

    for x in range(len(main_list)) :

        if len(main_list[x]) == 1 :
            for y in range(4) :
                compliment16.append(main_list[x][0][y])
            main_list[x] = compliment16
            compliment16 = []

    # adding complete shear force value changes due to distributions, ( from their beginning position to ending position ) after their ending positions

    for x in range(len(main_list)) :
        for y in compliment14 :

            if x >= y[0]  :

                if len(main_list[x]) == 0 :
                    main_list[x].append(y[1])

                elif len(main_list[x]) == 1:
                    main_list[x][0] = main_list[x][0] + y[1]

                elif len(main_list[x]) == 4 :
                    main_list[x][3] = main_list[x][3] + y[1]
    
    # only 'complete shear force value changes' to polynomial co-efficient format

    for x in range(len(main_list)) :

        if len(main_list[x]) == 1 :
            main_list[x] = [0.0,0.0,0.0,main_list[x][0]]

    # null 'complete shear force value changes' to polynomial co-efficient format

    for x in range(len(main_list)) :

        if len(main_list[x]) == 0 :
            main_list[x] = [0.0,0.0,0.0,0.0]

    # only support+load values to polynomial co-efficient format 

    for x in range(len(sub_list)) :

        if len(sub_list[x]) == 1 :
            sub_list[x] = [0.0, 0.0, 0.0, sub_list[x][0]]

    # null support+load values to polynomial co-efficient format

        elif len(sub_list[x]) == 0 :
            sub_list[x] = [0.0, 0.0, 0.0, 0.0]



    #-----------------------------------------------------------------------------------------------------------------------------------------------------


    # adding shear force value change within interval due to distributions ( from beginning position of distribution to beginning position of current interval )

    for x in main_dict['support_load_distribution_positions'] :
        for y in main_dict['distribution_positions'] :

            if x in y and ( y[0] == x ) :

                i = 0
                while main_dict['support_load_distribution_positions'][main_dict['support_load_distribution_positions'].index(x)+i] < y[1] :
                    if main_dict['support_load_distribution_positions'][i] > y[0] :
                        selected_function = compliment11[main_dict['distribution_positions'].index(y)]
                        value_change = selected_function(main_dict['support_load_distribution_positions'][i]) - selected_function(y[0])
                        main_list[i][3] = main_list[i][3] + value_change
                    i += 1   

    # adding support+load values to 'complete shear force value changes'

    if len(main_list) > 0 :
        for x in range(len(main_list)) :
            for y in range(4) :
                main_list[x][y] = main_list[x][y] + sub_list[x][y]
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------------

    # creating polynomial functions for shear force graph

    new_positions = []
    new_main_list = []

    # ensuring whether position 0 and it's polynomial value format is available

    if float(0) not in main_dict['support_load_distribution_positions'] :
        new_positions.append(float(0))
        new_main_list.append([0.0, 0.0, 0.0, 0.0])

    # appending rest of positions and their polynomial value formats

    for x in main_dict['support_load_distribution_positions'] :
        new_positions.append(x)

    for x in main_list :
        new_main_list.append(x)

    # ensuring whether position of ending corner is available

    if length not in main_dict['support_load_distribution_positions'] :
        new_positions.append(length)

    # accurate intercept calculation

    for x in range(len(new_main_list)) :

        if (( new_main_list[x][0] != 0 ) or (( new_main_list[x][1] != 0 ) or ( new_main_list[x][2] != 0 ))) :
            new_polynomial = new_main_list[x][0:3]
            new_polynomial.append(float(0))
            constant = new_main_list[x][3] - np.poly1d(new_polynomial)(new_positions[x])
            new_main_list[x][3] = constant

    # x values for shear forces graph

    SF_linspaces = []

    for x in range(len(new_positions)-1) :
        SF_linspaces.append(np.linspace(new_positions[x],new_positions[x+1],num=(50)))

    SF_polynomials = []
    SF_polynomial_values = []

    # final polynomial functions for shear forces

    for x in new_main_list :
        SF_polynomials.append(np.poly1d(x))

    # y values for shear forces graph

    for x in range(len(new_positions)-1) :
        SF_polynomial_values.append(SF_polynomials[x](SF_linspaces[x]))

    #-----------------------------------------------------------------------------------------------------------------------------------------------------


    # identifying unique positions for all items along with couples

    compliment20 = np.array(main_dict['couple_positions'])
    compliment21 = np.array(new_positions)
    compliment22 = np.union1d(compliment20,compliment21)

    BM_positions = []

    for x in compliment22 :
        BM_positions.append(x)

    #-----------------------------------------------------------------------------------------------------------------------------------------------------

    #-----------------------------------------------------------------------------------------------------------------------------------------------------


    # use of intergration to obtain general bending moment polynomial co-efficient format

    integrated = []

    new_main_list.append([float(0) for x in range(4)])

    for x in range(len(new_main_list)) :
        comp_list = []
        for y in range(4) :
            comp_list.append(new_main_list[x][y]/(4-y))
        comp_list.append(float(0))
        integrated.append(comp_list)

    #-----------------------------------------------------------------------------------------------------------------------------------------------------

    #-----------------------------------------------------------------------------------------------------------------------------------------------------


    # appending previous bending moment polynomial co-efficients to positions with couples

    BM_values = []

    for x in range(len(BM_positions)) :
            if (BM_positions[x] in new_positions)   :
                BM_values.append(integrated[new_positions.index(BM_positions[x])])
            else :
                i = 0
                while new_positions[i] < BM_positions[x] :
                    i += 1
                comp_list1 = []
                for y in integrated[i-1] :
                    comp_list1.append(y)
                BM_values.append(comp_list1)

    # adding positional bending moment value changes ( due to couples ) to polynomial co-efficients

    for x in range(len(BM_positions)) : 
        if (BM_positions[x] in main_dict['couple_positions']) :
            for y in range(x,len(BM_positions)) :
                BM_values[y][4] = BM_values[y][4] + main_dict['couple_values'][main_dict['couple_positions'].index(BM_positions[x])]

    # developing general polynomial functions ( no accuracy for intercept )

    compliment23 = []

    for x in range(len(BM_values)) :
        new_polynomial1 =  BM_values[x][0:4]
        new_polynomial1.append(float(0))
        polynomial_array = np.array(new_polynomial1) 
        compliment23.append(np.poly1d(polynomial_array))
    
    # accurate intercept calculation

    for x in range(len(BM_values)) :
        for y in range(x,len(BM_values)-1) :
            value_change1 = compliment23[x](BM_positions[x+1]) - compliment23[x](BM_positions[x])
            BM_values[y+1][4] = BM_values[y+1][4] + value_change1

    for x in range(len(BM_values)-1) :
        constant1 = BM_values[x+1][4] - compliment23[x+1](BM_positions[x+1])
        BM_values[x+1][4] = constant1

    # x values for bending moments graph

    BM_linspaces = []

    for x in range(len(BM_positions)-1) :
        BM_linspaces.append(np.linspace(BM_positions[x],BM_positions[x+1],num=(50)))

    BM_polynomials = []
    BM_polynomial_values = []

    # final polynomial functions for bending moments

    for x in BM_values :
        BM_polynomials.append(np.poly1d(x))

    # y values for bending moments graph

    for x in range(len(BM_positions)-1) :
        BM_polynomial_values.append(BM_polynomials[x](BM_linspaces[x])) 

#---------------------------------------------------------------------------------------------------------------------------------------------------------
    

    # using matplotlib to plot shear forces graph

    fig = Figure(figsize=(6,6))
    subplot1 = fig.add_subplot(1,1,1)
    subplot2 = fig.add_subplot(1,1,1)

    for x in range(len(new_positions)-1) : 
        subplot2.fill_between(SF_linspaces[x],SF_polynomial_values[x],color='#00DD00',alpha=0.6)
        subplot1.plot(SF_linspaces[x],SF_polynomial_values[x],c='blue',lw=0.5)
        subplot2.set_title('Shear Forces Diagram')
        subplot2.set_ylabel('Shear Forces Values')
        subplot2.set_xlabel('Distance Along Beam')

    canvas = FigureCanvasTkAgg(fig,frame1)
    canvas.get_tk_widget().grid(row=0,column=0)

    # using matplotlib to plot bending moments graph

    fig1 = Figure(figsize=(6,6))
    subplot3 = fig1.add_subplot(1,1,1)
    subplot4 = fig1.add_subplot(1,1,1)

    for x in range(len(BM_positions)-1) : 
        subplot4.fill_between(BM_linspaces[x],BM_polynomial_values[x],color='#00DD00',alpha=0.6)
        subplot3.plot(BM_linspaces[x],BM_polynomial_values[x],c='blue',lw=0.5)
        subplot4.set_title('Bending Moment Diagram')
        subplot4.set_ylabel('Bending Moment Values')
        subplot4.set_xlabel('Distance Along Beam')

    canvas1 = FigureCanvasTkAgg(fig1,frame2)
    canvas1.get_tk_widget().grid(row=0,column=0)

    # footer with developer name

    label_foot = ttk.Label(frame3,text=' Developed By Sharada Shehan ',anchor='e',font=('Arial',10))
    label_foot.grid(row=0,column=0,sticky='e')


#---------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------


# window for positional values

    class values_window(tk.Toplevel) :
        def __init__(self) :
            super().__init__()
            self.geometry('450x350+1000+150')
            self.title(" Positional Values ")
            self.resizable(False,False)
            self.lower(root)
            self.frame1 = ttk.Frame(self)
            self.frame1.pack()

# labelframes for positional values

    class positional_values(tk.LabelFrame) :
        def __init__(self,container,positions_list,polynomials_list,row_,text_) :
            super().__init__(container)
            global length
            self.compliment_list1 = positions_list
            self.compliment_list2 = polynomials_list
            value_0 = str(polynomials_list[0](0))
            self.label_theme = ttk.Label(self,text=text_,font=('Arial',10))
            self.configure(labelwidget=self.label_theme)
            self.label1 = ttk.Label(self,text=" Position : ",font=('Arial',12))
            self.label1.grid(row=0,column=0,padx=10,pady=(16,0))
            self.slider1 = tk.Scale(self,from_=0,to=length,orient='horizontal',troughcolor='#d91dff',length=200,command=self.slider_command )
            self.slider1.grid(row=0,column=1,padx=(10,0),pady=5)
            self.spinbox = ttk.Spinbox(self,width=5,values=(0.01,0.05,0.1,0.5,1,5,10))
            self.spinbox['command'] = lambda:self.spinbox_command(self.spinbox.get())
            self.spinbox['state'] = 'readonly'
            self.spinbox.grid(row=0,column=2,sticky='e',padx=(0,10),pady=(15,0))
            self.label2 = ttk.Label(self,text=" Value/s : ",font=('Arial',12))
            self.label2.grid(row=1,column=0,padx=10,pady=(10,20))
            self.label3 = ttk.Label(self,text=value_0,font=('Arial',15))
            self.label3.grid(row=1,column=1,padx=10,pady=(10,20))
            self.grid(row=row_,column=0,sticky='nsew',pady=(25,25*row_),padx=30)

# command to adjust slider resolution

        def spinbox_command(self,increment) :
            self.slider1['resolution'] = increment

# active command for changing positional value

        def slider_command(self,event) :
            slider_value = float(self.slider1.get())

            if slider_value in self.compliment_list1 : 
                value_position_index = self.compliment_list1.index(slider_value)

                if value_position_index == 0 :
                    value = self.compliment_list2[0](slider_value)
                    self.label3.configure(text=np.round(value,decimals=2))

                elif value_position_index == len(self.compliment_list1)-1 :
                    value = self.compliment_list2[value_position_index-1](slider_value)
                    self.label3.configure(text=np.round(value,decimals=2))

                else :
                    value1 = self.compliment_list2[value_position_index-1](slider_value)
                    value2 = self.compliment_list2[value_position_index](slider_value)

                    if value1 == value2 :
                        self.label3.configure(text=np.round(value1,decimals=2))

                    else :
                        value = str(np.round(value1,decimals=2)) + ' , ' + str(np.round(value2,decimals=2))
                        self.label3.configure(text=value)

            else :
                for x in range(len(self.compliment_list1)-1) :
                    if self.compliment_list1[x] < slider_value < self.compliment_list1[x+1]  : 
                        value_position_index = x
                        value = self.compliment_list2[value_position_index](slider_value)
                        self.label3.configure(text=np.round(value,decimals=2))
                        break


# positional values window appearance

    new_window = values_window()
    new_window.resizable(False,False)

# positioning labelframes for positional values

    positional_values(new_window.frame1,new_positions,SF_polynomials,0,' Shear Force Values ')
    positional_values(new_window.frame1,BM_positions,BM_polynomials,1,' Bending Moment Values ')

#---------------------------------------------------------------------------------------------------------------------------------------------------------


# closing settings window

    tl.destroy()

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------


# length setting window appearance

tl = settings(root)
settings_frame = Frame(tl)
Label(settings_frame,'Loading Configuration',0,0,2)

# length setting frame , labelframe

tlframe1 = tlFrames(settings_frame,1)
length_frame = LengthLabelFrame(tlframe1)

# wait variable to wait for go_to_graphs button click

tlframe1.wait_variable(length_var)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------


# procedure after go_to_graphs button clicked

# removing length label

tlframe1.grid_forget()

# setting new size and position for window

tl.geometry('1370x730+60+30')
tl.resizable(False,False)

root.title(' Loading Configuration ')
root.geometry('1200x620+100+50')
root.resizable(False,False)

#----------------------------------------------------------------------------------------------------------------------------------------------------------


# alignments of labelframes along with separators


# 1st frame

tlframe2 = tlFrames(settings_frame,2)

sep1 = ttk.Separator(tlframe2,orient='horizontal')
sep1.grid(row=1,column=0,columnspan=5,sticky='NSEW',pady=3)

create_supports (2,0)
sep1 = ttk.Separator(tlframe2,orient='horizontal')
sep1.grid(row=3,column=0,columnspan=5,sticky='NSEW',pady=3)

create_loads (4,0)
sep1 = ttk.Separator(tlframe2,orient='horizontal')
sep1.grid(row=5,column=0,columnspan=5,sticky='NSEW',pady=3)

create_couples (6,0)
note = ttk.Label(tlframe2,text=' ~Note that Clockwise Values are Positive (+) and Anti-Clockwise Values are Negative (-) ~ ',font=('Arial',10))
note.grid(row=7,column=0,columnspan=5,pady=(0,5))
sep1 = ttk.Separator(tlframe2,orient='horizontal')
sep1.grid(row=8,column=0,columnspan=5,sticky='NSEW',pady=3)


# 2nd frame

tlframe3 = tlFrames(settings_frame,3)

create_distributions(0,0)
sep1 = ttk.Separator(tlframe3,orient='horizontal')
sep1.grid(row=1,column=0,columnspan=4,sticky='NSEW',pady=3)


# alignment of go_to_graphs button

main_button = ttk.Button(tlframe3,text='Go To Graphs',command=error_check0)
main_button.grid(row=2,column=3,ipady=6,ipadx=30,padx=5,pady=1,sticky='e')



root.mainloop()


