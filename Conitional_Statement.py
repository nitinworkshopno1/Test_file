# Q1. Marks Grading System
# marks = int(input("Enter your marks: "))
# if(marks>=90):
#     print("Grade-'A'.")
# elif(marks>=80):
#     print("Grade-'B'.")
# elif(marks>=70):
#     print("Grade-'C'.")
# elif(marks>=33):
#     print("Grade-'D'")
# else:
#     print("Fail.")
                       
# Q2. WAP to check if a number entered by te user is odd or even
# number = int(input("Enter the Number"))
# if(number%2==0):
#     print("Even")
# else:
#     print("Odd")

# Q3. WAP to find the greatest of 3 number entered by the user
num1 = int(input("Enter number 1. ")) 
num2 = int(input("Enter number 2. "))
num3 = int(input("Enter number 3. ")) 

if(num1>num2):
    if(num1<num3):
        print(num3 , " is Greater")
    else:
        print(num1 , " is greater")
elif(num2>num3):
    if(num2<num1):
        print(num1, " is greater")
    else:
        print(num2 ," is Greater")
else:
    print(num3 , " is greater")
        
                                                                                                                                 