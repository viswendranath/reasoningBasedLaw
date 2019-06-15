from itertools import permutations,product
from collections import namedtuple
def add_dimension(old_values, new_dim_values, new_field_names):
NewTuple = namedtuple('_', new_field_names)
new_values = (NewTuple(*(x+(z,))) for x,z in product(old_values, new_dim_values))
    return new_values
def solution():
    nationalities = ['German','Dane','Englishman','Swede','Norwegian']
    drinks = ['tea', 'juice', 'milk', 'coffee', 'water']
    animals = ['dog', 'horse', 'birds', 'cats', 'rabbit']
    jobs = ['IBM','Microsoft','Wipro','Hospital','Amazon']
colors = ['red', 'green', 'White', 'yellow', 'blue']
nationality_permutations = permutations(nationalities)
drink_permutations = permutations(drinks)
animal_permutations = permutations(animals)
job_permutations = permutations(jobs)
color_permutations = permutations(colors)
    # (rules that operate on a single characteristic)
nationality_permutations = (x for x in nationality_permutations
            if x.index('Norwegian')==0) # rule 9
color_permutations = (x for x in color_permutations
            if x.index('green')-x.index('White')==1) # rule 4
drink_permutations = (x for x in drink_permutations
      if x.index('milk') == 2) # rule 8
TwoTuple = namedtuple('_',
            'nationality color')
possible_solutions = (TwoTuple(x,z) for x,z in product(nationality_permutations, color_permutations))
    # prune using nationality+color rules
possible_solutions = (x for x in possible_solutions
            if x.nationality.index('Englishman')==x.color.index('red')) # rule 1
possible_solutions = (x for x in possible_solutions
            if abs(x.nationality.index('Norwegian')-x.color.index('blue')) == 1) # rule 14
possible_solutions = add_dimension(possible_solutions, drink_permutations,
            'nationality color drink')
    # prune using nationality+drink and color+drink rules
possible_solutions = (x for x in possible_solutions
            if x.nationality.index('Dane')==x.drink.index('tea')) # rule 3
possible_solutions = (x for x in possible_solutions
            if x.color.index('green')==x.drink.index('coffee')) # rule 5
possible_solutions = add_dimension(possible_solutions, job_permutations,
            'nationality color drink job')
    # prune using nationality+job, color+job, and drink+job rules
possible_solutions = (x for x in possible_solutions
            if x.nationality.index('German')==x.job.index('Hospital')) # rule 13
possible_solutions = (x for x in possible_solutions
            if x.color.index('yellow')==x.job.index('IBM')) # rule 7
possible_solutions = (x for x in possible_solutions
            if x.drink.index('juice')==x.job.index('Microsoft')) # rule 12
possible_solutions = add_dimension(possible_solutions, animal_permutations,
            'nationality color drink job animal')
    # prune using rules that include animals (the others are already done)
possible_solutions = (x for x in possible_solutions
            if x.nationality.index('Swede')==x.animal.index('dog')) # rule 2
possible_solutions = (x for x in possible_solutions
            if x.job.index('Amazon')==x.animal.index('birds')) # rule 6
possible_solutions = (x for x in possible_solutions
            if abs(x.job.index('Wipro')-x.animal.index('cats'))==1) # rule 10
possible_solutions = (x for x in possible_solutions
            if abs(x.nationality.index('Norwegian')-x.animal.index('horse'))==1) # rule 11
possible_solutions = list(possible_solutions)
    if len(possible_solutions)==0:
        raise Exception('no solution found')
    if len(possible_solutions)>1:
        raise UserWarning('solution is not unique')
    sol = possible_solutions[0]
ans = 'It is the {} who drinks the water.\n'.format(sol.nationality[sol.drink.index('water')])
ans += 'The {} keeps the rabbit.'.format(sol.nationality[sol.animal.index('rabbit')])
    return ans
if __name__ == '__main__':
    print(solution())
