count = 0
class students:
    def __init__(self, id, fname, lname, course, year, gpa, university, email, mobile):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.course = course
        self.year = year
        self.gpa = gpa
        self.university = university
        self.email = email
        self.mobile = mobile
def counter():
    global count
    count += 1
    print(str(count) + " instances are created for above class named students")
list = []
# appending instances to list
list.append(students(1900001, "John", "smith", "EEE", 2, 9.0, "kl university", "Johnsmith@gmail.com", 1111111111))
for obj in list:
    print(obj.id, obj.fname, obj.lname, obj.course, obj.year, obj.gpa, obj.university, obj.email, obj.mobile)
counter()