from kivy.uix.screenmanager import ScreenManager

class NavigationController:
    def __init__(self, controller=None):
        self.screen_manager = ScreenManager()
        self.screen_manager.controller = controller
    
    # Add a screen to the screen manager
    def add_screen(self, screen, name):
        screen.name = name
        self.screen_manager.add_widget(screen)
    
    # Set the current screen
    def go_to_screen(self, screen_name):
        self.screen_manager.current = screen_name
        
    # Get the current screen
    def get_current_screen(self):
        return self.screen_manager.current_screen.name
    
    # Get the screen manager
    def get_screen_manager(self):
        return self.screen_manager