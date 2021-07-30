from ftplib import FTP


class Con2ftp:
    def __init__(self, address, folder):
        self.address = address
        self.folder = folder
        self.conexao = ''
        self.files_list = []

    def conn(self):
        self.conexao = FTP(self.address)
        try:
            self.conexao.login('queimadas', 'inpe_2012')
            return ">>>> " + self.conexao.getwelcome()
        except:
            return '  > Connection has been failed'

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

    def listFiles(self, files):
        return self.files_list