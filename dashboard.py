from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from style import GREEN


class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation="vertical", padding=30, spacing=20)

        self.balance_label = Label(font_size=24)

        
        self.add_widget(self.layout)

    def on_pre_enter(self):
        self.balance_label.text = f"💰 Balance: {self.manager.balance}"
