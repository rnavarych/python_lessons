import mysql.connector


class UseDatabase:

    def __init__(self, configuration: dict) -> None:
        self.configuration = configuration

    def __enter__(self) -> 'MySQLCursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
