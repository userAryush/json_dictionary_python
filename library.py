import json

def register():
    print("\n--------------Registration Page--------------\n")
    user = input("Username: ")
    password = input("Password: ")
    button = input("Type submit or cancel: ").lower()
    if button == 'cancel':
        return
    elif button == 'submit':
        
    
        user_details_dictionary = user_json_to_dict('librarylogin.txt')
        
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
    user = input("Admin: ")
    password = input("Password: ")
    button = input("Type sumbit or cancel: ").lower()
    if button == 'cancel':
        return
    elif button == 'submit':
        user_detail_dictionary= user_json_to_dict('librarylogin.txt')
        
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
                
            
def user_json_to_dict(filename):
    user_information = {}
    with open(filename, 'r') as file:
        user_data = file.read()
    
    user_data_list = user_data.split("|")
    
    for i in user_data_list:
        if i: #value cha ki nai checking to avoid empty i
            try:
                info_dict = json.loads(i)
                user_information.update(info_dict)
            except json.JSONDecodeError:
                continue 
    
    return user_information


def add_book():
    book_name = input('Book name: ')
    author = input('Author name: ')
    book_count = int(input('Book quantity: '))
    filename = 'books.txt'
    
    book_dict = {book_name:{"author":author,"quantity":book_count}}
    
    
    with open(filename) as file:
        data = file.read()
    try:
        if data:
            existing_books_list = data.split("|")
        else:
            existing_books_list = []
            
    except FileNotFoundError:
        existing_books_list = []
    
    with open(filename, 'a') as file:
        books_json = json.dumps(book_dict)
        if len(existing_books_list)>0:
            file.write('|')
        file.write(books_json)
        print("Successfully added in the library!")
        

def borrow_book():
    books_dict = user_json_to_dict('books.txt')
    
    if not books_dict:
        print("No books available in the library.")
        return
 
    print("Available books: ")
    for idx, book in enumerate(books_dict.keys()):
        print(f"{idx}. {book} ")
        
        
    book_name = input("Enter the name of book you want to borrow: ")
    if book_name not in books_dict:
        print(f"Sorry, '{book_name}' is not available in the library.")
        return
    if books_dict[book_name]["quantity"] > 0:
        books_dict[book_name]["quantity"] -= 1  # Reduce quantity by 1
        print(f"You have successfully borrowed '{book_name}'.")
    else:
        print(f"Sorry, '{book_name}' is currently out of stock.")
        return

    with open('books.txt', 'w') as file:
        book_entries = [json.dumps({key: value}) for key, value in books_dict.items()]
        file.write("|".join(book_entries))  # Store in the same format

    print("Library records updated successfully!")
    
    reader = input("Enter name of the reader: ")
    student_id = input("Enter the id: ")

    reader_dict = {student_id:{"name":reader,"book":book_name}}
    filename = 'reader.txt'
    with open(filename) as file:
        data = file.read()
    try:
        if data:
            existing_books_list = data.split("|")
        else:
            existing_books_list = []
            
    except FileNotFoundError:
        existing_books_list = []
    
    with open(filename, 'a') as file:
        books_json = json.dumps(reader_dict)
        if len(existing_books_list)>0:
            file.write('|')
        file.write(books_json)
        print("Reader information added!")
        
 
def return_book():
    pass       
    

def view_books():
    books_dict = user_json_to_dict('books.txt')

    if not books_dict:
        print("There are no books in this library yet!")
    else:
        for book in books_dict.keys():
            print(f"Title: {book}, Author: {books_dict[book]['author']}, Quantity: {books_dict[book]['quantity']}")


def admin_panel():
    while True:
        print("----Admin Panel----")
        print("1. View books \n2. Add book \n3. Borrowing \n4. Exit")
        user_choice = input("Type 1/2/3/4: ") 
     
    
        if user_choice == '1':
            view_books()
        elif user_choice == '2':
            add_book()
        elif user_choice == '3':
            borrow_book()
        elif user_choice == '4':
            break
    
        

def main():
    print("--Library--")
    user_log = input("Login/Register: ").lower()
    if user_log == "login":
        status, user = login()
    elif user_log == "register":
        register()
    else:
        print("You can only login or register in here!")
        return
    
    
    
    if status == 1:
        admin_panel()
main() 