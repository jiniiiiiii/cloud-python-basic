import pymysql


class DBConn:
    def __init__(self, host, user, password, database):
        self.host = host,
        self.user = user,
        self.password = password,
        self.database = database
        
        
    '''def dbConn(self):
        conn = pymysql.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )
        return conn'''

    def execQuery(self, sql):
        cursor=self.conn.cursor()
        result = cursor.execute(sql)
        if result: 
            return True
        else:
            return False