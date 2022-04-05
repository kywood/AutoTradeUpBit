from DBMGR.IDB_Lists import IDB_Lists
from DBMGR.cDBManager import cDBManager
from DBMGR.cDBProperty import cOracleProperty, cMysqlProperty
from DBMGR.cDB_Test import E_DB_ALIAS
from DBMGR.cMysqlDBOBJ import cMysqlDBOBJ
from DBMGR.cOracleDBOBJ import cOracleDBOBJ




class cDB_Info_Test( IDB_Lists ):
    def __init__(self):
        IDB_Lists.__init__(self ,
                           {
                               E_DB_ALIAS.MY_TEST: cMysqlDBOBJ(
                                   cMysqlProperty( host='127.0.0.1', port=3306 , user='min', passwd='oracle', db='min' ))
                           })

def main():

    DBM = cDBManager(cDB_Info_Test())

    # host='90.90.30.245', port=3306 , user='tsr', passwd='tsr_12345', db='tsr'

    # cDBManager.__call__().Test_Print()
    # DBM.SetDBInfo(  )
    #cDBManager.__call__().Connect( E_DB_ALIAS.ORA_TEST )

    DBObj = DBM.GetDbObject(E_DB_ALIAS.MY_TEST )
    DBObj.Connect()
    # DBM.Connect( E_DB_ALIAS.ORA_TEST )
    # cDBManager.ConnectAll()

    print(DBObj.ExecuteQuery("select * from user" ))
    print(DBObj.IsConnect())


if __name__ == '__main__':
    main()
