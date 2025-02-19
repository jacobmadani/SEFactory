salary=float(input("Please enter your salary: "))
month=input("Please enter the name of the month: ")
print("Please enter the percentages for each:")
savingsper=float(input("Savings(%): "))
rentper=float(input("Rent(%): "))
electricityper=float(input("Electricity(%): "))

savings=salary*(savingsper/100)
rent=salary*(rentper/100)
electricity=salary*(electricityper/100)

print("The ammount allocated to savings is "+str(savings)+"$")
print("The ammount allocated to rent is "+str(rent)+"$")
print("The ammount allocated to electricity is "+str(electricity)+"$")

total=savings+rent+electricity
print("The total amount spent is: "+str(total)+"$")

rem=salary-total
print("The remainder of your salary is: "+str(rem)+"$")

yrent=rent*12
yelectricity=electricity*12
print("Your estimate yearly rent cost is: "+str(yrent)+"$")
print("Your estimate yearly electricity cost is: "+str(yelectricity)+"$")

fun=pow(salary,2)
print("Your total salary for the month raised to the power of 2 is: "+str(fun)+"$")