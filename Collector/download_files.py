from con2ftp import Con2ftp
from datetime import date
import os


class Download_files(Con2ftp):
    def __init__(self, address, folder):
        self.files_day_directory = ''
        super().__init__(address, folder)

    def countFiles(self):
        self.conexao.cwd(self.folder)
        log = []
        nonpassive = False
        self.conexao.retrlines('LIST', callback=log.append)
        dirs = (line.rsplit(None, 1)[1] for line in log)
        if nonpassive:
            self.conexao.set_pasv(False)
        for file in dirs:
            self.files_list.append(file)
        del (self.files_list[0:2])
        return '>>>> ' + str(len(self.files_list)) + ' Files found'

    def listFiles(self):
        return self.files_list

    def downloadFiles(self, directory):
        nonpassive = False
        if nonpassive:
            self.conexao.set_pasv(False)
        try:
            for filename in self.files_list:
                local_filename = os.path.join(directory, filename)
                file = open(local_filename, 'wb')
                self.conexao.retrbinary('RETR ' + filename, file.write)
                file.close()
            self.conexao.quit()
            return 'Download has been finished!'
        except():
            self.conexao.quit()
            return 'Failed to download files...'

    def numberOfTodayFiles(self):
        actual_date = date.today()
        if actual_date.day < 10:
            day = "0" + str(actual_date.day)
        else:
            day = actual_date.day
        if actual_date.month < 10:
            month = "0" + str(actual_date.month)
        else:
            month = actual_date.month
        year = actual_date.year

        for d in self.files_list:
            if 'focos_terrama2q_' + str(year) + str(month) + str(day) in d:
                self.fileDay.append(d)

        return '>>>> ' + str(len(self.fileDay)) + ' Files found'

    def listFileDay(self):
        return self.fileDay

    def downloadFilesDay(self, directory):
        self.files_day_directory = directory
        nonpassive = False
        if nonpassive:
            self.conexao.set_pasv(False)
        try:
            print(" >>> Saving all today's Files... ")

            for filename in self.fileDay:
                if os.path.isfile(directory + '/' + filename):
                    pass
                else:
                    local_filename = os.path.join(directory, filename)
                    file = open(local_filename, 'wb')
                    self.conexao.retrbinary('RETR ' + filename, file.write)
                    file.close()
            self.conexao.quit()
            return 'Download has been finished!'
        except():
            self.conexao.quit()
            return 'Failed to download files...'