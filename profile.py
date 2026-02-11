from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        self.layout.add_widget(Label(text="User Profile", font_size=22))

        self.score_label = Label(text="Score: 0")
        self.layout.add_widget(self.score_label)

        back_btn = Button(text="Back to League")
        back_btn.bind(on_press=self.back)
 
        self.layout.add_widget(back_btn)
        self.add_widget(self.layout)

    def on_pre_enter(self):
        score = getattr(self.manager, "user_score", 0)
        self.score_label.text = f"Score earned: {score}"

    def back(self, instance):
        self.manager.current = "league"
