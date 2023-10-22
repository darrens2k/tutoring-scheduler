# tutoring-scheduler
A small Python project toying around with OOP.    

### Creation Notes: 22/10/2023
This is a quick project I whipped up that was inspired by my time working as a tutor and the constant issues that would come up with scheduling. The project consists of 3 classes.    

Tutor Class:
* Tutor Name (a string name of each tutor)
* Tutor ID (a unique integer identifier for each tutor)
* Students each hour (each tutor can work 4 hours, each hour is represented by a list of students that the tutor is seeing that hour)
* Current amount of students (4 separate integers that track how many students the tutor has in each hour, a tutor can have a maximum of 3 students at once)

Student Class:
* Student name (a string name of the student)
* Student ID (a unique integer identifier for each student)
* Courses they need tutoring in (list of strings representing the courses a student needs tutoring in)
* Hours they need tutoring (an integer representing the amount of hours of tutoring the student would like to receive, must be at least as large as the amount of different courses they want tutoring in)

School Class:
* School Name (a string name of the school)
* Tutors (a list of tutors that work at the school)
* Students (a list of students that attend the school and need tutoring)
* Scheduler (a function that will assign the students to tutors appropriately)

Intended Use: Create a list of tutors, create a list of students, then create a school and add the students and tutors to the school. Then call the scheduler, and the scheduler will print out the scheduler of each tutor for the day. Each class will be in its own python file, and there will be a main python file that demonstrates this intended use.
