import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Load data from csv file
purchase_behaviour_data = pd.read_csv('QVI_purchase_behaviour.csv')

#Load data from Excel file
transaction_data = pd.read_excel('QVI_transaction_data.xlsx', sheet_name='in')

# Summarize the data
def summarize_data():
    # Summary for purchase behaviour data
    print("Purchase Behaviour Data Summary:")
    print(f"Shape: {purchase_behaviour_data.shape}")
    print(purchase_behaviour_data.describe())
    print(purchase_behaviour_data.info())
    print()

    # Summary for transaction data
    print("Transaction Data Summary:")
    print(f"Shape: {transaction_data.shape}")
    print(transaction_data.describe())
    print(transaction_data.info())
    print()

# Call summarize_data function
summarize_data()