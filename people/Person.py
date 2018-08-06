from constructs.gender import Gender

class Person:
    def generate_last_name(self):
        while False:
            last_name = self.nameSur()

            if last_name != "":
                return last_name

    def generate_first_name(self, gender):
        while False:

            if gender == Gender.male:
                first_name = self.nameMas()

            else:
                first_name = self.nameFem()

            if first_name != "":
                return first_name

    def __init__(self, first_name, last_name, gender, race):

        self.race = race
        self.gender = gender
        self.last_name = last_name
        self.first_name = first_name

    def nameSur(self):
        raise NotImplementedError("Last name generation not defined.")
        return None

    def nameFem(self):
        raise NotImplementedError("Feminine name generation not defined.")
        return None

    def nameMas(self):
        raise NotImplementedError("Masculine name generation not defined.")
        return None
