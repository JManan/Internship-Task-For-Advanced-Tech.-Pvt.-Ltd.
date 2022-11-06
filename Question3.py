import csv

def UserDeatils(id):

    with open('users.csv', 'r') as csv_reader:
        csv_reader = csv.reader(csv_reader)
        next(csv_reader)

        for line in csv_reader:
            if id == line[0]:
                return line
        
        return f"User doesnt exist"

print("Enter the Id of a user: ")
id = input()
print(UserDeatils(id))
