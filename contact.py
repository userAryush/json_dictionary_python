# 2. Contact Book
# Store contacts in a dictionary ({"name": {"phone": "...", "email": "..."}}).
# Save the dictionary to a file (JSON format).
# Allow users to add, search, update, and delete contacts.
# maya manbhari

import json

def add():
    name = input("Enter your name: ").capitalize()
    phone = input("Enter your phone number: ")
    email = input("Enter your email address: ")
    
    user_dict = {name:{"phone":phone, "email":email}}
    
    try:
        # opeing in a reading mode for just adding comma later if there is no content then we don't need to add comma
       with open("contact.txt", "r") as f:
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
    
    with open('contact.txt', 'a') as file:
        information_json = json.dumps(user_dict)
        if len(existing_data_list) > 0:
            file.write("|")  # Append comma only if the file has data
        file.write(information_json)
        
    print("Contact added successfully!")
        
    

def search():
    information = json_to_dictionary()   
        
    name = input("Enter the name of the contact you want to search: ").capitalize()
    if name not in information:
        print(f"No contact found named {name}")
    else:
        phone = information[name]['phone']
        email = information[name]['email']
        print(f"{name}'s contact:\nNumber = {phone}\nEmail = {email}")

def update():
    information = json_to_dictionary()
    name = input("Enter the name of the contact you want to update: ").capitalize()
    if name not in information:
        print(f"No contact found named{name}")
        
    else:
        phone = input("Enter your phone number: ")
        email = input("Enter your email address: ")  
        information[name]['phone']= phone
        information[name]['email'] = email
        
        with open('contact.txt', 'w') as file:
            information_json = json.dumps(information)
            
            file.write(f"{information_json}|")
            
        print(f"{name}'s Contact updated successfully!")
    

def delete():
    information = json_to_dictionary() 
    name = input("Enter the name of contact you want to delete: ").capitalize()
    if name not in information:
        print(f"No contact found named {name}")
    else:
        information.pop(name)
        
        with open('contact.txt', 'w') as file:
            information_json = json.dumps(information)
            
            file.write(f"{information_json}|")
            
        print(f"{name}'s Contact deleted successfully!")
    

def json_to_dictionary():
    information = {}
    with open('contact.txt', 'r') as file:
        user_data = file.read()
    
    user_data_list = user_data.split("|")
    
    for i in user_data_list:
        if i: #value cha ki nai checking to avoid empty i
            try:
                info_dict = json.loads(i)
                information.update(info_dict)
            except json.JSONDecodeError:
                continue    
    return information
    
    
while True:  
    print("\n-------------------Contanct Book-------------------\n")
    print("Menu")
    print("\n1. Add \n2. Search \n3. Update \n4. Delete")
    choice = input("\nEnter you choice(1/2/3/4/exit): ")


        

    if choice == "exit":
        break

    elif choice == '1':
        add()

    elif choice == '2':
        search()

    elif choice == '3':
        update()

    elif choice == '4':
        delete()
    else:
        print("Enter a valid input(1/2/3/4/exit)")