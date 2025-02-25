# Student Grade Manager
# Read student data from a file (students.txt).
# Store it in a dictionary ({"student_id": {"name": "X", "marks": [90, 85, 88]}}).
# Allow users to add new students, update marks, and calculate averages.
# Save changes back to the file.

import json

def add_student():
    student_info = json_to_dict()
    student_id = input("Enter the id for the student: ")
    if student_id in student_info:
        print("The student id already exits!")
        return
    name = input("Enter name of the student: ").capitalize()
    marks=[]
    phy = int(input("Enter the marks of physics: "))
    chem = int(input("Enter the marks of chemistry: "))
    bio = int(input("Enter the marks of biology: "))
    marks.append(phy)
    marks.append(chem)
    marks.append(bio)
    
    student_dict = {student_id:{'name':name,'marks':marks}}
    
    with open('student.txt','a') as file:
        student_json = json.dumps(student_dict)
        
        file.write(f"{student_json}|")
    print("Added new student successfully!")

def search_student():
    student_info = json_to_dict()
    
    id = input("Enter student id to search for details: ")
    if id not in student_info:
        print(f"{id} not found in the database!")
        return
    else:
        name = student_info[id]['name']
        marks = student_info[id]['marks']
        
        print(f"{id} details:\nName = {name} \nMarks of physics, chemistry and biology = {marks}")

def update_marks():
    student_info = json_to_dict()
    
    id = input("Enter student id to search for details: ")
    if id not in student_info:
        print(f"{id} not found in the database!")
        return
    else:
        name = student_info[id]['name']
        marks=[]
        phy = int(input("Enter new marks of physics: "))
        chem = int(input("Enter new marks of chemistry: "))
        bio = int(input("Enter new marks of biology: "))
        marks.append(phy)
        marks.append(chem)
        marks.append(bio)
    
        student_info[id]['marks']=marks
        
        with open('student.txt', 'w') as f:
            student_json = json.dumps(student_info)
            f.write(f"{student_json}|")
            
        print("Grade updated successfully!")

def calculate_average():
    student_info = json_to_dict()
    
    
    id = input("Enter student id to calculate average marks: ")
    if id not in student_info:
        print(f"{id} not found in the database!")
        return
    else:
        name = student_info[id]['name']
        sum = 0
        for i in student_info[id]['marks']:
            sum+=i
        avg = sum/len(student_info[id]['marks'])
        
        print(f"The average marks of {name} is {avg}")
    


def json_to_dict():
    student_info ={}
    
    with open("student.txt") as file:
        student_data = file.read()
        
    student_data_list = student_data.split("|")
    
    for i in student_data_list:
        if i:
            try:
                student_data_dict = json.loads(i)
                student_info.update(student_data_dict)
            except json.JSONDecodeError:
                continue
                
    return student_info

while True:  
    print("\n-------------------Student Grade Manager-------------------\n")
    print("Menu")
    print("\n1. Add Student \n2. Search Student \n3. Update Marks \n4. Calculate average")
    choice = input("\nEnter you choice(1/2/3/4/exit): ")


        

    if choice == "exit":
        break

    elif choice == '1':
        add_student()

    elif choice == '2':
        search_student()

    elif choice == '3':
        update_marks()

    elif choice == '4':
        calculate_average()
    else:
        print("Enter a valid input(1/2/3/4/exit)")