first = input("Enter First Number :")
operator = input("Enter oprator (+,-,/,*,%) : ")
second = input("Enter Second Number :")

if operator == "+":
    print(int(first) + int(second) )

elif operator == "-":
    print(int(first) - int(second) )

elif operator == "/":
    print(int(first) / int(second) )

elif operator == "*":
    print(int(first) * int(second) )

elif operator == "%":
    print(int(first) % int(second) )

else:
    print("Invalid Opration")
