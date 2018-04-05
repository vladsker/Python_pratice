print("Hello, dear. This is simple echo program. if you want to quit, please, type \'quit\'")

trigger = True

while trigger:
    echo = input("\nPlease, type something:\t")

    if echo == "quit":
        trigger = False
    else:
        print("Your echo is:\t\t" + echo)
