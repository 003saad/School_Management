from school import School
from person import Student, Teacher
from classroom import Classroom
from subject import Subject


school = School("ABC School", "Dhaka")

eight = Classroom("Eight")
nine = Classroom("Nine")
ten = Classroom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)


rahim = Student("Rahim", eight)
karim = Student("Karim", nine)
fahim = Student("Fahim", ten)
hamim = Student("Hamim", ten)

school.student_addmission(rahim)
school.student_addmission(karim)
school.student_addmission(fahim)
school.student_addmission(hamim)

abul = Teacher("Abul")
babul = Teacher("Babul")
kabul = Teacher("Kabul")

bangla = Subject("Bangla", abul)
physics = Subject("Physics", babul)
chemistry = Subject("Chemistry", kabul)
biology = Subject("Biology", kabul)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(biology)
nine.add_subject(chemistry)
nine.add_subject(physics)
ten.add_subject(biology)
ten.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject


eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)