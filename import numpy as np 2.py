import numpy as np
num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))
marks = np.empty((num_students, num_subjects))
for i in range(num_students):
    print(f"Enter marks for student {i+1}:")
    for j in range(num_subjects):
        marks[i][j] = float(input(f"Subject {j+1}: "))
total_marks = np.sum(marks, axis=1)
percentage = (total_marks / (num_subjects * 100)) * 100

# Define the grade boundaries
grades = ['A', 'B', 'C', 'D', 'E', 'F']

# Calculate the grade for each student
grade_index = np.digitize(percentage, [40, 50, 60, 70, 80])
grade = np.array([grades[i] for i in grade_index])
print("Student\tTotal Marks\tPercentage\tGrade")
for i in range(num_students):
    print(f"{i+1}\t{total_marks[i]}\t\t{percentage[i]:.2f}%\t\t{grade[i]}")
import numpy as np

# Get the number of students and subjects from the user
num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))

# Create an empty numpy array to store the marks
marks_array = np.zeros((num_students, num_subjects))

# Loop through each student and subject to input their marks
for i in range(num_students):
    for j in range(num_subjects):
        marks_array[i, j] = float(input(f"Enter marks for student {i+1} in subject {j+1}: "))

# Calculate the total marks for each student using numpy sum() function
total_marks = np.sum(marks_array, axis=1)

# Calculate the percentage for each student
percentage = (total_marks / (num_subjects * 100)) * 100

# Define the grading system
grading_system = {
    "A+": 90,
    "A": 80,
    "B+": 70,
    "B": 60,
    "C": 50
}

# Calculate the grade for each student based on their percentage
grades = []
for p in percentage:
    for grade, cutoff in grading_system.items():
        if p >= cutoff:
            grades.append(grade)
            break
    else:
        grades.append("F")

# Display the result for each student in a tabular format
print("Student\tTotal Marks\tPercentage\tGrade")
for i in range(num_students):
    print(f"{i+1}\t{total_marks[i]}\t\t{percentage[i]}%\t\t{grades[i]}")
 