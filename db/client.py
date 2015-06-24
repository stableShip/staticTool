from littledb import pool, Connection
from configs import config

configParser = config.configParser
dbConfig = dict(configParser.items('db'))
dbPool = None
# print("dbPool %s " % dbPool)
def conn():
    if dbPool == None:
        init()
    return Connection(host=dbConfig['host'] + ":" + dbConfig['port'],
                      database=dbConfig['name'],
                      user=dbConfig['user'],
                      password=dbConfig['pswd'],
                      pool=dbPool)


def init():
    dbPool = pool(host=dbConfig['host'],
                  port=int(dbConfig['port']),
                  database=dbConfig['name'],
                  user=dbConfig['user'],
                  password=dbConfig['pswd'])
    # print("dbPool %s " % dbPool)

