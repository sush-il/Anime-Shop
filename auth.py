import sqlite3

conn = sqlite3.connect('info.db')
cur = conn.cursor()

class Authenticatioin:
    def __init__(self,container):
        self.container = container

    def login(self):
        #self.username = self.container.username.get()
        #self.password = self.container.password.get()
        self.username = 'sushil@gmai.com'
        self.password = 'lkdfjsdlk'
        #self.usertype = usertype

        cur.execute(f"""SELECT Email,Password from Customer 
                        WHERE Email = ? AND Password = ? """,(self.username,self.password))

        """if not cur.fetchone():
            return "Login Failed"
        else:
            self.container.controller.show_frame(self.usertype)"""