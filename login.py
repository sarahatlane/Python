#function
from certifi import contents


def read_logins():
    with open('login.txt', 'r') as f:
        new_contents = f.readlines()

        # print(contents)
        new_contents = []
        
        for line in contents:
            fields = line.split(',')
            fields [1] = fields[1].rstrip()
            new_contents.append(fields)

            # return new_contents
            return new_contents
        
logins = read_logins()

#function 
def login():
    ask_username = str(input('Username'))
    ask_password = str(input('Password'))

    logged_in = False

for line in logins:
    if line[0] == ask_password and logged_in == False:
        if line[1] == ask_password:
            logged_in = True


            if logged_in == True:
                print('Logged in sucessfuly')
            else:
                print('Username / Password is incorrect')


login()



#--------------------------------------------------------------------------------------------

#str stands for "string." It's a data type used to represent text as a sequence of characters
#def is a keyword used to define functions)