import getpass  


users = {'john': 'password123', 'jane': 'password456', 'bob': 'password789'}  

username = input('Enter username: ')  
password = getpass.getpass('Enter password: ')  

if username in users and users[username] == password:  
    print('Access granted')  
else:  
    print('Access denied')  