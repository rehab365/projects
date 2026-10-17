import random
Letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
Numbers = "0123456789"
icons = "!@#$%^&*()_+-=~`"
while True:
   n_letters = int(input("Enter the number of letters: "))
   n_numbers = int(input("Enter the number of numbers: "))
   n_icons = int(input("Enter the number of icons: "))
   password = ""
   for i in range(n_letters):
        password += random.choice(Letters)
   for i in range(n_numbers):
        password += random.choice(Numbers)
   for i in range(n_icons):
        password += random.choice(icons)
        password = ''.join(random.sample(password, len(password)))
   print(f"Your password is: {password}") 
   choice = input("Do you want to generate another password? (y/n): ")
   if choice == 'n':
        break       