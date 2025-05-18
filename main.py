from datetime import date

from classes import Patient, Medication, Address

patient = Patient(
    id=1,
    full_name="Jean Dupont",
    birth_date=date(1985, 6, 12),
    email="jean.dupont@example.com",
    address=Address(
        street="10 rue Victor Hugo",
        city="Paris",
        zip_code="75001"
    ),
    medications=[
        Medication(name="Paracétamol", dosage_mg=500.0, start_date=date(2024, 12, 1)),
        Medication(name="Ibuprofène", dosage_mg=200.0, start_date=date(2024, 11, 1), end_date=date(2024, 12, 1))
    ]
)

print(patient)
print(f"Âge du patient : {patient.age} ans")
print("Email validé :", patient.email)