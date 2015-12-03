#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd


def getXlsData(file):
    """
    获取xls文件数据
    :param file:文件路径
    :return:
    """
    try:
        book = xlrd.open_workbook(file)
        sheet = book.sheet_by_index(0)
        # 标题数组(第一行数据)
        headers = sheet._cell_values[0]
        # 列数
        cols = sheet.ncols
        # 行数
        rows = sheet.nrows
        # 除了第一行之外的所有数据
        datas = sheet._cell_values[1:]

        return {
            "headers": headers,
            "cols": cols,
            "rows": rows,
            "datas": datas
        }
    except:
        raise "找不到文件,请先上传" + file
