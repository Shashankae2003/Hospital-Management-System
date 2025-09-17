# 🏥 Hospital Management System (Python Project)

## 📌 Overview
This is a **menu-driven Hospital Management System** built in Python.  
It allows you to:
- Add patients and doctors
- Book appointments
- View all records
- Save & load data using JSON file handling

The project demonstrates **OOP concepts, collections (lists, dicts), file handling, and exception handling**.

---

## 📂 Project Structure

```
HospitalManagementSystem/
├── appointment.py   # Appointment model
├── doctor.py        # Doctor model
├── hospital.py      # Core hospital management system
├── main.py          # Menu-driven CLI app
├── patient.py       # Patient model
├── person.py        # Base class for common attributes
└── hospital_data.json (auto-created after saving)
```

---

## 🚀 How to Run

1. **Extract the ZIP**  
   Unzip `HospitalManagementSystem.zip` anywhere (Desktop, Documents, etc.).

2. **Open a terminal / command prompt**  
   Navigate to the extracted folder:
   ```bash
   cd HospitalManagementSystem
   ```

3. **Run the program**  
   ```bash
   python main.py
   ```
   (or `python3 main.py` if needed)

4. **Use the Menu**  
   Example interaction:
   ```
   🏥 HOSPITAL MANAGEMENT SYSTEM
   1. Add Patient
   2. Add Doctor
   3. Book Appointment
   4. View Patients
   5. View Doctors
   6. View Appointments
   7. Save & Exit
   ```

5. **Data Persistence**  
   - All records are saved in `hospital_data.json` when you exit.
   - Next time you run the program, it auto-loads previous data.

---

## 🛠️ Requirements
- Python 3.x  
- No external libraries (only uses Python's built-in `json` module).

---

## 📖 Concepts Covered
- **OOP:** Classes for `Person`, `Patient`, `Doctor`, `Appointment`
- **Inheritance:** `Patient` and `Doctor` extend `Person`
- **Collections:** 
  - Dictionary for patients & doctors
  - List for appointments
- **File Handling:** JSON save/load
- **Exception Handling:** Prevents duplicate appointments and invalid IDs


| Concept                | Where It’s Used                 | Example                                |
| ---------------------- | ------------------------------- | -------------------------------------- |
| **OOP (Classes)**      | Patients, Doctors, Appointments | `Patient("P1", "Alice", 30, "Flu")`    |
| **Inheritance**        | `Person` → `Patient` & `Doctor` | Reuse attributes (id, name, age)       |
| **List**               | Appointments                    | `[Appointment(...), Appointment(...)]` |
| **Dictionary**         | Store Patients & Doctors by ID  | `self.patients["P1"] → Alice`          |
| **Set** (optional)     | Ensure unique IDs               | Could track all `doctor_id`s           |
| **Tuple** (optional)   | Appointment details             | `(patient_id, doctor_id, time)`        |
| **File Handling**      | Save & load hospital data       | JSON file                              |
| **Exception Handling** | Prevent double bookings         | `"Doctor already booked!"`             |

---

✅ Perfect for interview demos — shows Python fundamentals + practical application.
