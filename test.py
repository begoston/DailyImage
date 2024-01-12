import datetime
import json
import random

daily_img = random.randint(1, 10)
def check_data():
    try:
        # Jsonfile olvasás próba
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        # Ha a fájl nem létezik, dictionariadatok létrehozása íráshoz
        data = {'current_value': datetime.datetime.now().day, 'last_update': 0, 'daily_img': daily_img}

    # dictionari filebaírása
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)


def upgrade_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    print(data['current_value'], data['last_update'])
    if data['current_value'] == data['last_update']:
        #ha egyenlo, cover ne toltodjon be
        print("A mai kepet mar megkaptad.")
        print(data['daily_img'])
    else:
        # ha nem egyenlo a legutobbi frissites datummal, frissul a last_update a maira, és frissul a daily_img
        data['last_update'] = datetime.datetime.now().day
        data['daily_img'] = daily_img
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=2)
        print("Uj kepet kaptal.")
        print(data['daily_img'])


check_data()
upgrade_data()

# d = 6
# date = datetime.datetime.now()
# print(datetime.datetime.now().day, d)

# l = ['wfsdf', '12wdfw', 'khjk']
# print(random.choice(l))


# import random
#
# imgfolder = 'images/'
# imglist = ['Image01.jpg', 'Image02.jpg', 'Image03.jpg']
# selectedimg = random.randint(0, len(imglist)-1)
#
# print(selectedimg)
# print(imgfolder + imglist[selectedimg])