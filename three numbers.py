p = int(input("Enter a number: "))
q = int(input("Enter a number: "))
r = int(input("Enter a number: "))
if p>q and p>r:
  print("P is largest")
elif q>r and q>p:
  print("Q is largest")
else:
  print("R is largest")