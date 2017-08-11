import datetime
import os

import tornado.httpserver
import tornado.ioloop
import tornado.web


get_count = 0

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        msg = 'Hello, world ({}) : #{}'
        get_count += 1
        time_str = datetime.datetime.now().isoformat()
        msg = 'Hello, world ({}) : #{}'
        self.write(msg.format(time_str, get_count))


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
