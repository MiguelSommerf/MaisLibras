from kivymd.uix.screen import MDScreen
from kivy.config import Config
from kivy.core.window import Window
Config.set('graphics', 'borderless', True)  # Remove the title bar

# Window Settings
Window.borderless = True  # Remove the title bar

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

KVRegister = """
MDScreen:
    md_bg_color: 49/255, 54/255, 56/255, 1

    MDIconButton:
        icon: "close"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1 
        on_release: app.stop()  # Fecha o aplicativo
        pos_hint: {"right": 1, "top": 1}  # Posiciona o botão no canto superior direito
    
    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(20)
        padding: dp(20)
        size_hint: None, None
        size: dp(300), dp(550)
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        md_bg_color: 237/255, 235/255, 215/255, 1
        radius: [10, 10, 10, 10]

        MDLabel:
            text: "Cadastrar"
            font_style: "H4"
            halign: "center"
            color: 0, 0, 0, 1

        MDBoxLayout:
            orientation: "vertical"
            size_hint_y: None
            height: dp(100)
            padding: dp(10)
            pos_hint: {"center_x": 0.5}  # Center the icon
            radius: [20, 20, 20, 20]
            FitImage:
                source: ""  # Path to your icon image
                size_hint: None, None
                size: dp(100), dp(100)
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                radius: [dp(50), dp(50), dp(50), dp(50)]

        MDTextField:
            id: name_field
            hint_text: "Nome"
            icon_left: "account"
            mode: "line"
            helper_text: "Digite seu nome"
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
                text: "Entrar"
                md_bg_color: 66/255, 62/255, 55/255, 1
                text_color: 1, 1, 1, 1
                elevation: 1
                on_release: app.root.controller.View('LoginScreen')  # Call the add_screen method

            MDRaisedButton:
                text: "Cadastrar"
                md_bg_color: 227/255, 178/255, 60/255, 1
                text_color: 49/255, 54/255, 56/255, 1
                elevation: 1
                on_release: app.root.controller.userController.insertUser(email_field.text, password_field.text)  # Call the registerUser method
"""

class RegisterScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = Builder.load_string(KVRegister)
        self.add_widget(layout)