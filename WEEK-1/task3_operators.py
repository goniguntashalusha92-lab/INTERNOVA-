# Task 3e: Operators demo
a, b = 15, 4
print("Arithmetic  :", a + b, a - b, a * b, a / b, a // b, a % b, a ** b)
print("Comparison  :", a > b, a < b, a == b, a != b, a >= b, a <= b)
print("Logical     :", (a > 10 and b > 10), (a > 10 or b > 10), not (a > b))
print("Assignment  :", end=" ")
x = 10
x += 5; x -= 3; x *= 2
print(x)
print("Membership  :", 3 in [1, 2, 3], "cat" not in ["dog", "cow"])
