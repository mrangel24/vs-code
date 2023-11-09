class Vehicle: # superclass
    def __init__(self, vehicle_type):
        # Constructor 
        self.vehicle_type = vehicle_type

# Automobile class inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        # constructor of the parent class Vehicle
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        # format display information
        return (
            f"Vehicle type: {self.vehicle_type}\n"
            f"Year: {self.year}\n"
            f"Make: {self.make}\n"
            f"Model: {self.model}\n"
            f"Number of doors: {self.doors}\n"
            f"Type of roof: {self.roof}\n"
        )

def main():
    vehicle_type = input("Vehicle type: ")
    year = input("Year manufactured: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("# of Doors: ")
    roof = input("Type of roof: ")
    
    car = Automobile(vehicle_type, year, make, model, doors, roof)
    
    print(car.display_info())

main()

