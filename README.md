Install
-------

_$ pip install -U git+https://github.com/nikitinsm/zabbix-battery.git_

Run
---
_$ python -m zabbix_battery.server_

CLI
---

_$ python -m zabbix_battery.cli -h_

    usage: cli.py [-h] [--extract [EXTRACT]] method [params [params ...]]
    
    Make JSON-RPC call to server
    
    positional arguments:
      method               JSON-RPC method name
      params               JSON-RPC method position args
    
    optional arguments:
      -h, --help           show this help message and exit
      --extract [EXTRACT]  JSON-RPC extract single value (simple path)


CLI examples
------------

_$ python -m zabbix_battery.cli battery.charge name 1_
    
    { 
      u'jsonrpc': u'2.0', 
      u'result': True, 
      u'id': u'1' 
    }
    
_$ python -m zabbix_battery.cli battery.discharge name_
    
    { 
      u'jsonrpc': u'2.0',
      u'result': 1.0, 
      u'id': u'1'
    }
    
_$ python -m zabbix_battery.cli battery.discharge name --extract=result_
    
    1.0 // equal to operation {'result': 1.0}.get('result')
    
Docker
------

_build_
    
    docker build -t zabbix-battery . 
    
_run_
    
    docker run --name -d zabbix-battery -it -p 8000:80 zabbix-battery
    