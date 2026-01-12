from new_student import Student


student = Student(name="Edward", surname="agle")
print(student)
student = Student(name="", surname="")
print(student)

try:
    student = Student(name="Edward", surname="agle", id="toto")
except Exception as e:
    print("Error:", e)
