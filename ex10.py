tabby_cat = "\tIm'm tabbed in." # \t inserts a tab
persian_cat = "I'm split\non a line." # \n inserts a new line
backslash_cat = "I'm \\ a \\ cat." # escape a back slash
how_tall = "I am 6'2\" tall." # escape double-quote inside string
this_tall = 'I am 6\'2" tall.' # escape single-quote inside string
beep_beep_beep = "beep\a beep\a beep\a" # \a adds a beep

# \v adds a vertical tab (a new line)
fat_cat = """
I'll do a list:
\v\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print how_tall
print this_tall
print beep_beep_beep

# this while loop makes a '|' spin
#while True:
#    for i in ["/","-","|","\\","|"]:
#        print "%s\r" % i,
