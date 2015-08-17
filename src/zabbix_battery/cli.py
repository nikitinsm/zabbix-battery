import json
import urllib2
import argparse


command_line_parser = argparse.ArgumentParser\
    ( description='Make JSON-RPC call to server'
    )
command_line_parser.add_argument\
    ( '--extract'
    , type=str
    , nargs='?'
    , help='JSON-RPC extract single value (simple path)'
    )
command_line_parser.add_argument\
    ( '--coerce'
    , choices=['int', 'float']
    , nargs='?'
    , help='JSON-RPC coerce result value to python type example: (int, float, str and etc)'
    )
command_line_parser.add_argument\
    ( '--host'
    , type=str
    , nargs='?'
    , help='server host'
    )
command_line_parser.add_argument\
    ( '--port'
    , type=int
    , nargs='?'
    , help='server port'
    )
command_line_parser.add_argument\
    ( 'method'
    , type=str
    , help='JSON-RPC method name'
    )
command_line_parser.add_argument\
    ( 'params'
    , type=str
    , nargs='*'
    , help='JSON-RPC method position args'
    )


CORCE_MAP = \
    { 'int': int
    , 'float': float
    }


def json_rpc_call(method, host=None, port=None, params=None):
    host = host or 'localhost'
    port = port or 80

    url = 'http://%s:%d/json-rpc/' % (host, port)
    
    json_request =\
        { "id": "1"
        , "jsonrpc": "2.0"
        , "method": method
        , "params": params or []
        }

    headers = \
        { "Content-Type": "application/json"
        }

    return json.loads(urllib2.urlopen(urllib2.Request(url, json.dumps(json_request), headers)).read())


def get(data, path, default=None):
    path = path.split('.')
    result = data
    for key in path:
        try:
            result = result[key]
        except KeyError:
            return default
    return result

def main():
    args = command_line_parser.parse_args()
    result = json_rpc_call\
        ( args.method
        , host=args.host
        , port=args.port
        , params=args.params
        )

    if args.extract:
        result = get(result, args.extract)
        if args.coerce:
            result = CORCE_MAP[args.coerce](result)

    return result


if __name__ == '__main__':
    print main()
