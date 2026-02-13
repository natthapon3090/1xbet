from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class DepositScreen(Screen):

    def on_pre_enter(self):
        self.clear_widgets()

        layout = BoxLayout(orientation="vertical", padding=30, spacing=15)

        self.input = TextInput(hint_text="Deposit Amount", multiline=False, input_filter="int")
        layout.add_widget(self.input)

        btn = Button(text="💳 CONFIRM DEPOSIT")
        btn.bind(on_press=self.deposit)
        layout.add_widget(btn)

        back = Button(text="⬅ BACK")
        back.bind(on_press=lambda x: setattr(self.manager, "current", "dashboard"))
        layout.add_widget(back)

        self.add_widget(layout)
    def deposit(self, instance):
        if self.input.text:
            self.manager.balance += int(self.input.text)
            self.manager.profit_history.append(self.manager.balance)
            self.manager.current = "dashboard"
