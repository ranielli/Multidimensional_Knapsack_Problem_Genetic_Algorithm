import random


def start_problem_of_file(file_name):

    count = 0
    constraints = []
    item_dimension_best_score = []
    problem = None
    lista = []
    items_benefits_space = [] 

    file_pack = open(file_name, 'r')

    for line in file_pack :
        if count == 0:
            problem = line.rstrip()
        elif count == 1 or count%92==1 :
            item_dimension_best_score.append(line.rsplit())
        elif count%92==0 :
                constraints.append(line.rsplit())
        else:
            lista.extend(line.rsplit())
        count += 1

    while len(lista) > 0:
        #import ipdb; ipdb.set_trace()
        temp=[]
        temp.append(lista[:100])
        del lista[:100]
        temp.append(lista[:100])
        del lista[:100]
        temp.append(lista[:100])
        del lista[:100]
        temp.append(lista[:100])
        del lista[:100]
        temp.append(lista[:100])
        del lista[:100]
        temp.append(lista[:100])
        del lista[:100]

        items_benefits_space.append(temp)
    
    return  constraints, item_dimension_best_score, problem,items_benefits_space 

def generate_population(size, chromosomes):
    population = []
    i = 0
    while (i < size):
        j = 0
        individual = []
        while (j < chromosomes):
            chromosome = random.randint(0, 1)
            individual.append(chromosome)
            j += 1
        if individual not in population:
            population.append(individual)
            i += 1
    return population

def generate_population_fake(size, chromosomes):
    population = []
    i = 0
    while (i < size):
        j = 0
        individual = []
        while (j < chromosomes):
            chromosome = random.randint(0, 1)
            individual.append(chromosome)
            j += 1
        if individual not in population:
            population.append(individual)
            i += 1
    return population

def evaluation(population,itens_benefits_space):
    eval = []
    
    for i in range(len(population)):
        value_benefits = 0
        # print("individual:",i)
        # print("->:",population[i])
        for c in range(len(itens_benefits_space[0])):
            if(population[i][c]== 1):
                value_benefits += int(itens_benefits_space[0][c])                
        eval.append(value_benefits)
    return eval

def evaluation_order(population,itens_benefits_space):
    eval= []
    
    for i in range(len(population)):
        value_benefits = 0
        # print("individual:",i)
        # print("->:",population[i])
        for c in range(len(itens_benefits_space[0])):
            if(population[i][c]== 1):
                value_benefits += int(itens_benefits_space[0][c])
        # list with individual and eval                        
        eval.append([population[i],value_benefits])
        from operator import itemgetter

    return sorted(eval, key=itemgetter(1))


def evaluation_valid(population, items_benefits_space,dimension):
    eval_valid = []
    i=0
    for i in range(len(population)):
        value_benefits = 0
        space_valid = [0,0,0,0,0]
        # print("individuo:",i)
        #print("->:",population[i])
        for c in range(len(items_benefits_space[0])):
            if(population[i][c]== 1):
                value_benefits += int(items_benefits_space[0][c])
                space_valid[0] += int(items_benefits_space[1][c])
                space_valid[1] += int(items_benefits_space[2][c])
                space_valid[2] += int(items_benefits_space[3][c])
                space_valid[3] += int(items_benefits_space[4][c])
                space_valid[4] += int(items_benefits_space[5][c])        
        for res in range(dimension):
            # print(space_valid)
            # print(constraints[res])
            if not((space_valid[0] > int(constraints[res][0])) and (space_valid[1] > int(constraints[res][1])) and (space_valid[2] > int(constraints[res][2])) and 
            (space_valid[3] > int(constraints[res][3])) and (space_valid[4] > int(constraints[res][4]))):                
                eval_valid.append([population[i],value_benefits])
    return eval_valid

def select_roulette(pop_order):
    parents = []
    fitness = []
    for i in range(len(pop_order)):
        fitness.append(pop_order[i][1])
    for i in range(len(pop_order)):
        father = random.choices(pop_order, fitness, k=1)
        parents.append(father[0][0])  

    return parents

def crossover(parents):
    children = []
    for i in range(1,len(parents),2):
       
        father = parents[i-1]
        mother = parents[i]
      
        cut = random.randint(0, len(parents)-1)
        son_f = father[0:cut] 
        son_m = mother[cut:len(mother)]
        son = son_f + son_m
        daughter_f = mother[0:cut]
        daughter_m  = father[cut:len( mother)]
        daughter = daughter_f + daughter_m
       
        children.append(son)
        children.append(daughter)
    return children

def mutation(individual, tax_mut):
    
    rand = random.random()
    index = random.choices([i for i in range(len(individual)-1)])
    if rand < tax_mut:
        individual[index[0]] = 1 - individual[index[0]]

def size_list(select):
    for i in range(len(select)):
        print('size vector:', len(select))


if __name__== "__main__":

    file_name = 'mknapcb1.txt' 
    constraints, item_dimension_best_score, problem, items_benefits_space  = start_problem_of_file(file_name)



    print('problem:', problem)
    print('itens:', (item_dimension_best_score[0][0]))
    print('dimension:', (item_dimension_best_score[0][1]))
    print('best_score:', (item_dimension_best_score[0][2]))
    print('constraints_space:', len(constraints))
    print('itens_benefits_space:',len(items_benefits_space))

    size_population = 100
    interactions = 1000
    interaction = 0
    problems = int(problem)
    
    #tests
        # eval_valid = []
        # print(interaction)
        # pop = generate_population(size_population,len(items_benefits_space[0][0]))
        # print(pop)

        # eval_valid  = evaluation_valid(pop,items_benefits_space[0],int(item_dimension_best_score[0][1]))
        # print('tamanho ', len(eval_valid))
        # if len(eval_valid) > 0:
        #     print('Population valid INIT :' , eval_valid)

    for p in range(problems):
        print('##Problem number## : ', p+1)
        print('#constraints_space:', constraints[p])
        pop = generate_population(size_population,len(items_benefits_space[p][0]))
        eval = evaluation_order(pop,items_benefits_space[p])
        #print('individuos e fitnes order: ' , eval)

        eval_valid  = evaluation_valid(pop,items_benefits_space[p],int(item_dimension_best_score[p][1]))
        if len(eval_valid) > 0:
            print('individuals valid INIT :' , eval_valid)
        else:
            print('individual NOT valid INIT :' , eval_valid)

        valids = []
        while interaction < interactions:
            pop_old = pop      
            eval = evaluation_order(pop,items_benefits_space[p])
            #print('individuos e fitnes order: ' , eval)

            #print('roulette')
            select = select_roulette(eval)
            # print('select of size of roulette: ', select)
            children = crossover(select)
            # print('cross of size: ',len(children))

            pop_mut = []
            tax_mut = 0.05
            
            for child in children:
                mutation(child, tax_mut)
                pop_mut.append(child)
            pop = pop_mut
            
            eval_valid  = evaluation_valid(pop,items_benefits_space[p],int(item_dimension_best_score[p][1]))
            if len(eval_valid) > 0:
                valids.extend(eval_valid)
            
            interaction += 1
            
        print("Valids:",valids)
       

    