import random
import string
import os
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard
from kivy.clock import Clock
from kivy.utils import get_color_from_hex

# Integrazione AdMob
try:
    from kivmob import KivMob
except ImportError:
    KivMob = None

class MatrixBackground(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = get_color_from_hex('#00FF41')
        self.opacity = 0.6
        self.font_size = '14sp'
        self.halign = 'center'
        self.valign = 'middle'
        Clock.schedule_interval(self.update_matrix, 0.15)

    def update_matrix(self, dt):
        caratteri = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*+<>?/\\"
        righe = []
        for _ in range(50): 
            righe.append('  '.join(random.choice(caratteri) for _ in range(30)))
        self.text = '\n'.join(righe)

class MatrixPasswordApp(App):
    def build(self):
        # Inizializzazione AdMob con i tuoi ID REALI
        if KivMob:
            # Tuo ID APP reale
            self.ads = KivMob("ca-app-pub-2537033671132924~2402224670")
            # Tuo ID Unità Banner reale
            self.ads.new_banner("ca-app-pub-2537033671132924/3739357078", top_pos=False)
            self.ads.request_banner()
            self.ads.show_banner()

        main_layout = FloatLayout()
        main_layout.add_widget(MatrixBackground())
        
        ui_layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        self.lbl_password = Label(
            text="MATRIX PASSGEN",
            font_size='28sp',
            font_name='Roboto',
            color=get_color_from_hex('#00FF41'),
            bold=True,
            halign='center'
        )
        ui_layout.add_widget(self.lbl_password)
        
        btn_generate = Button(
            text="GENERA E COPIA",
            size_hint=(1, 0.2),
            background_color=get_color_from_hex('#008F11'),
            color=(1, 1, 1, 1),
            font_size='20sp',
            bold=True
        )
        btn_generate.bind(on_release=self.genera_e_suona)
        ui_layout.add_widget(btn_generate)
        
        main_layout.add_widget(ui_layout)
        return main_layout

    def genera_password_sicura(self):
        lunghezza = 16
        maiuscole = string.ascii_uppercase
        minuscole = string.ascii_lowercase
        numeri = string.digits
        speciali = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        password = [
            random.choice(maiuscole),
            random.choice(minuscole),
            random.choice(numeri),
            random.choice(speciali)
        ]
        
        tutti_caratteri = maiuscole + minuscole + numeri + speciali
        password += [random.choice(tutti_caratteri) for _ in range(lunghezza - 4)]
        random.shuffle(password)
        return ''.join(password)

    def genera_e_suona(self, instance):
        nuova_pass = self.genera_password_sicura()
        self.lbl_password.text = nuova_pass
        Clipboard.copy(nuova_pass)
        
        sound = SoundLoader.load('ding.mp3')
        if sound:
            sound.play()

if __name__ == '__main__':
    MatrixPasswordApp().run()
