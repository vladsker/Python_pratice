def show_magicians(magicians_names):
    """ func """
    for magician in magicians_names:
        print("Magician is " + magician + "\n")

def make_great(magicians, great_magicians):
    """ func """
    for i in range(len(magicians)):
        print(i)
        great_magicians.append("The great " + magicians[i-1])

magicians_list = ["Vlad Skuba", "Alla Kvitka", "Damian Zaremba"]

great_magicians_list = []
make_great(magicians_list[:], great_magicians_list)

show_magicians(magicians_list)
show_magicians(great_magicians_list)