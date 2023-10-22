# creating the tutor class

class Tutor:

    """
    A class to represent a tutor. Below the main methods and instantiation variables will be summarized.
    Tutor Name (a string name of each tutor)
    Tutor ID (a unique integer identifier for each tutor)
    Courses (a list of courses that a tutor can teach)
    Students each hour (each tutor can work 4 hours, each hour is represented by a list of students that the tutor is seeing that hour)
    Current amount of students (4 separate integers that track how many students the tutor has in each hour, a tutor can have a maximum of 3 students at once)

    assign_student() is a function that will assign students to a tutor
    """

    def __init__(self, name, tutor_id, courses):
        self.name = name
        self.tutor_id = tutor_id
        self.courses = courses
        self.students_each_hour = [[],[],[],[]]
        self.current_students = [0, 0, 0, 0]

    def assign_student(self, student, course):

        # only returns true if the student was assigned
        result = False

        # find an hour with a free spot
        for hour in range(4):

            # check if the current hour has less than 3 students
            if self.current_students[hour] < 3:

                # enter if current hour has space

                # assign student
                self.students_each_hour[hour].append(student)

                # update hourly student counter
                self.current_students[hour] += 1

                # reduce amount of hours student needs
                student.hours_needed -= 1

                # remove the course that the tutor is tutoring from the list 
                student.courses.remove(course)

                # change result
                result = True

        return result

    def __str__(self):
        return f'Tutor {self.name} (ID: {self.tutor_id})'