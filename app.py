# coding=utf-8
__author__ = 'JIE'

import tornado.ioloop
import tornado.web
import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
from routes import file
from routes import upload
from routes import setting

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "public"),
    "template_path": os.path.join(os.path.dirname(__file__), "views"),
    "gzip": True,
    "debug": True,
}

application = tornado.web.Application([
    ("/", tornado.web.RedirectHandler, {"url": "/static/index.html"}),
    ("/file", file.file),
    ("/upload", upload.UploadHander),
    ("/setting", setting.Setting)
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    print 'Server start in port : 8888'
    tornado.ioloop.IOLoop.current().start()
