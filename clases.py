from student import Student

student1 = Student("Ion", "Business", 4.5, True)
student2 = Student("Silviu", "IT", 1.5, False)

print(student1.name)
print(student1.gpa)

print(student2.major + "\n")

print(student1.on_honor_roll())
print(student2.on_honor_roll())

