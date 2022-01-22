#FIRST QUESTION

print("Problem 1", "\n")
string1 = "Python is a case sensitive language"
print("length of the string =", len(string1))
string1 = string1[::-1]
print("reversed order: ", string1)
string1 = string1[::-1]
new_string = string1[10:26]
print("New string: ", new_string)
string1 = string1.replace("a case sensitive","object oriented")
print("Replaced string: ",string1)
string1 = "Python is a case sensitive language"
print("Index of substring 'a' in the input string is", string1.index("a"))
string1 = string1.replace(" ","")
print("After removing white spaces the string is:" ,string1)


#SECOND QUESTION

print("Problem 2", "\n")
name = "Om"
sid = 21105087
dept_name = "ECE"
CGPA = 9.5
print("Hey, %s Here!\nMy SID is %d\nI am from %s department and my CGPA is %f"%(name,sid,dept_name,CGPA))


#THIRD QUESTION

print("Problem 3", "\n")
a = 56
b = 10
print("a&b :", a&b)
print("a|b :", a|b)
print("a^b :", a^b)
print("Left shift a and b with 2 bits:", a<<2,  b<<2)
print("Right shift a with 2 bits and b with 4 bits:", a>>2, b>>4)


#FOURTH QUESTION

print("Problem 4", "\n")
a = int(input("Enter 1st number :"))
b = int(input("Enter 2nd number :"))
c = int(input("Enter 3rd number :"))

if a>b :
    if a>c:
        print("Greatest number :",a)
    else:
         print("Greatest number :",c)
if b>a:
    if b>c:
        print("Greatest number :",b)
    else:
        print("Greatest number :",c)


#FIFTH QUESTION

print("Problem 5", "\n")
string_1 = input("Enter a string:")
string_1 = string_1.lower()

if "name" in string_1:
    print("Yes")
else:
    print("No")


#SIXTH QUESTION

print("Problem 6", "\n")
side_a = int(input("Length of side A:"))
side_b = int(input("Length of side B:"))
side_c = int(input("Length of side C:"))

if side_a>side_b+side_c or side_b>side_a+side_c or side_c>side_a+side_b:
    print("No")
else:
    print("Yes")
    

    
        


        

        
            
          
    
            
                  
