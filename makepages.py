import matplotlib.pyplot as plt; plt.rcdefaults()
from jinja2 import Environment, PackageLoader, select_autoescape
import os
import csv
import matplotlib as plt
import numpy as np
import pandas as pd

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
    plt.pyplot.title('Coffee Shops')
    plt.pyplot.savefig('out/Report.png', dpi=100)


def create_graph2(data):
    managers = list(data.keys())
    managers_data = list(data.values())
    data_out = []
    age_range = ['18-24', '25-35', '45-60']
    male_female= ['male','female']
    i=1
    for entry in managers_data:
        data1 = entry['18-24']
        data2 = entry['25-35']
        data3 = entry['45-60']
        
        hired_male=(data1['gender_m_true'] / (data1['gender_m_true'] + data1['gender_m_false']) * 100)
        hired_female=(data1['gender_f_true'] / (data1['gender_f_true'] + data1['gender_f_false']) * 100)
        
        hired_male2=(data3['gender_m_true'] / (data3['gender_m_true'] + data3['gender_m_false']) * 100)
        hired_female2=(data3['gender_f_true'] / (data3['gender_f_true'] + data3['gender_f_false']) * 100)
        
        hired_male3=(data2['gender_m_true'] / (data2['gender_m_true'] + data2['gender_m_false']) * 100)
        hired_female3=(data2['gender_f_true'] / (data2['gender_f_true'] + data2['gender_f_false']) * 100)
        
        data_out = [[hired_male, hired_female], [hired_male2, hired_female2], [hired_male3, hired_female3]]
    
        data_dict = dict(zip(age_range, data_out))

        df=pd.DataFrame(data=data_dict, index=male_female,columns=age_range)
        fig0, ax0 = plt.pyplot.subplots()
        ax1 = ax0.twinx()
        ax1.set_yticklabels([])
        df.plot(kind='bar', ax=ax1)
        plt.pyplot.ylabel('Hiring Success')
        plt.pyplot.ylabel('Hiring Success')
        title="Manager "+str(i)
        plt.pyplot.title(title)
        i+=1
        plt.pyplot.savefig("out/Report"+str(i)+".png", dpi=100)


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


### Example 3

hiring_managers_data3 = {}

for i in range(1,6):
    hiring_managers_data3[str(i)] = {}
    for j in ["18-24", "25-35", "45-60"]:
        hiring_managers_data3[str(i)][j] = {
        'gender_m_true': 0,
        'gender_m_false': 0,
        'gender_f_true': 0,
        'gender_f_false': 0,
    }


with open('example3.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        age = 2018 - int(row[1])
        if age < 25:
            age_range = "18-24"
        elif age < 45:
            age_range = "25-35"
        else:
            age_range = "45-60"
        if row[0] == "M":
            if row[3] == 'True':
                hiring_managers_data3[row[2]][age_range]['gender_m_true'] += 1
            else:
                hiring_managers_data3[row[2]][age_range]['gender_m_false'] += 1
        else:
            if row[3] == 'True':
                hiring_managers_data3[row[2]][age_range]['gender_f_true'] += 1
            else:
                hiring_managers_data3[row[2]][age_range]['gender_f_false'] += 1

create_graph2(hiring_managers_data3)

with open(os.path.join(output_dir, "example3.html"), "w") as file:
    file.write(env.get_template('example3.html').render(hiring_managers_data=hiring_managers_data3))

