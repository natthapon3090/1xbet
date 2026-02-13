from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class BillScreen(Screen):

    def on_pre_enter(self):
        self.clear_widgets()

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        layout.add_widget(Label(text="🧾 BETTING BILL", font_size=24))

        bill = self.manager.current_bill

