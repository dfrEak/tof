import json
import sys

class packet:
    # local file
    sys.path.append('../')
    from string_table import str_parser

    def encoding_package(ip,xshut,range):
        # a Python object (dict):
        data_dict = {
            str_parser.IP : ip,
            str_parser.XSHUT : xshut,
            str_parser.RANGE : range
        }
        # convert into JSON and return it
        return json.dumps(data_dict)

    def decoding_package(byte):
        return json.loads(byte.decode("utf-8"))