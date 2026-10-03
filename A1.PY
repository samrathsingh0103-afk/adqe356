student_profile = ("Samrath", "Grade 6", "Section E", 5)
 
print("Student Profile:")

student_name = student_profile[0]
grade = student_profile[1]
section = student_profile[2]
total_subjects = student_profile[3]
 
print("Student Name:", student_name)
print("Grade:", grade)
print("Section:", section)
print("Total Subjects:", total_subjects)
 
print("First two details:", student_profile[0:2])

monday_subjects = {"Math", "English", "Hindi", "Science", "Social Science"}
tuesday_subjects = {"Maths", "Hindi", "English", "Sports", "Music",}
 
print("Monday Subjects:", monday_subjects)
print("Tuesday Subjects:", tuesday_subjects)
 
monday_subjects.add("Library")
print("After adding Library to Monday:", monday_subjects)
 
monday_subjects.discard("Computer")
print("After removing Computer from Monday:", monday_subjects)
 
tuesday_subjects.add("Computer")
print("After adding Computer to Tuesday:", tuesday_subjects)
 
tuesday_subjects.discard("Music")
print("After removing Music from Tuesday:", tuesday_subjects)
 
all_subjects = monday_subjects.union(tuesday_subjects)
common_subjects = monday_subjects.intersection(tuesday_subjects)
only_monday = monday_subjects.difference(tuesday_subjects)
only_tuesday = tuesday_subjects.difference(monday_subjects)
different_subjects = monday_subjects.symmetric_difference(tuesday_subjects)

print("All Subjects:", all_subjects)
print("Common Subjects:", common_subjects)
print("Only Monday Subjects:", only_monday)
print("Only Tuesday Subjects:", only_tuesday)
print("Different Subjects:", different_subjects)