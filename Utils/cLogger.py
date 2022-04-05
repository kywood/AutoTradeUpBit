from urllib3.connectionpool import xrange

import sys
import time
import traceback
import os

from Utils.SingletonInstane import SingletonInstane


class E_LOG:

    EXCEPTION = "EXCEPTION"
    DEBUG   = "DEBUG"
    WARNING = "WARNING"
    ERROR   = "ERROR"
    INFO    = "INFO"


class cLogger(SingletonInstane):


    def getTracebackStr2(self):
        lines = traceback.format_exc().strip().split('\n')
        rl = [lines[-1]]
        lines = lines[1:-1]
        lines.reverse()
        nstr = ''
        for i in range(len(lines)):
            line = lines[i].strip()
            if line.startswith('File "'):
                eles = lines[i].strip().split('"')
                basename = os.path.basename(eles[1])
                lastdir = os.path.basename(os.path.dirname(eles[1]))
                eles[1] = '%s/%s' % (lastdir, basename)
                rl.append('^\t%s %s' % (nstr, '"'.join(eles)))
                nstr = ''
            else:
                nstr += line
        return '\n'.join(rl)

    def getTracebackStr(self):
        lines = traceback.format_exc().strip().split('\n')
        rl = [lines[-1]]
        lines = lines[1:-1]
        lines.reverse()
        for i in xrange(0, len(lines), 2):
            rl.append('^\t%s at %s' % (lines[i].strip(), lines[i + 1].strip()))
        return '\n'.join(rl)




    def PrintV(self, e_log , version , *mes  ):
        now = time.localtime()
        timeStr = "%04d-%02d-%02d %02d:%02d:%02d" % (
        now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        f_code = sys._getframe(1).f_code
        # ## [ 2018-10-10 11:67:22 ][ERROR][ FILE FUNC LINE] MESSAGE
        # print( """[ {0} ][{1}][{2} {3} {4}] {5}""".format( timeStr ,e_log ,  f_code.co_filename ,f_code.co_name , f_code.co_firstlineno , message  ))

        ## [ 2018-10-10 11:67:22 ][ERROR][ FILE FUNC LINE] MESSAGE
        # print("""[ {0} ][{1}][{2} {3} ] {4}""".format(timeStr, e_log, f_code.co_filename, f_code.co_name,
        #                                                   message.encode('euckr')))

        message = ""

        for v in mes:
            message += v

        if e_log == E_LOG.EXCEPTION:
            self.PrintExcept( timeStr ,f_code , message  )
        else:
            print ("""[ {0} ][ {1} ][ {2} {3} ][ {4} ]{5}""".format( timeStr ,e_log ,  f_code.co_filename , f_code.co_name , version , message ))
            # print "[" , timeStr , "][" ,  e_log , "][" , f_code.co_filename, " " , f_code.co_name , "]" , message


    def Print( self, e_log , *mes ):
        now = time.localtime()
        timeStr = "%04d-%02d-%02d %02d:%02d:%02d" % (
        now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        f_code = sys._getframe(1).f_code
        # ## [ 2018-10-10 11:67:22 ][ERROR][ FILE FUNC LINE] MESSAGE
        # print( """[ {0} ][{1}][{2} {3} {4}] {5}""".format( timeStr ,e_log ,  f_code.co_filename ,f_code.co_name , f_code.co_firstlineno , message  ))

        ## [ 2018-10-10 11:67:22 ][ERROR][ FILE FUNC LINE] MESSAGE
        # print("""[ {0} ][{1}][{2} {3} ] {4}""".format(timeStr, e_log, f_code.co_filename, f_code.co_name,
        #                                                   message.encode('euckr')))

        message = ""

        for v in mes:
            message += v

        if e_log == E_LOG.EXCEPTION:
            self.PrintExcept( timeStr ,f_code , message  )
        else:
            print("[" , timeStr , "][" ,  e_log , "][" , f_code.co_filename, " " , f_code.co_name , "]" , message)


    #
    # def Print( self, e_log , message):
    #     now = time.localtime()
    #     timeStr = "%04d-%02d-%02d %02d:%02d:%02d" % (
    #     now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    #     f_code = sys._getframe(1).f_code
    #     # ## [ 2018-10-10 11:67:22 ][ERROR][ FILE FUNC LINE] MESSAGE
    #     # print( """[ {0} ][{1}][{2} {3} {4}] {5}""".format( timeStr ,e_log ,  f_code.co_filename ,f_code.co_name , f_code.co_firstlineno , message  ))
    #
    #     ## [ 2018-10-10 11:67:22 ][ERROR][ FILE FUNC LINE] MESSAGE
    #     # print("""[ {0} ][{1}][{2} {3} ] {4}""".format(timeStr, e_log, f_code.co_filename, f_code.co_name,
    #     #                                                   message.encode('euckr')))
    #
    #     if e_log == E_LOG.EXCEPTION:
    #         self.PrintExcept( timeStr ,f_code , message  )
    #     else:
    #         print "[" , timeStr , "][" ,  e_log , "][" , f_code.co_filename, " " , f_code.co_name , "]" , message


    def PrintExcept(self , time_str , f_code ,  message):

        print("[", time_str, "][ EXCEPTION ][", f_code.co_filename, " ", f_code.co_name, "]", message)
        print (self.getTracebackStr2())

        pass

