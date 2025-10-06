import pandas as pd
import random
from datetime import timedelta
import os

# Set paths
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
visits_path = os.path.join(base_path, 'data', 'raw', 'visits.csv')
billing_output_path = os.path.join(base_path, 'data', 'raw', 'billing.csv')

# Load visits.csv
visits = pd.read_csv("C:/Users/szeer/OneDrive/Desktop/Capstone Project/data/raw/visits.csv")


# Ensure visit_date is datetime
visits['visit_date'] = pd.to_datetime(visits['visit_date'])

# Create billing data
billing = visits[['visit_id', 'visit_date', 'cost']].copy()
billing['billing_id'] = range(1, len(billing) + 1)

# Simulate insurance providers
insurance_providers = ['Blue Cross', 'United Health', 'Aetna', 'Cigna', 'Self-Pay']
billing['insurance_provider'] = [random.choice(insurance_providers) for _ in range(len(billing))]

# Simulate amount_paid = 80% to 100% of cost
billing['amount_paid'] = billing['cost'].apply(lambda x: round(x * random.uniform(0.8, 1.0), 2))

# Simulate payment_date = visit_date + 0–30 days
billing['payment_date'] = billing['visit_date'] + pd.to_timedelta(
    [random.randint(0, 30) for _ in range(len(billing))], unit='D'
)

# Finalize columns
billing = billing[['billing_id', 'visit_id', 'insurance_provider', 'amount_paid', 'payment_date']]

# Save to CSV
billing.to_csv(billing_output_path, index=False)
print("✅ billing.csv generated based on visits.csv")
