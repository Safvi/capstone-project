#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import logging

# Setup logging
logging.basicConfig(
    filename='../logs/pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

print("Running data pipeline...")

try:
    os.system("jupyter nbconvert --to notebook --execute ../notebooks/01_clean_patients.ipynb")
    logging.info("Cleaned patients data")
    
    os.system("jupyter nbconvert --to notebook --execute ../notebooks/02_clean_doctors.ipynb")
    logging.info("Cleaned doctors data")

    os.system("jupyter nbconvert --to notebook --execute ../notebooks/03_clean_visits.ipynb")
    logging.info("Cleaned visits data")

    os.system("jupyter nbconvert --to notebook --execute ../notebooks/04_clean_billing.ipynb")
    logging.info("Cleaned billing data")

    os.system("jupyter nbconvert --to notebook --execute ../notebooks/05_integrate_data.ipynb")
    logging.info("Integrated all data")

except Exception as e:
    logging.error("Pipeline failed: " + str(e))

print("Pipeline completed.")


# In[ ]:




