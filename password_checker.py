username = input("Enter your name: ").capitalize()
password = input("Enter your password: ")

password_len = len(password)

password_hidden = '*' * password_len


print(f"{username}, your password {password_hidden} is  {password_len} characters long.")
