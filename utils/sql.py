import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from config.config import *

APP_CONFIG_PATH = '.\config\config.ini'
app_config = Config(APP_CONFIG_PATH)


class SQL:
    def __init__(self, sql_base):
        self.engine = None
        self.conn = None
        self.session = None

        # print(datetime.now().strftime("%H:%M:%S"), '|', f'Connecting to SQL DB {self.database}...')
        try:
            if self.engine is None:
                connection_uri = get_db_url(sql_base)
                self.engine = create_engine(connection_uri, fast_executemany=True)
                self.conn = self.engine.connect()
                self.session = sessionmaker(self.engine)
        except sqlalchemy.exc.InterfaceError as e:
            print(datetime.now().strftime("%H:%M:%S"), '|', f"Can't connection to DB {sql_base}: " + str(e))
        else:
            print(datetime.now().strftime("%H:%M:%S"), '|', f'Connected to SQL DB {sql_base}!')

    def get_people_by_telegram_id(self, telegram_id):
        sql_query = f'SELECT DESCR FROM dbo.People P ' \
                    f'INNER JOIN dbo.People_Ext PE ON PE.People_ID = P.ID WHERE PE.TelegramChatID = ({telegram_id})'
        return f"'{self.conn.exec_driver_sql(sql_query).first()[0]}'"


def get_db_url(sql_base):
    driver = 'ODBC Driver 17 for SQL Server'
    server = ''
    port = ''
    database = ''
    username = ''
    password = ''

    if sql_base == 'PetrykivkaSupportBot':
        server = app_config.get_setting('SQL_Bot', 'server')
        port = app_config.get_setting('SQL_Bot', 'port')
        database = app_config.get_setting('SQL_Bot', 'database')
        username = app_config.get_setting('SQL_Bot', 'username')
        password = app_config.get_setting('SQL_Bot', 'password')

    if sql_base == 'petrykivka_bi':
        server = app_config.get_setting('SQL_PBI', 'server')
        port = app_config.get_setting('SQL_PBI', 'port')
        database = app_config.get_setting('SQL_PBI', 'database')
        username = app_config.get_setting('SQL_PBI', 'username')
        password = app_config.get_setting('SQL_PBI', 'password')

    return f'mssql+pyodbc://{username}:{password}@{server}:{port}' \
           f'/{database}?driver={driver}&MARS_Connection=Yes'
