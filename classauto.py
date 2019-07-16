class Car ():
    def __init__(self,version, model, year):
        """add method car with version, model, year you must put values, and default odometer value as 0"""
        self.version = version
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def describe_name (self): 
        """print car"""
        long_name = ( "Model: " + self.model + " Version: " + self.version + " Year: " + str (self.year))
        print (long_name.title())
    
    def read_odometer(self):
        """read odometer values"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def change_odometer(self, mileage):
        """change odometer values"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print ("You can't roll back an odometer")

    def incremant_odometer (self, miles):
        """add odometer miles"""
        self.odometer_reading+=miles


class Electrocar(Car):
    def __init__(self,version,model,year):
        super().__init__(version,model,year)
        self.battery_size = 70

    def describe_battery (self):
        print ("This car battery has a " + str (self.battery_size) + " size")

    def get_range (self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range 270
    
