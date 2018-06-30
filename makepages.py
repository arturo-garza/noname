import matplotlib.pyplot as plt; plt.rcdefaults()
from jinja2 import Environment, PackageLoader, select_autoescape
import os
import csv
import matplotlib as plt
import pandas as pd
import numpy as np

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

def create_graph(data):
    hiring_managers = data.keys()
    final_topics = []
    final_numbers = []
    for manager in hiring_managers:
        statistic = data[manager]

        hired_male=(statistic['gender_m_true'] / (statistic['gender_m_true'] + statistic['gender_m_false']) * 100)
        hired_female=(statistic['gender_f_true'] / (statistic['gender_f_true'] + statistic['gender_f_false']) * 100)
        final_numbers+=[hired_male,hired_female]
        final_topics+=[hired_male,hired_female]

    #print(final_numbers)
    #print(final_topics)
    y_pos = np.arange(len(final_numbers))

    bars=plt.pyplot.bar(y_pos, final_numbers, align='center', alpha=0.5)

    for num in range(0, len(final_numbers)):

        if num%2==0:
            bars[num].set_color('xkcd:blue')
        else:
            bars[num].set_color('xkcd:pink')
    labels =[]
    for manager in hiring_managers:
        labels.append("Manager")
        labels.append(manager)
    plt.pyplot.xticks(y_pos, labels)
    plt.pyplot.ylabel('Hiring Success')
    plt.pyplot.title('Coffee Shops in Belfast')
    plt.pyplot.savefig('out/Report.png', dpi=100)




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

create_graph(hiring_managers_data)

with open(os.path.join(output_dir, "example1.html"), "w") as file:
    file.write(env.get_template('example1.html').render(hiring_managers_data=hiring_managers_data))



### Example 2

with open(os.path.join(output_dir, "example2.html"), "w") as file:
    file.write(env.get_template('example2.html').render(hiring_managers_data=hiring_managers_data))
