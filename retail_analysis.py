import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Load data from csv file
purchase_behaviour_data = pd.read_csv('QVI_purchase_behaviour.csv')

#Load data from Excel file
transaction_data = pd.read_excel('QVI_transaction_data.xlsx', sheet_name='in')