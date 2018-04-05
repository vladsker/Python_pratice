class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print("This is restaurant " + self.name + "\nCuisine type is " + self.cuisine)

    def open_restaurant(self):
        print("Restaurant " + self.name + " is open now")

kiki = Restaurant("Kiki", "Indonesian")
kiki.describe_restaurant()
kiki.open_restaurant()