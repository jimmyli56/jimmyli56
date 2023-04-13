# creates an empty list to store grades
grades = []

# asks the user for the number of courses taken
courses = int(input("How many courses have you taken? "))

# get the grades for each course
for i in range(courses):
  grade = float(input("Enter your grade (0-100) for course {}: ".format(i+1)))
  grades.append(grade)

# calculate the average grade
average_grade = sum(grades) / len(grades)

# convert the average grade to a GPA scale
if average_grade >= 90:
  gpa = 4.0
elif average_grade >= 85:
  gpa = 3.7
elif average_grade >= 80:
  gpa = 3.3
elif average_grade >= 77:
  gpa = 3.0
elif average_grade >= 73:
  gpa = 2.7
elif average_grade >= 70:
  gpa = 2.3
elif average_grade >= 67:
  gpa = 2.0
elif average_grade >= 63:
  gpa = 1.7
elif average_grade >= 60:
  gpa = 1.3
else:
  gpa = 0.0

# print the GPA
print("Your GPA is: {:.2f}".format(gpa))
