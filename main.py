import pandas as pd

# Load the processed COVID-19 dataset
df = pd.read_csv("data/covid-analysis-ready.csv")

# Display basic dataset information
print("COVID-19 Dataset Analysis")
print("-------------------------")
print("Total Records:", len(df))
print("Total Countries:", df["country"].nunique())
print("Date Range:", df["date"].min(), "to", df["date"].max())

# Find the latest record for each country
latest_data = df.sort_values("date").groupby("country").tail(1)

# Find the top 5 countries by total cases
top_countries = latest_data.nlargest(5, "total_cases")

print("\nTop 5 Countries by Total Cases:")
print(top_countries[["country", "total_cases"]])
