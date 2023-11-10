# dictionary of a dictionary

cities = {
    'richmond': {
        'state': 'va',
        'country': 'usa',
        'population': 1000000,
        'feature': ' mayflower'
    },
    'sevilla': {
        'state': 'andalusia',
        'country': 'spain',
        'population': 2000000,
        'feature': ' retirement'
    },
}

for city, facts in cities.items():
    print("\nThese are " + city.title() + "'s features: ")
    print("\tState: " + facts['state'].title() +
        "\n\tCountry: " + facts['country'].title() +
        "\n\tPopulation: " + str(facts['population']) +
        "\n\tFeature: " + facts['feature'].title())

print("\n")
