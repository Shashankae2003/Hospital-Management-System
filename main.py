from hospital import Hospital
from patient import Patient
from doctor import Doctor

def main():
    hospital = Hospital()
    hospital.load_data()

    while True:
        print("\n🏥 HOSPITAL MANAGEMENT SYSTEM")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Book Appointment")
        print("4. View Patients")
        print("5. View Doctors")
        print("6. View Appointments")
        print("7. Save & Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pid = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            age = int(input("Enter Patient Age: "))
            disease = input("Enter Disease: ")
            hospital.add_patient(Patient(pid, name, age, disease))
            print("✅ Patient added successfully!")

        elif choice == "2":
            did = input("Enter Doctor ID: ")
            name = input("Enter Doctor Name: ")
            age = int(input("Enter Doctor Age: "))
            specialty = input("Enter Specialty: ")
            hospital.add_doctor(Doctor(did, name, age, specialty))
            print("✅ Doctor added successfully!")

        elif choice == "3":
            pid = input("Enter Patient ID: ")
            did = input("Enter Doctor ID: ")
            time = input("Enter Appointment Time (e.g., 10:00 AM): ")
            try:
                hospital.book_appointment(pid, did, time)
                print("✅ Appointment booked successfully!")
            except ValueError as e:
                print(f"❌ Error: {e}")

        elif choice == "4":
            print("\n📋 Patients List:")
            for pid, patient in hospital.patients.items():
                print(f"{pid}: {patient.name}, Age {patient.age}, Disease: {patient.disease}")

        elif choice == "5":
            print("\n👨‍⚕️ Doctors List:")
            for did, doctor in hospital.doctors.items():
                print(f"{did}: {doctor.name}, Age {doctor.age}, Specialty: {doctor.specialty}")

        elif choice == "6":
            print("\n📅 Appointments:")
            for app in hospital.appointments:
                print(f"Patient {app.patient_id} with Doctor {app.doctor_id} at {app.time}")

        elif choice == "7":
            hospital.save_data()
            print("💾 Data saved. Exiting system. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
