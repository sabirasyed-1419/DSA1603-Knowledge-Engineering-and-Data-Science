
import matplotlib.pyplot as plt

grades = ['F', 'E', 'D', 'C', 'B', 'A', 'S']
students = [3, 4, 5, 8, 9, 7, 4]

# Pie chart
plt.pie(students, labels=grades, autopct='%1.1f%%')
plt.title("Grade Percentage")
plt.legend(grades)
plt.show()

# Bar chart
plt.bar(grades, students)

for i, n in enumerate(students):
    plt.text(i, n, str(n), ha='center')

plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.title("Student Grade Analysis")
plt.show()

# Maximum and minimum grades
print("Maximum grade:",
      grades[students.index(max(students))])

print("Minimum grade:",
      grades[students.index(min(students))])

# A and S combined percentage
percentage = (7 + 4) / 40 * 100
print("A and S percentage:", percentage, "%")