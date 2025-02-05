def cal_num(a, b):
 sum = a + b
 diff = a - b
 pro = a * b
 quot = a / b if b != 0 else "Cannot divide by zero"
 return (sum, diff, pro, quot)
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
r = cal_num(n1, n2)
print(f"\nResults:")
print(f"Sum: {r[0]}")
print(f"Difference: {r[1]}")
print(f"Product: {r[2]}")
print(f"Quotient: {r[3]}")
