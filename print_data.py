import sys
import json
from prettytable import PrettyTable

SKIPPEND_FIELDS = ['labels', 'sample_uri', 'official', 'run_uri', 'product_name', 'owner']

x = PrettyTable()


with open(sys.argv[1]) as data_file:
    # make valid json
    wrap_data_file = '{"data": [%s]}' % ','.join(data_file)
    data = json.loads(wrap_data_file)

keys = []

for row in data['data']:

    row_values = []

    for key, value in row.items():

        if key in SKIPPEND_FIELDS:
            continue

        if key not in keys:
            keys.append(key)

        row_values.append(value)

    x.add_row(row_values)

x._set_field_names(keys)

print x
