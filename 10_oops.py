class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def display_info(self):
        print("Car Information:")
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Color:", self.color)

def main():
    # Get input from the user
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    year = int(input("Enter the year of manufacture of the car: "))
    color = input("Enter the color of the car: ")
    
    # Create an object of the Car class with user input
    my_car = Car(make, model, year, color)

    print()

    # Display information about the car
    my_car.display_info()

if __name__ == "__main__":
    main()
