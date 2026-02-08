age = int(input("Enter age: "))

if age<5:
  print("Ticket Is Free")
elif age>=5 and age<=17:
  print("Ticket price is 5 Pounds")
elif age>=18 and age<=59:
  print("Ticket price is 10 Pounds")
elif age>=60:
  print("Ticket price is 6 Pounds")
else:
  print("Invalid age")