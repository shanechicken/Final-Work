import pymysql

'''
mysql -u root -p'123456' -h 120.25.251.110 -P 3306 -D schema_pm
'''

db_config = {
    "host": "120.25.251.110", 
    "port": 3306, 
    "user": "root", 
    "password": "123456", 
    "database": "schema_pm"
}

db_connection = pymysql.connect(host = db_config["host"], 
                                port = db_config["port"], 
                                user = db_config["user"], 
                                password = db_config["password"], 
                                database = db_config["database"])

db_connection.close()
