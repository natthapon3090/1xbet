from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window

Window.size = (360, 640)


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=15
        )

        title = Label(
            text="⚽ Football Predictor",
            font_size=26,
            size_hint=(1, 0.2)
        )

        self.username = TextInput(
            hint_text="1xbet",
            multiline=False,
            size_hint=(1, 0.15)
        )

        self.password = TextInput(
            hint_text="5555",
            password=True,
            multiline=False,
            size_hint=(1, 0.15)
        )

        login_btn = Button(
            text="Login",
            size_hint=(1, 0.15),
            background_color=(0.2, 0.7, 0.3, 1)
        )
        login_btn.bind(on_press=self.login)

        register_btn = Button(
            text="Register",
            size_hint=(1, 0.15),
            background_color=(0.2, 0.4, 0.8, 1)
        )
        register_btn.bind(on_press=self.register)

        self.message = Label(
            text="",
            color=(1, 0, 0, 1),
            size_hint=(1, 0.1)
        )

        main_layout.add_widget(title)
        main_layout.add_widget(self.username)
        main_layout.add_widget(self.password)
        main_layout.add_widget(login_btn)
        main_layout.add_widget(register_btn)
        main_layout.add_widget(self.message)

        self.add_widget(main_layout)

    def login(self, instance):
        user = self.username.text
        pwd = self.password.text

        if user == "" or pwd == "":
            self.message.text = "❌ Please fill all fields"
        elif user == "admin" and pwd == "1234":
            self.message.text = "✅ Login successful"
            self.show_popup("Success", "Welcome back!")
            # ต่อไปเปลี่ยนหน้าได้
            # self.manager.current = "league"
        else:
            self.message.text = "❌ Invalid username or password"

    def register(self, instance):
        self.show_popup("Register", "Go to register screen")

    def show_popup(self, title, text):
        popup = Popup(
            title=title,
            content=Label(text=text),
            size_hint=(0.7, 0.3)
        )
        popup.open()


class FootballApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        return sm


if __name__ == "__main__":
    FootballApp().run()
