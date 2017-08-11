import datetime
import os

import json

import tornado.httpserver
import tornado.ioloop
import tornado.web


def handle_get_for_browsertest(request):
    time_str = datetime.datetime.now().isoformat()
    msg = 'Hello, world! ...  TIME = {}'
    return msg.format(time_str)


def handle_post_for_webhook(request):
    report = 'headers=[{!r}]'.format(dict(request.headers))
    body = tornado.escape.json_decode(request.body)
    report += '  //  body=[{!r}]'.format(body)
    response = 'OK! // {!s} // DONE OK! '.format(report)
    response = tornado.escape.native_str(response)
    return response


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        response = handle_get_for_testpoke(self.request)
        self.write(response)

    def post(self):
        response = handle_post_for_webhook(self.request)
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
