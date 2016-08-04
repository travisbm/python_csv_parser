import user
import csv

def build_user_array(file_name):
    users = []

    with open(file_name) as csvfile:
        user_list = csv.reader(csvfile)
        for row in user_list:
            users.append(user.User(row[0], row[1], row[2]))
    return users
