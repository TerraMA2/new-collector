# Importar do arquivo con2ftp a classe Con2ftp
from con2ftp import Con2ftp
from db_connection import Db_connection
from download_files import Download_files
from read_csv import Read_csv

if __name__ == '__main__':

    print("Connecting to FTP server...")
    reader = Read_csv('ftp.dgi.inpe.br', '/terrama2q/TerraMA2Q_408')
    print(reader.conn())

    print("\nSearching for burn files...")
    print(reader.countFiles())

    print("\nlisting all files of FTP Server...")
    #print(reader.listFiles())

    print("\nDownloading all files")
    #print(reader.downloadFiles('C:\\git\\new-collector\\Collector\\Files'))

    print("\nNumber of files today...")
    print(reader.numberOfTodayFiles())

    print("\nListing all today's Files...")
    # print(reader.listFileDay())

    print("\nDownloading today's files")
    print(reader.downloadFilesDay('C:\\git\\new-collector\\Collector\\Files'))

    #print(reader.filesDirectory())

    print("\nThe File's folder is: ")
    print(reader.readFiles())

    # todo: Classe para inserilos lidos no POSTGIS

    # db_con = Db_connection('localhost', 'postgis_31_sample', 'postgres', 'postgres')
    # print("Connecting to Postgis Data base")
    # print(db_con.connection())
    #
    # print("Selecting all itens from any table")
    # print(db_con.select_itens())