# Python Foundations
# 06 - For Loops
# Purpose: Demonstrate iteration, ranges, accumulation,
#          filtering, and nested loops.

print("=== Number Analysis ===")

total = 0
even_numbers = []
odd_numbers = []

for number in range(1, 11):
    total += number

    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Numbers: 1-10")
print("Total:", total)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)


print("\n=== Multiplication Table ===")

number = int(input("Enter a number: "))

for multiplier in range(1, 11):
    result = number * multiplier
    print(f"{number} × {multiplier} = {result}")


print("\n=== Pattern ===")

for row in range(1, 6):
    print("*" * row)
