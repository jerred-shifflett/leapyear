#Jerred Shifflett
#homework one
#Program checks user integer input- then display if that year is aleap year of not.




def isItLeapYear(year):
	if(year%4)==0:
		if(year%100)==0:
			if(year%400)==0:
				print(f"{year} : Is a leap year.\n")
			else:
				print(f"{year} : Is a not leap year.\n")
		else:
			#it is not divisable by 100
			print(f"{year} : Is a not leap year.\n")
	else:
		#it is not divisable by 4
		print(f"{year} : Is a not leap year.\n")


def main():
	exit = 0
	try:
		while exit !=1:
			
			userChoice = int(input("Enter 0 to enter a year to check and see if a year is leap year\nOr Enter 1 to exit\n"))
			if userChoice ==1:
				print("Goodbye.\n")
				exit =1
			elif userChoice ==0:
				year =int(input("Enter the year and I will display wether or not it is a leap year or not.\n"))
				isItLeapYear(year)
			else:
				print("Enter the right input")
	except(ValueError):
		print("You did not listen. Put in the right input please.\n Now re-run the Program")
main()




