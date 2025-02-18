class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def __str__(self):
        return f"Course Code: {self.course_code}, Course Name: {self.course_name}, Credit Hours: {self.credit_hours}"


# Subclass for CoreCourse
class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def __str__(self):
        return f"{super().__str__()}, Required for Major: {self.required_for_major}"



class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def __str__(self):
        return f"{super().__str__()}, Elective Type: {self.elective_type}"

if __name__ == "__main__":
    core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
    elective_course = ElectiveCourse("HIS210", "World History", 3, "Liberal Arts")
    print(core_course)
    print(elective_course)

from employee import Employee
emp = Employee("John Doe", 50000)
print(f"Employee Name: {emp.get_name()}")
print(f"Employee Salary: ${emp.get_salary()}")
