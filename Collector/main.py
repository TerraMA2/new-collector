import os
from dotenv import load_dotenv
from db_connection import Db_connection

load_dotenv()

USER_FTP = os.getenv('USER_FTP')
PASS_FTP = os.getenv('PASS_FTP')
HOST = os.getenv('HOST')
USER_DATABASE = os.getenv('USER_DATABASE')
PASS_DATABASE = os.getenv('PASS_DATABASE')
DATABASE = os.getenv('DATABASE')
TABLE = os.getenv('TABLE')
FTP_HOST = os.getenv('FTP_HOST')
FOLDER_FTP = os.getenv('FOLDER_FTP')
DIRECTORY_FOLDER = os.getenv('DIRECTORY_FOLDER')

if __name__ == '__main__':
    db_con = Db_connection(HOST, DATABASE, USER_DATABASE, PASS_DATABASE, TABLE, FTP_HOST, FOLDER_FTP)

    print("Connecting to FTP server...")
    print(db_con.conn(USER_FTP, PASS_FTP))

    print("\nSearching for burn files...")
    print(db_con.countFiles())

    print("\nlisting all files of FTP Server...")
    # print(reader.listFiles())

    print("\nDownloading all files")
    # print(reader.downloadFiles('C:\\git\\new-collector\\Collector\\Files'))

    print("\nNumber of files today...")
    print(db_con.numberOfTodayFiles())

    #print("\nListing all today's Files...")
    # print(db_con.listFileDay())

    #######################################################################
    def select_option():
        data = {
            1: "Download Files in range of dates",
            2: "Download all today's files",
            3: "Exit"
        }
        print("Choose an option: ")
        for options in sorted(data):
            print("{} - {}".format(options, data[options]))
        value = input("Option: ")
        if not value.isdigit() or not int(value) in data:
            invalid_value(value)
        elif value == "1":
            db_con.down_in_range()
        elif value == "2":
            pass
        elif value == "3":
            print("Finalizing software ...")
            exit()

    def invalid_value(value):
        print("This option " + value + " is invalid, please select another option\n")
        select_option()

    select_option()

    print(db_con.downloadFilesDay(DIRECTORY_FOLDER))

    print("\nReading files... ")
    print(db_con.readFiles())

    print("\nConnecting to Postgis Data base")
    print(db_con.connection())

    #######################################################################
    def select_insert_option():
        data = {
            1: "Insert all files from Latin America",
            2: "Insert only Brazilian files",
            3: "Insert files of a specific state",
            4: "Exit"
        }
        print("Choose an option: ")
        for options in sorted(data):
            print("{} - {}".format(options, data[options]))
        value = input("Option: ")
        if not value.isdigit() or not int(value) in data:
            invalid_insert_value(value)
        elif value == "1":
            print("\nInserting all values on DataBase...")
            db_con.insert_all_values()
        elif value == "2":
            print("\nInserting Brazilian values on DataBase...")
            db_con.insert_brazil_values()
        elif value == "3":
            db_con.insert_specified_values()
        elif value == "4":
            print("Finalizing software ...")
            exit()

    def invalid_insert_value(value):
        print("This option " + value + " is invalid, please select another option\n")
        select_insert_option()

    select_insert_option()

