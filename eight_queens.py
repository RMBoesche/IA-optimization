import random


def evaluate(individual):
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 10.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """

    num_lines_and_columns = 8
    num_attacks = 0

    for i in range(num_lines_and_columns):
        queen = individual[i]

        for j in range(num_lines_and_columns):
            if i == j:
                pass

            elif (individual[j] == queen or 
                  individual[j] == (queen - (i - j)) or 
                  individual[j] == (queen + (i - j))):
                num_attacks += 1

    num_attacks = num_attacks / 2

    return num_attacks


def tournament(participants):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """
    return min(participants, key=evaluate)


def crossover(parent1, parent2, index):
    """
    Realiza o crossover de um ponto: recebe dois indivíduos e o ponto de
    cruzamento (indice) a partir do qual os genes serão trocados. Retorna os
    dois indivíduos com o material genético trocado.
    Por exemplo, a chamada: crossover([2,4,7,4,8,5,5,2], [3,2,7,5,2,4,1,1], 3)
    deve retornar [2,4,7,5,2,4,1,1], [3,2,7,4,8,5,5,2].
    A ordem dos dois indivíduos retornados não é importante
    (o retorno [3,2,7,4,8,5,5,2], [2,4,7,5,2,4,1,1] também está correto).
    :param parent1:list
    :param parent2:list
    :param index:int
    :return:list,list
    """
    return parent1[:index] + parent2[index:], parent2[:index] + parent1[index:] 


def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    if random.random() < m:
        index = random.randint(0, 7)
        mutation_value = random.randint(1, 8)
        
        while individual[index] == mutation_value:
            mutation_value = random.randint(1, 8)

        individual[index] = mutation_value

    return individual


def run_ga(generations, population_size, number_of_participants, mutation_probability, elitist_individuals):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:int - número de indivíduos no elitismo
    :return:list - melhor individuo encontrado
    """
    crossover_probability = 0.8
    results = []
    maior_list, menor_list, media_list = [], [], []

    population = create_population(population_size)

    for _ in range(generations):
        new_population = elitism(population, elitist_individuals)

        required_individuals = population_size - len(new_population)
        for _ in range(required_individuals):
            parent1 = tournament(choose_participants(population, number_of_participants))
            parent2 = tournament(choose_participants(population, number_of_participants))

            # Crossover
            if (random.random() < crossover_probability) and (parent1 != parent2):
                index = 4
                # print('Crossover')
                # print(parent1, parent2)
                child1, child2 = crossover(parent1, parent2, index)
                # print(child1, child2)

            else:
                child1, child2 = parent1, parent2

            # Mutation
            child1 = mutate(child1, mutation_probability)
            child2 = mutate(child2, mutation_probability)

            new_population.append(child1)
            new_population.append(child2)

        population = new_population

        maior,menor,media=printa_resultados(population)
        maior_list.append(maior)
        menor_list.append(menor)
        media_list.append(media)

        # Append results for this generation
        highest = max(population, key=evaluate)
        mean = sum([evaluate(x) for x in population]) / len(population)
        smallest = min(population, key=evaluate)
        results.append([highest, mean, smallest])

    # # Print results
    for i, result in enumerate(results):
        print(f"Generation {i+1}: Highest: {result[0]} = {evaluate(result[0])}, Mean: {result[1]}, Smallest: {result[2]} = {evaluate(result[2])}")

    return population

def create_individual():
    individual = [random.randint(1, 8) for _ in range(8)]
    return individual


def create_population(population_size):
    population = []

    for _ in range(population_size):
        individual = create_individual()
        population.append(individual)

    return population


def elitism(population, elitist_individuals):
    sorted_pop = sorted(population, key=evaluate)
    print([evaluate(x) for x in sorted_pop])
    elitist = sorted_pop[:elitist_individuals]
    return elitist


def choose_participants(population, participants_tournaments):
    participants = random.sample(population, participants_tournaments)
    return participants

def printa_resultados(pop):
    maior=0
    menor=10
    media=0
    for ind in pop:
        valor_ind=evaluate(ind)
        if valor_ind>maior:
            maior=valor_ind
        if valor_ind<menor:
            menor=valor_ind
        media+=valor_ind
    media=media/len(pop)
   
    print("maior")
    print(maior)
    print("menor")
    print(menor)
    print("media")
    print(media)
    return  maior, menor, media


