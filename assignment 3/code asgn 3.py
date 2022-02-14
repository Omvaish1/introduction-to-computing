#Question 1

print("Question 1")
#taking input from user
string_input= input("Enter a string- ")
string_input=string_input.lower().strip()
i=0
#defining empty dictionary to use later to store element, and its occurence
dict={}

#checking if the string input is a word or a sentence
if " " not in string_input:
     
     while i<len(string_input):
          occurence=0
          k=0
          while k<len(string_input):
               if string_input[i]==string_input[k]:
                    occurence=occurence+1
                    k=k+1
               else:
                    k=k+1
          
          dict.update({string_input[i]:occurence})
          i=i+1

else:
     #making a list of words using split method
     list = str.split(string_input)
    
     while i<len(list):
          occurence=0
          k=0
          while k<len(list):
               if list[i]==list[k]:
                    occurence=occurence+1
                    k=k+1
               else:
                    k=k+1
                   
          dict.update({list[i]:occurence})
          i=i+1
#Printing the final result
print("Total occurances")
print(dict)


#Question 2

print("Question 2")
#Taking input from user
day=int(input('enter the Day- '))
month=int(input('enter the Month- '))
year=int(input('enter the Year- '))


#Removing all the invalid cases
if day>30 and month in {2,4,6,9,11}:
    condition=False
elif day>31 and month in {1,3,5,7,8,10,12}:
    condition=False
elif (day==29 or day==30) and month==2 and year%4!=0:
    condition=False
elif day==30 and month==2 and year%4==0:
    condition=False
else:
    condition=True
if month>12:
    condition=False


#After checking the condition, following if-else statement is executed
if condition:
    #changing for new year
    if day==31 and month==12:
        year1=year+1
    else:
        year1=year
    if month==12 and day==31:
        month1=1
    else:
        month1=month


    #for months with 31 days
    if month in {1,3,5,7,8,10,12}:
        if day==31:
            day1=1
            if month!=12:
                month1=month+1
            else:
                month1=1
        else:
            next_day=day+1
    #for the month of february
    elif month==2:
        if year%4==0:
            if day==29:
                day1=1
                month1=3
            else:
                day1=day+1
        else:
            if day==28:
                day1=1
                month1=3
            else:
                day1=day+1

    #for months with 30 days
    else:
        if day==30:
            day1=1
            month1=month+1
        else:
            day1=day+1
    #printing the calculations
    print("Next Date is: ",day1, month1, year1)

else:
    #gives a warning and ends the program
    print("Entered date is noy valid")


#Question 3
print("Question 3")
# defining an empty list
list1 = []

# taking input from user
list1=eval(input("Enter the list:"))
list2=[]
for i in list1:
    list2.append((i, i**2))
print("Output:",list2)


#Question 4

grade_score=int(input("Enter grade score:"))
#Forming a dictionary of statements
dict1={10:"Your grade is 'A+' and Outstanding performance.",
     9:"Your grade is 'A' and Excellent performance.",
     8:"Your grade is 'B+' and Very Good performance.",
     7:"Your grade is 'B' and Good performance.",
     6:"Your grade is 'C+' and Average performance.",
     5:"Your grade is 'C' and Below Average performance.",
     4:"Your grade is 'D' and Poor performance."}
#Applying Conditions for correct grade range
if 4<=grade_score<=10:
    #Taking required statement from dictionary
    result=dict1.get(grade_score)
    #printing final result
    print(result)
else:
    #printing error message when grade is out of range
    print("ERROR!")



#Question 5
print('Question 5')

print("The pattern is printed below:\n")
# Letters to be printed
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
# Applying while loop to print only required rows
i = 1
while i <= 6:
    # printing 1st row intially when i=1
    for j in letters:
        print(j , end="")
    # forming second row elements to be printed
    letters.pop()  # removing last element of list
    letters.pop()  # removing last element of list
    letters.insert(0, " ")  # insertind space
    print()  # changing line using print()
    i = i + 1
 


#Question 6

print("Question 6")
#By default 1st run
repeat="Y"
#Intially empty dictionary
dic={}
dic2={}
#List containing Y or N
list1=["Y","y","n","N"]

while repeat=="Y" or repeat=="y":
    #Taking input name and sid
    name = str(input("Enter student name:"))
    sid = int(input("Enter student SID:"))
    if sid<0:
        print("\nError\nSID can't be negative\n")
    else:
        # Updating dic with 'sid':'name'
        dic.update({sid: name})
        # updating dic 2 with 'name':'sid'
        dic2.update({name:sid})
        # Asking if want to enter more input or not
        repeat = str(input("Enter Y to continue or N to end:"))
    if repeat=="N" or repeat=="n":
        break
    elif repeat not in list1:
        print("\nError\nPlease enter valid input['Y' or 'N']")
        repeat=str(input("\nEnter Y to continue or N to end:"))

# a
#printing the dictionary

print("The Dictionary containing {'SID':'Name'} is shown below")
print(dic)
# b
#sorting according to name

list2=sorted(dic2)
dic3={}
for i in list2:
    dic3.update({dic2.get(i):i})
print("The Dictionary after sorting according to name:")
print(dic3)

# c
#sorting according to SID

sort_dic = sorted(dic)
dic4 = {}
for j in sort_dic:
    dic4.update({j: dic.get(j)})
print("The Dictionary after sorting according to SID:")
print(dic4)
# d
# Taking input SID to be searched

enter_sid = int(input("Enter SID to get name of student:"))
# Searching for sid as key in dic
output_name = str(dic.get(enter_sid))
# printing name with key sid
print("Name of student with SID ",enter_sid ," is" , output_name)




#Question 7

print("Question 7")
terms=int(input("Total elements of Fibonacci sequence that you want- "))

a1=1
a2=0
n=0

sum=a1+a2

print("Fibonnaci sequence with " , terms, " terms")
print(a1)    #printing the first term
#Printing the rest of the fibonnaci terms
while n<terms-1:
    an=a2+a1
    a2=a1
    a1=an
    print(an)
    n=n+1
    sum+=an
average=sum/terms
#printing the program end prompt
print("Average of total ", terms ," terms of sequence is", average)




#Question 8

print("Question 8")
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

print("Part a")
set_A=Set1^Set2
print("set with elements not common in both is", set_A)

print("Part b")
set_B=Set1^Set2^Set3
print("Set of elements that is only present in one set is", set_B)

print("Part C")
set_C=(Set1|Set2|Set3)- (Set1^Set2^Set3)-(Set1&Set2&Set3)
print("Set of elements that is only present in two set is", set_C)

print("Part d")
set4=set()
for n in range(1,11) :
    set4.add(n)
set5=set4- Set1
print("set of all integers in the range 1 to 10 that are not in Set1", set5)

print("Part e")
set6=set()
for  n in range(1,11) :
    set6.add(n)
set7=set6 - (Set1|Set2|Set3)
print("set of all integers in the range 1 to 10 that are not in Set1 and Set2 and Set3 ", set7)
