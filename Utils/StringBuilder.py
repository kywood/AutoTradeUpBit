import sys


class StringBuilder:

    def __init__(self):

        self.Stringlists=[]

        pass

    def Append(self,str):
        self.Stringlists.append(str)
        pass

    def ToString(self):
        RetStr=""
        for str in self.Stringlists:
            RetStr = RetStr + str

        return RetStr


def main(argv):
    sb = StringBuilder()

    sb.Append("1")
    sb.Append("1")
    sb.Append("1")
    sb.Append("1")

    print(sb.ToString())

    pass

if __name__ == '__main__':
    main(sys.argv)

