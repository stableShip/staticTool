# coding=utf-8
__author__ = 'JIE'
import tornado.web
from models.createFile import createFile
from models import dataToMysql
import os
import traceback

class file(tornado.web.RequestHandler):
    def post(self):
        try:
            type = self.get_argument("type", None)
            if type == "mysql":
                result1 = dataToMysql.data_to_mysql()
                if "error" in result1:
                    return self.write(result1)
            result = createFile.mysql_to_file()
            if result:
                print "生成文件成功"
                self.write("SUCCESS")
            else:
                self.write("FAIL")
        except Exception as e:
            traceback.print_exc()
            self.write(str(e))

    def get(self):
        file_type = self.get_argument("type", None)
        if file_type == "toml":
            self.set_header('Content-Type', 'application/octet-stream')
            self.set_header('Content-Disposition', 'attachment;filename=toml.zip')
            # 读取的模式需要根据实际情况进行修改
            with open("./public/toml.zip", 'rb') as f:
                while True:
                    data = f.read(500)
                    if not data:
                        break
                    self.write(data)
            self.finish()
        elif file_type == "json":
            self.set_header('Content-Type', 'application/octet-stream')
            self.set_header('Content-Disposition', 'attachment;filename=json.zip')
            # 读取的模式需要根据实际情况进行修改
            with open("./public/json.zip", 'rb') as f:
                while True:
                    data = f.read(500)
                    if not data:
                        break
                    self.write(data)
            self.finish()
        elif file_type == "xls":
            self.set_header('Content-Type', 'application/octet-stream')
            self.set_header('Content-Disposition', 'attachment;filename=xls.zip')
            # 读取的模式需要根据实际情况进行修改
            with open("./tmp/xls.zip", 'rb') as f:
                while True:
                    data = f.read(500)
                    if not data:
                        break
                    self.write(data)
            self.finish()

    def put(self):
        upload_path = os.path.join(os.path.dirname(__file__), 'files')  # 文件的暂存路径
        file_metas = self.request.files['file']  # 提取表单中‘name’为‘file’的文件元数据
        for meta in file_metas:
            filename = meta['filename']
            filepath = os.path.join(upload_path, filename)
            with open(filepath, 'wb') as up:  # 有些文件需要已二进制的形式存储，实际中可以更改
                up.write(meta['body'])
            self.write('finished!')


