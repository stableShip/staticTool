#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import os
from common import zipTool


class UploadHander(tornado.web.RequestHandler):
    def post(self):

        basepath = os.path.curdir
        upload_path = os.path.join(basepath, 'tmp')  # 文件的暂存路径
        # 清空文件夹下的所有文件
        os.popen('rm ' + upload_path + '/* -f')
        file_metas = self.request.files['file']  # 提取表单中‘name’为‘file’的文件元数据
        for meta in file_metas:
            filename = meta['filename']
            if (os.path.splitext(filename)[1][1:] == "zip"):
                filename = "xls.zip"
                filepath = os.path.join(upload_path, filename)
                with open(filepath, 'wb') as up:  # 有些文件需要已二进制的形式存储，实际中可以更改
                    up.write(meta['body'])
                zipTool.extract_to(filepath, "./public/file")
                self.write('上传成功')
            else:
                self.write("必须为zip文件")
