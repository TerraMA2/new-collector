from read_csv import Read_csv
import os


class Delete_files(Read_csv):
    def delete_files(self):
        for infile in self.fileDay:
            os.remove(self.files_day_directory + '\\' + infile)
        return 'Files Removeds!'