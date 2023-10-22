from tutor import Tutor
from student import Student
from school import School

# a script to test the scheduler

# Create tutors
tutor1 = Tutor("Tutor 1", 1, ["Math", "Science"])
tutor2 = Tutor("Tutor 2", 2, ["English", "History"])
tutor3 = Tutor("Tutor 3", 3, ['English', 'Science'])

# Create students
student1 = Student("Student 1", 101, ["Math", "English"], 2)
student2 = Student("Student 2", 102, ["Science", "History"], 2)

# Create a school and add tutors and students
school = School("My School")
school.add_tutor(tutor1)
school.add_tutor(tutor2)
school.add_student(student1)
school.add_student(student2)

# Call the scheduler
school.scheduler()
