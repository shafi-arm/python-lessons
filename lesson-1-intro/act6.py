# Check if a number is PRIME NUMBER

num = int(input("Enter a number to check"))

if num > 1:

    for i in range(2,num):

        if num % i == 0:

           print(f"{num} is not PRIME NUMBER..")

           break

        else:

           print(f"{num} is PRIME NUMBER")

