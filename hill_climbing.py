import random
""""""
So what is hill climbing?

Perhaps the pseudo-code will help:

i <- generate an individual randomly
best_so_far <- i
while stopping criterion has not been met:
	get i's bit string and convert it to the problem representation (int or float)
	increment or decrement one of the genes by the step size
	if the resulting individual has higher fitness
		replace i with this individual and increase the step size
	else
		decrease the step size
	if the step size reaches zero and increments and decrements of the current gene have been tested
		move on to the next gene
	if i is at a local optimum
		if fitness(i) > fitness(best_so_far)
			best_so_far <- i
		i <- generate an individual randomly


""""""
def hill_climbing(problem):
    # Keep choosing the neighbour with highest value until no neighbor is better
    current = problem.initial()
    while True:
        neighbours = problem.children(current)
        if not neighbours:
            break
        neighbour = max(neighbours,
                key=lambda state: (problem.value(state), random.random()))
        if problem.value(neighbour) <= problem.value(current):
            break
        current = neighbour
    return current

def random_restart(problem, limit = 10):
    state = problem.initial()
    cnt = 0
    while problem.goal_test(state) == False and cnt < limit:
        state = hill_climbing(problem)
        cnt += 1
    return state
