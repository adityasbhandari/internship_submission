📄 Resume Data Analytics & Visualization System

📌 Internship Task – Data Science / Data Analytics (Veridia)

🔍 Project Overview

This project analyzes a large **resume dataset** to extract meaningful insights that help improve **recruitment strategies and organizational decision-making**.
It uses **automated data cleaning**, **exploratory data analysis**, **statistical hypothesis testing**, and **interactive dashboards** to provide recruiter-friendly insights.

🎯 Objectives
* Automate resume data cleaning & preprocessing
* Perform Exploratory Data Analysis (EDA)
* Build interactive dashboards for visualization
* Validate insights using statistical analysis
* Provide business recommendations backed by data
* (Optional) Predict candidate job category using ML

🛠 Tech Stack
* **Programming Language:** Python
* **Data Handling:** Pandas, NumPy
* **Visualization:** Plotly, Streamlit
* **Statistics:** SciPy
* **Machine Learning:** Scikit-learn
* **Dataset Source:** Kaggle – Resume Dataset


📁 Project Structure
resume-data-analytics/
│
├── Resume.csv
├── demo.py                # Streamlit dashboard
├── requirements.txt
└── README.md

📊 Dataset Description
* Contains resumes and corresponding job categories
* Includes technical and non-technical roles
* Used for analyzing resume patterns, skills, and trends

🔄 Automated Data Cleaning Pipeline
✔ Duplicate removal
✔ Resume length calculation
✔ Text normalization (lowercase, special character removal)
✔ Feature engineering for analysis

This ensures consistent and reusable preprocessing without manual effort.

📈 Exploratory Data Analysis (EDA)
Key analyses performed:
* Resume distribution across job categories
* Resume length statistics
* Department-wise resume comparison
* Keyword frequency analysis

📉 Statistical Analysis
**Hypothesis Tested:**
> Resume length differs across job categories
* **Test Used:** One-way ANOVA
* **Result:** p-value < 0.05
* **Conclusion:** Resume patterns vary significantly by role
This supports **role-specific recruitment strategies**.

📊 Interactive Dashboard
Built using **Streamlit + Plotly** with:
* “All Resumes” overview tab
* Department-wise analysis tabs
* Resume length distributions
* Top skills/keywords visualization
* Key recruitment metrics (KPIs)


This demonstrates feasibility of **automated resume screening**.
## 💼 Business Recommendations
* Implement role-specific resume screening criteria
* Use keyword-based skill filtering for faster shortlisting
* Adopt automated resume classification to reduce manual effort
* Optimize hiring strategy based on department-wise data trends
* Use continuous analytics pipeline for scalable recruitment

▶️ How to Run the Projec
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run Dashboard
streamlit run demo.py

Ensure `Resume.csv` is present in the `data/` folder.

🚀 Future Enhancements
* Skill-based search inside resumes
* Download filtered data
* Advanced ML models
* Cloud deployment

 Author
Aditya Bhandari


