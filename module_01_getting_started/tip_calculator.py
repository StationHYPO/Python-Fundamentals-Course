#Simple tip calculator.

#Get the bill total from the customer.
bill = float(input("Enter the bill total: $"))

#Get the desired tip percentage from the user.
tip_percent = float(input("Enter the tip total in percent: "))
tip = tip_percent / 100

#Calculate the total tip.
tip = bill * tip

#Calculate the total bill.
total = bill + tip

#Display the total tip and total bill.
print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")