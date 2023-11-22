"""Designing a simple calculator with basic arithmetic operations 
which Prompts the user to input two numbers and an operation choice.
Perform the calculation and display the result."""
print("Enter two numbers to perform arithemetic operations on them.")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("1 - Addition\n2 - Difference\n3 - Multiplication\n4 - Division\n5 - Modulus\n6 - Exponentiation\n")
choice=int(input("Enter the number for operation choice : "))
if(choice==1):
      print("The Addition of %d and %d is %d\n%d + %d = %d"%(num1,num2,num1+num2,num1,num2,num1+num2))
elif(choice==2):
      if(num1>num2):
            print("The Difference of %d and %d is %d\n%d - %d = %d"%(num1,num2,num1-num2,num1,num2,num1-num2))
      else:
            print("The Difference of %d and %d is %d\n%d - %d = %d"%(num1,num2,num2-num1,num2,num1,num2-num1))
elif(choice==3):
      print("The Multiplication of %d and %d is %d\n%d * %d = %d"%(num1,num2,num1*num2,num1,num2,num1*num2))
elif(choice==4):
      print("The Division of %d and %d is %d\n%d / %d = %d"%(num1,num2,num1/num2,num1,num2,num1/num2))
elif(choice==5):
      print("The Modulus of %d and %d is %d\n%d %% %d = %d"%(num1,num2,num1%num2,num1,num2,num1%num2))
elif(choice==6):
      print("The Exponentiation of %d to the %d is %d\n%d ** %d = %d"%(num1,num2,num1**num2,num1,num2,num1**
      num2))
else:
      print("PLEASE ENTER VALID OPERATION CHOICE!!!")
      