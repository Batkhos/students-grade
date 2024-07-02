students_grade = {}

def add_student(name,grade):
    students_grade[name]=grade
    print(f'add {name} with {grade}')
def update_student(name,grade):
    if name in students_grade:
        students_grade[name]=grade
        print(f'update {name} with {grade}')
    else:
        print('this namae not found')
def delete_student(name):
    if name in students_grade:
        del students_grade[name]
        print(f'{name} is deleted')
    else:
        print('this name not found')
def display_all_students():
        for name, grade in students_grade.items():
            print(f'{name} : {grade}')

def main():
    while True:
        print('what do want to do?')
        print('1-Add student')
        print('2-Update student grade')
        print('3-Delete student')
        print('4-Display all students')
        print('5-Exit')
        choice = int(input('enter your choice number = '))
        if choice == 1:
            name = input('Enter name of student = ')
            grade = int(input('Enter student grade = '))
            add_student(name, grade)
        elif choice == 2:
            name = input('Enter name of student = ')
            grade = int(input('Enter student grade = '))
            update_student(name, grade)
        elif choice == 3:
            name = input('Enter name of student = ')
            delete_student(name)
        elif choice == 4:
            display_all_students()
        elif choice == 5:
            break

main()
