from kivymd.app import MDApp
from Controllers.AppController import AppController

class MainApp(MDApp):
    def build(self):
        self.appController = AppController()
        self.appController.View('LoginScreen')
        
        # Calling the method from AppController to set the screen
        return self.appController.navigationController.get_screen_manager()
    
if __name__ == "__main__":
    MainApp().run()