import sys
import json
from prettytable import PrettyTable

SKIPPEND_FIELDS = ['sample_uri', 'official', 'run_uri', 'product_name', 'owner', 'timestamp']

x = PrettyTable()


with open(sys.argv[1]) as data_file:
    # make valid json
    wrap_data_file = '{"data": [%s]}' % ','.join(data_file)
    data = json.loads(wrap_data_file)

keys = []

keys_order = ['cloud', 'test', 'metric', 'value', 'unit']

VALUE = {
    'cloud': None,
    'metric': None,
    'value': None,
    'test': None,
    'unit': None,
}

for row in data['data']:

    row_values = []

    for key, value in row.items():

        if key in SKIPPEND_FIELDS:
            continue

        if key == "labels":
            if 'cloud' not in keys:
                keys.append('cloud')

            values = value.split("|,|")
            for key in values:
                if 'cloud' in key:
                    VALUE['cloud'] = key.split(':')[1]
        else:

            if key not in keys:
                keys.append(key)

            VALUE[key] = value

    x.add_row(list([VALUE[key] for key in keys_order]))

x._set_field_names(keys_order)

print x

name = sys.argv[1].split(".")[0]

with open(name + ".txt", "w+") as new_file:

    new_file.write(str(x))
