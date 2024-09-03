class Car:
    # Initialize the Car object with make, model, and year attributes
    def __init__(self, make, model, year):
        self.make = make  # The make of the car 
        self.model = model  # The model of the car 
        self.year = year  # manufacture year

    # Method to display the car's information
    def display_info(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")


my_car = Car("Land Rover", "Defender", 2010)
my_car.display_info()