num = int(input("Enter a number: "))

last_digit = num % 10

if last_digit == 4:
    print("Yes, the last digit is 4.")
else:
    print("No, the last digit is not 4.")