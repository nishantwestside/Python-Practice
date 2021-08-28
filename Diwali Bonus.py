name=input("Enter the employee's name: ")
gender=input("Enter the employee's gender (M or F): ")
salary=float(input("Enter the salary: "))
if(gender=='M'):
    if(salary<10000):
        bsalary=salary+(salary*0.12)
    else:
        bsalary=salary+(salary*0.10)
elif(gender=='F'):
    if(salary<10000):
        bsalary=salary+(salary*0.07)
    else:
        bsalary=salary+(salary*0.05)
else:
    print("Wrong input")
print("Employee's Name: ",name)
print("Employee's Salary with Diwali bonus: ",bsalary)
