from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

class UI(Widget):
    pass

class LoginKvApp(App):
    username = ''
    password = ''
    def build(self):
        print("build is called. ---")
        return UI()

    # Arranging that what you wri te will be shown to you
    # in IDLE
    def username_listener(self):
        text = self.root.ids.username_input.text
        print(f"username_listener. {text}")
        self.username = text
    
    def password_listener(self):
        text = self.root.ids.password_input.text
        print(f"password_listener. {text}")
        self.password = text

    def login_button_listener(self):
        print(f"login_button_listener is called. {self.username}, {self.password}")
        if self.username and self.password:
            print("username and password are not empty.")


if __name__ == "__main__":
    app = LoginKvApp()
    app.run()