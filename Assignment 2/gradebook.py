#Name: Tanay Garg, Date: 31/10/2025, Title: Grade Book Analyzer

print("Lecturers often need a fast and accurate way to compute statistics on student marks. " \
"Instead of manually calculating averages or assigning grades, " \
"this mini project helps automate the entire process via a Python-based GradeBook Analyzer CLI. " \
"The system will read marks from input or a CSV file, perform key statistical analysis, assign grades, "
"and generate summaries in a user-friendly format.\n")

import csv
def calculate_average(marks_dict):
      total=sum(marks_dict.values())
      count=len(marks_dict)
      avg=total/count
      print(f"The average of the marks is:{avg}")

def calculate_median(marks_dict):
        values= sorted(marks_dict.values())
        length=len(values)
        if length%2 !=0:
            print(f"The median of marks is: {values[length//2]}")
        else:    
            mid1= values[length//2-1]
            mid2= values[length//2]
            print(f"The median of the marks are: {(mid1 + mid2)/2}") 

def find_max_score(marks_dict):
     maxnumber=max(marks_dict.values())
     print(f"The maximum marks scored is: {maxnumber}")

def find_min_score(marks_dict):
     minnumber=min(marks_dict.values())
     print(f"The minimum marks scored is: {minnumber}")

while True:     
     print("CHOOSE ONE OF THE FOLLOWING WAY TO ENTER:")
     print("1. Manual Input")
     print("2. CSV")
     print("3. EXIT")

     choice=int(input("Enter the mode from the above to enter(1/2):"))

     if choice==1:
          M={}
          grades={}
          total_students=int(input("Enter the total no. of students for which the data needs to be stored:"))
          for i in range(total_students):
               name=input("Enter the name of the student:")
               marks=int(input("Enter the marks obtained:"))
               M[name]=marks
               if marks>=90:
                    grades[name]="A"
               elif marks>=80 and marks<90:
                    grades[name]="B"
               elif marks>=70 and marks<80:
                    grades[name]="C"
               elif marks>=60 and marks<70:
                    grades[name]="D"
               elif marks<60:
                    grades[name]="F"
               else:
                    print("Enter correct Values!")

          values=list(grades.values())
          print("SUMMARY!")
          print("The number of students with A Grade are:",values.count("A"))
          print("The number of students with B Grade are:",values.count("B"))
          print("The number of students with C Grade are:",values.count("C"))
          print("The number of students with D Grade are:",values.count("D"))
          print("The number of students with F Grade are:",values.count("F"))                                    
          calculate_average(M)
          calculate_median(M)
          find_max_score(M)
          find_min_score(M)
          passed_students  = [name for name, marks in M.items() if marks >= 40]
          failed_students  = [name for name, marks in M.items() if marks < 40]
          print("PASSED STUDENTS!")
          print("Total students Passed:",len(passed_students))
          print("Passed Student's names:",passed_students)
          print("FAILED STUDENTS!")
          print("Total students Failed:",len(failed_students))
          print("Failed student's names:",failed_students)
          
          print("RESULTS TABLE")
          print(f"{"Name":<15}\tMarks\t\tGrade")
          print("----------------------------------------------")
          for name, marks in M.items():
               print(f"{name}\t\t{marks}\t\t{grades[name]}")
     
     elif choice==2:
          M={}
          grades={}
          file_name=input("Enter the name of the csv file to open:")
          f=open(f"{file_name}.csv","r")
          csvreader=csv.reader(f)
          next(csvreader)
          for i in csvreader:
               name=i[0]
               marks=int(i[1])
               M[name]=marks
               if marks>=90:
                    grades[name]="A"
               elif marks>=80 and marks<90:
                    grades[name]="B"
               elif marks>=70 and marks<80:
                    grades[name]="C"
               elif marks>=60 and marks<70:
                    grades[name]="D"
               elif marks<60:
                    grades[name]="F"
               else:
                    print("Enter correct Values!")
          values=list(grades.values())
          print("SUMMARY!")
          print("The number of students with A Grade are:",values.count("A"))
          print("The number of students with B Grade are:",values.count("B"))
          print("The number of students with C Grade are:",values.count("C"))
          print("The number of students with D Grade are:",values.count("D"))
          print("The number of students with F Grade are:",values.count("F"))        
          calculate_average(M)
          calculate_median(M)
          find_max_score(M)
          find_min_score(M)
          passed_students  = [name for name, marks in M.items() if marks >= 40]
          failed_students  = [name for name, marks in M.items() if marks < 40]
          
          print("PASSED STUDENTS!")
          print("Total students Passed:",len(passed_students))
          print("Passed Student's names:",passed_students)
          print("FAILED STUDENTS!")
          print("Total students Failed:",len(failed_students))
          print("Failed student's names:",failed_students)
          
          print("RESULTS TABLE")
          print(f"{"Name":<15}\tMarks\t\tGrade")
          print("----------------------------------------------")
          for name, marks in M.items():
               print(f"{name}\t\t{marks}\t\t{grades[name]}")
     elif choice==3:
          break
     else:
          print("Pls enter proper input!!")