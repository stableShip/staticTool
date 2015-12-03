#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from common import xlsTool
from db import client
import traceback


def data_to_mysql():
    """
    将数据插入mysql中
    :return:
    """
    try:
        result = isValidRequset()
        if "error" not in result:
            # 获取xls与数据库表之间的映射关系
            xls_table_map = get_xls_table_map()
            for rows in xls_table_map:
                table = rows.table_name
                xls = rows.xls_name
                # xls文件存放位置
                file_dir = "./public/file/"
                datas = xlsTool.getXlsData(file_dir + xls + ".xls").get("datas")
                # 清空数据库表数据
                delDbData(table)
                # 插入数据
                insert_data_to_db(datas, table)
            return {"result": "success"}
        else:
            return result
    except Exception, e:
        traceback.print_exc()
        return e


def isValidRequset():
    """
    判断数据库字段和excel表的字段长度是否一致
    :return:bool
    """
    try:
        xls_table_map = get_xls_table_map()
        for rows in xls_table_map:
            # xls文件存放位置
            file_dir = "./public/file/"
            table_rows = getDbHead(rows.table_name)
            xls_rows = xlsTool.getXlsData(file_dir + rows.xls_name + ".xls").get("headers")
            print rows.table_name, "数据库表字段长度:", len(table_rows), "      ", rows.xls_name, "xls文件字段长度", len(xls_rows)
            if len(table_rows) != len(xls_rows):
                error_message = rows.table_name + "表与 " + rows.xls_name + "文件 数据需求长度不一致,数据库:" + str(len(
                    table_rows)) + " 文件:" + str(len(xls_rows))
                return {"error": error_message}
        return {"result": "success"}
    except Exception, e:
        traceback.print_exc()
        return e


def getDbHead(table_name):
    """
    获取数据库表所有字段数据
    :param table_name:
    :return:
    """
    try:
        conn = client.conn()
        sql = "SHOW FULL FIELDS FROM {0}"
        sql = sql.format(table_name)
        result = conn.query(sql)
        return result
    except:
        traceback.print_exc()
        return False


def get_xls_table_map():
    """
    获取xls与数据库表之间的映射关系
    :return:
    """
    try:
        conn = client.conn()
        sql = "select * from xls_table_map"
        result = conn.query(sql)
        return result
    except:
        traceback.print_exc()
        return False


def delDbData(table_name):
    """
    删除数据库表数据
    :param table_name:
    :return:
    """
    try:
        print "清理表:", table_name
        conn = client.conn()
        sql = "truncate table `{0}`"
        sql = sql.format(table_name)
        result = conn.execute(sql)
        return result
    except:
        traceback.print_exc()
        return False


def insert_data_to_db(datas, table):
    """
    插入数据
    :param datas:
    :param table:
    :return:
    """
    try:
        conn = client.conn()
        string = ""
        for data in datas:
            temp_str = json.dumps(tuple(data), ensure_ascii=False)
            temp_str = temp_str.replace("[", "(")
            temp_str = temp_str.replace("]", ")")
            temp_str = temp_str.replace("%", "%%")
            string += temp_str + ","
        sql = " insert into {0} values {1}"
        sql = sql.format(table, string[:-1])
        print sql
        result = conn.execute(sql)
        return result
    except:
        traceback.print_exc()
        return False
