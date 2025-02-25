import json


def login():
    print("\n----------------Login Page----------------\n")
    user = input("Username: ")
    password = input("Password: ")
    login_dict={}
    
    
    with open('login.txt') as file:
        user_data = file.read()
        
    user_data_list = user_data.split("|")
    
    for i in user_data_list:
        user_dict = json.loads(i)
        login_dict.update(user_dict)
    if user not in user_dict:
        print(f"{user} doesnt have an account")
        signup=input("Please Sign up first. Do you want to register or login again?(register/login): ").lower()
        if signup == "register":
            registration()
        elif signup == "login":
            login()
        
    else:       
        if password == user_dict[user]:
            print("Login SuccessFull!")
        else:
            print("Password incorrect!")
            login()

def registration():
    print("\n--------------Registration Page--------------\n")
    user = input("Username: ")
    password = input("Password: ")
    button = input("Type register or cancel: ")
    if button == 'cancel':
        return
    elif button == 'register':
        user_dict = {user:password}
        
        
        try:
        # opeing in a reading mode for just adding comma later if there is no content then we don't need to add comma
            with open("login.txt", "r") as f:
                existing_data = f.read()
                # data cha vane split into list
                if existing_data:
                    existing_data_list = existing_data.split("|")
                #empty cha vane list initialize gairakhne so that append part ma comma wala handle garxa as 0>0 false so no comma will be added
                else:
                    existing_data_list = []
    #file vetena vane error ma janxa ani initialize garera ani tala append part ma new file create garxa ani initailization compare garxa           
        except FileNotFoundError:
            # print("File not found. Creating new file ")
            existing_data_list = []

        with open("login.txt", "a") as f:
            user_data_json = json.dumps(user_dict) #transform a dictionary into a string format that can be easily written to a file.
            if len(existing_data_list) > 0:
                f.write("|")  # Append comma only if the file has data
            f.write(user_data_json)
            
            
            print("Registration successfull!")
        log =  input("Do you want to login now?(y/n): ").lower()
        if log == 'y':
            login() 

login_choice = input("Do you want to login or register?(login/register): ").lower()
if login_choice == "login":
    login()
elif login_choice == "register":
    registration()
    
else:
    print("You can only login or register in this page!")