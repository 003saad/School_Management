class Classroom:
    def __init__(self,name) -> None:
        self.name = name
        self.students = [] # [student_objects]
        self.subjects = [] # [subject_objects]
    def add_students(self,student): # rahim, eight e vorti hbe
        roll_no = f"{self.name}-{len(self.students)+1}" # eight-2
        student.id = roll_no
        self.students.append(student)
    def add_subject(self,subject):
        self.subjects.append(subject)
    def take_semester_final_exam(self):
        for subject in self.subjects:
            subject.exam(self.students)
        for student in self.students:
            student.final_grade()