# Importar do arquivo con2ftp a classe Con2ftp
from con2ftp import Con2ftp

if __name__ == '__main__':

    print('Connecting to FTP server...')
    conn = Con2ftp('ftp.dgi.inpe.br','/terrama2q/TerraMA2Q_408')
    print(conn.conn())

    print('Searching for burn files...')
    print(conn.countFiles())
    print(conn.listFiles(''))