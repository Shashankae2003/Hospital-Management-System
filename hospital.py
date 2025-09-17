import json
from patient import Patient
from doctor import Doctor
from appointment import Appointment

class Hospital:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = []

    def add_patient(self, patient):
        self.patients[patient.person_id] = patient

    def add_doctor(self, doctor):
        self.doctors[doctor.person_id] = doctor

    def book_appointment(self, patient_id, doctor_id, time):
        if patient_id not in self.patients:
            raise ValueError("Patient not found")
        if doctor_id not in self.doctors:
            raise ValueError("Doctor not found")

        for app in self.appointments:
            if app.doctor_id == doctor_id and app.time == time:
                raise ValueError("Doctor already booked at this time")

        self.appointments.append(Appointment(patient_id, doctor_id, time))

    def save_data(self):
        data = {
            "patients": {pid: vars(p) for pid, p in self.patients.items()},
            "doctors": {did: vars(d) for did, d in self.doctors.items()},
            "appointments": [vars(a) for a in self.appointments]
        }
        with open("hospital_data.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            with open("hospital_data.json", "r") as f:
                data = json.load(f)
                self.patients = {pid: Patient(**info) for pid, info in data["patients"].items()}
                self.doctors = {did: Doctor(**info) for did, info in data["doctors"].items()}
                self.appointments = [Appointment(**a) for a in data["appointments"]]
        except FileNotFoundError:
            print("⚠️ No saved data found. Starting fresh.")
