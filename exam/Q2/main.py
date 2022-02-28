class StudentInfo:
    # constructor
    def __init__(self,nameInfo: str, personalID: int,  departInfo: str, jobInfo: str):
        self.nameInfo = nameInfo
        self.personalID = personalID
        self.departInfo = departInfo
        self.jobInfo = jobInfo
    
    # getters | accessors 
    def get_nameInfo(self):
        return self.nameInfo   
    
    def get_personalID(self):
        return self.personalID   
    
    def get_departInfo(self):
        return self.departInfo   
    
    def get_jobInfo(self):
        return self.jobInfo   
    
    # setters | mutators
    def set_nameInfo(self, nameInfo):
        self.nameInfo = nameInfo
        
    def set_personalID(self, personalID):
        self.personalID = personalID

    def set_departInfo(self,departInfo):
        self.departInfo = departInfo

    def set_jobInfo(self, jobInfo):
        self.jobInfo = jobInfo
        
    # default function called when object is printed
    def __str__(self) -> str:
        return f'''
        Person
        ----------------------------------
        Name:       {self.nameInfo}
        IUKLID:     {self.personalID}
        Department: {self.departInfo}
        Job:        {self.jobInfo}
                 '''

# creating three objects to represent three students 
# student1 = StudentInfo("Arjan", 1000,"Computer Science", "Web development")
# student2 = StudentInfo("Amit", 1001,"Account", "Student")
# student3 = StudentInfo("Aakanshya", 1002,"Law", "Lawyer")

# displaying student info
# print(student1)
# print(student2)
# print(student3)

# second part of the question to store student objects in a list and perform crud operations
import json

class Student_crud:
    student_dict= {}
    
    def add_student(self,student: StudentInfo):
        id = student.get_personalID()
        self.student_dict[id] = student

    def search_student(self, studentID)-> StudentInfo: 
        try:
            return self.student_dict[studentID] 
        except:    
            print(f"---student {studentID} not found---")
            return None
            
    def update_student(self, studentID, nameInfo: str,  departInfo: str, jobInfo: str):
        student =  self.search_student(studentID=studentID)
        student.set_nameInfo(nameInfo)
        student.set_departInfo(departInfo)
        student.set_jobInfo(jobInfo)
        
        # saving the student data
        self.add_student(student)
        return student
        
    def delete_student(self, studentID):
        del self.student_dict[studentID]
        
    def save_to_file(self):
        json_dict =  {}
        for x , y in self.student_dict.items():
            json_dict[x] = json.dumps(y.__dict__)
            
        json_data = json.dumps(json_dict)
        with open("dict.data.json","w") as f:
            # write json data to file
            f.write(json_data)
            
        
    # reading data from a file during initialization
    def __init__(self): 
        try:
            f= open("dict.data.json","r")
            data = json.load(f)
            # loading data and initializing the values
            for x in data:
                # self.add_student(StudentInfo())
                record = json.loads(data[x]) 
                self.add_student(StudentInfo(
                        record["nameInfo"],
                        record["personalID"],
                        record["departInfo"],
                        record["jobInfo"] )
                    )
        except: 
            print("---file not found---")
        finally: 
            f.close()

            

        
# initializing the records 
# student_records = Student_crud()
# # adding student to the dictionary 
# student_records.add_student(student1)
# student_records.add_student(student2)
# student_records.add_student(student3)

# searching for student
# print(student_records.search_student(1001))
# print(student_records.search_student(1002))


# # updating student info
# print(student_records.update_student(1001, "Rjan", "Computer","Software Developer"))

# # deleting student 
# student_records.delete_student(1000)
# # trying to access the deleted student
# student_records.search_student(1000)

# # saving data to file in json format 


# code for menu creation 
student_records = Student_crud()

while(True):
    choice = input("Enter a for add, s for search, d for delete and u for update, e for exit: ")[0]
    
    if choice == 'a':
        nameInfo = input(" Enter student name: ") 
        personalID = int(input(" Enter student IUKLID: "))
        departInfo = input(" Enter student department: ")
        jobInfo = input(" Enter student job info: ")
        
        student = StudentInfo(nameInfo, personalID, departInfo, jobInfo)
        student_records.add_student(student)
    elif choice == 's':
        personalID = int(input(" Enter student IUKLID: "))
        print(f'The student is \n{student_records.search_student(personalID)}')
    elif choice == 'u':
        print("Enter the data to update")
        nameInfo = input(" Enter student name: ") 
        personalID = int(input(" Enter student IUKLID: "))
        departInfo = input(" Enter student department: ")
        jobInfo = input(" Enter student job info: ")
        
        print(f'updated student: \n {student_records.update_student(personalID,nameInfo,departInfo,jobInfo)}')
        
    elif choice == 'd':
        personalID = int(input(" Enter student IUKLID to delete: "))
        student_records.delete_student(personalID)
        
    elif choice == 'e':
        student_records.save_to_file()
        
        break
                     
    
        

        
            

