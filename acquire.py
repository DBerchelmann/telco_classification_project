import pandas as pd
import numpy as np
import os
# acquire
from env import host, user, password
from pydataset import data

# visualize
import seaborn as sns
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(11, 9))
plt.rc('font', size=13)

# turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")

os.path.isfile('telco_df.csv')


# Create helper function to get the necessary connection url.
def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

    

# Use the above helper function and a sql query in a single function.
def new_telco_data():
    '''
    This function reads data from the Codeup db into a df.
    '''
    telco_sql = "SELECT * \
                 FROM customers \
                 JOIN contract_types USING(contract_type_id) \
                 JOIN internet_service_types USING(internet_service_type_id)\
                 JOIN payment_types USING(payment_type_id);"    
    return pd.read_sql(telco_sql, get_connection('telco_churn'))

def get_telco_data(cached=False):
    '''
    This function reads in telco churn data from Codeup database and writes data to
    a csv file if cached == False or if cached == True reads in telco df from
    a csv file, returns df.
    '''
    if cached == False or os.path.isfile('telco_df.csv') == False:
        
        # Read fresh data from db into a DataFrame.
        df = new_telco_data()
        
        # Write DataFrame to a csv file.
        df.to_csv('telco_df.csv')
        
    else:
        
        # If csv file exists or cached == True, read in data from csv.
        df = pd.read_csv('telco_df.csv', index_col=0)
        
    return df