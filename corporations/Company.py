class Company:
	COMPANIES = []

	def __init__(self
				 , name=None
				 , founder=None
				 , industry=None
				 , employees=None
				 , directors=None
				 , shareholders=None
				 , IncorporationDate=None
				 , ShutdownDate=None
				 , Status=None
				 , EntityType=None
				 , Constitution=None
				 , location=None
				 , FRAMonth=None
				 , GUP=None
				 , CompanyNumber=None
				 , BN=None):

		Company.COMPANIES.append(self)

		self.name = name
		self.founder = founder
		self.industry = industry
		self.employees = employees
		self.directors = directors
		self.shareholders = shareholders
		self.IncorporationDate = IncorporationDate
		self.ShutdownDate = ShutdownDate
		self.Status = Status
		self.EntityType = EntityType
		self.Constitution = Constitution
		self.location = location
		self.FRAMonth = FRAMonth
		self.GUP = GUP
		self.CompanyNumber = CompanyNumber
		self.BN = BN

		self.name_check()
		self.founder_check()
		self.industry_check()
		self.employees_check()
		self.directors_check()
		self.shareholders_check()
		self.IncorporationDate_check()
		self.ShutdownDate_check()
		self.Status_check()
		self.EntityType_check()
		self.Constitution_check()
		self.location_check()
		self.FRAMonth_check()
		self.GUP_check()
		self.CompanyNumber_check()
		self.BN_check()

	# region checkers
	def name_check(self):
		if self.name is None:
			pass

	def founder_check(self):
		if self.founder is None:
			pass

	def industry_check(self):
		if self.industry is None:
			pass

	def employees_check(self):
		if self.employees is None:
			self.employees = {}

	def directors_check(self):
		if self.directors is None:
			pass

	def shareholders_check(self):
		if self.shareholders is None:
			pass

	def IncorporationDate_check(self):
		if self.IncorporationDate is None:
			pass

	def ShutdownDate_check(self):
		if self.ShutdownDate is None:
			pass

	def Status_check(self):
		if self.Status is None:
			pass

	def EntityType_check(self):
		if self.EntityType is None:
			pass

	def Constitution_check(self):
		if self.Constitution is None:
			pass

	def location_check(self):
		if self.location is None:
			pass

	def FRAMonth_check(self):
		if self.FRAMonth is None:
			pass

	def GUP_check(self):
		if self.GUP is None:
			pass

	def CompanyNumber_check(self):
		if self.CompanyNumber is None:
			pass

	def BN_check(self):
		if self.BN is None:
			pass

			# endregion
