def total_marks(marks):
    return sum(marks)

def percentage(marks):
    return total_marks(marks) / len(marks)

def grade(per):
    if per >= 90:
        return "A"
    elif per >= 75:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 50:
        return "D"
    else:
        return "F"

name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = int(input("Enter marks: "))
    marks.append(mark)

total = total_marks(marks)
per = percentage(marks)
g = grade(per)

print("\nStudent Result:")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", per)
print("Grade:", g)
