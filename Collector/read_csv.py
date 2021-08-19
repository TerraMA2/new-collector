import csv
import sys

from download_files import Download_files


class Read_csv(Download_files):
    def __init__(self, address, folder):
        self.file_path = []
        super().__init__(address, folder)

    def readFiles(self):
        for file in self.fileDay:
            with open(self.files_day_directory + '\\' + file, 'rt', encoding='UTF-8') as data:
                reader = csv.reader(data)
                try:
                    for line in reader:
                        print(line)
                except csv.Error as e:
                    sys.exit('File %s, line %d: %s' % (file, reader.line_num, e))
        return '>>> All files has been reads!'