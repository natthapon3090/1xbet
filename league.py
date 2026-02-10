from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class LeagueScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        layout.add_widget(Label(text="Select League", font_size=22))

        leagues = ["Premier League", "La Liga", "Bundesliga", "Thai League"]
        for league in leagues:
            btn = Button(text=league)
            btn.bind(on_press=self.go_match)
            layout.add_widget(btn)

        self.add_widget(layout)
    def go_match(self, instance):
        self.manager.current = "match"
