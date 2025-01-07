#Greatest of 3 Number

num1=float(input("Enter a first number"))
num2=float(input("Enter a Second number"))
num3=float(input("Enter a Third number"))

if(num1>num2 and num1>num3):
    print("Number \t",num1,"\t is Greater than other Two")
elif(num2>num1 and num2>num3):
    print("Number \t",num2," \t is greater than other Two")
else:
    print("Number \t",num3,"\t is greaterthan other Two")


