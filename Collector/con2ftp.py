from ftplib import FTP


class Con2ftp:
    def __init__(self, address, folder):
        self.address = address
        self.folder = folder
        self.conexao = ''
        self.files_list = []
        self.fileDay = []

    def conn(self, USER_FTP, PASS_FTP):
        self.conexao = FTP(self.address)
        try:
            self.conexao.login(USER_FTP, PASS_FTP)
            return ">>>> " + self.conexao.getwelcome()
        except():
            return ' >> Connection has been failed'