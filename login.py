#function
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
            print(new_contents)

#function 
def login():
    ask_username = str(input('Username'))
    ask_password = str(input('Password'))

login()



#--------------------------------------------------------------------------------------------

#str stands for "string." It's a data type used to represent text as a sequence of characters
#def is a keyword used to define functions)