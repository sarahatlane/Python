def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    with open("users.txt", "a") as file:
        file.write(f"{username}:{password}\n")
    print("Registration successful!")