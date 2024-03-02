import StudentClass as s

student_id = input("Student ID: ")
name = input("Name: ")
dob = input("Date of Birth(m-d-Year): ")
classification = input("Classification(Sr, Jr, So, Fr): ")

student = s.Student(student_id,name,dob,classification)

print("Age:",student.calculate_age())

print("Registration Dates:",student.registration_dates())