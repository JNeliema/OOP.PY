# Smartphone class definition
class Smartphone:
    # Constructor to initialize attributes
    def __init__(self, brand, model, battery_percentage=100):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage
        self.is_on = False
    
    # Method to turn on the smartphone
    def turn_on(self):
        if self.is_on:
            print(f"{self.model} is already on!")
        else:
            self.is_on = True
            print(f"{self.model} is now on.")
    
    # Method to turn off the smartphone
    def turn_off(self):
        if not self.is_on:
            print(f"{self.model} is already off!")
        else:
            self.is_on = False
            print(f"{self.model} is now off.")
    
    # Method to charge the smartphone
    def charge(self, charge_amount):
        self.battery_percentage += charge_amount
        if self.battery_percentage > 100:
            self.battery_percentage = 100
        print(f"{self.model} is charging. Battery is now at {self.battery_percentage}%.")
    
    # Method to display the current status of the smartphone
    def display_status(self):
        status = "on" if self.is_on else "off"
        print(f"{self.model} ({self.brand}) is {status}. Battery: {self.battery_percentage}%")


# Create an object of Smartphone
phone1 = Smartphone("Apple", "iPhone 14", 50)

# Interact with the phone
phone1.display_status()
phone1.turn_on()
phone1.charge(30)
phone1.turn_off()
phone1.display_status()
