import os
os.environ['KIVY_NO_CONSOLELOG'] = "1"

#create local config files
cwd = os.getcwd()
os.environ['KIVY_HOME'] = cwd + "/conf"

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.config import Config
from kivy.animation import Animation
import random
import datetime
import json

Config.set('graphics', 'resizeable', True)



class MainWidget(RelativeLayout):
    def __init__(self):
        super().__init__()

        extension = '.jpg'
        imgfolder = 'images/'
        imglist = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010']
        daily_img = random.choice(imglist)
        current_value = datetime.datetime.now().day


        def check_data():
            try:
                # Jsonfile olvasás próba
                with open('data.json', 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                # Ha a fájl nem létezik, dictionariadatok létrehozása íráshoz
                data = {'last_update': 0, 'daily_img': daily_img}

            # dictionari filebaírása
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=2)

        def upgrade_data():
            with open('data.json', 'r') as file:
                data = json.load(file)
            if current_value != data['last_update']:
                # ha nem egyenlo a legutobbi frissites datummal, frissul a last_update a maira, és frissul a daily_img
                data['last_update'] = datetime.datetime.now().day
                data['daily_img'] = daily_img
                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=2)

        check_data()
        upgrade_data()

        with open('data.json', 'r') as file:
            data = json.load(file)

        img = Image(source=imgfolder + data['daily_img'] + extension, size_hint=(0.8, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        cover = Image(source='images/Cover.jpg', size_hint=(0.8, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.5}, color=(1,1,1,1))
        anim = Animation(color=(1,1,1,0))

        def start_animation(instance):
            anim.start(cover)

        bigbtn = Button(size_hint=(1, 1), background_color=(0,0,0,0), on_press=(start_animation))
        self.add_widget(img)
        self.add_widget(cover)
        self.add_widget(bigbtn)






class DailySexPoseApp(App):
    def build(self):
        return MainWidget()



if __name__ == "__main__":
    DailySexPoseApp().run()
