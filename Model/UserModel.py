from config.connect import connection
import bcrypt

class UserModel:
    
    def __init__(self):
        self.conn = connection()
        
        # Creating a cursor object to interact with the database
        self.sql = self.conn.cursor()
        
    # Inserting data into the database
    def insertDataUser(self, email, password):
        try:
            # Hashing the password
            passhash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            
            self.sql.execute("INSERT INTO usuario (email, senha) VALUES (?, ?)", (email, passhash))
            self.conn.commit()
            print("Dados inseridos com sucesso!")
        except Exception as error:
            print(f"Erro ao inserir dados: {error}")
            self.conn.rollback()
    
    # Logging user into the system
    def logginUser(self, email, password):
        try:
            self.sql.execute("SELECT senha FROM usuario WHERE email = ?", (email,))
            result = self.sql.fetchone()
            
            if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
                print("Login bem-sucedido!")
                return True
            else:
                print("E-mail ou senha incorretos.")
                return False
        except Exception as error:
            print(f"Erro ao consultar dados: {error}")
            return False
    
    # Updating userdata in the database
    def updateDataUser(self, email, password):
        try:
            self.sql.execute("UPDATE usuario SET senha = ? WHERE email = ?", (password, email))
            if(self.sql.rowcount == 1):
                self.conn.commit()
                print("Senha atualizada com sucesso!")
            else:
                print("Email não encontrado.")
                self.conn.rollback()
        except Exception as error:
            print(f"Erro ao atualizar dados: {error}")
            self.conn.rollback()
            
    # Deleting userdata from the database
    def deleteDataUser(self, email):
        try:
            self.sql.execute("DELETE FROM usuario WHERE email = ?", (email,))
            if(self.sql.rowcount == 1):
                self.conn.commit()
                print("Usuário deletado com sucesso!")
            else:
                print("Usuário não encontrado.")
                self.conn.rollback()
        except Exception as error:
            print(f"Erro ao deletar dados: {error}")
            self.conn.rollback()
            
    # Verifying if the email already exists in the database
    def verifyEmail(self, email):
        try:
            self.sql.execute("SELECT * FROM usuario WHERE email = ?", (email,))
            result = self.sql.fetchone()
            if(result):
                print("Este email já foi cadastrado, tente utilizar outro endereço de email.")
                return True
            else:
                return False
        except Exception as error:
            print(f"Erro ao verificar email: {error}")
            return False
    
    # Closing the connection to the database
    def closeConnection(self):
        try:
            self.conn.close()
        except Exception as error:
            print(f"Erro ao fechar a conexão com o banco: {error}")