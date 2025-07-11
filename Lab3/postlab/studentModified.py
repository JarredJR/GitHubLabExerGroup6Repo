import random

class Student:
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __ge__(self, other):
        return self.name >= other.name

    def __str__(self):
        return f"Student(Name: {self.name}, Age: {self.age}, Grade: {self.grade})"

def main():
    students = []

    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        print(f"\nEnter details for Student {i + 1}:")
        name = input("  Name: ")
        age = int(input("  Age: "))
        grade = input("  Grade: ")
        students.append(Student(name, age, grade))
    
    print("\nOriginal Student List:")
    for student in students:
        print(student)
    
    random.shuffle(students)
    print("\nShuffled Student List:")
    for student in students:
        print(student)
    
    students.sort()
    print("\nSorted Student List:")
    for student in students:
        print(student)

if __name__ == "__main__":
    main()
