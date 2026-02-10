from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=30, spacing=15)
        layout.add_widget(Label(text="⚽ Football Predictor", font_size=24))

        self.username = TextInput(hint_text="Username", multiline=False)
        self.password = TextInput(hint_text="Password", password=True, multiline=False)

        login_btn = Button(text="Login")
        login_btn.bind(on_press=self.login)

        self.message = Label(text="")

        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(login_btn)
        layout.add_widget(self.message)

        self.add_widget(layout)
