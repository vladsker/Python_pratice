class user():
    def __init__(self,username,name,surname,age,univ_class):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        self.univ_class = univ_class
        self.login_attempts = 0

    def describe_user(self):
        print("==============================")
        print("Username: " + self.username.lower())
        print("User name and surname: " + self.name.title() + " " +
              self.surname.title())
        print("Age: " + str(self.age))
        print("University class is: " + self.univ_class)
        print("Login attempts: " + str(self.login_attempts))
        print("==============================")

    def greet_user(self):
        print("Aloha, " + self.username.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = user("Wallie", "Damian", "Zaremba", 12, "12-A")
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.describe_user()
user1.increment_login_attempts()
user1.describe_user()
user1.increment_login_attempts()
user1.describe_user()
user1.increment_login_attempts()
user1.describe_user()
user1.increment_login_attempts()
user1.describe_user()
user1.reset_login_attempts()
user1.describe_user()
user2 = user("lambda", "Greig", "Marshall", 42, "12-A")
user2.describe_user()
user2.greet_user()