#Question 1


print("Question 1\n")
print("Solution the problem of tower of Hanoi with three disks.")
print()
#defining function
def tower(n , source, destination, aux):
    
    if n==1:
        print ("Move disk 1 from",source,"to",destination)
        return
    tower(n-1, source, aux, destination)
    print ("Move disk",n,"from",source,"to",destination)
    tower(n-1, aux, destination, source)

#Using the defined function for 3 disks 
tower(3,"A","C","B")


#Question2


print("Question.2\n")

n = int(input("Enter the number of rows in Pascal's Triangle: "))

#using recursions
print("\nUsing recursions:\n")
def ptriangle(n, originaln=n):
    if n == 0:
        return
    
    ptriangle(n-1,originaln)

    #printing the spaces
    print('  '*(originaln-n), end='')

    #first number is always 1
    entry = 1
    for i in range(1, n+1):

        print(entry, end ='   ')

        #using Binomial Coefficient
        entry = entry * (n - i) // i
    print()
ptriangle(n)

#using loops
print("\nUsing loops:\n")
for line in range(1, n+1):

    #everything else same as recursion
    print('  '*(n - line), end='')

    x = 1
    for i in range(1, line+1):

        print(x, end='   ')

        x = x * (line - i) // i
    print()
print("")



#Question3


print("Question.3\n")
#Taking input from the user
n1=int(input("Enter an Integer:"))
n2=int(input("Enter another Integer:"))
#Making a list of return values
list1=list(divmod(n1,n2))
#Quotient
quo=list1[0]
#Remainder
rem=list1[1]
#printing the quotient and remainder
print(f"\nThe quotient when {n1} is divided by {n2} is {quo}.")
print(f"The remainder when {n1} is divided by {n2} is {rem}.")

#Que3.a
print("\nQue3.a")
c1=callable(divmod(n1,n2))
if c1==True:
    print(f"Function is callable")
if c1==False:
    print(f"Function is Not-callable")
#Que3.b
print("\nQue3.b")
#list of values
listv=[quo,rem]
zero=False
if zero in listv:
    zero=True
    print("All result values are NOT 'non-zero'")
else:
    zero=False
    print("All result values are 'non-zero'")
#Que3.c
print("\nQue3.c")
#new values of list
listr=[quo,rem]
for i in range (4,7):
    listr.append(i)
print(f"Appended (4,5,6) in the values ({quo},{rem})")
listv2=[]
#adding number > 4 from listr to listv2
for i in listr:
    if i>4:
        listv2.append(i)
#a new list listv3 with same elements as listv2 but in string form
listv3=list(map(str,listv2))
#Using join
v=",".join(listv3)
print(f"Values greater than 4 is {v}")
#Que3.d
print("\nQue3.d")
set1=set()

#adding above result in set datatype
for el in listv2:
    set1.add(el)
print("Above result in set form is shown below:")
print(set1)
#Que3.e
print("\nQue3.e")
#Making set1 immutable
frozenset(set1)
print("The above set has been converted to immutable.")
#Que3.f
print("\nQue3.f")
print(f"Max value from set is {max(set1)}")
#using hash function
hash_value=hash(max(set1))
print(f"Hash value of {max(set1)} is {hash_value}")


#Question 4


print("Question.4\n")
#forming a class named student
class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid
    
    def __del__(self):
        print("Object destroyed")

#creating object
student1 = Student("Om Vaish", 21105087)
print("Object created")

#printing the assigned values
print(f"The name of the student it {student1.name} and SID is {student1.sid}.")

#deleting object
del student1


#Question.5


print("Question.5\n")
#forming class employees
class employees:
    #Using constructor to form class objects
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def pfunc(self):
        print(f"Employee Name is {self.name} and Salary is {self.salary} ")
#emp_n name and salaray
emp_1=employees("Mehak",40000)
emp_2=employees("Ashok",50000)
emp_3=employees("Viren",60000)
#print employee detail
emp_1.pfunc()
emp_2.pfunc()
emp_3.pfunc()
#Updating salary of Mehak to 70000
print("\nQue.5a")
emp_1.salary=70000
print("Mehak salary Updated to 70000")
emp_1.pfunc()
#Deleting Viren's data
print("\nQue.5b")
del emp_3
print("Record of employee Viren has been deleted")


#Question 6


print("Question 6\n")

print("WELCOME TO THE FRIENDSHIP GAME")
#definig principle of game i.e. anagram
def anagram(word1,word2):
    #converting all letters to lowercase
    word1=word1.lower()
    word2=word2.lower()
    #form empty list to store letters of words
    l1=[]
    l2=[]
    for i in word1:
        l1.append(i)
    for j in word2:
        l2.append(j)
    #sorting the list alphabetically
    l1.sort()
    l2.sort()
    if l1==l2:
        return True
    else:
        return False

#taking player name input
player1=str(input("Enter Player1 name:"))
player2=str(input("Enter Player2 name:"))
#taking words 
word_player1=str(input(f"Enter Word by {player1}:"))
word_player2=str(input(f"Enter Word by {player2}:"))
#using anagram function
result=anagram(word_player1,word_player2)
#printing the final result
if result==True:
    print(f"\nFriendship of {player1} and {player2} is REAL")
elif result==False:
    print(f"\nFriendship of {player1} and {player2} is FAKE")
