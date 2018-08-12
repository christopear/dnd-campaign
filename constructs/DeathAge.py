import numpy as np


def survival(t, alpha=80, beta=0.7, beta_x=0.05):
	LHS = np.divide(t, alpha)

	RHS = np.add(beta, np.multiply(beta_x, t))
	M = np.power(LHS, RHS)
	retter = np.math.exp(-M)
	return retter


def get_death_age():
	grim_reaper = np.random.uniform(0, 1, (1,))

	s2 = np.vectorize(survival)
	years = np.arange(0, 10000)

	results = s2(years)

	return sum(np.less(grim_reaper, results))
