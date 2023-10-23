class Student:

    """
    A class to represent a student. Below the main methods and instantiation variables will be summarized.

    Student name (a string name of the student)
    Student ID (a unique integer identifier for each student)
    Courses they need tutoring in (list of strings representing the courses a student needs tutoring in)
    Hours they need tutoring (an integer representing the amount of hours of tutoring the student would like to receive, must be equal to the length of the courses list)
    In Class (a list to show if a student is with a tutor during an hour, 1 = with tutor, 0 = not with a tutor)

    Note that the school schedules only 1 hour sessions.
    So if a student wants 2 hours of math, 'Math' should appear twice in their courses list
    
    """

    def __init__(self, name, student_id, courses, hours_needed):
        self.name = name
        self.student_id = student_id
        self.courses = courses
        self.hours_needed = hours_needed
        self.in_class = [0,0,0,0]

    def __str__(self):
        return f'Student {self.name} (ID: {self.student_id})'

