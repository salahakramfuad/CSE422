import random

# Step 1: Chromosomes generated
def generate_chromosome():
    return {
        "stop_loss": round(random.uniform(1, 99)),
        "take_profit": round(random.uniform(1, 99)),
        "trade_size": round(random.uniform(1, 99))
    }

# Step 2: Population Generated
def initialize_population():
    population = []
    for i in range(4):
        population.append(generate_chromosome())
    return population

# Step 3: Evaluate Fitness (Profit Calculation)
def trading(strategy, historical_prices, initial_capital=1000):
    capital = initial_capital
    for change in historical_prices:
        trade_amount = (capital * strategy["trade_size"]) / 100
        if change <= -strategy["stop_loss"]:
            loss = trade_amount * (strategy["stop_loss"] / 100)
            capital -= loss
        elif change >= strategy["take_profit"]:
            profit = trade_amount * (strategy["take_profit"] / 100)
            capital += profit
        else:
            capital += trade_amount * (change / 100)
    return capital

def evolve(population, historical_prices):
    fitness_scores = []
    for chromosome in population:
        final_capital = trading(chromosome, historical_prices)
        profit = final_capital - 1000
        fitness_scores.append((profit, chromosome))
    return sorted(fitness_scores, key=lambda x: x[0], reverse=True)


#Step 4: Select Parents (Random Selection)

def parent_selection(x):
    parent1, parent2 = random.sample(x, 2)
    return parent1,parent2


# Step 5: Crossover (Recombine Parent Genes)
def single_point_crossover(parent1, parent2):
    split = random.randint(1, 2)
    child1 = {}
    child2 = {}
    keys = list(parent1.keys())
    for i in range(len(keys)):
        key = keys[i]
        if i < split:
            child1[key] = parent1[key]
            child2[key] = parent2[key]
        else:
            child1[key] = parent2[key]
            child2[key] = parent1[key]
    return child1, child2

# Step 6: Mutation (Introduce Random Changes)
def mutate(chromosome, mutation_rate=0.05):
    if random.random() < mutation_rate:
        genes = list(chromosome.keys())
        gene_to_mutate = random.choice(genes)
        if gene_to_mutate == "trade_size":
            chromosome[gene_to_mutate] = round(random.uniform(15, 30))
        else:
            chromosome[gene_to_mutate] = round(random.uniform(1, 5))
    return chromosome

# Step 7: Generate New Population (Next Generation)
def generate_new_population(population, historical_prices, generations=10):
    for _ in range(generations):
        evaluated = evolve(population, historical_prices)
        new_population = [evaluated[0][1], evaluated[1][1]]
        while len(new_population) < len(population):
            parent1,parent2=parent_selection(initial_population)
            child1, child2 = single_point_crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.append(child1)
            new_population.append(child2)
        population = new_population[:len(population)]
    best_chromosome = evolve(population, historical_prices)[0][1]
    return best_chromosome

# Main Program
historical_prices = [-1.2, 3.4, -0.8, 2.1, -2.5, 1.7, -0.3, 5.8, -1.1, 3.5]
initial_population = [
    {"stop_loss": 2, "take_profit": 5, "trade_size": 20},
    {"stop_loss": 3, "take_profit": 7, "trade_size": 30},
    {"stop_loss": 1.5, "take_profit": 4, "trade_size": 25},
    {"stop_loss": 2.5, "take_profit": 6, "trade_size": 15}
]
best_strategy = generate_new_population(initial_population, historical_prices)
print("Best Strategy:", best_strategy)

final_capital=trading(best_strategy,historical_prices)

print('Profit: ',final_capital-1000)





# Part 2




initial_population = [
    {"stop_loss": 2, "take_profit": 5, "trade_size": 20},
    {"stop_loss": 3, "take_profit": 7, "trade_size": 30},
    {"stop_loss": 1.5, "take_profit": 4, "trade_size": 25},
    {"stop_loss": 2.5, "take_profit": 6, "trade_size": 15}
]

def two_point_crossover(parent1, parent2):
    keys = list(parent1.keys())
    point1, point2 = sorted(random.sample(range(len(keys) + 1), 2))

    child1 = {}
    child2 = {}

    for i in range(len(keys)):
        key = keys[i]
        if i < point1 or i >= point2:
            child1[key] = parent1[key]
            child2[key] = parent2[key]
        else:
            child1[key] = parent2[key]
            child2[key] = parent1[key]

    return child1, child2


parent1, parent2 = random.sample(initial_population, 2)
child1, child2 = two_point_crossover(parent1, parent2)


print("Parent 1:", parent1)
print("Parent 2:", parent2)
print("Child 1:", child1)
print("Child 2:", child2)