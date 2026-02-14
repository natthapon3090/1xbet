from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.label import Label
import random


class MatchScreen(Screen):

    def on_pre_enter(self):
        self.clear_widgets()
        self.manager.selected_matches = []
        matches = {
            "Premier League": [
                ("Man City", "Arsenal"),
                ("Liverpool", "Chelsea"),
                ("Tottenham", "Newcastle"),
                ("Aston Villa", "West Ham")
            ],
            "La Liga": [
                ("Real Madrid", "Barcelona"),
                ("Atletico", "Sevilla"),
                ("Valencia", "Villarreal"),
                ("Sociedad", "Betis")
            ],
            "Bundesliga": [
                ("Bayern", "Dortmund"),
                ("Leipzig", "Leverkusen"),
                ("Frankfurt", "Stuttgart"),
                ("Wolfsburg", "Bremen")
            ],
            "Thai League": [
                ("Buriram", "BG Pathum"),
                ("Port", "Chonburi"),
                ("Muangthong", "Ratchaburi"),
                ("Chiangrai", "Police Tero")
            ]
        }
       
