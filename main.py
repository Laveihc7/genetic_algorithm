import numpy
import os
from random import random, uniform
from matplotlib import pylab as plt
from operator import itemgetter

from numpy.core.tests.test_mem_overlap import xrange

MAX = 0
MIN = 0
gen_num = 0
time = 0
popsize = 0
bestindividual = None
pop = []

def init(parameter):
    min = parameter[2]
    max = parameter[1]

    for i in parameter[3]:
        gene_info = []
        gene_info.append(random.uniform(min, max))
        fitness = fitness_get(gene_info)
        pop.append({'Gene': gene_info, 'fitness': fitness})

def target(x):
    return x

def fitness_get(gene):
    fitness = gene
    return fitness

def select_best(population):
    inds = sorted(population, key = itemgetter('fitness'), reverse = True)
    return inds[0]

def selction(population, k):
    inds = sorted(population, key = itemgetter('fitness'), reverse = True)
    fit_sum = sum(1/ind['fitness'] for ind in population)
    chosen = []
    sum_now = 0
    for a in xrange(k):
        x = random.random()*fit_sum
        for ind in inds:
            sum_now += 1/ind['fitness']
            if sum_now > x:
                chosen.append(ind)
                break
    return chosen

def crossoperate(population):
    range = len(population[0]['Gene'])
    gene_info_1 = population[0]['Gene']
    gene_info_2 = population[1]['Gene']

    index_1 = random.randrange(1,range)
    index_2 = random.randrange(1,range)

    product = []

    for i in range:
        if (i >= min(index_1, index_2) and i <= max(index_1, index_2)):
            product.append({'Gene':gene_info_1[i]})
        else:
            product.append({'Gene':gene_info_2[i]})

    return product

def mutation(offspring, p_range):
    range = len(offspring[0]['Gene'])
    index = random.randrange(1,range)
    offspring[0]['Gene'][index] = random.uniform(p_range[1],p_range[0])
    return offspring

def algo_main(parameters):
    popsize = parameters[3]
    bestindividual = select_best(pop)
    for k in parameters[2]:
        selcted = selction(pop, parameters[3])
        newoff = []
        while len(newoff) != popsize:
            off = [random.choice(selcted[g] for g in xrange(2))]
            if random.random() > c_prob:
                crossoff = crossoperate(off)
                crossoff_fit = fitness_get(crossoff)
                if random.random() > m_prob:
                    mutaoff = mutation(crossoff, parameters)
                    mutaoff_fit = fitness_get(mutaoff)
                    newoff.append({'Gene':mutaoff, 'fitness':mutaoff_fit})
                else:
                    newoff.append({'Gene':crossoff, 'fitness':crossoff_fit})

        pop = newoff
        best_ind = select_best(pop)
        fits_all = [pop[k]['fitness'] for k in len(pop)]
        if best_ind['fitness'] > bestindividual:
            bestindividual = best_ind


if __name__ == "__main__":
    parameter = [MAX, MIN, gen_num, popsize]
    init(parameter)
    algo_main(parameter)
