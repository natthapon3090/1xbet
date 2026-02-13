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

        for l in leagues:
            btn = Button(text=l)
            btn.bind(on_press=self.select)
            layout.add_widget(btn)

        back = Button(text="⬅ BACK")
        back.bind(on_press=lambda x: setattr(self.manager, "current", "dashboard"))
        layout.add_widget(back)

        self.add_widget(layout)

    def select(self, instance):
        self.manager.selected_league = instance.text
        self.manager.current = "match"
