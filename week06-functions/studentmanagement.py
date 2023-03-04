# studentmanagement.py
#Author: Kealan McGuinness
# create a program that allows a user to create new students and to view students

def display_menu () :
    print ("What would you like to do?")
    print ("\t(a) Add a new student")
    print ("\t(v) View students")
    print ("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip ()
    return choice

def do_add (students):
    current_student = {}
    current_student["name"]=input("enter name: ")
    current_student["modules"]= read_modules()
    students.append(current_student)

def read_modules():
    modules = []
    module_name = input("\tEnter the first Module name (blank to quit): ").strip()

    while module_name != "":
        module = {}
        module["name"] = module_name

        module["grade"]=int(input("\t\tEnter grade: "))
        modules.append(module)

        module_name = input("\tEnter next module name (blank to quit): ").strip()
    return modules



def display_modules(modules):
    print ("\tName \tGrade")
    for module in modules: 
        print (f"\t{ module['name']} \t {module['grade']}")
        
def do_view(students):
    for current_student in students:
        print (current_student['name'])
        display_modules(current_student['modules'])
        

students = []
choice = display_menu()
while(choice != "q"):
    if choice == "a" :
        do_add(students)
    elif choice == "v" :
        do_view(students)
    elif choice != "q" :
        print ("\n\nplease select either a, v, or q")
    choice=display_menu()








