print(" This is a calculator. To exit, please, use \'q\'")

while True:

    a = input("Please, type a number a ")
    if a != 'q':
        try:
            int_a = int(a)
        except ValueError:
            print("Input is not a number. Please, provide correct data.")
            continue
    else:
        break

    b = input("Please, type a number b ")

    if b != 'q':
        try:
            int_b = int(b)
        except ValueError:
            print("Input is not a number. Please, provide correct data.")
            continue
    else:
        break
