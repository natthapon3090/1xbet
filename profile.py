from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=30, spacing=20)

        self.balance_label = Label(font_size=24)

        back = Button(text="⬅ Back")
        back.bind(on_press=lambda x: setattr(self.manager, "current", "dashboard"))

        layout.add_widget(self.balance_label)
        layout.add_widget(back)

        self.add_widget(layout)

    def on_pre_enter(self):
        self.balance_label.text = f"💰 Current Balance: {self.manager.balance}"
