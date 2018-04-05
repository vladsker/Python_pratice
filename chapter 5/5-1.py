import time

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    time.sleep(2)
    print("\nAdding " + requested_topping + ".")

print("\n\nFinished making your pizza!")