#!/usr/bin/python3

import pycurl as curl
from io import BytesIO
from helpers.path import PathHelper


class CurlCPU:
    def __init__(self, link, tracking_id):
        self.link = link
        self.buffer = None
        self.http_code = None
        self.content_type = None
        self.content_length = None
        self.referer = "https://www.ultimate-guitar.com/"
        self.cookie = str(PathHelper().path + "/cookies/cookie_" + str(tracking_id) + ".txt")

    def access(self):
        buffer = BytesIO()
        c = curl.Curl()
        c.setopt(c.URL, self.link)
        c.setopt(c.USERAGENT, "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0")
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.FOLLOWLOCATION, True)
        c.setopt(c.HEADER, False)
        c.setopt(c.NOPROGRESS, True)
        c.setopt(c.REFERER, self.referer)
        c.setopt(c.SSL_VERIFYPEER, False)
        c.setopt(c.SSL_VERIFYHOST, False)
        c.setopt(c.CONNECTTIMEOUT, 30)
        c.setopt(c.COOKIEJAR, self.cookie)
        c.setopt(c.COOKIEFILE, self.cookie)
        c.perform()
        c.close()

        self.buffer = buffer.getvalue().decode('utf-8')

    def check_link(self):
        buffer = BytesIO()
        c = curl.Curl()
        c.setopt(c.URL, self.link)
        c.setopt(c.USERAGENT, "Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0")
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.FOLLOWLOCATION, True)
        c.setopt(c.HEADER, False)
        c.setopt(c.NOPROGRESS, True)
        c.setopt(c.REFERER, self.referer)
        c.setopt(c.SSL_VERIFYPEER, False)
        c.setopt(c.SSL_VERIFYHOST, False)
        c.setopt(c.CONNECTTIMEOUT, 30)
        c.setopt(c.COOKIEJAR, self.cookie)
        c.setopt(c.COOKIEFILE, self.cookie)
        c.perform()

        self.http_code = c.getinfo(c.HTTP_CODE)
        c.close()

    def read_image(self):
        self.check_link()

        buffer = BytesIO()
        c = curl.Curl()
        c.setopt(c.URL, self.link)
        c.setopt(c.USERAGENT, "Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0")
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.FOLLOWLOCATION, True)
        c.setopt(c.HEADER, False)
        c.setopt(c.NOPROGRESS, True)
        c.setopt(c.REFERER, self.referer)
        c.setopt(c.SSL_VERIFYPEER, False)
        c.setopt(c.SSL_VERIFYHOST, False)
        c.setopt(c.CONNECTTIMEOUT, 30)
        c.setopt(c.COOKIEJAR, self.cookie)
        c.setopt(c.COOKIEFILE, self.cookie)
        c.perform()

        self.buffer = buffer
        c.close()

    def download(self, save_as):
        self.check_link()

        if str(self.http_code) == "200":
            with open(save_as, "wb") as fp:
                c = curl.Curl()
                c.setopt(c.URL, self.link)
                c.setopt(c.USERAGENT, "Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0")
                c.setopt(c.WRITEDATA, fp)
                c.setopt(c.FOLLOWLOCATION, True)
                c.setopt(c.HEADER, False)
                c.setopt(c.NOPROGRESS, True)
                c.setopt(c.REFERER, self.referer)
                c.setopt(c.SSL_VERIFYPEER, False)
                c.setopt(c.SSL_VERIFYHOST, False)
                c.setopt(c.CONNECTTIMEOUT, 30)
                c.setopt(c.COOKIEJAR, self.cookie)
                c.setopt(c.COOKIEFILE, self.cookie)
                c.perform()
                c.close()
            print("Fisier salvat!")
        else:
            print("Eroare fisier!")

    def check_type(self):
        buffer = BytesIO()
        c = curl.Curl()
        c.setopt(c.URL, self.link)
        c.setopt(c.USERAGENT, "Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0")
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.FOLLOWLOCATION, True)
        c.setopt(c.HEADER, False)
        c.setopt(c.NOBODY, True)
        c.setopt(c.HEADERFUNCTION, buffer.write)
        c.setopt(c.NOPROGRESS, True)
        c.setopt(c.REFERER, self.referer)
        c.setopt(c.SSL_VERIFYPEER, False)
        c.setopt(c.SSL_VERIFYHOST, False)
        c.setopt(c.CONNECTTIMEOUT, 30)
        c.setopt(c.COOKIEJAR, self.cookie)
        c.setopt(c.COOKIEFILE, self.cookie)
        c.perform()

        # self.content_type = c.getinfo(c.CONTENT_TYPE)
        self.content_length = c.getinfo(c.CONTENT_LENGTH_DOWNLOAD)
        c.close()






