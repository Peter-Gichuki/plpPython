# A program that implements a class hierarchy for smartphones, game consoles, and tablets, demonstrating inheritance and polymorphism.
# The base class is Smartphone, which has methods to send text messages and take photos.
# The GameConsole class inherits from Smartphone and adds methods for playing games.
# The Tablet class inherits from GameConsole and adds methods for watching movies.
# The EcoSmartphone class demonstrates polymorphism by overriding the send_text method to include eco mode functionality.

#Creating the base class Smartphone which has methods to send text messages and take photos.
class Smartphone:

    def __init__(self, brand, model, storage_capacity): # Initialize the smartphone with brand, model, and storage capacity
        self.brand = brand
        self.model = model
        self.storage_capacity = storage_capacity

    def send_text(self, contact, message):
        print(f"Sending text to {contact}: {message}")
    
    def take_photo(self):
        print(f"{self.brand} {self.model} takes the best quality photos!")

# Creating the GameConsole class which inherits from Smartphone and adds methods for playing games with additional attributes like battery life and gpu.    
class GameConsole(Smartphone):
    def __init__(self, brand, model, storage_capacity, battery_life, gpu):# Initialize the game console with brand, model, storage capacity, battery life, and gpu
        super().__init__(brand, model, storage_capacity)# Initialize the base class
        self.battery_life = battery_life
        self.gpu = gpu

    def play_game(self, game_name):
        print(f"Playing {game_name} on {self.brand} {self.model} with {self.gpu} gpu and {self.battery_life} of battery life.")

# Creating the Tablet class which inherits from GameConsole and adds methods for watching movies with additional attributes like screen size and operating system.
class Tablet(GameConsole):
    def __init__(self, brand, model, storage_capacity, battery_life, gpu, screen_size, operating_system):
        super().__init__(brand, model, storage_capacity, battery_life, gpu)# Initialize the base class
        self.screen_size = screen_size
        self.operating_system = operating_system

    def watch_movie(self, movie_name):
        print(f"I am watching {movie_name} on my {self.brand} {self.model} tablet with  {self.screen_size} and {self.storage_capacity} storage capacity.")
        print(f"This tablet runs on {self.operating_system} operating system with {self.battery_life} of battery life and {self.gpu} gpu.")


#implementation of polymorphism
# Creating the EcoSmartphone class which inherits from Smartphone and overrides the send_text method to include eco mode functionality.
# The EcoSmartphone class has additional attributes like eco mode and methods to enable and disable eco mode.
# EcoSmartphone class demonstrates polymorphism by overriding the send_text method to include eco mode functionality.
class EcoSmartphone(Smartphone):
    def __init__(self, brand, model, storage_capacity, eco_mode=False):
        super().__init__(brand, model, storage_capacity)
        self.eco_mode = eco_mode

    def enable_eco_mode(self):
        self.eco_mode = True
        print("Eco mode enabled: Reducing display brightness, limiting app usage, and minimizing background activities.")

    def disable_eco_mode(self):
        self.eco_mode = False
        print("Eco mode disabled: Restoring normal settings.")

    def send_text(self, contact, message):
        if self.eco_mode:
            print(f"Sending text to {contact} in eco mode: {message}")
        else:
            super().send_text(contact, message)
 
# Example usage of the classes
# Creating instances of each class, Smartphone, GameConsole, Tablet, and EcoSmartphone classes and call their methods.
my_phone = Smartphone("Samsung", "Galaxy S21 Ultra", "512GB")
my_game_console = GameConsole("Sony", "PlayStation 5", "825GB", "10 hours", "AMD RDNA 2") 
my_tablet = Tablet("Apple", "iPad Pro", "1TB", "12 hours", "Apple M1", "12.9 inches", "iOS")
my_eco_phone = EcoSmartphone("Nokia", "EcoPhone", "64GB")

# Calling methods from each class to demonstrate functionality
my_phone.send_text("+254112345678", "Hello, how are you?")
my_phone.take_photo()

my_game_console.play_game("The Last of Us Part II")

my_tablet.watch_movie("Inception")

# Calling methods from EcoSmartphone class to demonstrate polymorphism
my_eco_phone.enable_eco_mode()
my_eco_phone.send_text("+254876543210", "Hello, this is an eco-friendly message!")
my_eco_phone.disable_eco_mode()

        