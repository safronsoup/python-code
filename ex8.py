# when using %r, the quotes are added to what is printed out
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
# when there is an apostrophe in the sentence, then the printed
# sentence gets double quotes.
print formatter % (
  "I had this thing.",
  "That you could type up right.",
  "But it didn't sing.",
  "So I said goodnight."
)

# when using %s, the quotes are not added to what is printed out
formatter = "%s %s %s %s"
print formatter % ("Dog", "Cats", "Jeff's bike", "Bill's garage")
