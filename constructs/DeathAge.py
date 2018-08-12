import numpy as np

death_years = np.arange(0, 10000)


def survival(alpha=80, beta=0.7, beta_x=0.05):
	t = death_years
	LHS = np.divide(t, alpha)

	RHS = np.add(beta, np.multiply(beta_x, t))
	M = np.power(LHS, RHS)
	retter = np.math.exp(-M)
	return retter


def death_odds():
	pass


def get_death_odds(current_age):
	'''
	this function gets the odds of dying in the next year
	:return: the probability of death
	'''


# alive = survival()
# dead = ((lag(alive)) - alive) / (lag(alive))
# dead[1] = 0


def get_death_age():
	grim_reaper = np.random.uniform(0, 1, (1,))

	s2 = np.vectorize(survival)

	results = s2()

	return sum(np.less(grim_reaper, results))
