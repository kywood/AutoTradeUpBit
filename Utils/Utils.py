import ftplib
import time
import datetime
import platform
from urllib.request import urlopen

from Utils.cLogger import cLogger

global G_FTP_SLEEP_TIME



class Utils:

    G_FTP_SLEEP_TIME = 0.05



    @staticmethod
    # def CurrentTimeString(_format="""%Y%m%d-%H:%M:%S"""):
    def CurrentTimeString(_format="""%Y%m%d%H%M%S"""):
        return datetime.datetime.now().strftime(_format)

    @staticmethod
    def MakeTailSlash(path):
        # path = "C:\Python27\\"
        length = len(path)
        slashV = "/"

        if platform.system().upper() == "WINDOWS":
            slashV = "\\"

        if path[length - 1] != slashV:
            path = path + slashV

        return path

    @staticmethod
    def GetFileName(path):
        idx = path.rfind('/')
        return path[idx + 1:len(path)]

    @staticmethod
    def WebDownLoad( remote_url , local_path , file_name = None):

        localPath = local_path

        if file_name == None:
            localPath = localPath + '/' + Utils.GetFileName( remote_url )

        if file_name != None:
            localPath = Utils.MakeTailSlash(local_path) + file_name

        filedata = urlopen(remote_url)
        data_to_write = filedata.read()

        with open(localPath, 'wb') as f:
            f.write(data_to_write)

        pass

    @staticmethod
    def FtpGetFile(ftp_ip, ftp_id, ftp_pw, remote_full_path, local_full_path):
        ftp = ftplib.FTP(ftp_ip)

        try:
            ftp.login(ftp_id, ftp_pw)

            time.sleep(G_FTP_SLEEP_TIME)

            result = ftp.retrbinary("RETR " + remote_full_path, open(local_full_path, "wb").write)
            if result[:3] == "226":
                cLogger.instance().Print(cLogger.E_LOG.INFO, 'FILE DOWNLOAD SUCCESS... REMOTE_PATH : {0} / REMOTE_PATH : {1}'.format(remote_full_path,
                                                                                                                                     local_full_path))
                # logging.info('FILE DOWNLOAD SUCCESS... REMOTE_PATH : {0} / REMOTE_PATH : {1}'.format(remote_full_path,
                #                                                                                      local_full_path))
            else:
                cLogger.instance().Print(cLogger.E_LOG.ERROR, "RESULT RETURN MESSAGE : [ {0} ]".format(result))
                raise Exception( "Ftp RETR ERROR " + "RESULT RETURN MESSAGE : [ {0} ]".format(result) )
                # logging.error("RESULT RETURN MESSAGE : [ {0} ]".format(result))

        except ftplib.all_errors as E:

            cLogger.instance().Print(cLogger.E_LOG.EXCEPTION , "FILE DOWNLOAD ERROR..\nREMOTE_PATH = [ {0} ] LOCAL_PATH = [ {1} ]".format(remote_full_path,local_full_path))
            # logging.exception(
            #     "FILE DOWNLOAD ERROR..\nREMOTE_PATH = [ {0} ] LOCAL_PATH = [ {1} ]".format(remote_full_path,
            #                                                                                local_full_path))

            cLogger.instance().Print(   cLogger.E_LOG.ERROR , remote_full_path )

            raise E
            # logging.error(remote_full_path)
            # return False

        except BaseException as E:
            cLogger.instance().Print(cLogger.E_LOG.EXCEPTION , "ETC ERROR.." )
            # logging.exception("ETC ERROR..")
            # return False

            raise E

        finally:
            ftp.quit()
            ftp.close()

        return True

    @staticmethod
    def FtpPutFile(ftp_ip, ftp_id, ftp_pw, remote_full_path, local_full_path):
        ftp = ftplib.FTP(ftp_ip)

        try:
            ftp.login(ftp_id, ftp_pw)
            time.sleep(G_FTP_SLEEP_TIME)

            result = ftp.storbinary("STOR " + remote_full_path, open(local_full_path, "rb"))

            if result[:3] == "226":
                cLogger.instance().Print( cLogger.E_LOG.INFO , 'FILE UPLOAD SUCCESS... REMOTE_PATH : {0} / REMOTE_PATH : {1}'.format(remote_full_path,
                                                                                                   local_full_path) )

                # logging.info('FILE UPLOAD SUCCESS... REMOTE_PATH : {0} / REMOTE_PATH : {1}'.format(remote_full_path,
                #                                                                                    local_full_path))
            else:
                cLogger.instance().Print( cLogger.E_LOG.ERROR , "RESULT RETURN MESSAGE : [ {0} ]".format(result) )
                # logging.error("RESULT RETURN MESSAGE : [ {0} ]".format(result))

        except ftplib.all_errors:
            cLogger.instance().Print( cLogger.E_LOG.EXCEPTION , "FILE UPLOAD ERROR..\nREMOTE_PATH = [ {0} ] LOCAL_PATH = [ {1} ]".format(remote_full_path,
                                                                                                       local_full_path) )
            # logging.exception("FILE UPLOAD ERROR..\nREMOTE_PATH = [ {0} ] LOCAL_PATH = [ {1} ]".format(remote_full_path,
            #                                                                                            local_full_path))
            return False

        except BaseException:
            cLogger.instance().Print(cLogger.E_LOG.EXCEPTION,"ETC ERROR..")
            # logging.exception("ETC ERROR..")
            return False

        finally:
            ftp.quit()
            ftp.close()

        return True
