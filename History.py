from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class HistoryScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets()
        layout = BoxLayout(orientation="vertical", padding=30, spacing=10)
        layout.add_widget(Label(text="📜 Betting History", font_size=24))

        for item in self.manager.history:
            layout.add_widget(Label(text=item))

        back = Button(text="⬅ Back")
        back.bind(on_press=lambda x: setattr(self.manager, "current", "dashboard"))

        layout.add_widget(back)
        self.add_widget(layout)
