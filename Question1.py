import requests
import csv
import schedule

response = requests.get("https://random-data-api.com/api/v2/users?size=1&response_type=json")
myjson = response.json()
dict = {'id' : myjson['id'], 'first-name':myjson['first_name'], 'email': myjson['email'], 'avatar':myjson['avatar'],'gender':myjson['gender'], 'Dob':myjson['date_of_birth'],'address':myjson['address']['street_name'] + myjson['date_of_birth'] + myjson['address']['street_address']}

with open('users.csv', 'a', newline='') as users:
    csv_writer = csv.DictWriter(users, fieldnames = dict)
    csv_writer.writeheader()


def func():
    response = requests.get("https://random-data-api.com/api/v2/users?size=1&response_type=json")
    myjson = response.json()
    dict = {'id' : myjson['id'], 'first-name':myjson['first_name'], 'email': myjson['email'], 'avatar':myjson['avatar'],'gender':myjson['gender'], 'Dob':myjson['date_of_birth'],'address':myjson['address']['street_name'] + myjson['date_of_birth'] + myjson['address']['street_address']}
    
    with open('users.csv', 'a', newline='') as users:
        csv_writer = csv.DictWriter(users, fieldnames = dict)
        csv_writer.writerow(dict)

schedule.every(1).seconds.do(func)


while True:
    schedule.run_pending()


