prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

cities=[]

while True:
    city=input("Please, input city you visited last year ")
    cities.append(city)
    
    if city == "quit":
        break
    else:
        print("I would love to go to "+city)