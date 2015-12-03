# coding=utf-8
__author__ = 'JIE'
# http://www.oschina.net/code/snippet_89296_9122

import os
import zipfile
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def zip_dir(dirname, zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else:
        for root, dirs, files in os.walk(dirname):
            for name in files:
                if name != ".gitignore":
                    filelist.append(os.path.join(root, name))
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        zf.write(tar, arcname)
    zf.close()


def extract_to(file, path):
    print "extract file"
    zfile = zipfile.ZipFile(file, 'r')
    for p in zfile.namelist():
        __extract(p, path, zfile)


def __extract(filename, path, zfile):
    if not filename.endswith('/'):
        f = os.path.join(path, filename).decode('gbk')
        dir = os.path.dirname(f)
        if not os.path.exists(dir):
            os.makedirs(dir)
        file(f, 'wb').write(zfile.read(filename))
