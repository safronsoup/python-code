x = 10
y = 15
z = 10.0

# greater than
print( x > y )
print( y > x )

# less than
print( x < y )
print( y < x )

# equal values
print( x ==y )

# not equal
print( x != y )

# greater than or equal to
print( x >= y )

# less than or equal to
print( x <= y )

if (x > y):
    print("x is bigger than y.")
else:
    print("x is smaller than y.")

# compare integer and float - is 10.0 = to 10?
print ( z == x )

# OR table
# true | false | result
#----------------------
#   0      0       0
#   0      1       1
#   1      0       1
#   1      1       1

# AND table
# true | false | result
#----------------------
#   0      0       0
#   0      1       0
#   1      0       0
#   1      1       1

print( 10 >=15 or True)
print( 10 >=15 and True)