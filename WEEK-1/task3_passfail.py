# Task 3b: User Input + Operators -> Predict Pass/Fail from marks
name = input("Enter student name: ")
marks = float(input("Enter marks (0-100): "))
attendance = float(input("Enter attendance %: "))

PASS_MARK = 40
if marks >= PASS_MARK and attendance >= 75:
    result = "PASS"
elif marks >= PASS_MARK and attendance < 75:
    result = "PASS (but attendance shortage)"
else:
    result = "FAIL"

print(f"\nStudent : {name}")
print(f"Marks   : {marks}")
print(f"Result  : {result}")
