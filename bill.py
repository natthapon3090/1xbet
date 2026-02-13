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
        # ถ้าไม่มีบิล
        if not bill:
            layout.add_widget(Label(text="No bill available"))
        else:

            # แสดงรายการที่เลือก
            selections = bill.get("selections", [])

            if selections:
                for s in selections:
                    match = s.get("match", "")
                    team = s.get("team", "")
                    odds = s.get("odds", "")
                    layout.add_widget(
                        Label(text=f"{match} | {team} @ {odds}")
                    )

            # แสดงข้อมูลรวม
            layout.add_widget(Label(text=f"Bet Amount: {bill.get('bet', '')}"))
            layout.add_widget(Label(text=f"Total Odds: {bill.get('total_odds', '')}"))
            layout.add_widget(Label(text=f"Result: {bill.get('result', '')}"))

        # ปุ่มกลับ Dashboard
        back_btn = Button(text="⬅ Back to Dashboard")
        back_btn.bind(
            on_press=lambda x: setattr(self.manager, "current", "dashboard")
        )

        layout.add_widget(back_btn)

        self.add_widget(layout)


