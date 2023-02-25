# student.py
# Author: Kealan McGuinness
# stores a student name and a list of her courses and
# grades in a dict, the program should then print out her data.

student = {
    "name":"Mary",
    "modules": [
        {"course_name":"Programming",
        "Grade": 45
        },
        {
            "course_name":"History",
            "Grade":99
        }
    ]
}
print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["course_name"], module["Grade"]))
    