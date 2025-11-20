import random

def monty_hall_simulation(switch=True):
    wins = 0#胜场数
    trials = 10000#模拟次数
    for _ in range(trials):#模拟次数
        doors = [False] * 3
        car_door = random.randint(0, 2)
        doors[car_door] = True
        initial_choice = random.randint(0, 2)
        revealed_door = (initial_choice + 1) % 3 if initial_choice != car_door else (initial_choice + 2) % 3
        final_choice = (revealed_door + 1) % 3 if initial_choice == revealed_door else revealed_door
        if switch:
            final_choice = (final_choice + 1) % 3
        if doors[final_choice]:
            wins += 1
    return wins / trials

print(f"切换选择获胜概率: {monty_hall_simulation(True)}")
print(f"坚持选择获胜概率: {monty_hall_simulation(False)}")