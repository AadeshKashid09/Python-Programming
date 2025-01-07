# Check it multiple of number or not

number=int(input("Enter a Number"))
checkNum=int(input("Enter he number you want to check"))

if(number%7==0):
    print("The\t",number,"is  Multiple of\t",checkNum)
else:
    print("The\t",number,"\t is not multiple of\t",checkNum)