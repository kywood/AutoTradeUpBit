import configparser
import sys

from Utils.FileUtil import FileUtil
from Utils.FileWriter import E_FILE_MODE


def main(argv):

    file= FileUtil('config.conf')
    file.Open(E_FILE_MODE.R)

    file.ReadLine()
    #
    # config = configparser.ConfigParser()
    # config.read('config.conf')
    # config.sections()
    # print( config['Common']['BaseUrl'])
    # print( config['Test']['Ticker'])
    pass





if __name__ == "__main__":
    main(sys.argv)