import sqlite3

class DbContext:

    def __init__(self):
        self.host = "data.db"
        self.connection = None
    
    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection
    
    def __exit__(self,exe_type,exe_value,exe_tb):
        if exe_type or exe_value or exe_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()