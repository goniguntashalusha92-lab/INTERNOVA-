# Task 3d: Age eligibility checker (e.g. for an AI-based voting/ID system)
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote and to get a driving licence.")
elif age >= 16:
    print("Not eligible to vote, but eligible for a learner's licence (2-wheeler, no gear).")
else:
    print("Not eligible yet. Years remaining to be 18:", 18 - age)
