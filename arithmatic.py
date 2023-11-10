
# this equals 8
add1 = 3 + 5
add2 = 5 + 3

# this equals 14
sub1 = 20 - 6

# this equals -14
sub2 = 6 - 20
print(sub2)

# this equals 35
mult1 = 7  * 5
mult2 = 5 * 7

# this equals 0.2
div1 = 20 / 100
print(div1, type(div1))

# equals 125
exp1 = 5 ** 3
print(exp1)

# floor division - double division sign; scrape of any integer remainder that is associated
# with division
floor = 101 // 25
print(floor)

# modular math is opposit of floor division; shows the remainder
mod1 = 8 % 3
print(mod1)

# arithmetic order of operations
# please excuse my dear aunt sally
# parentheses, exponent, multiplication/division, addition, subtraction
result1 = (3 + 7) * 15 / 22
print(result1)

result2 = 3 + 7 * 15 / 22
print(result2)

# priority of implicit conversion/casting; when performing math of different types
# e.g.: the answer of an integer multiplied bya float is a float
# division will always result in a float
# lowest to highest
# bool, integer, float, complex

# boolean - True = 1; False = 0
# when True is converted to an integer, it becomes 1, False becomes 0
# when True is converted to a float, it becomes 1.0, False becomes 0.0
# when True is converted to a complex number, it becomes 1j, False becomes 0j
