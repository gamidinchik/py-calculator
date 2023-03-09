age = int(input("How old are you? "))
if age >= 25:
    print("You are allowed to enter")
elif age >= 18 and (age < 25):
    print("You are allowed to enter with your parents")
else:
    print("You are denied entry")
