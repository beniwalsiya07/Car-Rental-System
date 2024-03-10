class Car:
    def __init__(self, model, price_per_day):
        self.model = model
        self.price_per_day = price_per_day
        self.available = True

class RentalSystem:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def rent_car(self, model, rental_duration):
        for car in self.cars:
            if car.model == model and car.available:
                total_price = car.price_per_day * rental_duration
                car.available = False
                return f"Car rented successfully for {rental_duration} days. Total amount to pay: {total_price}"
        return "Car not available for rent."

    def return_car(self, model):
        for car in self.cars:
            if car.model == model and not car.available:
                car.available = True
                return "Car returned successfully. Thank you!"
        return "Car not rented or already returned."

    def inquire_cars(self, model=None, max_price=None):
        results = []
        for car in self.cars:
            if (not model or car.model.lower() == model.lower()) and (not max_price or car.price_per_day <= max_price):
                results.append(car)
        return results

# Create rental system and add some cars
rental_system = RentalSystem()
rental_system.add_car(Car("Toyota Camry", 50))
rental_system.add_car(Car("Honda Accord", 60))
rental_system.add_car(Car("Ford Mustang", 70))

while True:
    print("\nMenu:")
    print("1. Rent a car")
    print("2. Return a car")
    print("3. Inquire about cars")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        model = input("Enter the model of the car you want to rent: ")
        rental_duration = int(input("Enter the rental duration (in days): "))
        print(rental_system.rent_car(model, rental_duration))
    elif choice == "2":
        model = input("Enter the model of the car you want to return: ")
        print(rental_system.return_car(model))
    elif choice == "3":
        model = input("Enter the model of the car you are looking for (leave blank for any): ")
        max_price = input("Enter the maximum price per day you want to pay (leave blank for any): ")
        if max_price:
            max_price = float(max_price)
        results = rental_system.inquire_cars(model=model, max_price=max_price)
        if results:
            print("\nMatching cars found:")
            for car in results:
                print(f"Model: {car.model}, Price per day: {car.price_per_day}")
        else:
            print("\nNo matching cars found.")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")




    