import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
letters = lower + upper
symbols = "~`!@#$%:^&*()_-+={[}]|\;<,>.?/>"
numbers = "1234567890"
password = ""

print("Choose Character Types from below:")
print(" 1. Letters & Numbers \n 2. Letters & Symbols \n 3. Letters, Numbers & Symbols")

while True:
    charset = int(input("Enter your choice:"))
    
    if charset == 1:
        all_chars = letters + numbers
        break
    elif charset == 2:
        all_chars = letters + symbols
        break
    elif charset == 3:
        all_chars = letters + numbers + symbols
        break
    else:
        print("Enter a valid choice.....")

length = int(input("Enter length:"))

for i in range(length):
    password += random.choice(all_chars)

print("Your password is:", password) 
