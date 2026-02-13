from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle


class HistoryScreen(Screen):

    def on_pre_enter(self):
        self.clear_widgets()

        root = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        bills = self.manager.bills

        # ===== คำนวณสถิติ =====
        total_profit = 0
        win_count = 0
        total_count = len(bills)

        for bill in bills:
            result = bill.get("result", "")

            if "WIN" in result:
                win_count += 1

                # ดึงกำไรจากข้อความ เช่น "WIN +2500"
                try:
                    profit = float(result.split("+")[1])
                    total_profit += profit
                except:
                    pass

            elif "LOSE" in result:
                try:
                    loss = float(result.split("-")[1])
                    total_profit -= loss
                except:
                    pass

