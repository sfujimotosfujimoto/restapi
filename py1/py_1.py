
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args):
        return cls(friend_name, origin.school, *args)


class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title


anna = WorkingStudent("Anna", "Oxford", 20.00, "Boss")
print(anna.salary)

friend = WorkingStudent.friend(anna, "Greg", 17.00, "CEO")
print(friend.name)
print(friend.school)