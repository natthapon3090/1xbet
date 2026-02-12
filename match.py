from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MatchScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.matches = [
            "Manchester City vs Arsenal",
            "Liverpool vs Chelsea",
            "Manchester United vs Tottenham"
        ]

        layout = BoxLayout(orientation="vertical", padding=30, spacing=20)
        layout.add_widget(Label(text="🔥 Choose Match", font_size=24))

       
