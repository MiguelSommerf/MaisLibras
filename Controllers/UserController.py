from Model.UserModel import UserModel

class UserController:
    def __init__(self):
        self.user_model = UserModel()

    # Inserting data into the database
    def insertUser(self, email, password):
        if not email or not password:
            print("O campo de e-mail e o campo de senha precisam estar preenchidos.")
            return False
        else:
            if self.user_model.verifyEmail(email) == False:
                self.user_model.insertDataUser(email, password)
    
    # Checking if the user is valid
    def logginUser(self, email, password):
        if not email or not password:
            print("O campo de e-mail e o campo de senha precisam estar preenchidos.")
            return False
        else:
            self.user_model.logginUser(email, password)     