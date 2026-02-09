from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.login import LoginScreen
from screens.league import LeagueScreen
from screens.match import MatchScreen
from screens.predict import PredictScreen
from screens.profile import ProfileScreen


class FootballApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(LeagueScreen(name="league"))
        sm.add_widget(MatchScreen(name="match"))
        sm.add_widget(PredictScreen(name="predict"))
        sm.add_widget(ProfileScreen(name="profile"))
        return sm


if __name__ == "__main__":
    FootballApp().run()
