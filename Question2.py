import csv
from operator import itemgetter

header = ['id', 'first-name', 'email', 'avatar','gender', 'Dob','address']
list = []

with open('users.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    for line in csv_reader:
        list.append(line)

newlist = sorted(list, key=itemgetter(1))

with open('users-sorted.csv', 'a', newline='') as users_sorted:
    csv_writer = csv.DictWriter(users_sorted, fieldnames=header)
    csv_writer.writeheader()

    for line in newlist:
        list.append(line)
        dict = {'id' : line[0], 'first-name':line[1], 'email': line[2], 'avatar':line[3],'gender':line[4], 'Dob':line[5],'address':line[6]}
        csv_writer.writerow(dict)
