def make_tshirt(t_shirt_size = "XL",t_shirt_text = "I love Python", t_shirt_color = ""):
    if not t_shirt_color:
        print("T-shirt size is: " + str(t_shirt_size))
        print("T-shirt text is: " + t_shirt_text)

print("1\n")
make_tshirt(36 , "Hello,world")
print("2\n")
make_tshirt(t_shirt_size = 36, t_shirt_text = "Hello, Yamaika")
print("3\n")
make_tshirt(t_shirt_text="Hello, Yamaika", t_shirt_size=36)
print("4\n")
make_tshirt()