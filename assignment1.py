salary=float(input("Please enter your salary: "))
month=input("Please enter the name of the month: ")
print("Please enter the percentages for each:")
savingsper=float(input("Savings(%): "))
rentper=float(input("Rent(%): "))
electricityper=float(input("Electricity(%): "))
def salary_calculator(salary,savingsper,rentper,electricityper,value):
    rent=salary*(rentper/100)
    electricity=salary*(electricityper/100)
    salary+=value
    savings=salary*(savingsper/100)
    print("\n")
    print("The ammount allocated to savings is "+str(savings)+"$")
    print("The ammount allocated to rent is "+str(rent)+"$")
    print("The ammount allocated to electricity is "+str(electricity)+"$")
    print("\n")

    total=savings+rent+electricity
    print("The total amount spent is: "+str(total)+"$")

    rem=salary-total
    print("The remainder of your salary is: "+str(rem)+"$")
    print("\n")

    yrent=rent*12
    yelectricity=electricity*12
    print("Your estimate yearly rent cost is: "+str(yrent)+"$")
    print("Your estimate yearly electricity cost is: "+str(yelectricity)+"$")
    print("\n")

    fun=pow(salary,2)
    print("Your total salary for the month raised to the power of 2 is: "+str(fun)+"$")
msg="Here is your finances for "+str(month)
print(msg.center(50)) 
salary_calculator(salary,savingsper,rentper,electricityper,0) 
print("\n")
random=input("Would you like to add additional amount?(yes/no): ")
if random=="yes":
      value=float(input("How much additional amount would u like to add?"))
      print("The amounts allocated after adding the new value will be as follow: ")
      salary_calculator(salary,savingsper,rentper,electricityper,value) 
else:
    print("See you again!")

