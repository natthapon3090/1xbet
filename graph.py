from kivy.uix.screenmanager import Screen
import matplotlib.pyplot as plt


class GraphScreen(Screen):

    def on_pre_enter(self):
        plt.plot(self.manager.profit_history)
        plt.title("Balance History")
        plt.xlabel("Rounds")
        plt.ylabel("Balance")
        plt.show()
        self.manager.current = "dashboard"
