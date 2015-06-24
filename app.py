# coding=utf-8
__author__ = 'JIE'

import tornado.ioloop
import tornado.web
import os

from routes import file

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "public"),
    "template_path": os.path.join(os.path.dirname(__file__), "views"),
    "gzip": True,
    "debug": True,
}

application = tornado.web.Application([
    ("/", tornado.web.RedirectHandler, {"url": "/static/index.html"}),
    ("/file",file.file),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    print 'server start'
    tornado.ioloop.IOLoop.current().start()
