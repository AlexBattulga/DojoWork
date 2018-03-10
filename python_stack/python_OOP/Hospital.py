class Patient(object):
    patient_count = 0
    def __init__(self, name, allergies):
        self.id = Patient.patient_count
        self.name = name
        self.allergies = allergies
        self.bed_num = None
        Patient.patient_count += 1

    def display(self):
        print 'Full Name: {}\nAllergic to: {}'.format(self.name, self.allergies)
        return self
class Hospital(object):
    def __init__(self, hospital_name, capacity):
        self.patients = []
        self.hospital_name = hospital_name
        self.capacity = capacity
        self.beds = self.get_a_bed()

    def get_a_bed(self):
        beds = []
        for i in range(1, self.capacity):
            beds.append({
                "bed_id": i,
                "available": True
            })
        return beds

    def admit(self, new_patient):
        if len(self.patients) <= self.capacity:
            self.patients.append(new_patient)
            for i in range(0, len(self.beds)):
                if self.beds[i]["available"]:
                    new_patient.bed_num = self.beds[i]["bed_id"]
                    self.beds[i]["available"] = False
                    break
            print "Patient {} admitted to bed #{}".format(new_patient.name, new_patient.bed_num)
            return self
        else:
            print "hospital is at full capacity"
            return self

    def discharge(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                for bed in self.beds:
                    if bed["bed_id"] == patient.bed_num:
                        bed["Available"] = True
                        break

                self.patients.remove(patient)
                return "Patient #{} sucessfully discharged.  Bed #{} now available".format(patient.id, patient.bed_num)
        return "Patient not found"

hospital = Hospital("Medical Clinic", 5)
patient1 = Patient("Alex Broyles", "nuts")
patient2 = Patient("Julie Enderson", "egg")
patient3 = Patient("Roberto Carlos", "peanuts")
patient4 = Patient("Bob Hughes", "mayo")
patient5 = Patient("Donald Duck", "egg")

# hospital.admit(patient1).admit(patient2).admit(patient3).admit(patient4).discharge(patient3).admit(patient5)
hospital.admit(patient3).discharge(patient2)
patient1.display()
