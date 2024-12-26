#A simple calculator which will convert F to C.

f_temp = float(input("Enter the temperature in F: "))

#Convert F to C.
c_temp = (f_temp - 32) * 5/9

#Output the new temp to the user.
print(f"{f_temp:.2f} degrees Farenheit is {c_temp:.2f} degrees Celcius.")
