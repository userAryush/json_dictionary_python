import json

def register():
    print("\n--------------Registration Page--------------\n")
    user = input("Username: ")
    password = input("Password: ")
    button = input("Type register or cancel: ").lower()
    if button == 'cancel':
        return
    elif button == 'register':
        
    
        user_details_dictionary = user_json_to_dict()
        
        if user in user_details_dictionary:
            print("User already Exists. Try another Username! ")
            register()
            
        else:
            user_dict = {user:password}
            try:
                with open("librarylogin.txt","r") as file:
                    existing_data = file.read()
                    
                if existing_data:
                    existing_data_list = existing_data.split("|")
                else:
                    existing_data_list = []
            except FileNotFoundError:
                existing_data_list = []
                
                
            with open("librarylogin.txt","a") as file:
                user_json = json.dumps(user_dict)
                if len(existing_data_list)>0:
                    file.write("|")
                file.write(user_json)
            print("Registration successfull!")
            
            log = input("Do you want to login now? (y/n): ")
            if log =='y':
                login()
            

def login():
    
    print("\n--------------Login Page--------------\n")
    user = input("Username: ")
    password = input("Password: ")
    button = input("Type login or cancel: ").lower()
    if button == 'cancel':
        return
    elif button == 'login':
        user_detail_dictionary = user_json_to_dict()
        
        if user not in user_detail_dictionary:
            reg = input(f"{user} is not registered yet!\nDo you want to register/login again?(register/login): ")
            if reg == "register":
                register()
            else:
                login()
                
        else:
            
            if password != user_detail_dictionary[user]:
                print("Incorrect password! Login again.")
                login()
            else:
                print("Login successfull!")
                return 1, user
                
            
def user_json_to_dict():
    user_details = {}
    
    with open('librarylogin.txt') as file:
        user_data = file.read()
        
    user_data_list = user_data.split("|")
    
    for i in user_data_list:
        if i:
            try:
                user_data_dict = json.loads(i)
                user_details.update(user_data_dict)
            except json.JSONDecodeError:
                continue
    
    return user_details

def add_book():
    pass

def borrow_book():
    pass

def view_books():
    pass

def main():
    print("--Library--")
    user_log = input("Login/Register: ").lower()
    if user_log == "login":
        status, user = login()
    elif user_log == "register":
        register()
    
    
    if status == 1:
        print("")
main() 