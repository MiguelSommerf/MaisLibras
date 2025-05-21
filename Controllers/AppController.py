from Views.Login import LoginScreen
from Views.Register import RegisterScreen
from Controllers.NavigationController import NavigationController
from Controllers.UserController import UserController

class AppController:
    def __init__(self):
        self.userController = UserController()
        self.navigationController = NavigationController(controller=self)
        
    def View(self, name):
        if name == 'LoginScreen':
            loginView = LoginScreen()
            if not self.navigationController.screen_manager.has_screen('LoginScreen'):
                self.navigationController.add_screen(loginView, 'LoginScreen')
                self.navigationController.go_to_screen('LoginScreen')
            else:
                self.navigationController.go_to_screen('LoginScreen')
            
            return self.navigationController.get_screen_manager()
        
        if name == 'RegisterScreen':
            registerScreen = RegisterScreen()
            if not self.navigationController.screen_manager.has_screen('RegisterScreen'):
                self.navigationController.add_screen(registerScreen, 'RegisterScreen')
                self.navigationController.go_to_screen('RegisterScreen')
            else:
                self.navigationController.go_to_screen('RegisterScreen')
                
            return self.navigationController.get_screen_manager()