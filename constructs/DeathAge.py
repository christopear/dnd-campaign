import numpy as np


class DeathAge:
	def __init__(self, alpha=80, beta=0.7, beta_x=0.05):
		"""
		:param alpha: while not exactly equal, can be thought of as the turning point, the median death age
		:param beta: represents the curvature of the distribution
		:param beta_x: represents the curvature of the distribution
		"""
		self.alpha = alpha
		self.beta = beta
		self.beta_x = beta_x

	def survival(self, t):
		"""
		generalised survival function for calculating the percentage of the population remaining x years after birth
		:param t: represents age
		:return: the percentage left alive
		"""
		t = np.asarray(t)

		LHS = np.divide(t, self.alpha)

		RHS = np.add(self.beta, np.multiply(self.beta_x, t))
		M = np.power(LHS, RHS)
		retter = np.math.exp(-M)
		return retter

	def death_odds(self, t):
		"""
		a function to calculate the probability of surviving at any particular year
		:param t: represents age
		:return: the odds of surviving at that age
		"""
		t = np.asarray(t)

		return np.vectorize(self.survival)(t) / np.vectorize(self.survival)(np.subtract(t, 1))
