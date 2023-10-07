class student:
def__init__(self,name,roll_number,cgpa):
  self.name = Name
  self.roll_number = roll_number
  self.cgpa = cgpa
def sort_students(student_list):
  #Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_List,
     key=lambda student: student .cgpa
     reverse=True)
  #Syntax _ lambda arg:exp
   return sorted_students
  #example usage:
  
  students = [
      Student("Sara","A123",7.8),
      Student("Ani","A124",8.9),
      Student("Saranya","A125",9.1),
      Student("Raja","A126",9.9),
  ]
  sorted_students = sort_students(students)
  #Print the sorted list of students 
  for student in sorted_students:
    print("Name:{}, Roll number:{},CPGA:{}".format(student.name,
                                                  student.roll_number,
                                                   student.cgpa))
    
                                                   