qsold=int(input("Enter the quantity sold: "))
price=float(input("Enter the price of unit item: ""₹"))
discount=float(input("Enter the discount: ""₹"))
tax=float(input("Enter the tax applied in ₹: "))
bill=float(((qsold*price)+tax)-(discount))
print("The total bill amount: ",bill)