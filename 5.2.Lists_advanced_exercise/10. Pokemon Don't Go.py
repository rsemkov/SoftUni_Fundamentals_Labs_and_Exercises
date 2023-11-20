pokemons_list = [int(i) for i in input().split()]

removed_pokemons = []
while len(pokemons_list) > 0:
    index_to_remove = int(input())

    if index_to_remove < 0:
        index_to_remove = 0
        removed_pokemon_value = pokemons_list[index_to_remove]
        pokemons_list[index_to_remove] = pokemons_list[-1]
    elif index_to_remove >= len(pokemons_list):
        index_to_remove = len(pokemons_list) - 1
        removed_pokemon_value = pokemons_list[index_to_remove]
        pokemons_list[index_to_remove] = pokemons_list[0]
    else:
        removed_pokemon_value = pokemons_list.pop(index_to_remove)

    removed_pokemons.append(removed_pokemon_value)

    for index in range(len(pokemons_list)):
        if pokemons_list[index] <= removed_pokemon_value:
            pokemons_list[index] += removed_pokemon_value
        else:
            pokemons_list[index] -= removed_pokemon_value

print(sum(removed_pokemons))
