from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class HistoryScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets()
        layout = BoxLayout(orientation="vertical", padding=30, spacing=10)

