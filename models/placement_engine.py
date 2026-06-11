import pandas as pd

companies = pd.read_csv(
    "datasets/companies.csv"
)

def get_companies():
    return list(companies["company"])
