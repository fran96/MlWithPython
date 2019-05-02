# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Fransciso',
    'OR': 'Buq',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY state has: ", cities['NY'])

#dict
print("Michigan has: ", cities[states['California']])

# print every state abbreviation
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city")

# print now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry no texas")

# get a city with a defualt value
city = cities.get('TXT', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")
