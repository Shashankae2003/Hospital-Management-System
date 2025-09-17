from person import Person

class Doctor(Person):
    def __init__(self, person_id, name, age, specialty):
        super().__init__(person_id, name, age)
        self.specialty = specialty
