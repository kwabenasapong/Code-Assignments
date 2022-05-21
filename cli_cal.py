# Declare operators
add = "+"
sub = "-"
mul = "x"
div = "/"
mod = "%"

#User to select an operation
operation = input("Select an operator, (+ x - / %): ")

#Get 1st input from user
user_input_1 = input("Type 1st number: ")
user_input_1 = float(user_input_1)

#Check user_input_1 number validity
try:
    user_input_1 = float(user_input_1)
except:
    print("Not a number, Try again")

#Get 2nd input from user
user_input_2 = input("Type 2nd number: ")
user_input_2 = float(user_input_2)

#Check user_input_2 number validit
try:
    user_input_2 = float(user_input_2)
except:
    print("Not a number, Try again")

#Perform Operation
if operation == add:
    result = user_input_1 + user_input_2
    user_input_1 = str(user_input_1)
    user_input_2 = str(user_input_2)
    print(user_input_1, add, user_input_2, "=",  result)

elif operation == mul:
    result = user_input_1 * user_input_2
    user_input_1 = str(user_input_1)
    user_input_2 = str(user_input_2)
    print(user_input_1, mul, user_input_2, "=",  result)

elif operation == sub:
    result = user_input_1 - user_input_2
    user_input_1 = str(user_input_1)
    user_input_2 = str(user_input_2)
    print(user_input_1, sub, user_input_2, "=",  result)

elif operation == div:
    result = user_input_1 / user_input_2
    user_input_1 = str(user_input_1)
    user_input_2 = str(user_input_2)
    print(user_input_1, div, user_input_2, "=",  result)

elif operation == mod:
    result = user_input_1 % user_input_2
    user_input_1 = str(user_input_1)
    user_input_2 = str(user_input_2)
    print(user_input_1, mod, user_input_2, "=",  result)

#Ask if user wants to perform another operation
print("Do you want to perform another operation?")

more_oper = input("Type y for yes and n for no: ")

if more_oper == "y":
    print("let's start the process, rerun the program from your terminal")
    #repeat from step 1

else:
    print("Thanks for using Koby's Calculator, Bye")
