class Member:
    def __init__(self, name):
        self.full_name = name

    def introduce(self):
        print(f'Hi! My name is {self.full_name}')


class Instructor(Member):
    def __init__(self, name, bio):
        self.bio = bio
        self.skills = []
        super().__init__(name)

    def add_skill(self, skill):
        self.skills.append(skill)


class Student(Member):
    def __init__(self, name, reason):
        self.reason = reason
        super().__init__(name)


class Workshop:
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.students = []
        self.instructors = []

    def add_participant(self, person):
        self.students.append(person.__dict__) if isinstance(
            person, Student) else self.instructors.append(person.__dict__)

    def print_details(self):
        print(f"=> \n")
        self.__print_details()
        self.__print_students()
        self.__print_instructors()

    def __print_details(self):
        print(f"Workshop - {self.date} - {self.subject} \n ")

    def __print_students(self):
        print("Students")
        for (i, students) in enumerate(self.students):
            print(str(i+1) + ". " + students['full_name'] +
                  " - " + students["reason"])

    def __print_instructors(self):
        print("\nInstructors")
        for (i, instructor) in enumerate(self.instructors):
            print(str(i+1) + ". " + instructor['full_name'] +
                  " ", *instructor["skills"])
            print("\t"+instructor["bio"])


workshop = Workshop("12/03/2014", "Shutl")

jane = Student(
    "Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor(
    "Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()
