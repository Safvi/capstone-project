# Project Title: Patient Demographics, Readmission Rates, and Financial Insights Analysis

**Date:** September, 2025  
**Prepared For:** [Capstone Project]

---

## 1. 📝 Executive Summary

This report provides an in-depth analysis of patient demographics, readmission rates, and financial trends derived from hospital data. By examining key visualizations developed in Power BI, the report highlights critical healthcare patterns based on gender, age, diagnosis, and insurance status.

The findings offer valuable insights for decision-makers seeking to improve patient care strategies, reduce readmissions, and optimize cost-efficiency in healthcare services.

---

## 2. Objectives

- Analyze demographic trends by age, gender, and diagnosis.
- Identify diagnoses with the highest readmission rates.
- Understand financial contributions and disparities by diagnosis, gender, and insurance status.
- Provide data-driven recommendations to improve healthcare delivery and resource allocation.

---

## 3. Data Sources

The analysis was based on the following datasets:
- **patients.csv**
- **doctors.csv**
- **visits.csv**
- **billing.csv**
- **final_dataset.csv**


After cleaning and preprocessing, these datasets were merged into a single integrated dataset used for the Power BI dashboard and statistical analysis.

---

## 4. Key Visuals & Analysis

### 🔹 Visual 1: Count of Gender by Diagnosis and Age Group

#### **Hypothesis:** 
The distribution of patients by gender, across different diagnoses and age groups, reveals specific demographic risk patterns, and tendencies for certain conditions, helping identify which groups are more affected and influencing healthcare demands.

- **Finding:** 
The distribution of patients across age groups and diagnoses indicates that middle-aged and older adults (45–59 and 60–74) constitute the majority of the patient population for most diagnoses. This is particularly evident in chronic conditions like Hypertension and Diabetes, which show higher prevalence in these age groups, aligning with established clinical patterns.
In contrast, conditions like Infection and Allergy show broader distribution, including younger age groups such as 18–29 and even Under 18, indicating that these ailments are not age-specific and can affect a wide demographic.
This demographic segmentation reveals specific risk trends and helps healthcare providers anticipate demand by age and gender, ensuring better-targeted interventions and resource allocation.


---

### 🔹 Visual 2: Average Readmission by Diagnosis

#### **Hypothesis:** 
Specific diagnoses are significantly correlated with higher average readmission rates, suggesting possible issues in treatment indicating potential gaps in post-discharge care or disease management for these conditions.

- **Finding:** The average readmission rates provide insight into how well certain diagnoses are managed post-discharge. Diagnoses such as Asthma and Flu show relatively higher average readmission rates, suggesting potential issues with the continuity of care, such as inadequate follow-up, recurrence of symptoms, or poor patient adherence to prescribed treatment.
Meanwhile, Diabetes, Hypertension, and Injury reflect lower readmission averages, potentially indicating more effective outpatient management or less frequent acute episodes requiring re-hospitalization.
From a clinical perspective, targeted efforts to enhance post-discharge care—particularly for Asthma and Flu patients—may significantly reduce hospital burden and improve patient outcomes.

- **Implication:** Post-discharge programs should be prioritized for Asthma and Flu patients.

---

### 🔹 Visual 3: Sum of Amount Paid by Diagnosis and Age Group

#### **Hypothesis:** 
The total amount paid varies by diagnosis, and these costs differ further across different age groups.


- **Finding:** 
Financial analysis across diagnoses shows that chronic conditions such as Diabetes and Hypertension are the leading contributors to total healthcare costs. This is particularly true among the older age groups (45–74), further emphasizing the financial strain of managing chronic diseases in aging populations.
Asthma also contributes notably to healthcare expenditure but shows a broader age group distribution. This may be attributed to its early onset and long-term management requirements.
The findings underscore the need for effective chronic disease management strategies to curb long-term costs and reduce the economic burden on healthcare systems.

---

### 🔹 Visual 4: Amount Paid by Gender & Diagnosis (Table View)

#### **Hypothesis:**
While some diagnoses will have similar costs across different gender categories, others may show notable financial disparities due to varying prevalence, treatment pathways, or disease severity.


- **Finding:** 
A detailed breakdown of the amount paid by gender categories reveals significant disparities in financial contributions across diagnoses. Notably, Polygender individuals appear to incur higher costs in diagnoses such as Hypertension and Flu, possibly reflecting more frequent healthcare utilization or differences in treatment pathways.
While Male and Female patients contribute significantly, the inclusion of non-binary and gender-diverse categories highlights the importance of considering gender diversity in health economics. Certain diagnoses like Asthma, Injury, and Flu exhibit substantial costs among Agender, Polygender, and Genderqueer patients.
This analysis supports a more inclusive approach to healthcare planning, acknowledging that gender-diverse populations may experience unique healthcare needs and financial burdens that warrant further exploration.


---

### 🔹 Visual 5: Average Amount Paid by Insurance Status (Insured vs. Self-Pay)

#### **Hypothesis:**
Patients without insurance (Self-pay) will incur a significantly higher average amount paid compared to insured patients, highlighting disparities in pricing structures or negotiated rates.

- **Finding:** 
There is a clear disparity in average amount paid between Insured and Self-pay patients, with self-pay individuals incurring higher costs (~$1.9K vs. ~$1.7K). This likely stems from the absence of negotiated insurance discounts, leading to self-pay patients bearing the brunt of full-cost healthcare services.
This financial inequality highlights the vulnerability of uninsured patients and reinforces the importance of expanding access to insurance or implementing financial aid mechanisms to mitigate the cost burden on these individuals.
From a policy perspective, these insights support advocacy for equitable pricing structures and improved coverage for vulnerable populations.


---

## 5. Summary of Key Insights

- **Middle-aged and older adults** dominate most diagnoses, especially for chronic conditions.
- **Asthma and Flu** are the top diagnoses for readmissions — requiring better patient education and discharge follow-up.
- **Diabetes and Hypertension** have the highest total treatment costs, despite lower readmission rates.
- **Gender-based analysis** reveals that some gender identities experience a disproportionate financial burden.
- **Insurance status** significantly affects average cost, disadvantaging self-pay patients.

---

## 6. Recommendations

- Strengthen chronic disease management for 45+ age groups.
- Develop targeted post-discharge care programs for Asthma and Flu patients.
- Investigate gender-based cost disparities to inform inclusive healthcare initiatives.
- Offer financial support or payment flexibility to self-pay patients.

---

## 7. Appendix

- Data cleaning and transformation steps are available in the `/notebooks` folder.
- The Power BI dashboard is saved in `/dashboards/hospital_dashboard.pbix`.
- Detailed pipeline execution logs are in `/logs/pipeline_log.ipynb`.

---

> 📄 _For project structure, scripts, and further documentation, refer to the main [README.md](../README.md) in the root directory._

