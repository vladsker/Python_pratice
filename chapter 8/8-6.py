def city_coutry(city="", country=""):
    if city != "" and country !="":
        print(city.title() + ", " + country.title())
        return({city:country})

a = city_coutry("Singapore", "malasia")
b = city_coutry("Kiev", "Ukraine")
c = city_coutry("New-York", "usa")

print(a)
print(b)
print(c)