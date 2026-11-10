# COVID-19 Data Analysis with Python

**Project Type:** Exploratory Data Analysis (EDA), Statistical Analysis & Data Visualization  
**Dataset:** Our World in Data (OWID) COVID-19 Dataset  
**Tools:** Python, NumPy, Pandas, Matplotlib, Seaborn, Jupyter Notebook

## Project Overview

This project performs an exploratory and statistical analysis of global COVID-19 data, with a special focus on Bangladesh.

The objective is to understand the spread of COVID-19, analyze death trends, investigate vaccination progress, explore relationships between variables, and identify meaningful patterns through data visualization.

## Objectives

- Analyze global COVID-19 cases and deaths.
- Investigate Bangladesh's COVID-19 situation.
- Examine vaccination progress and coverage.
- Calculate Case Fatality Rate (CFR).
- Perform descriptive and correlation analysis.
- Identify countries with the highest reported cases and deaths.
- Generate meaningful visualizations and statistical findings.

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Project Structure

```text
covid19-data-analysis/
├── data/
│   ├── covid-data.csv
│   └── covid-analysis-ready.csv
├── notebooks/
│   └── covid_analysis.ipynb
├── visualizations/
│   └── Generated charts
├── reports/
│   ├── final_project_report.md
│   ├── final_project_report.html
│   └── Statistical CSV reports
├── README.md
└── requirements.txt
```

## Key Analysis

1. Data loading and inspection
2. Data cleaning and preprocessing
3. Exploratory Data Analysis
4. Feature engineering
5. Global COVID-19 trend analysis
6. Bangladesh COVID-19 analysis
7. Vaccination analysis
8. Descriptive statistical analysis
9. Correlation analysis
10. Final report generation

## Visualizations

The project generates visualizations covering:

- Global COVID-19 cases trend
- Global COVID-19 deaths trend
- Bangladesh cases and deaths trends
- Top 10 countries by confirmed cases
- Top 10 countries by deaths
- Bangladesh vaccination statistics
- Vaccination coverage comparison
- COVID-19 correlation heatmap
- Testing versus cases relationship

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/covid19-data-analysis.git
cd covid19-data-analysis
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the environment on macOS/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open `notebooks/covid_analysis.ipynb` and run the cells.

## Dataset

The dataset is sourced from Our World in Data:

https://ourworldindata.org/coronavirus

## 📄  Reports

The `reports/` directory contains statistical summaries, country-wise analysis, Bangladesh analysis, vaccination findings, and the final project report.
[View Full Project Report (PDF)](reports/COVID-19%20Data%20Analysis%20Report.pdf)

[View HTML Report](reports/final_project_report.html)

## Limitations

- COVID-19 reporting practices vary across countries.
- Missing values may affect some analyses.
- Reported cases and deaths may not represent the actual number of infections and deaths.
- Correlation does not imply causation.
- Country comparisons may be affected by differences in population and reporting dates.

## Author

**Your Name**  
Computer Science and Engineering  
GitHub: https://github.com/rifat9754
