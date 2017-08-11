import datetime
import os

import json

import tornado.httpserver
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        time_str = datetime.datetime.now().isoformat()
        msg = 'Hello, world! ...  TIME = {}'
        self.write(msg.format(time_str))

    def post(self):
        report = 'headers=[{!r}]'.format(dict(self.request.headers))
        body = tornado.escape.json_decode(self.request.body)
        report += '  //  body=[{!r}]'.format(body)
        response = 'OK! // {!s} // DONE OK! '.format(report)
        response = tornado.escape.native_str(response)
        self.write(response)


def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    PORT = os.environ.get('PORT', 8080)
    http_server.listen(PORT)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
