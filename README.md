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
      

import random
print('*'*50)
print()
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
	+ "Rock vs Paper : Paper wins \n"
	+ "Rock vs Scissors : Rock wins \n"
	+ "Paper vs Scissors : Scissor wins")
print()
print('*'*50)

while True:
	print("Enter your choice \n 1 : Rock \n 2 : Paper \n 3 : Scissors \n")
	
	choice=int(input("Enter your choice :"))
	print('*'*25)
	while choice > 3 or choice <1:
	    choice=int(input('Enter a valid choice please '))
		
	if choice == 1:
		choice_name= 'Rock'
	elif choice == 2:
		choice_name= 'Paper'
	else:
		choice_name= 'Scissors'
		
	
	print('User choice is : \n',choice_name)
	print('Now its Computers Turn....')

	comp_choice = random.randint(1,3)

	while comp_choice == choice:
		comp_choice = random.randint(1,3)
	
	if comp_choice == 1:
		comp_choice_name = 'rock'
	elif comp_choice == 2:
		comp_choice_name = 'paper'
	else:
		comp_choice_name = 'scissor'
	print('*'*30)
	print("Computer choice is : \n", comp_choice_name)
	print('*'*30)
	print(choice_name,'Vs',comp_choice_name)

	if choice == comp_choice:
		print('<= Its a TIE =>\n',end="")
		result="DRAW"
	
	if (choice==1 and comp_choice==2):
		print('<= paper wins =>\n',end="")
		result='papeR'
	elif (choice==2 and comp_choice==1):
		print('<= paper wins =>\n',end="")
		result='Paper'
		
	
	if (choice==1 and comp_choice==3):
		print('<= Rock wins =>\n',end= "")
		result='Rock'
	elif (choice==3 and comp_choice==1):
		print('<= Rock wins =>\n',end= "")
		result='rocK'
		
	if (choice==2 and comp_choice==3):
		print('<= Scissors wins =>\n',end="")
		result='scissoR'
	elif (choice==3 and comp_choice==2):
		print('<= Scissors wins =>\n',end="")
		result='Rock'

	if result == 'DRAW':
		print("TIE")
	if result == choice_name:
		print("USER WINS")
	else:
		print("COMPUTER WINS")
	print('*'*30)
	print('Do you want to play again? ( Type "Y" for YES / Type "N" for NO) : ')

	ans = input()
	ans=ans.lower()
	if ans =='n':
		break
print('*********************************************************************')
print('*********************************************************************')
print("Thanks for playing\n !!!Have a Good day!!!")
