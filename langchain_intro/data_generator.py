# Correcting the mismatch and generating the full dataset
import pandas as pd 
import numpy as np 
# Let's ensure each list has exactly 500 elements

# Reuse the original data structure to extend for 500 entries
# names = ["Joseph Johnson", "Jason Williams", "Jesse Gordon", "Heather Smith", "Kayla Hunter DDS"]
# schools = ["Johns Hopkins", "Mayo Clinic", "David Geffen", "NYU", "Davinci Med"]
# salaries = [200000, 180000, 150000, 220000, 210000]
#
# # Generate the full data
# full_data = {
#         "physician_name": [np.random.choice(names) for _ in range(500)],
#         "physician_id": list(range(500)),
#         "physician_dob": [pd.Timestamp('1950-01-01') + pd.DateOffset(months=np.random.randint(0, 12 * 70)) for _ in range(500)],
#         "physician_grad_year": [pd.Timestamp('1980-01-01') + pd.DateOffset(months=np.random.randint(0, 12 * 40)) for _ in range(500)],
#         "medical_school": [np.random.choice(schools) for _ in range(500)],
#         "salary": [np.random.choice(salaries) for _ in range(500)]
# }
#
# df_full_physicians = pd.DataFrame(full_data)
#
# # Save to CSV file
# full_csv_path = "data/physicians.csv"
# df_full_physicians.to_csv(full_csv_path, index=False)
#
# df_full_physicians.head(), df_full_physicians.shape, full_csv_path
# payer_data = {
#         "payer_id": [0, 1, 2, 3, 4],
#         "payer_name": ["Medicaid", "UnitedHealthcare", "Aetna", "Cigna", "Blue Cross"]
# }
#
# df_payers = pd.DataFrame(payer_data)
#
# # Save to CSV file
# payers_csv_path = "data/payers.csv"
# df_payers.to_csv(payers_csv_path, index=False)
#
# df_payers.head(), payers_csv_path
import random

# Random data generation for visits.csv
random.seed(0)  # For reproducibility

# Sample data sizes and ranges
num_records = 9998
hospital_ids = [10, 20, 30, 40, 50]  # Example hospital IDs
payer_ids = [0, 1, 2, 3, 4]  # Corresponding to payers.csv created previously
admission_types = ['Elective', 'Emergency', 'Urgent']
test_results = ['Inconclusive', 'Normal', 'Abnormal']
visit_statuses = ['ON_VISIT', 'DISCHARGED']

# Creating random data
visits_data = {
        "visit_id": list(range(num_records)),
        "patient_id": [random.randint(1, 3000) for _ in range(num_records)],  # Assuming 3000 unique patients
        "date_of_admission": [pd.Timestamp('2020-01-01') + pd.DateOffset(days=random.randint(0, 700)) for _ in range(num_records)],
        "room_number": [random.randint(100, 500) for _ in range(num_records)],
        "admission_type": [random.choice(admission_types) for _ in range(num_records)],
        "chief_complaint": ["General checkup" if random.random() < 0.5 else "Special consultation" for _ in range(num_records)],
        "treatment_description": ["Routine exam" if random.random() < 0.5 else "Emergency surgery" for _ in range(num_records)],
        "test_results": [random.choice(test_results) for _ in range(num_records)],
        "discharge_date": [pd.Timestamp('2020-01-02') + pd.DateOffset(days=random.randint(1, 704)) for _ in range(num_records)],
        "physician_id": [random.randint(1, 500) for _ in range(num_records)],  # Assuming 500 physicians
        "hospital_id": [random.choice(hospital_ids) for _ in range(num_records)],
        "payer_id": [random.choice(payer_ids) for _ in range(num_records)],
        "billing_amount": [random.randint(200, 5000) for _ in range(num_records)],
        "visit_status": [random.choice(visit_statuses) for _ in range(num_records)]
}

# Ensuring discharge date is after admission
visits_data["discharge_date"] = [max(adm, dchg) for adm, dchg in zip(visits_data["date_of_admission"], visits_data["discharge_date"])]

df_visits = pd.DataFrame(visits_data)

# Save to CSV file
visits_csv_path = "data/visits.csv"
df_visits.to_csv(visits_csv_path, index=False)

df_visits.head(), df_visits.shape, visits_csv_path
