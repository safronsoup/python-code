# favorite languages using list in a dictionary
print("\n")

favorite_languages = {
    'jen':['ruby',], 'jeff':['python', 'perl'],
    'craig':['c', 'c##'], 'billy':['fortran', 'pascal'],
    'geek':['assembly', 'os2', 'bash'],
    }

# for each name (key) and the value associate with the each key (a list
# of languages)
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite programming language is: ")
    else:
        print("\n" + name.title() + "'s favorite programming languages are: ")
# for each language in each languages list
    for language in languages:
        print("\t" + language.title())

print("\n")
