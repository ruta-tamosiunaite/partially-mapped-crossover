import random

def partially_mapped_crossover(parent1, parent2, number_of_children=1):
    size = len(parent1)
    # Step 1: Select crossover range at random
    start, end = sorted(random.sample(range(1, size - 2), 2))  # Avoid the first and last gene (the hive) (Last element of the list is (length - 1). Thus, it is (length - 2) to avoid the last gene)

    # Step 2: Create offspring by exchanging the selected range
    child1 = parent1[:start] + parent2[start:end] + parent1[end:]
    child2 = parent2[:start] + parent1[start:end] + parent2[end:]

    # Step 3: Determine the mapping relationship to legalize offspring
    mapping1 = {parent2[i]: parent1[i] for i in range(start, end)}
    mapping2 = {parent1[i]: parent2[i] for i in range(start, end)}

    # Step 4: Legalize children with the mapping relationship
    for i in list(range(start)) + list(range(end, size)):
        if child1[i] in mapping1:
            while child1[i] in mapping1:
                child1[i] = mapping1[child1[i]]
        if child2[i] in mapping2:
            while child2[i] in mapping2:
                child2[i] = mapping2[child2[i]]
    if number_of_children == 1:
        if random.random() < 0.5:
            return child1
        else:
            return child2
    else:
        return child1, child2


# Define parent genes
parent1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
parent2 = [0, 5, 4, 6, 9, 2, 1, 7, 8, 3, 0]

# Select 2 or 1 children per pair
number_of_children = 2

# Perform crossover
child = partially_mapped_crossover(parent1, parent2, number_of_children)

# Print Child 1 and Child 2*
if number_of_children == 1:
    print(child)
else:
    for c in child:
        print(c)

