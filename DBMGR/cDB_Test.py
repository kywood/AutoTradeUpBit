
from DBMGR.IDB_Lists import IDB_Lists
from DBMGR.cDBManager import cDBManager
from DBMGR.cDBProperty import cOracleProperty, cMysqlProperty
from DBMGR.cDB_DEFINES import I_DB__ALIAS
from DBMGR.cMysqlDBOBJ import cMysqlDBOBJ
from DBMGR.cOracleDBOBJ import cOracleDBOBJ



class E_DB_ALIAS(I_DB__ALIAS):
    MYSQL_TSR = 100
    MYSQL_KMA = 110

class cDBConnectInfo( IDB_Lists ):
    def __init__(self):
        IDB_Lists.__init__(self ,
                           {
                               E_DB_ALIAS.MYSQL_TSR: cMysqlDBOBJ(
                                   cMysqlProperty(host='127.0.0.1', port=3306, user='min', passwd='oracle', db='min')),
                               E_DB_ALIAS.MYSQL_KMA: cMysqlDBOBJ(
                                   cMysqlProperty(host='127.0.0.1', port=3306, user='min', passwd='oracle',
                                                  db='min')) ,
                           })


class cDB_Info_Test( IDB_Lists ):
    def __init__(self):
        IDB_Lists.__init__(self ,
                           {
                               E_DB_ALIAS.ORA_TEST: cOracleDBOBJ(cOracleProperty("ID/PASS@DB")),
                               E_DB_ALIAS.MY_TEST: cMysqlDBOBJ(
                                   cMysqlProperty(host='127.0.0.1', port=3306, user='min', passwd='oracle', db='min'))
                           })



def main():
    '''
    0 : dest
    1 : src
    '''

    #cDB_Info_Test()

    DBM = cDBManager(cDB_Info_Test())
    # DBM = cDBManager(cDBConnectInfo())


    # cDBManager.__call__().Test_Print()
    # DBM.SetDBInfo(  )
    #cDBManager.__call__().Connect( E_DB_ALIAS.ORA_TEST )


    DBM.Connect( E_DB_ALIAS.ORA_TEST )

    # cDBManager.ConnectAll()

    print (DBM.ExecuteQuery(E_DB_ALIAS.ORA_TEST ,
                                             "select * from user  "))

    print (DBM.IsConnect(E_DB_ALIAS.ORA_TEST))
    # DBM.Close(E_DB_ALIAS.ORA_TEST)

    #
    # print cDBManager.__call__().ExecuteQuery(E_DB_ALIAS.MY_TEST ,
    #                                          "select * from user  ")
    # print cDBManager.__call__().IsConnect(E_DB_ALIAS.MY_TEST)
    # cDBManager.__call__().Close(E_DB_ALIAS.MY_TEST)
    #
    # print cDBManager.__call__().IsConnect(E_DB_ALIAS.MY_TEST)

if __name__ == '__main__':
    main()
