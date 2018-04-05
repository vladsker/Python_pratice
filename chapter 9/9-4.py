class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("This is restaurant " + self.name + "\nCuisine type is " + self.cuisine)

    def open_restaurant(self):
        print("Restaurant " + self.name + " is open now")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self,increment):
        self.number_served += increment

    def print(self):
        print("Restaurant name: " + self.name + ". Customers served: " + str(
            self.number_served))

restaurant = Restaurant("Kiki", "Indonesian")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.print()
restaurant.set_number_served(6)
restaurant.print()
restaurant.increment_number_served(6)
restaurant.print()
restaurant.increment_number_served(6)
restaurant.print()
restaurant.increment_number_served(6)
restaurant.print()
restaurant.increment_number_served(6)
restaurant.print()