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


def evaluation(population,itens_benefits_space):
    eval = []
    
    for i in range(len(population)):
        value_benefits = 0
        print("individuo:",i)
        print("->:",population[i])
        for c in range(len(itens_benefits_space[0])):
            if(population[i][c]== 1):
                value_benefits += int(itens_benefits_space[0][c])                
        eval.append(value_fitnes)
        print('print valor fitnees:', value_benefits)
    return eval

def evaluation_valid(population, items_benefits_space,dimension):
    eval_valid = []
    i=0
    for i in range(len(population)):
        value_benefits = 0
        space_valid = [0,0,0,0,0]
        # print("individuo:",i)
        # print("->:",population[i])
        for c in range(len(items_benefits_space[0])):
            if(population[i][c]== 1):
                value_benefits += int(items_benefits_space[0][c])
                space_valid[0] += int(items_benefits_space[1][c])
                space_valid[1] += int(items_benefits_space[2][c])
                space_valid[2] += int(items_benefits_space[3][c])
                space_valid[3] += int(items_benefits_space[4][c])
                space_valid[4] += int(items_benefits_space[5][c])
        print('espaço_peso _analisado')
        print(space_valid)
        for res in range(dimension):
            if not((space_valid[0] > int(constraints[res][0])) or (space_valid[1] > int(constraints[res][1])) or (space_valid[2] > int(constraints[res][2])) or 
            (space_valid[3] > int(constraints[res][3])) or (space_valid[4] > int(constraints[res][4]))):
                print(space_valid[0])
                print(constraints[res])
                eval_valid.append(value_benefits)
        # if res in range(len())
        # print(constraints[i])

        #    eval_valid.append(value_fitnes)
        # print('print valor fitnees:', value_fitnes)
        # print('print valor espaco ocupado:', space_valid)
    return eval_valid


if __name__== "__main__":

    file_name = 'mknapcb1.txt' 
    constraints, item_dimension_best_score, problem, items_benefits_space  = start_problem_of_file(file_name)


    print('problem:', problem)
    print('itens:', (item_dimension_best_score[0][0]))
    print('dimension:', (item_dimension_best_score[0][1]))
    print('best_score:', (item_dimension_best_score[0][2]))
    print('constraints_space:', len(constraints))
    print('constraints_space:', constraints[0])
    print('itens_benefits_space:',len(items_benefits_space))

    size_population = 100
    pop = generate_population(size_population,len(items_benefits_space[0][0]))
   
    #eval = evaluation(pop,itens_benefits_space[0])
    #print('Avaliacao: ', len(eval))
    # eval_valid  = evaluation_valid(pop,items_benefits_space[0],int(item_dimension_best_score[0][1]))
    