from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from login import LoginScreen
from dashboard import DashboardScreen
from league import LeagueScreen
from match import MatchScreen
from predict import PredictScreen
from profile import ProfileScreen
from history import HistoryScreen


class FootballApp(App):
    def build(self):
        sm = ScreenManager()

        # Global Data
        sm.balance = 1000
        sm.history = []
        sm.selected_match = ""

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
