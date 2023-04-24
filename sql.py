from config.config import *
from sqlalchemy import create_engine
from datetime import datetime

APP_CONFIG_PATH = 'config.ini'
app_config = Config(APP_CONFIG_PATH)


class SQL:
    def __init__(self):
        self.engine = None
        self.conn = None
        self.driver = 'ODBC Driver 17 for SQL Server'
        self.server = app_config.get_setting('SQL', 'server')
        self.port = app_config.get_setting('SQL', 'port')
        self.database = app_config.get_setting('SQL', 'database')
        self.username = app_config.get_setting('SQL', 'username')
        self.password = app_config.get_setting('SQL', 'password')

        # print(datetime.now().strftime("%H:%M:%S"), '|', f'Connecting to SQL DB {self.database}...')
        try:
            if self.engine is None:
                connection_uri = f'mssql+pyodbc://{self.username}:{self.password}@{self.server}:{self.port}' \
                                 f'/{self.database}?driver={self.driver}'
                self.engine = create_engine(connection_uri, fast_executemany=True)
                self.conn = self.engine.connect()
        except sqlalchemy.exc.InterfaceError as e:
            print(datetime.now().strftime("%H:%M:%S"), '|', f"Can't connection to DB {self.database}: " + str(e))
        else:
            print(datetime.now().strftime("%H:%M:%S"), '|', f'Connected to SQL DB {self.database}!')

    def get_people_by_telegram_id(self, telegram_id):
        sql_query = f'SELECT DESCR FROM dbo.People P INNER JOIN dbo.People_Ext PE ON PE.People_ID = P.ID WHERE PE.TelegramChatID = ({telegram_id})'
        return f"'{self.conn.exec_driver_sql(sql_query).first()[0]}'"
