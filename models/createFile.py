# coding=utf-8
import json

__author__ = 'JIE'
import sys, os

reload(sys)
sys.setdefaultencoding('utf-8')
from db import client
import traceback
from common import zipTool
import funcy as _
from dataToMysql import get_xls_table_map


class createFile():
    @classmethod
    def mysql_to_file(cls):
        conn = client.conn()
        try:
            sql = "show table status"
            tables_infos = conn.query(sql)
            data = {}
            os.popen('rm ./public/toml/* -f')
            os.popen('rm ./public/json/* -f')
            xls_table_map = get_xls_table_map()
            table_names = _.pluck("table_name", xls_table_map)
            for k in tables_infos:
                if k.Name in table_names:
                    data["tableInfos"] = k
                    sql = "SELECT * FROM " + k.Name
                    result = (conn.query(sql))
                    data["record"] = result
                    sql = "SHOW FULL FIELDS FROM " + k.Name
                    result1 = conn.query(sql)
                    data["fieldInfo"] = result1
                    cls.toToml(data)
                    cls.toJson(data)
            zipTool.zip_dir("./public/toml", "./public/toml.zip")
            zipTool.zip_dir("./public/json", "./public/json.zip")
            return True
        except:
            traceback.print_exc()
            return False

    @classmethod
    def toToml(cls, data):
        toml_str = u""
        tableInfos = data['tableInfos']
        if tableInfos.Name != "xls_table_map":
            common = "#" + tableInfos.Name + ":" + tableInfos.Comment + "\n\n\n"
            fieldInfo = data['fieldInfo']
            for k in fieldInfo:
                common += "#" + k.Field + ":" + k.Comment + "\n"
            common += "\n\n\n"
            record = data['record']

            record.sort(key=lambda obj: obj["id"])
            for i in record:
                toml_str += u"[" + unicode(i.id) + u"]\n"
                for key, value in i.items():
                    if unicode(value).isdigit() or cls.isNum(unicode(value)):
                        toml_str += unicode(key) + u'=' + unicode(value) + u'\n'
                    else:
                        if not value:
                            toml_str += unicode(key) + u'=""\n'
                        else:
                            toml_str += unicode(key) + u'="' + unicode(value) + u'"\n'
                toml_str += u"\n\n"
            toml_str += u"\n"
            afile = open(u"./public/toml/" + tableInfos.Name + u".toml", "wt")
            afile.write(common + toml_str)
            afile.close()

            return True

    @classmethod
    def toJson(cls, data):
        tableInfos = data['tableInfos']
        if tableInfos.Name != "xls_table_map":
            record = data['record']
            datas = {}
            for data in record:
                for key, value in data.items():
                    if cls.isNum(unicode(value)):
                        if isinstance(value, float):
                            value = float(unicode(value))
                        data[key] = value
                    else:
                        if not value:
                            data[key] = ""
                        else:
                            data[key] = unicode(value)
                if cls.isNum(unicode(data.id)):
                    data.id = int(round(float(unicode(data.id))))
                datas[data.id] = data
            afile = open(u"./public/json/" + tableInfos.Name + u".json", "wt")
            afile.write(json.dumps(datas, indent=4, ensure_ascii=False, sort_keys=True))
            afile.close()

            return True

    @classmethod
    def isNum(cls, value):
        # 判断是否为数字
        try:
            float(value)
        except Exception, e:
            return False
        else:
            return True
