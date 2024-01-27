# Variable var is string text "Please enter a value ", concatenated with a string value of "23"
# "23" is an integer but converted into a string using string function
# var = input("please enter a value: " + str(23))

# "var" is a variable, assigned to the string text "please enter a value"
# input function allows for user to put their own value in the console, and the code will remember the value they had input as "var"
var = input("Please enter a value: ")

# 3a) print value of var as UPPER CASE:
# capitalize function to change first character of users' input, concatenated with the string "Your value is " as the response
value = var.upper()
print("Your value is " + value)

# 3b) print the number of characters in var
print("The number of characters in your value is", len(value))

# 3c) Does it contain numeric characters?
print("Does your value contain numeric characters?")
isNumeric1 = var.isdecimal()
print(isNumeric1)

# ---------------------------------------
# Q = best/easiest way to flag if your alphanumerical string (combo of text and numbers) contain numbers?
# isdecimal only works when string is either text or numbers, not combined. isdigit doesn't work with alphabet characters only

# isalpha method checks if all characters are in the alphabet. TRUE = Yes, all characters from alphabet, FALSE = No, there are numeric characters
# isNumeric2 = var.isalpha()
# # if/else condition:
# if isNumeric2 is True:
#     print("Your value does NOT contain numbers")
# else:
#     print("Your value DOES contain numbers")

# isdigit method checks if all characters are digits. TRUE = Yes, all characters digits, FALSE = No, there are alphabet characters
# isNumeric2 = var.isdigit()
# # if/else condition:
# if isNumeric2 is True:
#     print("Your value DOES contain numbers")
# else:
#     print("Your value does NOT contain numbers")
