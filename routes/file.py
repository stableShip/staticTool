# coding=utf-8
__author__ = 'JIE'
import tornado.web
from models import createFile
from common import zipTool


class file(tornado.web.RequestHandler):
    def post(self):
        result = createFile.createFile.mysql_to_file()
        if (bool(result)):
            print "success"
            self.write("SUCCESS")
        else:
            self.write("FAIL")

    def get(self):
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
