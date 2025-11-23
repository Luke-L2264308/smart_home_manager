class SmartObject:
    def __init__(self):
        self.switched_on = False
    def toggle_switch(self):
        self.switched_on = not self.switched_on

class SmartPlug(SmartObject):
    def __init__(self,consumption_rate=50):
        super().__init__()
        if type(consumption_rate) == float or type(consumption_rate) == int:
            if 0<=consumption_rate<=150:
                self._consumption_rate = consumption_rate
            else:
                raise ValueError("Invalid initialisation was blocked as consumption rate must be between 0 and 150")
        else:
            raise ValueError("Invalid initialisation was blocked as consumption rate must be a float")
        
    @property
    def consumption_rate(self):
        return self._consumption_rate
    @consumption_rate.setter
    def consumption_rate(self,rate):
        if 0<=rate<=150:
            self._consumption_rate = rate   
        else: 
            raise ValueError("Consumption rate needs to be between 0 and 150")
            
    def str_gui(self):
        on_string = "on" if self.switched_on else "off"
        return f"SmartPlug:{on_string} consumption rate: {self.consumption_rate}"
    def __str__(self):
        on_string = "on" if self.switched_on else "off"
        return f"SmartPlug is {on_string} with a consumption rate of {self.consumption_rate}"
def test_smart_plug():
    try:
        plug = SmartPlug(45)
    except ValueError as e:
        print(e)
    
    print(plug)
    plug.toggle_switch()
    print(plug)
    try:
        plug.consumption_rate = 75
    except ValueError as e:
        print(e)
    print(plug)
    plug.toggle_switch()
    print(plug)
    try:
        plug.consumption_rate = 200
    except ValueError as e:
        print(e)
    print(plug)
    try:
        plug.consumption_rate = -10
    except ValueError as e:
        print(e)
    print(plug)
    try:
        plug_1 = SmartPlug(-5)
    except ValueError as e:
        print(e)
    try:
        plug_2 = SmartPlug(160)
    except ValueError as e:
        print(e)
# test_smart_plug()

class SmartDoor(SmartObject):
    def __init__(self):
        super().__init__()
        self._lock_status = True    
    def toggle_lock(self):
        self._lock_status = not self._lock_status
    def str_gui(self):
        lock_string = "Yes" if self._lock_status else "No"
        on_string = "on" if self.switched_on else "off"
        return f"SmartDoor: {on_string} Locked: {lock_string}"
    
    def __str__(self):
        lock_string = "locked" if self._lock_status else "unlocked"
        on_string = "on" if self.switched_on else "off"
        return f"SmartDoor is {on_string} and {lock_string}"

class SmartLight(SmartObject):
    def __init__(self):
        super().__init__()
        self._brightness = 50
    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self,brightness):
        if type(brightness) != int and type(brightness) != float:
            raise TypeError("Brightness must be an integer or a float")
        elif 0<=brightness<=100:
            self._brightness = brightness
        else: 
            print("Brightness must be between 0 and 100")
            raise ValueError("Brightness must be between 0 and 100")
    
    def str_tkinter(self):
        return 

    def str_gui(self):
        on_string = "on" if self.switched_on else "off"
        brightness = self.brightness #check this bit before submitting (however seems like common sense)
        if not self.switched_on:
            brightness = 0    
        return f"Light: {on_string}, brightness: {brightness}"    

    def __str__(self):
        on_string = "on" if self.switched_on else "off"
        brightness = self.brightness #check this bit before submitting (however seems like common sense)
        if not self.switched_on:
            brightness = 0

        return f"SmartLight is {on_string} with a brightness of {brightness}"
    
def test_custom_device():
    door = SmartDoor()
    print(door)
    light = SmartLight()
    print(light)
    door.toggle_switch()
    print(door)
    light.toggle_switch()
    print(light)
    door.toggle_lock()
    print(door)
    try:
        light.brightness = 75
    except ValueError as e:
        print(e)
    print(light)
    try:
        light.brightness = -5
    except ValueError as e:
        print(e)
    print(light)
    try:
        light.brightness = 200
    except ValueError as e:
        print(e)
    print(light)
    
    
# test_custom_device()

class SmartHome:
    def __init__(self,max_items):
        self.devices = []
        if max_items>0:
            self.max_items = max_items
        else:
            return ValueError("Max items must be greater than 0")
    def add_device(self,device):
        if len(self.devices) == self.max_items:
            print("SmartHome is full")
        else:
            self.devices.append(device)
    def get_device(self,index):
        try:
            return self.devices[index]
        except IndexError:
            print("Index out of range")
        
    def update_device(self,index,value=None):
        print(type(self.devices[index]))
        if type(self.devices[index]) == SmartDoor:
            self.devices[index].toggle_lock()
        elif type(self.devices[index]) == SmartLight:
            try:
                self.devices[index].brightness = value
                print("Brightness updated")
            except ValueError as e:
                print(e)
        elif type(self.devices[index]) == SmartPlug:
            try:
                self.devices[index].consumption_rate = value
            except ValueError as e:
                print(e)
    def remove_device(self,index):
        try:
            self.devices.pop(index)
        except IndexError:
            print("Index out of range")
    def toggle_device(self,index):
        self.devices[index].toggle_switch()
    def switch_all_on(self):
        for device in self.devices:
            if not device.switched_on:
                device.toggle_switch()
    def switch_all_off(self):
        for device in self.devices:
            if device.switched_on:
                device.toggle_switch()
    
    def __str__(self):
        output = f"SmartHome has {len(self.devices)} devices and a limit of {self.max_items}\n"
        for device in self.devices:
            output += f"{device}\n"
        return output
    
def test_smart_home():
    home = SmartHome(3)
    plug = SmartPlug(50)
    door = SmartDoor()
    light = SmartLight()
    home.add_device(plug)
    home.add_device(door)
    home.add_device(light)
    print(home)
    print(home.get_device(0))
    print(home.get_device(1))
    print(home.get_device(2))
    home.toggle_device(0)
    home.toggle_device(1)
    home.toggle_device(2)
    print(home)
    home.switch_all_off()
    print(home)
    home.switch_all_on()
    print(home)
    try:
        home.add_device(SmartPlug(50))
    except ValueError as e:
        print(e)
    try:
        home.update_device(0,75)
    except ValueError as e:
        print(e)
    print(home)
    try:
        home.update_device(0,200)
    except ValueError as e:
        print(e)
    print(home)
    try:
        home.update_device(2,75)
    except ValueError as e:
        print(e)
    print(home)
    try:
        home.update_device(2,200)
    except ValueError as e:
        print(e)    
    try:
        home.remove_device(0)
    except IndexError as e:
        print(e)
    try:
        home.remove_device(2)
    except IndexError as e:
        print(e)
    try:
        home.remove_device(-6)
    except IndexError as e:
        print(e)
    print(home)
    




# test_smart_home()
    
