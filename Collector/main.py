# Importar do arquivo con2ftp a classe Con2ftp
from con2ftp import Con2ftp
from db_connection import Db_connection
from download_files import Download_files

if __name__ == '__main__':

    print("Connecting to FTP server...")
    conn = Download_files('ftp.dgi.inpe.br','/terrama2q/TerraMA2Q_408')
    print(conn.conn())

    print("Searching for burn files...")
    print(conn.countFiles())

    # print("listing all files of FTP Server...")
    # print(conn.listFiles())

    # print("Downloading all files")
    # print(conn.downloadFiles('C:\\git\\new-collector\\Collector\\Files'))

    print("listing all files of today...")
    print(conn.listFileDay())

    print("Downloading today's files")
    print(conn.downloadFilesDay('C:\\git\\new-collector\\Collector\\Files'))

    dbcon = Db_connection('localhost', 'postgis_31_sample', 'postgres', 'postgres')
    print("Connecting to Postgis Data base")
    print(dbcon.connection())

    print("Selecting all itens from any table")
    print(dbcon.select_itens())
