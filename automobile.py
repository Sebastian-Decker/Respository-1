class Automobile(object): #same as automobile:
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
    
    def set_make(self, make):
        self.__make = make

    def get_make(self):
        return self.__make

    def set_model(self, model):
        self.__model = model
    
    def get_make(self):
        return self.__model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def get_mileage(self):
        return self.__mileage

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

class Car(Automoblie):
    def __init__(self, make, model, mileage, price, doors):
        Automobile.__init__(make, model, mileage, price)

        self.__doors = doors

    def set_doors(self, doors):
        self.__doors = doors

    def get_doors(self):
        return self.__doors

    def __str__(self):
        return f"""
        Make: {self.get_make()}
        Model: {self.get_model()}
        Mileage: {self.get_mileage()}
        Price: ${self.get_price()}
        Drivetrain: {self.get_drive_train()}
        """
    def print_automobile(self, automobile: Automobile):
        print(automobile)


    def main(self):
        sams_car = Car("Honda", "EX", 125000, 3000, 2)
        kates_truck = Truck("GMC", "Sierra", 20000, 35000, 3, "4x4")
        kaylee_car = Car("Toyota", "Camry", 45000, 15000, 2)

    class Truck(Automobile):
        def __init__(self, make, model, mileage, price, drive_train):
            Automobile