for i in range(3):
    password = input("Please enter a password: ")
    password2 = input("Please re-enter your password: ")
    if password== password2:
        print(password)
        print("Welcome")
        break
    else:
        print("Incorrect password, please try again.")
        continue  
print()  

   
    