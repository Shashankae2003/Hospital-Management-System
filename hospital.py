import json
from patient import Patient
from doctor import Doctor
from appointment import Appointment
from datetime import datetime

class Hospital:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = []

    # -------------------
    # Add Patient
    # -------------------
    def add_patient(self, patient):
        self.patients[patient.person_id] = patient
        self.save_patients()

    def save_patients(self):
        with open("patients.json", "w") as f:
            json.dump({pid: vars(p) for pid, p in self.patients.items()}, f, indent=4)

    def load_patients(self):
        try:
            with open("patients.json", "r") as f:
                data = json.load(f)
                self.patients = {pid: Patient(**info) for pid, info in data.items()}
        except FileNotFoundError:
            self.patients = {}

    # -------------------
    # Add Doctor
    # -------------------
    def add_doctor(self, doctor):
        self.doctors[doctor.person_id] = doctor
        self.save_doctors()

    def save_doctors(self):
        with open("doctors.json", "w") as f:
            json.dump({did: vars(d) for did, d in self.doctors.items()}, f, indent=4)

    def load_doctors(self):
        try:
            with open("doctors.json", "r") as f:
                data = json.load(f)
                self.doctors = {did: Doctor(**info) for did, info in data.items()}
        except FileNotFoundError:
            self.doctors = {}

    # -------------------
    # Appointments
    # -------------------
    def book_appointment(self, patient_id, doctor_id, date_str, time_str):
        if patient_id not in self.patients:
            raise ValueError("Patient not found")
        if doctor_id not in self.doctors:
            raise ValueError("Doctor not found")

        # Parse date & time
        appointment_time = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")

        # Check conflicts (30 min per patient)
        for app in self.appointments:
            if app.doctor_id == doctor_id:
                existing_time = datetime.strptime(f"{app.date} {app.time}", "%Y-%m-%d %H:%M")
                if abs((appointment_time - existing_time).total_seconds()) < 30 * 60:
                    raise ValueError("Doctor is not available in this slot")

        # Add appointment
        self.appointments.append(Appointment(patient_id, doctor_id, date_str, time_str))
        self.save_appointments()

    def save_appointments(self):
        with open("appointments.json", "w") as f:
            json.dump([vars(a) for a in self.appointments], f, indent=4)

    def load_appointments(self):
        try:
            with open("appointments.json", "r") as f:
                data = json.load(f)
                self.appointments = [Appointment(**a) for a in data]
        except FileNotFoundError:
            self.appointments = []

    # -------------------
    # Show Doctor's Schedule
    # -------------------
    def show_doctor_schedule(self, doctor_id, date_str):
        if doctor_id not in self.doctors:
            raise ValueError("Doctor not found")

        print(f"\n Schedule for Dr. {self.doctors[doctor_id].name} on {date_str}:")
        found = False
        for app in self.appointments:
            if app.doctor_id == doctor_id and app.date == date_str:
                patient = self.patients.get(app.patient_id, None)
                patient_name = patient.name if patient else "Unknown"
                print(f" - {app.time}: Patient {app.patient_id} ({patient_name})")
                found = True
        if not found:
            print("No appointments for this day.")
