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
        layout = BoxLayout(orientation="vertical", padding=15, spacing=8)

        layout.add_widget(Label(text=f"{self.manager.selected_league}", font_size=22))

        for home, away in matches[self.manager.selected_league]:

            match_box = BoxLayout(orientation="vertical", spacing=5)

            match_box.add_widget(Label(text=f"{home} vs {away}", font_size=18))

            odds_home = round(random.uniform(1.5, 2.5), 2)
            odds_draw = round(random.uniform(2.5, 3.5), 2)
            odds_away = round(random.uniform(1.8, 3.0), 2)

            row = BoxLayout(spacing=5)

            btn_home = ToggleButton(text=f"{home}\n{odds_home}")
            btn_draw = ToggleButton(text=f"Draw\n{odds_draw}")
            btn_away = ToggleButton(text=f"{away}\n{odds_away}")

            for btn, team, odds in [
                (btn_home, home, odds_home),
                (btn_draw, "Draw", odds_draw),
                (btn_away, away, odds_away)
            ]:
                btn.bind(on_press=lambda inst, h=home, a=away, t=team, o=odds:
                         self.select_match(h, a, t, o))
                row.add_widget(btn)

            match_box.add_widget(row)
            layout.add_widget(match_box)

                next_btn = Button(text="➡ Confirm Selection")
        next_btn.bind(on_press=lambda x: setattr(self.manager, "current", "predict"))

        back = Button(text="⬅ Back")
        back.bind(on_press=lambda x: setattr(self.manager, "current", "league"))

        layout.add_widget(next_btn)
        layout.add_widget(back)

        self.add_widget(layout)

    def select_match(self, home, away, team, odds):

        selection = {
            "match": f"{home} vs {away}",
            "team": team,
            "odds": odds
        }

        # ถ้าเลือกแมตช์เดิมใหม่ ให้แทนที่
        self.manager.selected_matches = [
            s for s in self.manager.selected_matches
            if s["match"] != selection["match"]
        ]

        self.manager.selected_matches.append(selection)
