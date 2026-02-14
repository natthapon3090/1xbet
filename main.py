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
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(LeagueScreen(name="league"))
        sm.add_widget(MatchScreen(name="match"))
        sm.add_widget(PredictScreen(name="predict"))
        sm.add_widget(ProfileScreen(name="profile"))
        sm.add_widget(HistoryScreen(name="history"))

        return sm


if __name__ == "__main__":
    FootballApp().run()

