from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class rajbhar(MDApp):
    def build(self):
        return MDLabel(text="Welcome to Ayodhya....",halign="center")
if __name__ == '__main__':
        rajbhar().run()