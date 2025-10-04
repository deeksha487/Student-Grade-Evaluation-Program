# student_grade.py

marks = int(input("Enter marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)
# student_grade_average.py

marks = []
for i in range(5):
    m = int(input(f"Enter marks of subject {i+1}: "))
    marks.append(m)

average = sum(marks) / 5

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Average Marks:", average)
print("Grade:", grade)