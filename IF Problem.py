try:
    gross = float(input("Enter the gross salary: "))
    numchild = int(input("Enter the number of children: "))

    if gross < 1000:
        taxrate = 0.10
    elif gross < 2000:
        taxrate = 0.12
    elif gross < 4000:
        taxrate = 0.14
    else: taxrate = 0.18

    if gross < 2000:
        taxcut = numchild * 0.01
    else:
        taxcut = numchild * 0.005

    effectivetaxrate = float(taxrate - taxcut)

    netsalary = gross * (1 - effectivetaxrate)

    print(f"The next salary is: {netsalary:.2f}")

except ValueError:
    print("Please enter numeric values for gross salary and number of children.")