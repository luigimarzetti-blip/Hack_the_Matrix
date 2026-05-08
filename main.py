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

class MatrixBackground(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Testo verde brillante, leggermente sfumato
        self.color = get_color_from_hex('#00FF41')
        self.opacity = 0.6
        self.font_size = '14sp'
        self.halign = 'center'
        self.valign = 'middle'
        # Aggiorna i caratteri ogni 0.15 secondi
        Clock.schedule_interval(self.update_matrix, 0.15)

    def update_matrix(self, dt):
        # Genera righe di caratteri casuali stile Matrix
        caratteri = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*+<>?/\\"
        righe = []
        # Crea uno schermo pieno di finti "codici"
        for _ in range(50): 
            righe.append('  '.join(random.choice(caratteri) for _ in range(30)))
        self.text = '\n'.join(righe)

class MatrixPasswordApp(App):
    def build(self):
        # Sfondo nero profondo
        Window.clearcolor = (0, 0, 0, 1)
        
        # FloatLayout ci permette di sovrapporre i livelli (Sfondo sotto, Bottoni sopra)
        main_layout = FloatLayout()
        
        # Livello 1: Lo sfondo Matrix
        self.sfondo = MatrixBackground(size_hint=(1, 1), pos_hint={'x': 0, 'y': 0})
        main_layout.add_widget(self.sfondo)
        
        # Livello 2: I comandi centrali
        ui_layout = BoxLayout(orientation='vertical', spacing=20, size_hint=(0.8, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        # Etichetta del titolo
        self.lbl_titolo = Label(text="Genera password:", font_size='24sp', bold=True, color=get_color_from_hex('#FFFFFF'))
        ui_layout.add_widget(self.lbl_titolo)
        
        # Etichetta dove apparirà la password
        self.lbl_password = Label(text="---", font_size='30sp', bold=True, color=get_color_from_hex('#00FF41'))
        ui_layout.add_widget(self.lbl_password)
        
        # Bottone Genera
        btn_genera = Button(
            text="GENERA E COPIA", 
            font_size='20sp', 
            bold=True,
            size_hint_y=0.5,
            background_color=get_color_from_hex('#00FF41'),
            color=(0,0,0,1) # Testo nero per contrasto sul verde
        )
        btn_genera.bind(on_press=self.genera_e_suona)
        ui_layout.add_widget(btn_genera)
        
        main_layout.add_widget(ui_layout)
        
        return main_layout

    def genera_password_sicura(self):
        # Regole: Almeno 16 caratteri, 1 maiuscola, 1 minuscola, 1 numero, 1 carattere speciale
        lunghezza = 16
        maiuscole = string.ascii_uppercase
        minuscole = string.ascii_lowercase
        numeri = string.digits
        speciali = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        # Assicuriamoci che ci sia almeno uno di ogni tipo
        password = [
            random.choice(maiuscole),
            random.choice(minuscole),
            random.choice(numeri),
            random.choice(speciali)
        ]
        
        # Riempiamo il resto con caratteri misti
        tutti_caratteri = maiuscole + minuscole + numeri + speciali
        password += [random.choice(tutti_caratteri) for _ in range(lunghezza - 4)]
        
        # Mescoliamo l'ordine per non avere maiuscola, minuscola, numero all'inizio in modo prevedibile
        random.shuffle(password)
        return ''.join(password)

    def genera_e_suona(self, instance):
        # 1. Genera e mostra
        nuova_pass = self.genera_password_sicura()
        self.lbl_password.text = nuova_pass
        
        # 2. Copia negli appunti
        Clipboard.copy(nuova_pass)
        
        # 3. Suona il Ding (se il file esiste)
        if os.path.exists('ding.mp3'):
            suono = SoundLoader.load('ding.mp3')
            if suono:
                suono.play()

if __name__ == '__main__':
    MatrixPasswordApp().run()
