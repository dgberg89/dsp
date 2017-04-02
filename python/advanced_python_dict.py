#Q6

import csv
from collections import defaultdict
from itertools import islice

with open('faculty.csv', mode = 'r') as file:
    next(file, None)
    csvreader = csv.reader(file)
    
    keys = []
    values = []
    
    for row in csvreader:
        key = row[0].rsplit(None, 1)[-1]
        value = row[1:]
        keys.append(key)
        values.append(value)
    #print(keys)
    #print(values)
    
    faculty_list = list(zip(keys, values))
    #print(faculty_list)
         
    faculty_dict = defaultdict(list)
    for k, v in faculty_list:
        faculty_dict[k].append(v)
    #for k, v in faculty_dict.items():
        #print(k, v)
        
    top3 = dict(itertools.islice(faculty_dict.items(), 3))
    print(top3)
    
    
#Q7
    
import csv
from collections import defaultdict
from itertools import islice

with open('faculty.csv', mode = 'r') as file:
    next(file, None)
    csvreader = csv.reader(file)
    
    keys = []
    values = []
    
    for row in csvreader:
        #print(row)
        a = row[0].split()[0] + ' ' + row[0].split()[-1]
        key = str(a.split(' '))
        value = str(row[1:])
        keys.append(key)
        values.append(value)
    #print(keys)
    #print(values)
    
    faculty_list = list(zip(keys, values))
    #print(faculty_list)
         
    faculty_dict = defaultdict(list)
    for k, v in faculty_list:
        faculty_dict[k].append(v)
    #print(faculty_dict)
    #for k, v in faculty_dict.items():
        #print(k, v)
        
    top3 = dict(itertools.islice(faculty_dict.items(), 3))
    print(top3)

    
#Q8

import csv
from collections import defaultdict
from itertools import islice

with open('faculty.csv', mode = 'r') as file:
    next(file, None)
    csvreader = csv.reader(file)
    
    keys = []
    values = []
    
    for row in csvreader:
        #print(row)
        a = row[0].split()[0] + ' ' + row[0].split()[-1]
        key = str(a.split(' '))
        value = str(row[1:])
        keys.append(key)
        values.append(value)
    #print(keys)
    #print(values)
    
    faculty_list = list(zip(keys, values))
    #print(faculty_list)
         
    faculty_dict = defaultdict(list)
    for k, v in faculty_list:
        faculty_dict[k].append(v)
    #print(faculty_dict)
    for k, v in sorted(faculty_dict.items()):
        print("{}: {}".format(k, v))
