expenses = [10.50, 8, 5, 15, 20, 5, 3]
sum = 0

for x in expenses:
    sum = sum + x
# total = sum(expenses) is a way to do it without for loop

print("you spent $", sum, " on lunch this week", sep='')