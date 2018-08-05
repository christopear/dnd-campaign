class Person:

    @staticmethod
    def generate_person():
        # age = int(np.random.uniform(12, 90, 1))
        # death_age = int(np.random.uniform(age, 90, 1))
        # gender = np.random.choice([Gender.male, Gender.female])
        #
        # return Person(age, death_age, gender)
        pass

    def __init__(self, age, death_age, level, gender, family, ethnicity, alignment, common_name=""):
        self.age = age
        self.death_age = death_age
        self.level = level
        self.gender = gender
        self.family = family
        self.ethnicity = ethnicity
        self.alignment = alignment
        self.common_name = common_name

    def is_dead(self):
        return self.age > self.death_age