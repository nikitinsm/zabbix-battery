import json
import urllib2
import argparse


command_line_parser = argparse.ArgumentParser\
    ( description='Make JSON-RPC call to server'
    )
command_line_parser.add_argument\
    ( 'method'
    , type=str
    , help='JSON-RPC method name'
    )
command_line_parser.add_argument\
    ( '--extract'
    , type=str
    , nargs='?'
    , help='JSON-RPC extract single value (simple path)'
    )
command_line_parser.add_argument\
    ( 'params'
    , type=str
    , nargs='*'
    , help='JSON-RPC method position args'
    )



def json_rpc_call(method, host='localhost', port='8888', params=None):
    url = 'http://%s:%s/json-rpc/' % (host, port)
    
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
    result = json_rpc_call(args.method, params=args.params)

    if args.extract:
        result = get(result, args.extract)

    return result


if __name__ == '__main__':
    print main()
