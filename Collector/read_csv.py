from download_files import Download_files
import pandas as pd


class Read_csv(Download_files):
    def __init__(self, address, folder):
        self.readed_file = ''
        super().__init__(address, folder)

    def readFiles(self):
        for file in self.fileDay:
            data = pd.read_csv(self.files_day_directory + '\\' + file)
            df = pd.DataFrame(data,
                              columns=['data_hora_gmt', 'longitude', 'latitude', 'satelite', 'id_0', 'id_1', 'id_2',
                                       'pais', 'estado', 'municipio', 'bioma', 'bioma_id', 'foco_id'])
            self.readed_file = df
        return '>>> All files has been reads!'