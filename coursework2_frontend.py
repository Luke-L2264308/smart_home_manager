from tkinter import Tk, Frame, Label, Entry, Button, IntVar, StringVar, messagebox
from python_coursework_2_improvedplug import SmartHome, SmartDoor, SmartLight, SmartPlug
#THE ONE
#prevent entering empty data tomorrow in the gui
class SmartHomeApp:
    def __init__(self,smart_home,window=Tk()):
        self.win = window
        self.win.title("Smart Home App")
        self.width = 400
        self.height = 150
        self.win.geometry(f"{self.width}x{self.height}")
        self.win.resizable(True, True)

        self.main_frame = Frame(self.win)
        self.main_frame.grid(padx=10, pady=10)
        self.smart_home = smart_home
        
        
        
        self.num_rows = 1
        self.label_text = []
        self.toggles = []
        self.deletes = []
        self.edits = []
        self.labels = []
        self.value = IntVar()


    def run(self,on_own=False):
        if on_own:
            self.create_widgets()
            self.win.mainloop()
        else:
            self.win.withdraw()
        
    def create_widgets(self):
        
        button_turn_on_all = Button(self.main_frame,text="Turn On All", command=self.turn_on)
        button_turn_on_all.grid(row=0,column=0)

        button_turn_off_all = Button(self.main_frame,text="Turn Off All", command=self.turn_off)
        button_turn_off_all.grid(row=0,column=1)
        self.button_add = Button(self.main_frame,text="Add",command=lambda: self.create_item()) #for now this element is just text
        self.button_add.grid(row=self.num_rows+1,column=0)
        for i in range(len(self.smart_home.devices)):
            self.create_item_and_buttons(i,self.smart_home.get_device(i))
        
        
        

    
    def create_item_and_buttons(self,index,element,column_add=0):
        label_item_text = StringVar(self.main_frame)
        element = element.str_gui()
        if len(self.smart_home.devices) <= self.smart_home.max_items:
            self.num_rows +=1
            label_item_text.set(element)
            print(label_item_text.get())   
            if self.width != 0:    
                self.button_add.grid(row=self.num_rows+1+column_add,column=0)
            label_item = Label(self.main_frame,textvariable=label_item_text)
            label_item.grid(row=self.num_rows+column_add,column=0)
            self.labels.append(label_item)
            item_toggle = Button(self.main_frame,text="Toggle",command=lambda: self.toggle_individual_item(item_toggle))
            item_toggle.grid(row=self.num_rows+column_add,column=1)

            item_edit = Button(self.main_frame,text="Edit",command=lambda: self.edit_item(item_edit))
            item_edit.grid(row=self.num_rows+column_add,column=2)

            item_delete = Button(self.main_frame,text="Delete",command=lambda: self.delete_item(item_delete,item_toggle,item_edit,label_item))
            item_delete.grid(row=self.num_rows+column_add,column=3)

            self.label_text.append(label_item_text)
            self.toggles.append(item_toggle)
            self.deletes.append(item_delete)
            self.edits.append(item_edit)
            self.main_frame.update_idletasks() 
            width = self.main_frame.winfo_width()
            height = self.main_frame.winfo_height()
            self.win.geometry(f"{width+20}x{height+50}")
            print(self.smart_home)
        else:
            raise ValueError("Maximum limit of devices reached")
            
    
    def turn_on(self):
        self.smart_home.switch_all_on()
        print(self.smart_home)
        for i in range(len(self.smart_home.devices)):
            self.label_text[i].set(self.smart_home.get_device(i).str_gui())
    def turn_off(self):
        self.smart_home.switch_all_off()
        print(self.smart_home)
        for i in range(len(self.smart_home.devices)):
            self.label_text[i].set(self.smart_home.get_device(i).str_gui())

    def toggle_individual_item(self,item_toggle):
        value = self.toggles.index(item_toggle)
        self.smart_home.get_device(value).toggle_switch()
        self.label_text[value].set(self.smart_home.get_device(value).str_gui())
        print(self.smart_home)

    
    def edit_value(self,index,local_value,edit_window):
        edit_window.destroy()
        if type(self.smart_home.get_device(index)) != SmartDoor:
            try:
                value = local_value.get()
                value = int(value)
                if type(self.smart_home.get_device(index)) == SmartLight:    
                    try:
                        self.smart_home.get_device(index).brightness = value
                        self.label_text[index].set(self.smart_home.get_device(index).str_gui())

                    except (TypeError,ValueError) as error:
                        messagebox.showinfo(message=error)
                elif type(self.smart_home.get_device(index)) == SmartPlug:
                    try:
                        self.smart_home.get_device(index).consumption_rate = value
                        self.label_text[index].set(self.smart_home.get_device(index).str_gui())
                    except (TypeError,ValueError) as error:
                        messagebox.showinfo(message=error)
            except ValueError as error:
                messagebox.showinfo(message="Please enter a valid integer")
        print(self.smart_home)
    
    def toggle_lock_button(self,index,edit_window):
        self.smart_home.get_device(index).toggle_lock()
        self.label_text[index].set(self.smart_home.get_device(index).str_gui())
        edit_window.destroy()
        print(self.smart_home)
            
    
    def edit_item(self,item_edit):
        index = self.edits.index(item_edit)
        edit_window = Tk()
        label_edit_text = StringVar()
        edit_window.geometry("400x200")
        edit_window.title("Edit value")
        editmain_frame = Frame(edit_window)
        editmain_frame.grid(padx=10, pady=10)
        local_value = StringVar(edit_window)
        local_value.set(0)
        if type(self.smart_home.get_device(index)) == SmartLight:
            label_edit_text.set("Edit the brightness of the light")
            
        elif type(self.smart_home.get_device(index)) == SmartPlug:
            label_edit_text.set("Edit the consumption rate of the plug")
        else:
            label_edit_text.set("Toggle whether the door is locked or not")
        label_edit = Label(editmain_frame,text=label_edit_text.get())
        label_edit.grid(row=0,column=0)
        if type(self.smart_home.get_device(index)) != SmartDoor:
            entry_edit_value = Entry(editmain_frame,textvariable=local_value)
            entry_edit_value.grid(row=0,column=1)
            button_edit_value = Button(editmain_frame,text="Apply Changes",command=lambda: self.edit_value(index,local_value,edit_window))
            button_edit_value.grid(row=1,column=0)
        else:
            button_edit_value = Button(editmain_frame,text="Toggle Lock",command=lambda: self.toggle_lock_button(index,edit_window))
            button_edit_value.grid(row=1,column=0)
    
    def create_item(self,column_add=0):
        self.create_window = Tk()
        self.create_window.geometry("400x200")
        self.create_window.title("Create new device")
        self.createmain_frame = Frame(self.create_window)
        self.createmain_frame.grid(padx=10, pady=10)
        label_create = Label(self.createmain_frame,width=30,text="What type do you want your \n device to be, type 'light' \n for a light, 'door' for a door\n or 'plug' for a plug")
        label_create.grid(row=0,column=0,rowspan=2)
        entry_create_value = Entry(self.createmain_frame,textvariable=self.value)
        entry_create_value.grid(row=2,column=0)
        button_create_value = Button(self.createmain_frame,text="Create",command=lambda: self.create_device(entry_create_value,column_add,button_create_value,label_create))
        button_create_value.grid(row=3,column=0) 

    def create_device(self,entry_create_value,column_add,button_create_value,label_create):
        type_of_device = entry_create_value.get()
        label_text = StringVar(self.create_window)
        if type_of_device == "light":
            label_text.set("Put the brightness in here")
            button_create_value.destroy()
            label_create.destroy()
            entry_create_value.destroy()
        elif type_of_device == "plug":
            label_text.set("Put the consumption rate in here")
            button_create_value.destroy()
            label_create.destroy()
            entry_create_value.destroy()
        elif type_of_device == "door":
            label_text.set("Is the door locked?")
            button_yes = Button(self.create_window,text="Yes",command=lambda: self.add_item_list(type_of_device,"True",column_add))
            button_yes.grid(row=5,column=0)
            button_no = Button(self.create_window,text="No",command=lambda: self.add_item_list(type_of_device,"False",column_add))
            button_no.grid(row=5,column=1)
            button_create_value.destroy()
            label_create.destroy()
            entry_create_value.destroy()
        else:
            messagebox.showinfo(message="Entry box must contain either 'plug', 'door' or 'light'")
        label_explain = Label(self.create_window,text=label_text.get())
        label_explain.grid(row=4,column=0)
        if type_of_device == "light" or type_of_device == "plug":
            add_value = StringVar(self.create_window)
            entry_value = Entry(self.create_window,textvariable=add_value)
            entry_value.grid(row=5,column=0)
            button_add_item_list = Button(self.create_window,text="Add Device", command=lambda: self.add_item_list(type_of_device,add_value.get(),column_add))
            button_add_item_list.grid(row=6,column=0)
        
    def add_item_list(self,type_of_device,value,column_add):
        self.create_window.destroy()
        
        if type_of_device == "light":
            try:
                value = float(value)
                item = SmartLight()
                item.brightness = value
            except (ValueError,TypeError) as error:
                messagebox.showinfo(message=error)
        elif type_of_device == "plug":
            try:
                value = float(value)
                item = SmartPlug(value)
            except (ValueError,TypeError) as error:
                messagebox.showinfo(message=error)
        elif type_of_device == "door":
            item = SmartDoor()
            locked = True if value == "True" else False

            item._lock_status = bool(locked)
        
        if len(self.smart_home.devices) < self.smart_home.max_items:
            self.smart_home.add_device(item)
            self.create_item_and_buttons(index=len(self.smart_home.devices),element=item,column_add=column_add)   

        else:
            messagebox.showinfo(message="Maximum limit of devices")
        print(self.smart_home)

    def delete_item(self,item_delete,item_toggle,item_edit,label_item):
        value = self.deletes.index(item_delete)
        self.smart_home.remove_device(value)
        
        item_delete.destroy()
        item_edit.destroy()
        item_toggle.destroy()
        label_item.destroy()
        self.deletes.pop(value)
        self.label_text.pop(value)
        self.edits.pop(value)
        self.toggles.pop(value)
        self.labels.pop(value)
        print(self.smart_home)
    
       

    

def placeholder():
        pass


     

    
def main_task_4():
    
    sha = SmartHomeApp()
    sha.run(True)

def test_smart_home_system(on_own):
    smart_home = SmartHome(29)
    light = SmartLight()
    smart_home.add_device(light)
    door = SmartDoor()
    smart_home.add_device(door)
    plug = SmartPlug(50)
    smart_home.add_device(plug)
    plug_2 = SmartPlug(50)
    plug_3 = SmartPlug(50)
    plug_4 = SmartPlug(50)  
    smart_home.add_device(plug_2)
    smart_home.add_device(plug_3)
    smart_home.add_device(plug_4)
    sha = SmartHomeApp(smart_home)
    sha.run(on_own)  
    return sha

# main_task_4()

# test_smart_home_system(on_own=True)   