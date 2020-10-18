# This function checks if the new number already exists in the list
# If not, it is included.
def verification(any_number):
    while any_number in asc_order:
        any_number = float(input('Please, insert a different number.\n'))
    asc_order.append(any_number)


# A list is created with the first entered number
asc_order = [float(input('Insert the first number.\n'))]

# The seco
second_number = float(input('Now, insert the second number.\n'))
verification(second_number)

third_number = float(input('And, finally, insert the third number.\n'))
verification(third_number)

# Sort the list in ascending order
asc_order.sort(reverse=False)

# Shows up the list
print(asc_order)

