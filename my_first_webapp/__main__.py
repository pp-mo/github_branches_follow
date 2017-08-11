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
#        received_json = self.get_body_argument("message")
#        received_objects = json.loads(received_json)
#        len_json = len(received_json)
#        rx_type = type(received_objects)
##        len_objs = len(received_objects)
##        if rx_type == dict:
##            rx_names = received_objects.keys()
#        self.set_header("Content-Type", "text/plain")
#        msg = 'received: strlen={} rxtype={}'.format(
#            len_json, rx_type)
#        self.write(msg.format(time_str))
        self.write('OK!')


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
