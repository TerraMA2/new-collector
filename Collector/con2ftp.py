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

        for d in range(0, 2360, 10):
            if d < 10:
                self.fileDay.append('focos_terrama2q_' + str(year) + str(month) + str(day) + '_000' + str(d) + '.csv')
            elif 10 <= d <= 90:
                self.fileDay.append('focos_terrama2q_' + str(year) + str(month) + str(day) + '_00' + str(d) + '.csv')
            elif 100 <= d <= 990:
                self.fileDay.append('focos_terrama2q_' + str(year) + str(month) + str(day) + '_0' + str(d) + '.csv')
            else:
                self.fileDay.append('focos_terrama2q_' + str(year) + str(month) + str(day) + '_' + str(d) + '.csv')

        # TODO: COMPARAR SELF.FILE_LIST COM SELF.FILEDAY E REMOVER TODOS OS ITENS QUE NÃO EXISTEM EM FILE_LIST DE FILEDAY
        return self.fileDay

    def downloadFilesDay(self, directory):
        nonpassive = False

        if nonpassive:
            self.conexao.set_pasv(False)

        try:
            for filename in self.fileDay:
                local_filename = os.path.join(directory, filename)
                file = open(local_filename, 'wb')
                self.conexao.retrbinary('RETR ' + filename, file.write)
                file.close()
            self.conexao.quit()
            return 'Download has been finished!'
        except():
            self.conexao.quit()
            return 'Failed to download files...'
