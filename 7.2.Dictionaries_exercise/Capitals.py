countries = input().split(", ")
capitals = input().split(", ")
countries_with_capitals = dict(zip(countries, capitals))

for country, capital in countries_with_capitals.items():
    print(f"{country} -> {capital}")
