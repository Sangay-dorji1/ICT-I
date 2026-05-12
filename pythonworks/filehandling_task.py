

file = open("students.csv", "w")

file.write("101,Pema\n")
file.write("102,Mendrel\n")
file.write("103,Tashi\n")
file.write("104,Wangmo\n")
file.write("105,Thinley\n")

file.close()

print("File created successfully!")

# Read the file

file = open("students.csv", "r")

# Ask user for a name
search_name = input("Enter student name: ")

found = False

# Check each line
for line in file:

    data = line.strip().split(",")

    student_id = data[0]
    student_name = data[1]

    if student_name.lower() == search_name.lower():

        print("Student found!")
        print("Student ID:", student_id)

        found = True

# If not found
if found == False:
    print("Student not found")

file.close()