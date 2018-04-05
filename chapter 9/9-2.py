class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print("This is restaurant " + self.name + "\nCuisine type is " + self.cuisine + "\n==================================")

    def open_restaurant(self):
        print("Restaurant " + self.name + " is open now")


kiki = Restaurant("Kiki", "Indonesian")
miki = Restaurant("Miki", "Indonesian")
OllieBallen = Restaurant("OllieBallen", "Dutch")

kiki.describe_restaurant()
miki.describe_restaurant()
OllieBallen.describe_restaurant()
