# Arithmetic
a = 10
b = 3

print(a + b)   # Addition → 13
print(a - b)   # Subtraction → 7
print(a * b)   # Multiplication → 30
print(a / b)   # Division → 3.333...
print(a // b)  # Floor Division → 3 (no decimals)
print(a % b)   # Modulus → remainder → 1
print(a ** b)  # Exponent → 10^3 = 1000

# Why this way?

# / always gives decimals; // gives integers.

# % is great for checking divisibility (e.g., x % 2 == 0 means even).




# **********************************************      Comparison Operators   ********************************************

x = 5
y = 7

print(x == y)  # Equal → False
print(x != y)  # Not equal → True
print(x > y)   # Greater than → False
print(x < y)   # Less than → True
print(x >= y)  # Greater or equal → False
print(x <= y)  # Less or equal → True


# Why this way?

# These return True or False, often used in conditions.




# **********************************************  3️⃣ Logical Operators   **********************************************

# a = True
# b = False

# print(a and b)  # Both must be True → False
# print(a or b)   # At least one True → True
# print(not a)    # Opposite → False


# Why this way?

# and is stricter, or is more relaxed.

# not flips the truth value.




# **********************************************  3️4️⃣ Assignment Operators   **********************************************



x = 10
x += 5   # same as x = x + 5 → 15
x -= 3   # same as x = x - 3 → 12
x *= 2   # same as x = x * 2 → 24
x /= 4   # same as x = x / 4 → 6.0
print(x)
