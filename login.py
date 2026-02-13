from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from style import NEON_GREEN


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=50, spacing=20)

        layout.add_widget(Label(text="⚡ BETTING SIM PRO ⚡", font_size=32))

        self.user = TextInput(hint_text="Username", multiline=False)
        self.pw = TextInput(hint_text="Password", password=True, multiline=False)

        btn = Button(text="ENTER", background_color=NEON_GREEN)
        btn.bind(on_press=self.login)

        self.user = TextInput(hint_text="Username", multiline=False)
        self.pw = TextInput(hint_text="Password", password=True, multiline=False)

        btn = Button(text="LOGIN", background_color=GREEN)
        btn.bind(on_press=self.login)

        self.msg = Label(text="")

        layout.add_widget(self.user)
        layout.add_widget(self.pw)
        layout.add_widget(btn)
        layout.add_widget(self.msg)

        self.add_widget(layout)

    def login(self, instance):
        if self.user.text == "admin" and self.pw.text == "1234":
            self.manager.current = "dashboard"
        else:
            self.msg.text = "❌ Access Denied"
