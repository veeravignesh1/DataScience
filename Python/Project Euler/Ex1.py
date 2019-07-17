'''If we list all the natural numbers below 10 that are 
multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.'''

# List all natural numbers below 1000
# range(0,1001,1)
total_list = []
sumoflist = 0
for num in range(1, 1000):
    if (num % 3 == 0) or (num % 5 == 0):
        total_list.append(num)

print(total_list)

for ele in range(0, len(total_list)):
    sumoflist = sumoflist + total_list[ele]

print(sumoflist)
