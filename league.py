from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class LeagueScreen(Screen):

    def on_pre_enter(self):
        self.clear_widgets()

        layout = BoxLayout(orientation="vertical", padding=30, spacing=15)
        layout.add_widget(Label(text="🏆 SELECT LEAGUE", font_size=26))

        leagues = ["Premier League", "La Liga", "Bundesliga", "Thai League"]

        for league in leagues:
            btn = Button(text=league)
            btn.bind(on_press=self.go_match)
            layout.add_widget(btn)

        self.add_widget(layout)

    def go_match(self, instance):
        self.manager.current = "match"
