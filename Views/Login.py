from kivymd.uix.screen import MDScreen
from kivy.config import Config
Config.set('graphics', 'borderless', True)  # Remove the title bar

from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout

KVLogin = """
MDScreen:
    md_bg_color: 49/255, 54/255, 56/255, 1

    MDIconButton:
        icon: "close"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1 
        on_release: app.stop()  # Close the app
        pos_hint: {"right": 1, "top": 1}  # Posicionate the button in the top right corner

    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(20)
        padding: dp(20)
        size_hint: None, None
        size: dp(300), dp(400)
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        md_bg_color: 237/255, 235/255, 215/255, 1
        radius: [10, 10, 10, 10]

        MDLabel:
            text: "Entrar"
            font_style: "H4"
            halign: "center"
            color: 49/255, 54/255, 56/255, 1

        MDTextField:
            id: email_field
            hint_text: "Email"
            icon_left: "email"
            mode: "line"
            helper_text: "Digite seu email"
            helper_text_color_focus: 49/255, 54/255, 56/255, 1
            hint_text_color_focus: 49/255, 54/255, 56/255, 1
            hint_text_color_normal: 49/255, 54/255, 56/255, 1
            icon_left_color_focus: 49/255, 54/255, 56/255, 1
            icon_left_color_normal: 49/255, 54/255, 56/255, 1
            line_color_normal: 49/255, 54/255, 56/255, 1
            line_color_focus: 49/255, 54/255, 56/255, 1
            text_color_focus: 49/255, 54/255, 56/255, 1
            text_color_normal: 49/255, 54/255, 56/255, 1

        MDTextField:
            id: password_field
            hint_text: "Senha"
            icon_left: "lock"
            password: True
            mode: "line"
            helper_text: "Digite sua senha"
            hint_text_color_normal: 49/255, 54/255, 56/255, 1
            hint_text_color_focus: 49/255, 54/255, 56/255, 1
            icon_left_color_normal: 49/255, 54/255, 56/255, 1
            icon_left_color_focus: 49/255, 54/255, 56/255, 1
            line_color_normal: 49/255, 54/255, 56/255, 1
            line_color_focus: 49/255, 54/255, 56/255, 1
            helper_text_color_focus: 49/255, 54/255, 56/255, 1
            text_color_focus: 49/255, 54/255, 56/255, 1
            text_color_normal: 49/255, 54/255, 56/255, 1

        MDBoxLayout:
            orientation: "horizontal"
            spacing: dp(100)
            size_hint_y: None
            height: dp(50)

            MDRaisedButton:
                text: "Cadastrar"
                md_bg_color: 66/255, 62/255, 55/255, 1
                text_color: 1, 1, 1, 1
                elevation: 1
                on_release: app.root.controller.View('RegisterScreen')  # Call the View method in AppController

            MDRaisedButton:
                text: "Entrar"
                md_bg_color: 227/255, 178/255, 60/255, 1
                text_color: 49/255, 54/255, 56/255, 1
                elevation: 1
                on_release: app.root.controller.userController.logginUser(email_field.text, password_field.text)  # Call the logginUser method
                

"""

class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        layout = Builder.load_string(KVLogin)
        self.add_widget(layout)