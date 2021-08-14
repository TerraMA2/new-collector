import os
from ftplib import FTP
from datetime import date


class Con2ftp:
    def __init__(self, address, folder):
        self.address = address
        self.folder = folder
        self.conexao = ''
        self.files_list = []
        self.fileDay = []

    def conn(self):
        self.conexao = FTP(self.address)
        try:
            self.conexao.login('queimadas', 'inpe_2012')
            return ">>>> " + self.conexao.getwelcome()
        except:
            return ' >> Connection has been failed'

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
        global all_files
        all_files = self.files_list
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

    def listFileDay(self):
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

    def downloadFilesDay(self, directory):
        nonpassive = False
        if nonpassive:
            self.conexao.set_pasv(False)
        try:
            for filename in self.fileDay:
                local_filename = os.path.join(directory, filename)
                file = open(local_filename, 'wb')
                self.conexao.retrbinary('RETR ' + filename, file.write)
                print('Saving File: ' + filename)
                file.close()
            self.conexao.quit()
            return 'Download has been finished!'
        except():
            self.conexao.quit()
            return 'Failed to download files...'
