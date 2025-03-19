import time 

def file_to_dict(filepath):
    student = {}
    with open(filepath,'r') as f:
        for line in f.readlines():
            line = line.split(',')
            student[line[0]] = line[1:]
    return student

def dict_to_file(dictionary,filepath) :
    with open(filepath , 'w+') as f :
            for email in sorted(dictionary.keys()):
                f.write(f"{email},{','.join(str(i) for i in dictionary[email])}\n")

def get_student_info(mail):
    student = file_to_dict("student.csv")
    # mail = input("Enter E-Mail : ")
    if mail in student.keys() :
        # print(student)
        c,g,m = [],[],[]
        with open("student.csv",'r') as f :
            for line in f.readlines() :
                line = line.split(',')
                if line[0] == mail :
                    c.append(line[3])
                    g.append(line[4])
                    m.append(line[5])
        
        return student[mail][0],student[mail][1],c,g,m
    
    else :
        print("Student not found !!!")

def get_course_details(id):
    course = file_to_dict("course.csv")   
    if id in course.keys():
        return id,course[id][0],course[id][1]
    else :
        print("Course not found!!")

def get_professor_details(mail):
    professor  = file_to_dict("professor.csv")
    if mail in professor.keys():
        return [str(i) for i in professor[mail]]

def get_login_details():
    email = input("Enter Your mail : ")
    pwd = input("Enter the password : ")
    pwd  = TextSecurity(4).encrypt(pwd)
    return email,pwd

class Student():
    def __init__(self,f_name,l_name,c,g,m):
        self.f_name = f_name
        self.l_name = l_name
        self.course_id = c
        self.grades = g
        self.marks = m

    def display_records(self):
        
        print(f"First Name : {self.f_name}  Last Name : {self.l_name} ")
        print("Courses Enrolled,Grades,Marks")
        for i in (zip(self.course_id,self.grades,self.marks)):
            print(i[0],i[1],i[2],end ='')
        

    def check_my_grade(self):
        print("****** CHECKING GRADES ********")
        for i,j in zip(self.course_id,self.grades):
            print(i,j)

    def upadte_student_record(self,mail):
        print("********* Updating Student record ************")
        while True :
            lines = []
            print(
                """
    1. Mail Address
    2. First Name
    3. Last Name
    """)
            choice = int(input("Enter ur choice to modify : "))
            if choice in (1,2,3) :
                with open("student.csv",'r') as  f:
                    new_value = input("Enter new value : ")
                    for line in f.readlines():
                        line = line.split(',')
                        # if choice == 1 :
                        if line[0]==mail :
                            line[choice-1] = new_value
                            if choice == 1 :
                                llines = []
                                with open("login.csv",'r') as lf:
                                    for lline in lf.readlines():
                                        lline = lline.split(',')
                                        if lline[0] == mail :
                                            lline[0] = new_value
                                        llines.append(','.join(lline))
                                with open("login.csv",'w') as lf :
                                    lf.writelines(llines)
                                # Login.logout()
                        if choice == 2:
                            self.l_name = new_value
                        elif choice == 3 :
                            self.f_name = new_value
                        lines.append(','.join(line))
                
                with open("student.csv" , 'w') as f :
                    f.writelines(lines)

            else :
                print("Nothing selected")
            if choice ==  1:
                Login.logout()
            ans = input("If u want to update more enter y : ")
            if ans != 'y':
                break

            else :
                pass

    def check_my_marks(self):
        print("********** Checking Marks ***********")
        for i,j in zip(self.course_id,self.marks):
            print(i,j,end = "")

                
class Course() :
    def __init__(self,id,name,credits):
        self.id = id
        self.name = name
        self.credits = credits 

    def display_course(self) :
        print(f"Course ID : {self.id} , Name : {self.name} , Credits : {self.credits}")

    def add_new_course(self) :
        while True :
            new_course = input("Enter the new course to add in Database : ")
            course = file_to_dict("course,csv")
            if new_course in self.course :
                print("This course already exists !!!")
            else :
                name  = input("Enter the course name : ")
                description  = input("Enter the description : ")
                self.course[new_course] = [name,description]
            
            ans = input("Enter any value to exit : ")
            if ans :
                break
        dict_to_file(course,filepath="course.csv")   

    def delete_new_course(self) :
        new_course = input("Enter the course to delete from Database : ")

        if new_course not in self.course :
            print("Course does not exists")
        else :
            del self.course[new_course]


        
class Professor() :
    def __init__(self,name ,rank , course_id):
        self.name = name 
        self.rank = rank 
        self.course_id  = course_id

    def professor_details(self):
        print(f"Name : {self.name} Rank : {self.rank}")
        print(f"Teaches : {self.course_id}")

    def add_new_professor():
        pass

    def delete_professor():
        pass

    def update_professor(self,mail) :
        print("********* Updating Professor record ************")
        while True :
            lines = []
            print(
                """
    1. Mail Address
    2. First Name
    """)
            choice = int(input("Enter ur choice to modify : "))
            new_value = input("Enter the new value : ")
            if choice == 1 :
                llines=[]
                with open("pofessor.csv",'r') as f :
                    for line in f.readlines() :
                        line = line.split(',')
                        if line[0] == mail:
                            line[0] = new_value
                        lines.append(','.join(line))
                with open("login.csv",'r') as nf :
                    for line in nf.readlines() :
                        line=line.split(',')
                        if line[0] == mail :
                            line[0] = new_value
                        llines.append(','.join(line))
                with open("professor.csv",'w') as f :
                    f.writelines(lines)
                with open("login.csv",'w') as f :
                    f.writelines(llines)
                Login.logout()
            elif choice ==2 :
                with open("pofessor.csv",'r') as f :
                    for line in f.readlines() :
                        line = line.split(',')
                        if line[0] == mail:
                            line[1] = new_value
                        lines.append(','.join(line))
                with open("professor.csv",'w') as f :
                    f.writelines(lines)
                
                self.name = new_value

    def course_by_proessor(self) :
        print(self.course_id)


class Grade() :
    def __init__(self,score) :
        self.score = score

    def grade_report(self):
        if self.score in range(96,101) :
            return 'A'
        elif self.score in range(85,96) :
            return 'B'
        elif self.score in range(75,86) :
            return 'C'
        elif self.score in range(65,76) :
            return 'D'
        elif self.score <65 :
            return 'F'


class Login() :
    def __init__(self,email,password):
        self.email = email 
        self.password = password
        # self.ts = TextSecurity(4)

    def login(self) :
        login = file_to_dict(filepath="login.csv")
        if self.email in login.keys() :
            if self.password == login[self.email][0]:
                print(f"         Logged in with {self.email}          ")
                return login[self.email][1]
        
        else :
            print("Wrong Credentials !!!")
            return None

    @staticmethod
    def logout(self) :
        return

    def change_password(self) :
        print("Old password  : ",self.decrypt_password(self.password))
        new_p = input("Enter New Password : ")
        new_p = self.encrypt_password(new_p)
        lines = []
        with open("login.csv",'r') as f :
            for line in f.readlines() :
                line  = line.split(',')
                line[1] = new_p
                lines.append(','.join(line))
        with open("login.csv",'w') as f :
            f.writelines(lines)

    def _convert(self, text,s):
        result=""
        for i,ch in enumerate(text):
            if (ch.isupper()):
                result += chr((ord(ch) + s-65) % 26 + 65)   
            else:
                result += chr((ord(ch) + s-97) % 26 + 97)
        return result  

    def encrypt_password(self,a) :
        return self._convert(a,4%26)

    def decrypt_password(self,b) :
        return self._convert(b,26-4%26)

class TextSecurity():

    def __init__(self, shift):
        self.shifter=shift
        self.s=self.shifter%26
            
    def _convert(self, text,s):
        result=""
        for i,ch in enumerate(text):
            if (ch.isupper()):
                result += chr((ord(ch) + s-65) % 26 + 65)   
            else:
                result += chr((ord(ch) + s-97) % 26 + 97)
        return result       
    @staticmethod
    def encrypt(self,text):
        return self._convert(text,self.shifter)

    def decrypt(self, text):
        return self._convert(text,26-self.s)

class Admin():
    def __init__(self):
        pass

    def view_professors(self):
        with open("professor.csv",'r') as f :
            lines = f.readlines()
        
        for line in sorted(lines):
            print(line , end ="")
    
    def view_students(self):
        with open("student.csv",'r') as f :
            lines = f.readlines()
        
        for line in sorted(lines):
            print(line,end = "")

    def add_new_student(self):
        # student = file_to_dict(filepath="student.csv")
        mail = input("Enter E-Mail : ")
        f_name = input("Enter the First Name : ")
        l_name = input("Enter the Last Name : ")
        with open("student.csv",'a') as f :
            line = ','.join([mail,f_name,l_name,"NA","NA","NA"])
            f.write(line)
        

    def delete_student(self):
        print("********* Deleting student record *********")
        mail = input()
        with open("student.csv",'r') as f :
            lines= f.readlines()
            f.seek(0)
            for line in f.readlines():
                line = line.split(',')
                if line[0] == mail :
                    lines.remove(','.join(line))

        with open("student.csv",'w') as f:
            f.writelines(lines)


    def add_new_professor(self,email,password):
        professor = file_to_dict(filepath="professor.csv")
        mail = input("Enter E-Mail : ")
        f_name = input("Enter the First Name : ")
        rank = input("Enter the rank: ")
        c_id = input("Enter the course_id : ")
        professor[mail] = [f_name,rank,c_id]
        dict_to_file(professor,"professor.csv")

        login = file_to_dict(filepath="login.csv")
        pwd = input("Enter the password : ")
        e_pwd = Login(email,password).encrypt_password(pwd)

        login[mail] = [e_pwd,"professor"]

        dict_to_file(login,"login.csv")

    def delete_professor(self):
        print("********* Deleting Professor record *********")
        mail = input("Enter the mail address : ")
        professor = file_to_dict("professor.csv")

        try :
            del professor[mail]
        except Exception as e :
            print(e)
        else :
            print("Record Deleted")
        
        dict_to_file(professor,"professor.csv")

        login = file_to_dict("login.csv")

        try :
            del login[mail]
        except Exception as e :
            print(e)
        else :
            print("Record Deleted")
        
        dict_to_file(login,"login.csv")

class GradeApp() :
    def __init__(self):
        pass


def main():
    email,password = get_login_details()
    l = Login(email,password)
    ans = input("if want to change password press 'y' : ")
    if ans == 'y' :
        l.change_password()
    while True :
        start_time = time.perf_counter()
        role =  l.login()
        if role != None :
            # print(role)
            if role.strip() == "student" :
                # print("Entered inside")
                a1,a2,a3,a4,a5= get_student_info(email)
                s = Student(a1,a2,a3,a4,a5)
                print("""
                    1. Student Details
                    2. Show your Course Details 
                    3. My Grades
                    4. My Marks
                    5. Update Details
                    6. Report Card
                    7. Logout
                """)    
                choice  = int(input("Enter your choice to do : "))

                if choice == 1 :
                    s.display_records()
                
                elif choice == 2 :
                    for sub in s.course_id :
                        a1,a2,a3 = get_course_details(sub)
                        c = Course(a1,a2,a3)
                        c.display_course()
                
                elif choice == 3 :
                    s.check_my_grade()

                elif choice == 4:
                    s.check_my_marks()
                
                elif choice == 5 :
                    s.upadte_student_record(email)

                elif choice == 6 :
                    sum = 0
                    s.display_records()
                    print("Average marks : ")
                    for i in s.marks :
                        sum += int(i)
                    print(sum/3)
                    print("Overall Grade : ",Grade(sum//3).grade_report())
                    for sub in s.course_id :
                        a1,a2,a3 = get_course_details(sub)
                        c = Course(a1,a2,a3)
                        c.display_course()
                elif choice == 7 :
                    return
                    

            elif role.strip() == "professor" :
                a1,a2,a3,a4 = get_professor_details(email)
                p  = Professor(a1,a2,a3,a4)
                print("""
                    1. Professor record
                    2. Update Record
                    3. My course
                    4. Logout
    """)
                choice  = int(input("Enter the choice u want to do : "))
                if choice ==  1 :
                    p.professor_details()
                elif choice == 2 :
                    p.update_professor(email)
                elif choice == 3 :
                    p.course_by_proessor()
                elif choice == 4 :
                    return

            elif role.strip() == "admin" :
                a  = Admin()
                print("""
                    1. Add Student
                    2. Remove Student
                    3. Add Professor
                    4. Remove Professor
                    5. Show Professors Data
                    6. Show Students Data
                    7. Logout
    """)
                choice  = int(input("Enter the choice u want to do : "))
                if choice ==  1 :
                    a.add_new_student()
                elif choice == 2 :
                    a.delete_student()
                elif choice == 3 :
                    a.add_new_professor(email,password)
                elif choice == 4 :
                    a.delete_professor()
                elif choice == 5 :
                    a.view_professors()
                elif choice == 6 :
                    a.view_students()
                elif choice == 7 :
                    return 
            end_time = time.perf_counter()
            print(f"Total time taken to execute is {end_time - start_time}")    
           
if __name__ == "__main__" :
    main()
