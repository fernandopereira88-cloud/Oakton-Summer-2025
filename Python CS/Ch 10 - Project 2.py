class Student:
    def __init__(self,name,student_id,dept,program):
        self.__name = name
        self.__id = student_id
        self.__dept = dept
        self.__program = program
        
    #mutators
    def set_name(self,name):
        self.__name = name

    def set_id_number(self,sid):
        self.__id = sid

    def set_department(self,dept):
        self.__dept = dept

    def set_study_program(self,prog):
        self.__program = prog

    #accessors
    def get_name(self):
        return self.__name
    
    def get_id_number(self):
        return self.__id
    
    def get_department(self):
        return self.__dept
    
    def get_study_program(self):
        return self.__program

def make_list():
        students = []

#### 1
        iname = "Lilian Jones"
        istudent_id = "490242"
        idept = "Humanities"
        iprogram = """Bachelor's in English Literature""" 			
        student = Student(iname,istudent_id,idept,iprogram)
        students.append(student)
#### 2
        iname="Frank Stalfrei"
        istudent_id="784921"
        idept="Humanities"
        iprogram="""Master's in North American History"""
        student = Student(iname,istudent_id,idept,iprogram)        
        students.append(student)        
#### 3
        iname="Zheng Morsey"
        istudent_id="012523"
        idept="Physics"
        iprogram="""Bachelor's in Physics"""
        student = Student(iname,istudent_id,idept,iprogram)        
        students.append(student)          
#### 4
        iname="Antonio Moretta"
        istudent_id="472862"
        idept="Computer Science"
        iprogram="""Master's in Distributed Computing"""
        student = Student(iname,istudent_id,idept,iprogram)        
        students.append(student)

        return students
    
def display (slist):
    for i in slist:
             print("Name:",i.get_name())
             print("ID Number:",i.get_id_number())
             print("Department:",i.get_department())
             print("Study Program:",i.get_study_program())
             print()
            
    
def main():

    my_list = make_list()

    display(my_list)
              
    
main()
