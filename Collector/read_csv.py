import os.path

from download_files import Download_files
import pandas as pd

class Read_csv(Download_files):
    def __init__(self, address, folder):
        self.readed_file = ''
        super().__init__(address, folder)

    def readFiles(self):
        data_you_need = pd.DataFrame()
        for infile in self.fileDay:
            if os.stat(self.files_day_directory + '\\' + infile).st_size == 0:
                pass
            else:
                data = pd.read_csv(self.files_day_directory + '\\' + infile)
                data_you_need = data_you_need.append(data, ignore_index=True)
        self.readed_file = data_you_need
        return '>>> All files has been reads!'