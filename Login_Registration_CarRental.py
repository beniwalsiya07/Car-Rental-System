class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class CarRentalSystem:
    def __init__(self):
        self.users = []

    def register(self, username, password):
        for user in self.users:
            if user.username == username:
                return "Username already exists. Please choose a different username."
        self.users.append(User(username, password))
        return "Registration successful. You can now log in."

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return f"Welcome, {username}!"
        return "Invalid username or password."

# Sample usage
car_rental_system = CarRentalSystem()

while True:
    print("\nMenu:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        print(car_rental_system.register(username, password))
    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        print(car_rental_system.login(username, password))
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
