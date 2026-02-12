import random
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from wallet import Wallet
from style import GREEN, RED


class PredictScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.odds = {"Home": 1.8, "Draw": 3.2, "Away": 2.5}

        self.layout = BoxLayout(orientation="vertical", padding=30, spacing=20)

        self.match_label = Label(font_size=22)
        self.layout.add_widget(self.match_label)

        self.home = ToggleButton(text="Home Win 1.8", group="bet")
        self.draw = ToggleButton(text="Draw 3.2", group="bet")
        self.away = ToggleButton(text="Away Win 2.5", group="bet")

        self.layout.add_widget(self.home)
        self.layout.add_widget(self.draw)
        self.layout.add_widget(self.away)

        self.bet_input = TextInput(hint_text="Enter Bet Amount", multiline=False, input_filter="int")
        self.layout.add_widget(self.bet_input)

        self.result_label = Label(text="")
        self.layout.add_widget(self.result_label)

        btn = Button(text="🎯 Confirm Bet", background_color=GREEN)
        btn.bind(on_press=self.submit)
        self.layout.add_widget(btn)

        self.add_widget(self.layout)

    def on_pre_enter(self):
        self.match_label.text = f"Match: {self.manager.selected_match}"

    def submit(self, instance):
        if not self.bet_input.text:
            self.result_label.text = "❌ Enter Bet"
            return

        bet = int(self.bet_input.text)

        if not Wallet.withdraw(self.manager, bet):
            self.result_label.text = "❌ Not Enough Balance"
            return

        if self.home.state == "down":
            odds = self.odds["Home"]
        elif self.draw.state == "down":
            odds = self.odds["Draw"]
        elif self.away.state == "down":
            odds = self.odds["Away"]
        else:
            self.result_label.text = "❌ Select Result"
            return

        if random.choice([True, False]):
            win = bet * odds
            Wallet.deposit(self.manager, win)
            result = f"✅ WIN +{win}"
            self.result_label.color = GREEN
        else:
            result = f"❌ LOSE -{bet}"
            self.result_label.color = RED

        self.manager.history.append(result)
        self.manager.current = "profile"

