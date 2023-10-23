class School:

    """
    A class to represent a school. Below the main methods and instantiation variables will be summarized.
    The school only offers tutoring in 1 hour sessions.

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

        # iterate through all students that need to be scheduled
        for student in self.students:

            # if the student needs no more hours, move to next iteration
            if student.hours_needed < 0:
                continue

            # iterate through the number of tutors
            for tutor in self.tutors:

                # if the student needs no more hours, move to next iteration
                if student.hours_needed < 0:
                    continue

                # check if tutor teaches courses student needs
                for course in student.courses:
                    
                    # if the student needs no more hours, move to next iteration
                    if student.hours_needed < 0:
                        continue

                    if course in tutor.courses:
                        
                        # entered if the tutor teaches a course the student needs
                        assigned = tutor.assign_student(student, course)

                        # if the student needs no more hours, move to next iteration
                        if student.hours_needed < 0:
                            continue

        # print out schedule for each tutor
        for tutor in self.tutors:
            print(f'Schedule for {tutor}:')
            for hour, students in enumerate(tutor.students_each_hour):
                print(f'Hour {hour + 1}: {", ".join([str(student) + " " +  course for student, course in students])}')
            print()

