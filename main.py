from hospital import Hospital
from patient import Patient
from doctor import Doctor

def main():
    hospital = Hospital()
    hospital.load_patients()
    hospital.load_doctors()
    hospital.load_appointments()

    while True:
        print("\n===== Hospital Management System =====")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Book Appointment")
        print("4. View Doctor's Schedule")
        print("5. View Patients")
        print("6. View Doctors")
        print("7. View All Appointments")
        print("8. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            pid = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            age = int(input("Enter Patient Age: "))
            disease = input("Enter Patient Disease: ")
            hospital.add_patient(Patient(pid, name, age, disease))
            print("✅ Patient added successfully!")

        elif choice == "2":
            did = input("Enter Doctor ID: ")
            name = input("Enter Doctor Name: ")
            age = int(input("Enter Doctor Age: "))
            specialty = input("Enter Doctor Specialty: ")
            hospital.add_doctor(Doctor(did, name, age, specialty))
            print("✅ Doctor added successfully!")

        elif choice == "3":
            pid = input("Enter Patient ID: ")
            did = input("Enter Doctor ID: ")
            date = input("Enter Appointment Date (YYYY-MM-DD): ")
            time = input("Enter Appointment Time (HH:MM in 24hr format): ")
            try:
                hospital.book_appointment(pid, did, date, time)
                print("✅ Appointment booked successfully!")
            except ValueError as e:
                print(f"❌ Error: {e}")

        elif choice == "4":
            did = input("Enter Doctor ID: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            try:
                hospital.show_doctor_schedule(did, date)
            except ValueError as e:
                print(f"❌ Error: {e}")

        elif choice == "5":
            for p in hospital.patients.values():
                print(vars(p))

        elif choice == "6":
            for d in hospital.doctors.values():
                print(vars(d))

        elif choice == "7":
            for a in hospital.appointments:
                print(vars(a))

        elif choice == "8":
            print("💾 Data saved. Exiting...")
            hospital.save_patients()
            hospital.save_doctors()
            hospital.save_appointments()
            break

        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
