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

       
