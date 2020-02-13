# BLL code start here
StudentList=[]
class Student():
    def __init__(self):
        self.id=0
        self.name=''
    def AddStudent(self):
        StudentList.append(self)

    def showAll(self):
        return StudentList



# BLL code end here
# PL code start here (Crud )
while (True):
    print("1.Add Student\n2.Search Student\n3.Update Student\n4.Delete Student\nExit press 0")
    ch=int(input('Enter your choice'))
    if ch==1:
        stdt=Student()
        stdt.id=int(input('Enter your id:  '))
        stdt.name=input('Enter your Name:  ')
        stdt.AddStudent()
        print('Student Added successfully')
    if ch==5:
        stdt = Student()
        s =stdt.showAll()
        for stu in s:
            print(stu.id, stu.name)

# PL code end here
