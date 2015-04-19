from tornadorpc.json import JSONRPCHandler


def default_row():
    return \
        { 'sum': None
        , 'count': None
        , 'min': None
        , 'max': None
        }


class Battery(object):

    data = None
    float_precision = 3

    def __init__(self):
        self.data = dict()

    def charge(self, name, value):
        try:
            value = int(value)
        except ValueError:
            value = float(value)

        if name not in self.data:
            self.data[name] = default_row()
        self.data[name]['sum'] = (self.data[name]['sum'] or 0) + value
        self.data[name]['count'] = (self.data[name]['count'] or 0) + 1
        self.data[name]['min'] = value \
            if self.data[name]['min'] is None or value < self.data[name]['min'] \
            else self.data[name]['min']
        self.data[name]['max'] = value \
            if self.data[name]['max'] is None or value > self.data[name]['max'] \
            else self.data[name]['max']
        return True

    def discharge(self, name, value_type='avg'):
        assert value_type in ('avg', 'min', 'max', 'sum')
        data = self.data.get(name) or default_row()
        if value_type == 'avg' and data['count']:
            sum_val = data['sum'] or 0
            count = data['count'] or 0
            result = sum_val / float(count)
            result_precised = int(result * (10 ** self.float_precision)) / float(10 ** self.float_precision)
            data['sum'] = None
            data['count'] = None
            return result_precised or 0
        if value_type == 'sum':
            result = data['sum']
            data['sum'] = None
            data['count'] = None
            return result or 0
        result = data.get(value_type)
        if value_type != 'avg':
            data[value_type] = None
        return result or 0

    def get_data(self, name=None):
        if name:
            return self.data.get(name)
        return self.data


class JsonRpcBundleHandler(JSONRPCHandler):
    battery = Battery()