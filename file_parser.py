import parser

f = raw_input("Input CSV file name: ")

array = parser.build_user_array(f)

for user in array:
    user.print_user()
