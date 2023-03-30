"""
Shreyaas Sureshbabu
Assignment 9
Problem 1
"""
import datetime
#part 1
def valid_username(username): #checks if username fits given parameters based on ASCII values and if the first character is a letter or not
    i = 0
    if len(username) >= 5:
        if username.isalnum():
            if (ord(username[i]) >= 65 and ord(username[i]) <= 90) or (ord(username[i]) >= 97 and ord(username[i]) <= 122):
                return True #returns true if all parameters fit 
            else:
                return False #returns false if not
        else:
            return False
    else: return False

def uppercase_check(password): #helper function to count the number of uppercase letters in password: there must be at least one
    length = len(password)
    count = 0
    for i in range(0, length):
        passw = ord(password[i])
        if passw >= 65 and passw <= 90:
            count += 1
        else:
            continue
    return count    

def lowercase_check(password): #helper function to count the number of lowercase letters in password: there must be at least one
    length = len(password)
    count = 0
    for i in range(0, length):
        passw = ord(password[i])
        if passw >= 97 and passw <= 122:
            count += 1
        else:
            continue
    return count 

def digits_check(password): #helper function to count the number of digits in password: there must be at least one
    length = len(password)
    total = 0
    for i in range(0, length):
        if password[i].isnumeric() == True:
            total += 1
        else:
            continue
    return total

def valid_password(password): #checks to see if password fits parameters (checked by the helper functions)
    x = uppercase_check(password)
    y = lowercase_check(password)
    z = digits_check(password)
    if len(password) >= 5:
        if password.isalnum():
            if x >= 1:
                if y >= 1:
                    if z >= 1:
                        return True #returns true if password fits parameters
                    else:
                        return False #returns false if otherwise
                else:
                    return False
            else: 
                return False
        else:
            return False
    else:
        return False

#part b
def username_exists(username): #checks to see if username exists in the user_info.txt file
    user_file = open("user_info.txt", "r")
    user_data = user_file.read()
    user_data = user_data.split("\n")
    userdata_list = []
    for i in range(len(user_data)):
        userdata = user_data[i].split(",")
        userdata_list += userdata
    userdata_list = userdata_list[::2] #after list is split up, halves list so that only usernames are in the list
    for i in range(0, len(userdata_list)): #checks to see if user input is in the list
        if username in userdata_list:
            return True
        else:
            return False

def username_indice(username): #finds the index where the existing username is (if it doesn't exist, returns None)
    user_file = open("user_info.txt", "r")
    user_data = user_file.read()
    user_data = user_data.split("\n")
    userdata_list = []
    for i in range(len(user_data)):
        userdata = user_data[i].split(",")
        userdata_list += userdata
    userdata_list = userdata_list[::2]
    try:
        d = userdata_list.index(username)
        return d
    except:
        return None

def check_password(username, password): #makes sure that the password matches the given username by seeing if it's next to the given username in the list of info
    user_file = open("user_info.txt", "r")
    user_data = user_file.read()
    user_data = user_data.split("\n")
    userdata_list = []
    for i in range(len(user_data)):
        userdata = user_data[i].split(",")
        userdata_list += userdata
    x = username_exists(username)
    if x == True:
        try:
            if password in userdata_list[username_indice(username) * 2 + 1]:
                return True
            else:
                return False
        except:
            return False
    else:
        return False

#part 1c
def add_user(username, password): #adds a user by making sure inputted username isn't duplicate, then appends the info to the user_info.txt file
    if username_exists(username) == True:
        return False
    else:
        user_file = open("user_info.txt", "a")
        if valid_username(username) == True and valid_password(password) == True:
            user_file.write(username + "," + password + "\n") 
            user_file.close()
            return True
        else:
            return False

#part 1d
d = datetime.datetime.now()
month = d.month
day = d.day
year = d.year
hour = d.hour
minute = d.minute
second = d.second
time_day = str(hour) + ":" + str(minute) + ":" + str(second)
time_info = str(month) + "/" + str(day) + "/" + str(year) + " " + time_day

def send_message(sender, recipient, message): #sends a message by making a custom file (if it doesn't previously exist) and adding it in the correct format
    directory = "messages\\"
    filepath = directory + recipient + ".txt"
    ms = open(filepath, 'a') 	
    msg = str(sender) + "|" + str(time_info) + "|" + str(message) 
    ms.write(msg)
    ms.write("\n")

#part 1e
def print_messages(username): #prints all messages in a given messages .txt file
    directory = "messages\\"
    filepath = directory + username + ".txt"
    user_file = open(filepath, "r")
    user_msg = user_file.read()
    user_messages = user_msg.replace("\n", "|")
    user_messages = user_messages.split("|")
    user_messages.remove("")
    i = 0
    count = 1
    try:
        while i <= len(user_messages):
            print("Message #" + str(count) + " received from " + user_messages[i])
            print("Time: " + user_messages[i + 1])
            print(user_messages[i + 2])
            i += 3
            count += 1
            if i == len(user_messages):
                break
    except:
        print("There are no messages.")

def delete_messages(username): #deletes all messages by opening the file in "w" mode and writing nothing
    directory = "messages\\"
    filepath = directory + username + ".txt"
    user_file = open(filepath, "w")
    user_file.write("")

#part 1f
def menu(): #asks user to input l, r, or q
    user_input = input("(l)ogin, (r)egister or (q)uit: ")
    return user_input

def main(): #main function to run the program
    user_input = menu()
    if user_input == "r": #if user presses "r": registers user for an account based on their inputted username and password; if username isn't duplicate and both are valid, registers user
        print("Register for an account")
        username = input("Username (case sensitive): ")
        password = input("Password (case sensitive): ")
        if valid_username(username) == True:
            if username_exists(username) == False:
                if valid_password(password) == True: 
                    add_user(username, password)
                    print("Registration successful!")
                    send_message("admin", username, "Welcome to your account!") #makes an admin message every time an account is created
                    main()
                else:
                    print("Password is invalid, registration cancelled")
                    main()
            else:
                print("Duplicate username, registration cancelled")
                main()
        else:
            print("Username is invalid, registration cancelled")
            main()
    elif user_input == "l": #if user logs in, makes sure username and password are linked;
        print("Log In")
        username = input("Username (case sensitive): ")
        password = input("Password (case sensitive): ")
        if username_exists(username) == True:
            if check_password(username, password) == True:
                validcheck = False
                while not validcheck:
                    print("You have been logged in as " + username)
                    user_input_two = input("(r)ead messages, (s)end a message, (d)elete messages or (l)ogout: ") #user's options when they log in
                    if user_input_two == "r": #if user wants to read messages, prints the messages
                        print_messages(username)
                    elif user_input_two == "s": #if user wants to send a message, gets the sender and message the user wants to send, then adds it to respective text file
                        recipient = input("Username of recipient: ")
                        message = input("Type your message: ")
                        send_message(username, recipient, message)
                        print("Message sent!")
                    elif user_input_two == "d": #deletes all messages in users' text file
                        delete_messages(username)
                        print("Messages deleted.")
                    elif user_input_two == "l": #logs the user out and goes back to the l, r, or q menu
                        validcheck = True
                        print("Logging out as user " + username)
                        main()
            else: 
                print("Login invalid, try again")
                main()
        else:
            print("Login invalid, try again")
            main()
    elif user_input == "q": #if user quits, ends program 
        print()
        print("Goodbye!")

main()



    




