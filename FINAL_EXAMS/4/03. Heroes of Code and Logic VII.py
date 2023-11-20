def cast_spell(the_hero, mp_needed, spell_name, the_dict):
    if the_dict[the_hero][1] >= mp_needed:
        the_dict[the_hero][1] -= mp_needed
        mp_left = the_dict[the_hero][1]
        print(f"{the_hero} has successfully cast {spell_name} and now has {mp_left} MP!")
    else:
        print(f"{the_hero} does not have enough MP to cast {spell_name}!")
    return the_dict


def take_damage(the_hero, the_damage, the_attacker, the_dict):
    the_dict[the_hero][0] -= the_damage
    remaining_hp = the_dict[the_hero][0]
    if remaining_hp > 0:
        print(f"{the_hero} was hit for {the_damage} HP by {the_attacker} and now has {remaining_hp} HP left!")
    else:
        print(f"{the_hero} has been killed by {the_attacker}!")
        del the_dict[the_hero]
    return the_dict


def recharge(the_hero, the_amount, the_dict):
    if the_dict[the_hero][1] + the_amount > 200:
        recharge_amount = 200 - the_dict[the_hero][1]
    else:
        recharge_amount = the_amount
    the_dict[the_hero][1] += recharge_amount
    print(f"{the_hero} recharged for {recharge_amount} MP!")
    return the_dict


def heal(the_hero, the_amount, the_dict):
    if the_dict[the_hero][0] + the_amount > 100:
        recharge_amount = 100 - the_dict[the_hero][0]
    else:
        recharge_amount = the_amount
    the_dict[the_hero][0] += recharge_amount
    print(f"{the_hero} healed for {recharge_amount} HP!")
    return the_dict


heroes_count = int(input())
heroes_dict = {}
for _ in range(heroes_count):
    current_hero = input().split()
    name, hp, mp = current_hero[0], int(current_hero[1]), int(current_hero[2])
    heroes_dict[name] = [hp, mp]

while True:
    command = input()
    if command == "End":
        break
    command = command.split(" - ")
    action = command[0]
    hero_name = command[1]

    if action == "CastSpell":
        mp_required = int(command[2])
        spell = command[3]
        heroes_dict = cast_spell(hero_name, mp_required, spell, heroes_dict)
    elif action == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        heroes_dict = take_damage(hero_name, damage, attacker, heroes_dict)
    elif action == "Recharge":
        amount = int(command[2])
        heroes_dict = recharge(hero_name, amount, heroes_dict)
    elif action == "Heal":
        amount = int(command[2])
        heroes_dict = heal(hero_name, amount, heroes_dict)

for hero, stats in heroes_dict.items():
    current_hp = stats[0]
    current_mp = stats[1]
    print(f"{hero}\n\tHP: {current_hp}\n\tMP: {current_mp}")

