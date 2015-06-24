# coding=utf-8
__author__ = 'JIE'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from db import client
import traceback
from common import zipTool

class createFile():
    @classmethod
    def mysql_to_file(cls):
        conn = client.conn()
        try:
            sql = "show table status"
            tables_infos = conn.query(sql)
            data = {}
            for k in tables_infos:
                if (k.Name[0:2] != "st"):
                    continue
                data["tableInfos"] = k
                sql = "SELECT * FROM " + k.Name
                result = (conn.query(sql))
                data["record"] = result
                sql = "SHOW FULL FIELDS FROM " + k.Name
                result1 = conn.query(sql)
                data["fieldInfo"] = result1
                cls.toToml(data)
            zipTool.zip_dir("./public/toml", "./public/toml.zip")
            return True
        except:
            traceback.print_exc()
            return False

    @classmethod
    def toToml(cls, data):
        toml_str = u""
        tableInfos = data['tableInfos']
        common = "#" + tableInfos.Name + ":" + tableInfos.Comment + "\n\n\n"
        fieldInfo = data['fieldInfo']

        for k in fieldInfo:
            common += "#" + k.Field + ":" + k.Comment + "\n"
        common += "\n\n\n"
        common = unicode()
        record = data['record']
        for i in record:
            toml_str += u"[" + unicode(i.id) + u"]\n"
            for key in i:
                toml_str += unicode(key) + u'="' + unicode(i[key]) + u'"\n'
            toml_str += u"\n\n"
        toml_str += u"\n"
        afile = open(u"./public/toml/" + tableInfos.Name + u".toml", "wt")
        afile.write(common+toml_str)
        afile.close()

        return True

