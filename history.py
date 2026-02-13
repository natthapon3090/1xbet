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
        win_rate = round((win_count / total_count) * 100, 2) if total_count > 0 else 0

        # ===== แสดงสรุปด้านบน =====
        summary_box = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height=120,
            spacing=5
        )

        summary_box.add_widget(Label(
            text=f"💰 Total Profit: {round(total_profit,2)}",
            font_size=20
        ))

        summary_box.add_widget(Label(
            text=f"📊 Win Rate: {win_rate}%",
            font_size=18
        ))

        summary_box.add_widget(Label(
            text=f"🧾 Total Bills: {total_count}",
            font_size=16
        ))

        root.add_widget(summary_box)
        # ===== Scroll บิล =====
        scroll = ScrollView()

        content = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            spacing=10
        )
        content.bind(minimum_height=content.setter('height'))

        if not bills:
            content.add_widget(Label(text="No betting history yet."))
        else:
            for bill in bills:

                # แยก Single / Parlay
                selections = bill.get("selections", [])
                bet_type = "🏆 PARLAY" if len(selections) > 1 else "🎯 SINGLE"

                result_text = bill.get("result", "")
                # สีตามผล
                if "WIN" in result_text:
                    result_color = (0, 1, 0, 1)  # เขียว
                else:
                    result_color = (1, 0, 0, 1)  # แดง

                bill_box = BoxLayout(
                    orientation="vertical",
                    padding=10,
                    spacing=5,
                    size_hint_y=None,
                    height=150
                )

                bill_box.add_widget(Label(
                    text=f"{bet_type}",
                    font_size=16
                ))

                for s in selections:
                    match = s.get("match", "")
                    team = s.get("team", "")
                    odds = s.get("odds", "")
                    bill_box.add_widget(
                        Label(text=f"{match} | {team} @ {odds}")
                    )
