import tornado.ioloop
import tornado.web

from handlers import JsonRpcBundleHandler


if __name__ == '__main__':
    application = tornado.web.Application\
        ( [ (r"/json-rpc/", JsonRpcBundleHandler)
          ,
          ]
        #, debug=True
        )
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()