import psycopg2

class DBConnect:
    host = None
    database = None
    user = None
    password = None
    port = None

    connection = None

    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    def _create_db_connection(self):
        self.connection = psycopg2.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            keepalives=1,
            keepalives_idle=30,
            keepalives_interval=10,
            keepalives_count=5,
        )
        self.connection.autocommit = True
        return self.connection

    def get_connection(self):
        if self.connection and not self.connection.closed:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute('SELECT 1')
            except psycopg2.OperationalError:
                return self._create_db_connection()

            return self.connection
        else:
            return self._create_db_connection()
