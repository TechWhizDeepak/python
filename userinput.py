calculation_to_units = 24
name_of_units = "hours"

def days_to_units(number_of_days):
    print (number_of_days > 0)
    if number_of_days > 0:
        return f"{number_of_days} days are {number_of_days * calculation_to_units } {name_of_units}"
    else:
        return "You should enter Number only"

user_input = input("Hi, Please enter a number of days and I will convert it to hours!\n")
user_input_number = int(user_input)
calculated_values = days_to_units(user_input_number)
print(calculated_values)