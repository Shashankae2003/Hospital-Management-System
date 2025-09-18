class Appointment:
    def __init__(self, patient_id, doctor_id, date, time):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date        # YYYY-MM-DD
        self.time = time        # HH:MM (24-hr format)
