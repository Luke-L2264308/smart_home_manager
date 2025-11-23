from tkinter import Tk, Frame, Label, Entry, Button, IntVar, StringVar, messagebox,DoubleVar
from coursework2_frontend import SmartHomeApp,test_smart_home_system
from python_coursework_2_improvedplug import SmartHome, SmartDoor, SmartLight, SmartPlug
import os
class SmartHomesApp(SmartHomeApp):
    
    def __init__(self):
        self.win = Tk()
        self.win.title("Smart Home App")
        self.width = 400
        self.height = 50
        self.win.geometry(f"{self.width}x{self.height}")
        self.win.resizable(True, True)

        self.main_frame = Frame(self.win)
        self.main_frame.grid(padx=10, pady=10)
        self.num_rows = 0
        self.button_smart_homes = []
        self.smart_homes = []
        self.label_devices = []
        self.num_limits = []
    
    def run(self):
        self.create_widgets()
        self.win.mainloop()
    
    def create_widgets(self):
        
        button_overview = Button(self.main_frame,text="Overview",command=lambda: self.summary())
        button_overview.grid(row=0,column=0)
        self.button_add_home = Button(self.main_frame,text="Add home",command=lambda: self.smart_home_option())
        self.button_add_home.grid(row=0,column=self.num_rows+1)
        self.button_remove_home = Button(self.main_frame,text="Remove home",command=lambda: self.remove_smart_home())
        self.button_remove_home.grid(row=0,column=self.num_rows+2)
        self.save_button = Button(self.main_frame,text="Save",command=lambda: self.save())
        self.save_button.grid(row=0,column=self.num_rows+3)
        self.load()
        self.summary()
    
    def load(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
        file = open("smart homes","r")
        lines = file.readlines()
        index = -1
        if lines != ['\n']:
            for line in lines:
                line = line.split()
                if line[0] != "SmartHome":

                    class_type = self.get_class(line[0])
                    attribute = class_type
                    
                    attribute.switched_on = self.is_switched_on(attribute,line[2])
                    if attribute == SmartLight:
                        attribute.brightness = int(line[-1])
                    elif attribute == SmartDoor:
                        if line[-1] == "locked":
                            attribute.locked = True
                        else:
                            attribute.locked = False
                    elif attribute == SmartPlug:
                        attribute.consumption_rate = int(line[-1])
                    self.smart_homes[index].add_device(attribute)
                else:
                    if index != -1:
                        self.add_to_system(self.num_limits[index],self.smart_homes[index])
                    self.smart_homes.append(SmartHome(int(line[-1])))
                    self.num_limits.append(int(line[2]))
                    index += 1
                    self.height += 50
                    self.win.geometry(f"{self.width}x{self.height}")
            self.add_to_system(self.num_limits[index],self.smart_homes[index])
        print(self.smart_homes[3])
        

    def get_class(self,word):
        if word == "SmartLight":
            return SmartLight()
        elif word == "SmartDoor":
            return SmartDoor()
        elif word == "SmartPlug":
            return SmartPlug()
    
        

    def is_switched_on(self,attribute,word):
        if word == "on":
            attribute.switched_on = True
        else:
            attribute.switched_on = False
        return attribute.switched_on

    def save(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
        file = open("smart homes","w")
        for i in range(len(self.smart_homes)):
            file.write(str(self.smart_homes[i]))
            


    def remove_smart_home(self):
        self.destroy_widgets()
        self.update_window_size()
        num_remove = IntVar()
        label_instructions = Label(self.main_frame,text="type in the number of \n the smart home you \n want to remove")
        label_instructions.grid(row=1,column=0)
        entry_remove = Entry(self.main_frame,width=5,textvariable=num_remove)
        entry_remove.grid(row=1,column=1)
        button_remove = Button(self.main_frame,text="Press to Remove",command=lambda: self.remove_home(num_remove.get()))
        button_remove.grid(row=2,column=0)
    
    def remove_home(self,num_remove):
        try:
            self.button_smart_homes[num_remove-1].destroy()
            self.button_smart_homes.pop(num_remove-1)
            self.smart_homes.pop(num_remove-1)
            self.num_limits.pop(num_remove-1)
        except (IndexError) as error:
            messagebox.showinfo(message=error)
    
    
    def destroy_widgets(self):
        for widget in self.main_frame.winfo_children():
            grid_info = widget.grid_info()
            widget_row = int(grid_info.get("row", -1))
            if widget_row > 0:
                widget.destroy()
    
    
    def summary(self):
        self.destroy_widgets()
        for i in range(len(self.smart_homes)):
            num_switched_on = 0
            num_devices = len(self.smart_homes[i].devices)
            for j in range(num_devices):
                if self.smart_homes[i].get_device(j).switched_on:
                    num_switched_on += 1
            label_summary = Label(self.main_frame,text=f"SmartHome {i+1}\n  number of devices: {num_devices} \n limit:{self.num_limits[i]}  \n no. of devices switched on: {num_switched_on} ")
            label_summary.grid(row=i+1,column=0)
            
        self.update_window_size()
    
    def update_window_size(self):
        self.main_frame.update_idletasks() 
        width = self.main_frame.winfo_width()
        height = self.main_frame.winfo_height()
        self.win.geometry(f"{width+100}x{height+100}")
    
    def smart_home_option(self):
        self.destroy_widgets()
        self.update_window_size()
        num_limit = IntVar(self.main_frame)
        label_instructions = Label(self.main_frame,text="What is the maximum \n amount of devices this \n smart home should have")
        label_instructions.grid(row=1,column=0)
        entry_limit = Entry(self.main_frame,width=5,textvariable=num_limit)
        entry_limit.grid(row=1,column=1)
        button_limit = Button(self.main_frame,text="Confirm",command=lambda: self.add_smart_home(num_limit.get()))
        button_limit.grid(row=2,column=0)
    
    

    def add_smart_home(self,num_limit):
 
        try:
            smart_home = SmartHome(num_limit)
            
        except TypeError as error:
            messagebox.showinfo(message="Inputted value needs to be an integer number greater than 0")
        self.num_limits.append(num_limit)
        # smart_home = self.create_example_smart_home(smart_home)

        self.smart_homes.append(smart_home)
        self.add_to_system(num_limit,smart_home)
        

    def add_to_system(self,num_limit,smart_home):
        button_smart_home= Button(self.main_frame,text=f"Smart Home {len(self.button_smart_homes)+1}",command=lambda: self.access_smart_home(smart_home,button_smart_home))
        button_smart_home.grid(row=0,column=self.num_rows+1)
        self.button_smart_homes.append(button_smart_home)
        self.num_rows += 1
        self.button_add_home.grid(row=0,column=self.num_rows+1)
        self.button_remove_home.grid(row=0,column=self.num_rows+2)
        self.save_button.grid(row=0,column=self.num_rows+3)
        self.update_window_size()

        

    # def create_example_smart_home(self,smart_home):
    #     light = SmartLight()
    #     smart_home.add_device(light)
    #     door = SmartDoor()
    #     smart_home.add_device(door)
    #     plug = SmartPlug(50)
    #     smart_home.add_device(plug)
    #     plug_2 = SmartPlug(50)
    #     plug_3 = SmartPlug(self.num_rows)
    #     plug_4 = SmartPlug(50)
    #     smart_home.add_device(plug_2)
    #     smart_home.add_device(plug_3)
    #     smart_home.add_device(plug_4)
    #     return smart_home
    
    

    def access_smart_home(self,smart_home,button_smart_home):
        sha = SmartHomeApp(smart_home,self.win)
        sha.main_frame = self.main_frame
        
        self.destroy_widgets()
        sha.button_add = Button(self.main_frame,text="Add",command=lambda: sha.create_item(2))
        sha.button_add.grid(row=sha.num_rows+1,column=1)
        
        for i in range(len(smart_home.devices)):
            try:
                sha.create_item_and_buttons(i,smart_home.get_device(i),1)
            except ValueError as error:
                messagebox.showinfo(message=error)
        index = self.button_smart_homes.index(button_smart_home)
        self.smart_homes[index] = smart_home
        self.button_turn_on_all = Button(self.main_frame,text="Turn on all",command=lambda: sha.turn_on())
        self.button_turn_on_all.grid(row=1,column=2)
        self.button_turn_off_all = Button(self.main_frame,text="Turn off all",command=lambda: sha.turn_off())
        self.button_turn_off_all.grid(row=1,column=3)
        
       

def main():
    test_smart_home_system(on_own=False)
    
    sha = SmartHomesApp()
    sha.run()
    

main()
    
    