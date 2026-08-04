basic_sal =int(input("Enter the basic salary : "))

hra = basic_sal * 0.2
da = basic_sal * 0.1

gross = basic_sal + hra + da

print("Gross salary = ", gross)
