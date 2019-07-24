
from fuzzywuzzy import fuzz
import random
import string

#Title
print("Genetic Algorithm Demo\n")
#Creator
print("By: Mashrur.C\n")
#Description
print("Input a string and the genetic algorithm will learn to make your string, from sets of randomly generated strings.\n")

#Generate Agents
class Agent:

    def __init__(self, length):

        self.string = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        self.fitness = -1

    def __str__(self):

        return 'String: ' + str(self.string) + " | " + "Fitness: " + str(self.fitness) + "%"

#Set generations and batch size
in_str = None
in_str_len = None
population = int(input("Population:"))
generations = int(input("Generations:"))

#Handles main print functions and checks if any agent hasreached Fitness 100
def ga():

    agents = init_agents(population, in_str_len)

    for generation in range(generations+1):

        print('Generation: ' + str(generation))
        print("-------------------------------------------------------------")

        agents = fitness(agents)
        agents = selection(agents)
        agents = crossover(agents)
        agents = mutation(agents)
        
        #check if any agent has reached 100 fitness
        if any(agent.fitness == 100 for agent in agents):

            print("Your agent reached 100 Fitness in", str(generation), "generations!")
            exit(0)

#Sets all agents into a list
def init_agents(population, length):

    return [Agent(length) for _ in range(population)]

#Calculates the fitness for each agent
def fitness(agents):

    for agent in agents:

        agent.fitness = fuzz.ratio(agent.string, in_str)

    return agents

#Selects the top X% of agents to crossover DNA and repopulate the agents
def selection(agents):

    agents = sorted(agents, key=lambda agent: agent.fitness, reverse=True)
    print ('\n'.join(map(str, agents)))
    agents = agents[:int(0.25* len(agents))]

    return agents

#Takes sets of 2 agents, and crosses over DNA, and repopulates the agents list
def crossover(agents):

    offspring = []

    for _ in range((population - len(agents)) // 2):

        parent1 = random.choice(agents)
        parent2 = random.choice(agents)
        child1 = Agent(in_str_len)
        child2 = Agent(in_str_len)
        split = random.randint(0, in_str_len)
        child1.string = parent1.string[0:split] + parent2.string[split:in_str_len]
        child2.string = parent2.string[0:split] + parent1.string[split:in_str_len]

        offspring.append(child1)
        offspring.append(child2)

    agents.extend(offspring)

    return agents

#sets an X% chance to mutate a random letter in the string to reduce genetic plateau.
def mutation(agents):

    for agent in agents:

        for idx, param in enumerate(agent.string):

            if random.uniform(0.0, 1.0) <= 0.1:

                agent.string = agent.string[0:idx] + random.choice(string.ascii_letters) + agent.string[idx+1:in_str_len]
    return agents

#Gets input string from user and starts main function
in_str = input("String:")
in_str_len = len(in_str)
ga()

