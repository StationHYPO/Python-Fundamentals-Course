#Tip calculator.

#Get the bill total from the user.
bill_total = float(input("Enter the bill total: $"))

#Get the desired tip in %.
tip_pct = float(input("Enter the desired tip in %: "))

#Convert tip to decimal and get total tip amount.
tip = (tip_pct / 100) * bill_total
total = bill_total + tip

#Report the information to the user.
print(f"If you bill is ${bill_total:.2f} and you would like to leave a {tip_pct:.2f}% tip, then you should leave a ${tip:.2f} tip and the grand total will be ${total:.2f}.")