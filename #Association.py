#Association
class Doctor:

    def __init__(self, name: str):
        self.name = name


class Patient:

    def __init__(self, name: str):
        self.name = name
        self.doctor = None  

    def assign_doctor(self, doctor: Doctor):
        self.doctor = doctor

    def show_info(self):
        if self.doctor:
            print(f"Patient {self.name} is treated by Dr. {self.doctor.name}")


doc = Doctor("Smith")
patient = Patient("John")
patient.assign_doctor(doc)
patient.show_info()