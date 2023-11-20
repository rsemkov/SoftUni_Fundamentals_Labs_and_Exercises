population = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())

# check if equal distribution is possible at all:
if sum(population) / len(population) >= minimum_wealth:
    equal_distribution = True
else:
    equal_distribution = False

index_counter = 0
while min(population) < minimum_wealth and equal_distribution:
    if population[index_counter] < minimum_wealth:
        # give to the poor:
        wealth_transferred = minimum_wealth - population[index_counter]
        population[index_counter] += wealth_transferred
        # find the index of the rich, and take from him:
        index_of_wealthiest = population.index(max(population))
        population[index_of_wealthiest] -= wealth_transferred

    index_counter += 1

if equal_distribution:
    print(population)
else:
    print("No equal distribution possible")

