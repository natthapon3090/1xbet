from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from login import LoginScreen
from dashboard import DashboardScreen
from league import LeagueScreen
from match import MatchScreen
from predict import PredictScreen
from bill import BillScreen
from history import HistoryScreen
from profile import ProfileScreen
from deposit import DepositScreen
from graph import GraphScreen


class FootballApp(App):
    def build(self):
        sm = ScreenManager()

        sm.balance = 10000
        sm.selected_league = ""
        sm.selected_matches = []   # รองรับสเตป
        sm.current_bill = {}
        sm.bills = []
        sm.profit_history = [10000]
        
        screens = [
            LoginScreen(name="login"),
            DashboardScreen(name="dashboard"),
            LeagueScreen(name="league"),
            MatchScreen(name="match"),
            PredictScreen(name="predict"),
            BillScreen(name="bill"),
            HistoryScreen(name="history"),
            ProfileScreen(name="profile"),
            DepositScreen(name="deposit"),
            GraphScreen(name="graph"),
        ]

        for s in screens:
            sm.add_widget(s)

        return sm


if __name__ == "__main__":
    FootballApp().run()
