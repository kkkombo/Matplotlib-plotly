from die import Die

die = Die()

# Create a score table for Die results.
die_results = []

# Throwing dies.
for throw in range(0, 1000):
    throw = die.roll()
    die_results.append(throw)

# Analyse the results.
frequencies = {}
for value in range(1, die.num_sides+1):
    frequency = die_results.count(value)
    frequencies[value] = frequency
print(frequencies)

# Check all throws.
all_sum = 0
for value in frequencies.values():
    all_sum += value
print(all_sum)