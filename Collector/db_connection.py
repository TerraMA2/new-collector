from read_csv import Read_csv
import psycopg2

class Db_connection(Read_csv):
    def __init__(self, host, database, username, password, table, address, folder):
        super().__init__(address, folder)
        self.host = host
        self.database = database
        self.username = username
        self.password = password
        self.table = table
        self.cur = ''
        self.con = ''

    def connection(self):
        try:
            self.con = psycopg2.connect(host=self.host, database=self.database, user=self.username,
                                        password=self.password)
            self.cur = self.con.cursor()
            return ' >>> Connection created successfully!'
        except():
            return ' >>> Failed to connect to database'

    def insert_all_values(self):
        for index, row in self.readed_file.iterrows():
            try:
                self.cur.execute(
                        "INSERT INTO " + self.table + " (data_hora_gmt, longitude, latitude, satelite, id_0, id_1, id_2,"
                                                      "pais, estado, municipio, bioma, bioma_id, foco_id) "
                                                      "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (foco_id)"
                                                      " DO NOTHING;",
                        (row.data_hora_gmt, row.longitude, row.latitude, row.satelite, row.id_0, row.id_1, row.id_2,
                         row.pais, row.estado, row.municipio, row.bioma, row.bioma_id, row.foco_id))
                self.con.commit()
            except:
                print('>>>> The insert has been failed')
        self.cur.close()
        print('>>>> Files successfully added into database')

    def insert_brazil_values(self):
        for index, row in self.readed_file.iterrows():
            if row.pais == 'Brasil':
                try:
                    self.cur.execute(
                            "INSERT INTO " + self.table + " (data_hora_gmt, longitude, latitude, satelite, id_0, id_1, id_2,"
                                                          "pais, estado, municipio, bioma, bioma_id, foco_id) "
                                                          "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                                          "ON CONFLICT (foco_id) DO NOTHING;",
                            (row.data_hora_gmt, row.longitude, row.latitude, row.satelite, row.id_0, row.id_1, row.id_2,
                             row.pais, row.estado, row.municipio, row.bioma, row.bioma_id, row.foco_id))
                    self.con.commit()
                except:
                    print('>>>> The insert has been failed')
            else:
                pass
        self.cur.close()
        print('>>>> Files successfully added into database')

    def insert_specified_values(self):
        state = input('Insert the state name: ')
        for index, row in self.readed_file.iterrows():
            if row.pais == 'Brasil' and row.estado == state.upper():
                try:
                    self.cur.execute(
                        "INSERT INTO " + self.table + " (data_hora_gmt, longitude, latitude, satelite, id_0, id_1, id_2,"
                                                      "pais, estado, municipio, bioma, bioma_id, foco_id) "
                                                      "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                                      "ON CONFLICT (foco_id) DO NOTHING;",
                        (row.data_hora_gmt, row.longitude, row.latitude, row.satelite, row.id_0, row.id_1, row.id_2,
                         row.pais, row.estado, row.municipio, row.bioma, row.bioma_id, row.foco_id))
                    self.con.commit()
                except:
                    print('>>>> The insert has been failed')
            else:
                pass
        self.cur.close()
        print('>>>> Files successfully added into database')
