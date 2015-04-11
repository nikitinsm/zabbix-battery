import tornado.ioloop
import tornado.web

from zabbix_battery.handlers import JsonRpcBundleHandler


application = tornado.web.Application\
    ( [ (r"/json-rpc/", JsonRpcBundleHandler)
      ,
      ]
    , debug=True
    )
application.listen(8888)
tornado.ioloop.IOLoop.instance().start()