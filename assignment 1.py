# 1st program

print("Program 1 " ,"\n")
num1 =int(input("enter 1st number "))
num2 =int(input("enter 2nd number "))
num3 =int(input("enter 3rd number "))
Sum = num1+num2+num3
avg = Sum/3
print("Sum of given nos is ", Sum)
print("Average is ", avg , "\n")



# 2nd program

print("Program 2" ,"\n")
print(" All values are to be entered in dollars.")
gross_income =float(input("enter your gross income "))
dependents =int(input("enter no of dependents "))
tax_rate = 0.2
standard_deduction = 10000
dependent_deduction = 3000
taxable_income =(gross_income - standard_deduction - (dependent_deduction*dependents))
tax = taxable_income*tax_rate
print(" The tax is ", tax,"\n")



# 3rd program

print("Program 3 ", "\n")
print("Student = [sid, name, gender, course, cgpa]")
sid = int(input("enter your SID "))
name = input("enter your name ")
gender = input("enter your gender 'M', 'F', 'U' for male, female and unknown respectively")
course = input("enter your course name ")
cgpa = float(input("enter your cgpa "))
student = [sid, name, gender, course, cgpa]
print("Student info ", student, "\n")



# 4th program

print("Program 4 " ,"\n")
#taking input from user
a = int(input("enter marks of student 1 "))
b = int(input("enter marks of student 2 "))
c = int(input("enter marks of student 3 "))
d = int(input("enter marks of student 4 "))
e = int(input("enter marks of student 5 "))
#converting input data to list
marks = [a,b,c,d,e]
print("Marks of five students are ", marks)
#sorting in ascending and descending order
asc = marks.sort()
print("marks in ascending order ", marks)
desc = marks.sort(reverse = True)
print("marks in descending order ", marks, "\n")



# 5th program

print("Program 5 " ,"\n")
color = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
print("The provided list is ", color, "\n")
#removing the 4th term
color.pop(3)
print("The modified list is = ", color)

#replacing Black and Pink with Purple
color2 = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
color2[3:5] = ["Purple"]
print("The modified list is = ", color2)








