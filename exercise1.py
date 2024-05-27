students_list = []
students_dict = {}

name = input("Enter students name:")
age = int(input("Enter students age:"))
grade = int(input("Enter students grade:"))
students_list.append(name)
students_dict[name] = {"age":age, "grade":grade}
print("Student information added successfully")
print(students_dict.items())

search_name = input("Enter the name of the student to search or simply enter to skip:")
if search_name in students_list:
    info = students_dict[search_name]
    print(f"name: {search_name}, age: {info['age']}, grade: {info['grade']}")
else:
    print("Student not found!")

remove_name = input("Enter the students name to remove or else enter to skip:")
if remove_name in students_list:
    del students_dict[remove_name]
    students_list.remove(remove_name)
    print("Student removed successfully")
else:
    print("Student not found!")