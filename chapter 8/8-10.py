def show_magicians(magicians_names=[]):
    for magician in magicians_names:
        print("Magician is " + magician + "\n")

def make_great(magicians_names=[]):
    for i in range(len(magicians_names)):
        magicians_names[i] = "The great " + magicians_names[i]


magicians_list = ["Vlad Skuba", "Alla Kvitka", "Damian Zaremba"]

show_magicians(magicians_list)

make_great(magicians_list)

show_magicians(magicians_list)
