#initialiazation of empty list and empty dict.
Students_list = []
Students_dict = {}

#asking for user input
name = input("Enter student name: ")
age = input("Enter student age: ")
grade = input("Enter student grade: ")

#adding students name to the list and details to the dict.
Students_list.append(name)
Students_dict[name] = {
    "age":age,
    "grade":grade
}

#printing a success message
print("Your input has been successfully added to the stuudents details")
print(Students_dict)

#allowing users to search students by their name
studentname  = input("enter the students name: ")
if  studentname in Students_dict:
    print(f"Student found! Name: {studentname}, Age: {Students_dict[studentname]['age']}, Grade: {Students_dict[studentname]['grade']}")
else:
    print("student not found!")

#allowing user to remove students by entring their name 
remove_name = input("Enter student name: ")
if remove_name in Students_dict:
    Students_list.remove(remove_name)
    del Students_dict[remove_name]
    print(remove_name, "is successfully removed from students record")
else:
    print(remove_name, "is not in the student record")