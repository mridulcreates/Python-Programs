# Marks and their grades
total_marks = 0
num_subjects = 5

for i in range(1, num_subjects + 1):
    mark = float(input(f"Enter marks for subject {i}: "))
    total_marks += mark

percentage = (total_marks / (num_subjects * 100)) * 100

if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
else:
    grade = 'D'

print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")

# A year is a leap year or not
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")