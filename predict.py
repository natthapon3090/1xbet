import random
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class PredictScreen(Screen):
    def on_pre_enter(self):
        self.clear_widgets()

        layout = BoxLayout(orientation="vertical", padding=15, spacing=10)

        layout.add_widget(Label(text="🧾 Your Bet Slip", font_size=22))

        total_odds = 1

        for s in self.manager.selected_matches:
            total_odds *= s["odds"]
            layout.add_widget(
                Label(text=f"{s['match']} | {s['team']} @ {s['odds']}")
            )

        layout.add_widget(Label(text=f"🔥 Total Odds: {round(total_odds,2)}"))

        self.bet_input = TextInput(
            hint_text="Enter Bet Amount",
            multiline=False,
            input_filter="int"
        )
        layout.add_widget(self.bet_input)

        result_label = Label(text="")
        layout.add_widget(result_label)

        def submit(instance):

            if not self.bet_input.text:
                return

            bet = int(self.bet_input.text)

            if bet > self.manager.balance:
                result_label.text = "❌ Not enough balance"
                return
