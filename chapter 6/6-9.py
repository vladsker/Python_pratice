favourite_places={}

user_1 = input("What is your name? \n\t")
user_1_favourite = []
user_1_favourite.append(
    input("What is your first favourite place, " + user_1 + "? \n\t"))
user_1_favourite.append(
    input("What is your first favourite place, " + user_1 + "? \n\t"))
user_1_favourite.append(
    input("What is your first favourite place, " + user_1 + "? \n\t"))

user_2 = input("What is your name? \n\t")
user_2_favourite = []
user_2_favourite.append(
    input("What is your first favourite place, " + user_2 + "? \n\t"))
user_2_favourite.append(
    input("What is your first favourite place, " + user_2 + "? \n\t"))
user_2_favourite.append(
    input("What is your first favourite place, " + user_2 + "? \n\t"))

user_3 = input("What is your name? \n\t")
user_3_favourite = []
user_3_favourite.append(
    input("What is your first favourite place, " + user_2 + "? \n\t"))
user_3_favourite.append(
    input("What is your first favourite place, " + user_2 + "? \n\t"))
user_3_favourite.append(
    input("What is your first favourite place, " + user_2 + "? \n\t"))

favourite_places = {
    user_1: user_1_favourite,
    user_2: user_2_favourite,
    user_3: user_3_favourite
}

for i,y in favourite_places.items():
    print(str(i)+"\'s favourite numbers are: ","\n\tFirst number:\t",y[0],"\n\tSecond number:\t",y[1],"\n\tThird number:\t",y[2])