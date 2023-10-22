class School:

    """
    A class to represent a school. Below the main methods and instantiation variables will be summarized.

    Tutors (a list of tutors that work at the school)
    Students (a list of students that attend the school and need tutoring)
    Scheduler (a function that will assign the students to tutors appropriately)

    add_tutor() is a function to add tutors to the school after the school has already been created

    add_student() is a function to add students to the school after the school has already been created
    """

    def __init__(self, name):
        self.name = name
        self.tutors = []
        self.students = []

    def add_tutor(self, tutor):
        self.tutors.append(tutor)

    def add_student(self, student):
        self.students.append(student)

    def scheduler(self):
        # Assign students to tutors appropriately
        # initially a brute force implementation will be used
        for tutor in self.tutors:
            print(f'Schedule for {tutor}:')
            for hour, students in enumerate(tutor.students_each_hour):
                print(f'Hour {hour + 1}: {", ".join([str(student) for student in students])}')
            print()

