from person import Person

class Patient(Person):
    def __init__(self, person_id, name, age, disease):
        super().__init__(person_id, name, age)
        self.disease = disease
