aliens=[]

for alien_number in range(30):
    new_alien={"color":"green", "speed":(30-alien_number), "health":(alien_number+1)}
    aliens.append(new_alien)

print("================================================")

for i in aliens:
    print(i)

print("================================================")

for i in aliens[:]:
    if i["color"] == "green":
        i["color"] = "blue"

for i in aliens:
    print(i)


users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())