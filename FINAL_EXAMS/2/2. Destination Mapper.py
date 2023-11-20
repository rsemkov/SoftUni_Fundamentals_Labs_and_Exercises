import re
pattern = r"([=\/])([A-Z][A-Za-z]{2,})\1"
data_input = input()
matches = re.findall(pattern, data_input)

results = []
travel_points = 0
for match in matches:
    results.append(match[1])
    travel_points += len(match[1])

results = ", ".join(results)
print(f"Destinations: {results}\nTravel Points: {travel_points}")
