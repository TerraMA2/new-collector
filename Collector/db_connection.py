import psycopg2


class Db_connection:
    def __init__(self, host, database, username, password):
        self.host = host
        self.database = database
        self.username = username
        self.password = password
        self.cur = ''

    def connection(self):
        try:
            con = psycopg2.connect(host=self.host, database=self.database,
                                   user=self.username, password=self.password)
            self.cur = con.cursor()
            return ' >>> Connection created successfully!'
        except:
            return ' >>> Failed to connect to database'

    def select_itens(self):
        sql = 'SELECT srid, auth_name, auth_srid, srtext, proj4text FROM public.spatial_ref_sys;'
        self.cur.execute(sql)
        recset = self.cur.fetchall()
        for rec in recset:
            print(rec)