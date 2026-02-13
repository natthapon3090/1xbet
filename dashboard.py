from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from style import NEON_GREEN, GOLD, BLUE


class DashboardScreen(Screen):

    def on_pre_enter(self):
        self.clear_widgets()

        layout = BoxLayout(orientation="vertical", padding=30, spacing=20)

        self.balance_label = Label(font_size=24)
        self.balance_label.text = f"💰 BALANCE: {self.manager.balance}"

        self.live_label = Label(text="🔴 LIVE MATCH RUNNING", color=(1, 0, 0, 1))
        Clock.schedule_interval(self.blink, 0.5)

        btn1 = Button(text="⚽ BET NOW", background_color=NEON_GREEN)
        btn1.bind(on_press=lambda x: setattr(self.manager, "current", "league"))

        btn2 = Button(text="📜 BILLS")
        btn2.bind(on_press=lambda x: setattr(self.manager, "current", "history"))

        btn3 = Button(text="💳 DEPOSIT")
        btn3.bind(on_press=lambda x: setattr(self.manager, "current", "deposit"))

        btn4 = Button(text="📊 PROFIT GRAPH")
        btn4.bind(on_press=lambda x: setattr(self.manager, "current", "graph"))
        
        layout.add_widget(self.balance_label)
        layout.add_widget(self.live_label)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        self.add_widget(layout)

    def blink(self, dt):
        self.live_label.opacity = 1 if self.live_label.opacity == 0 else 0
