from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MortgageApp(MDApp):
    def build(self):
        return MDLabel(text='Hello Mortgage Calculator', halign='center')

if __name__ == "__main__":
    MortgageApp().run()

