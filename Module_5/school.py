class Student:
    def __init__(self,name,current_class,id):
        self.name = name
        self.id = id
        self.current_class = current_class

    def __repr__(self) -> str:
        return f'Student with name: {self.name}, class : {self.current_class}, id : {self.id}' 
    

class Teacher:
    def __init__(self,name,subject,id) -> None:
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self) -> str:
        return f'Faculty  with name: {self.name}, Taken CLass : {self.subject}, id : {self.id}' 

class School:
    def __init__(self,name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self,name,subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)

    def enroll(self,name,fee):
        if fee > 6500:
            return 'Not enough fee'
        else:
            id = len(self.students) +1
            student = Student(name, 'C',id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money{fee-6500}'
        
    def __repr__(self) -> str:
        print('Welcome to',self.name)
        print('-----Our Teacher------')
        for teacher in self.teachers:
            print(teacher)
        print('-----Our Students------')
        for student in self.students:
            print(student)    
        return 'All Done for now'



# alia = Student('Alia',9,1)
# ranbeed = Teacher('Ranbeer','Math',101)
# print(alia)
# print(ranbeed)

phitron = School('Phitron')
phitron.enroll('alia',6000)
phitron.enroll('rani',8000)
phitron.enroll('sakib',4500)
phitron.enroll('Tamim',6500)

phitron.add_teacher('Tom Cruise','DSA')
phitron.add_teacher('Mushfiq','CPP')
phitron.add_teacher('Rakib','Python')
phitron.add_teacher('Emon','HTML')

print(phitron)