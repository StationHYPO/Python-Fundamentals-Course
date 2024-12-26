#Calculate the curcumeference and area of a circle using only the radius as an input.

# Get the radius of the circle from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the circumference of the circle
circumference = 2 * 3.14159 * radius

# Calculate the area of the circle
area = 3.14159 * radius ** 2

# Display the circumference and area of the circle, rounded to 2 decimal places.
print(f"The circumference of the circle is: {round(circumference, 2)}")
print(f"The area of the circle is: {round(area, 2)}")