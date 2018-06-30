from jinja2 import Environment, PackageLoader, select_autoescape
import os
import csv

env = Environment(
    loader=PackageLoader('noname', 'templates')
)


output_dir = os.path.join(os.path.dirname(__file__), "out")

if not os.path.isdir(output_dir):
    os.makedirs(output_dir)


### Example 1

hiring_managers_data = {
    "1": {
        'gender_m_true': 0,
        'gender_m_false': 0,
        'gender_f_true': 0,
        'gender_f_false': 0,
    },
    "2": {
        'gender_m_true': 0,
        'gender_m_false': 0,
        'gender_f_true': 0,
        'gender_f_false': 0,
    },
    "3": {
        'gender_m_true': 0,
        'gender_m_false': 0,
        'gender_f_true': 0,
        'gender_f_false': 0,
    },
    "4": {
        'gender_m_true': 0,
        'gender_m_false': 0,
        'gender_f_true': 0,
        'gender_f_false': 0,
    },
    "5": {
        'gender_m_true': 0,
        'gender_m_false': 0,
        'gender_f_true': 0,
        'gender_f_false': 0,
    },
}

with open('example1.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        if row[0] == "M":
            if row[2] == 'True':
                hiring_managers_data[row[1]]['gender_m_true'] += 1
            else:
                hiring_managers_data[row[1]]['gender_m_false'] += 1
        else:
            if row[2] == 'True':
                hiring_managers_data[row[1]]['gender_f_true'] += 1
            else:
                hiring_managers_data[row[1]]['gender_f_false'] += 1


with open(os.path.join(output_dir, "example1.html"), "w") as file:
    file.write(env.get_template('example1.html').render(hiring_managers_data=hiring_managers_data))

