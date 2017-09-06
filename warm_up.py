# Variables
# Types we know (Integers, Floats, Strings, Boolean)

first_name = "Paul"
last_name = "Paul"
year = 2017
my_bank_account = 100000.00

print("My first name is", first_name)
print("My last name is " + last_name)



# Looping

# for loop
for number in range(15):
    print(number)

for number in range(15):
    my_bank_account = my_bank_account + 100
    print(my_bank_account)

print("Total: ", my_bank_account)

# Conditional Statements

# Functions

my_bank_account = 100
biweekly_salary = 1500
my_bank_account += biweekly_salary
for i in range(24):
    my_bank_account = my_bank_account + biweekly_salary

def payday(checking_amount, biweekly_salary):
    checking_amount = checking_amount + biweekly_salary
    return checking_amount

