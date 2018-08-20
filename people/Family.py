class Family:
	FAMILIES = []

	def __init__(self):
		Family.FAMILIES.append(self)

		self.family_members = []
