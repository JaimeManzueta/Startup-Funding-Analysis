import pandas as pd

# Importing The Raw_data:
raw_data = pd.read_csv(r"C:\Users\Jaime Manzueta\Startup-Funding-Analysis\raw_data\us_startup_funding_2019_2026_sample.csv").convert_dtypes()
print("Information Of The Raw Data----------------------------")
print(raw_data.info())


# Showing the first 10 companies from the dataset to see the dataset
print(raw_data.head(10))
print("\n")

# Inspect Structure & Data Types-----------------------------------------------------------------------------------


# Dropping columns
dropped_columns = raw_data.drop(columns=["company_domain","news_mentions","news_source","news_url","news_excerpt","fliar_profile_url"])

# Changing the columns names 
new_columns_name = {
    "round_id": "id",
    "company_name": "company_name",
    "announced_date": "announced_date",
    "year": "year_announced",
    "country": "country",
    "city": "city",
    "state": "state",
    "sector": "company_sector",
    "founded_year": "founded_year",
    "stage": "stage",
    "amount_usd": "amount_usd",
    "amount_status": "amount_status",
    "lead_investor": "lead_investor",
    "investor_count": "investor_count",
    "fliar_profile_url": "fliar_profile_url"
}


data = dropped_columns.rename(columns=new_columns_name)
print(data)

print("\n")

# Dectecting missing data 
print("Detecting Missing Data")
print(data.isna().sum())

# Dectecting duplicating data 




