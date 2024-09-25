def student_name_manager():
    student_name_list = []
    condition = True
    Id = 1

    while condition:
        user_in = input("Enter your name (if you want to exit, write 'stop'): ")

        if user_in.lower() == 'stop':
            condition = False
        else:
            duplicate_found = False 
            for student in student_name_list:
                if student[1] == user_in:
                    duplicate_found = True
                    break

            if duplicate_found:
                print(f"Duplicate name '{user_in}' found. Please enter a unique name.")
            else:
                tuple1 = (Id, user_in)
                student_name_list.append(tuple1)
                Id += 1

    print("\nComplete list of students with IDs:")
    for student in student_name_list:
        print(f"The ID {student[0]} and name {student[1]}")

    total_students = len(student_name_list)
    print(f"\nTotal number of students: {total_students}")

    total_name_length = 0
    for student in student_name_list:
        total_name_length += len(student[1])
    print(f"Total length of all student names combined: {total_name_length}")

    if student_name_list:
        longest_name = student_name_list[0]
        shortest_name = student_name_list[0]

        for student in student_name_list:
            if len(student[1]) > len(longest_name[1]):
                longest_name = student
            if len(student[1]) < len(shortest_name[1]):
                shortest_name = student

        print(f"Student with the longest name: {longest_name[1]} (ID: {longest_name[0]})")
        print(f"Student with the shortest name: {shortest_name[1]} (ID: {shortest_name[0]})")

student_name_manager()

