import sys


class FileNamePutInBetween:


    def __init__(self,_fileName,_putInString,_isUnderBar=True):
        self.FileName=_fileName
        self.PutInString=_putInString
        self.IsUnderBar = _isUnderBar
        pass

    def ToString(self):
        words=self.FileName.split('.')
        retStr=words[0]+("_" if self.IsUnderBar else "")+self.PutInString+"."+words[1]
        return retStr

        pass

    pass


def main(argv):
    sb = FileNamePutInBetween("UpBitCollectSample.csv" , "debug")
    print(sb.ToString())

    pass

if __name__ == '__main__':
    main(sys.argv)

