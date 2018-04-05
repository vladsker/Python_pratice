class user():
    def __init__(self,username,name,surname,age,univ_class):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        self.univ_class = univ_class

    def describe_user(self):
        print("==============================")
        print("Username: " + self.username.lower())
        print("User name and surname: " + self.name.title() + " " +
              self.surname.title())
        print("Age: " + str(self.age))
        print("University class is: " + self.univ_class)
        print("==============================")

    def greet_user(self):
        print("Aloha, " + self.username.title())


user1 = user("Wallie", "Damian", "Zaremba", 12, "12-A")
user1.describe_user()
user1.greet_user()
user2 = user("lambda", "Greig", "Marshall", 42, "12-A")
user2.describe_user()
user2.greet_user()