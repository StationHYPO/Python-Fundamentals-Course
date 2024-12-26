#Simple F to C converter.

f_temp = float(input("Enter the temmperature in F: "))
c_temp = float((f_temp - 32) * 5/9)

print(f"{f_temp:.2f} degrees F is {c_temp:.2f} degrees C.")