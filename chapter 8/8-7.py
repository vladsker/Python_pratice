def make_album(artist_name = "", album_name = "", number_of_tracks = 0):
    if artist_name != "" and album_name != "":
        if type(number_of_tracks) == "int" and number_of_tracks > 0:
            return {"artist_name":artist_name, "album_name": album_name, "number_of_tracks":number_of_tracks}
        else:
            return {"artist_name":artist_name, "album_name": album_name}

b = make_album("Oksana Kvitka", "Murka i ko", 12)
c = make_album("Oksana Kvitka", "Murka i ko", "12")
a = make_album("Oksana Kvitka", "Murka i ko")

print(a)
print(b)
print(c)