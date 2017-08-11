import datetime
import os

import tornado.httpserver
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def __init__(self, *args, **kwargs):
        super(self, MainHandler).__init__(*args, **kwargs)
        self.get_count = 0

    def get(self):
        msg = 'Hello, world ({}) : #{}'
        self.get_count += 1
        time_str = datetime.datetime.now().isoformat()
        msg = 'Hello, world ({}) : #{}'
        self.write(msg.format(time_str, self.get_count))


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
