import random

def birthday_paradox(n=23):
    birthdays = [random.randint(1, 365) for _ in range(n)]
    return len(birthdays) != len(set(birthdays))

trials = 1000
successes = sum(birthday_paradox() for _ in range(trials))
probability = successes / trials
print(f"Probability of at least two people sharing a birthday: {probability:.4f}")