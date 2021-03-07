import pandas as pd
import numpy as np
import os

### from acquire.py

from env import host, user, password
from pydataset import data
from acquire import get_connection, new_telco_data, get_telco_data

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer



# clean data followed by creating train/validate/test function

def clean_telco(df):
    '''
    clean_telco will take a dataframe acquired as df and remove columns that are:
    duplicates,
    have too many nulls,
    and will fill in the missing values in total_charges as 0 since those customers are in the first month of  contract
    We will be encoding gender, paperless billing, contract type, internet type, streaming tv, movies, paperless billing, contract type, and payment type.
    
    return: single cleaned dataframe
    '''
    df.drop_duplicates(inplace=True)
    
     # Converting the total charges column to a numeric type from object
    df["total_charges"] = pd.to_numeric(df.total_charges, errors='coerce')
    
    # Fill NaN values in total_charges column with 0
    df['total_charges'] = df['total_charges'].fillna(value=0)
    
     # create new average monthly charges column
    df['average_charges'] = round((df['total_charges']/df['tenure']), 2)
    
    
     # Encode gender in one column.
    df['churn'] = df['churn'].map( 
                   {'Yes':1 ,'No':0})
     # create new column for customer who have no partner and no dependents
    
    df['no_pd'] = (df['partner'] == 'No') & (df['dependents'] == 'No')
    
    # encode above boolean column into 0 or 1

    df.no_pd = df.no_pd.replace({True: '1', False: '0'})
    
    # phone_service and multiple_lines
    df['phone_lines'] = (df['phone_service'] == 'Yes') & (df['multiple_lines'] == 'Yes')
    
    # encode above boolean column into 0 or 1

    df.phone_lines = df.phone_lines.replace({True: '1', False: '0'})
    
    # create new column for customer who have streaming_tv & streaming_movies
    df['stream_tv_mov'] = (df['streaming_tv'] == 'Yes') & (df['streaming_movies'] == 'Yes')
    
    # encode above boolean column into 0 or 1

    df.stream_tv_mov = df.stream_tv_mov.replace({True: '1', False: '0'})
    
    # create new column for customer who have online_security & online_backup
    df['online_sec_bkup'] = (df['online_security'] == 'Yes') & (df['online_backup'] == 'Yes')
    
    # encode above boolean column into 0 or 1

    df.online_sec_bkup = df.online_sec_bkup.replace({True: '1', False: '0'})
    
     # create dummy columns of encoded categorical variables
    dummies = pd.get_dummies(df[['gender', 'partner', 'dependents', 'device_protection','tech_support', 'paperless_billing', 'contract_type', 'internet_service_type', 'payment_type']], drop_first=False)
   
    # create a dropcols where all columns that were created into dummies will be dropped
    dropcols = ['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'multiple_lines', 'gender', 'partner', 'dependents', 'phone_service', 'device_protection','online_security', 'online_backup', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'contract_type', 'internet_service_type', 'payment_type']
    
    # drop cols from above
    
    df.drop(columns=dropcols, inplace=True)
    
    # rename columns

  
    df = pd.concat([df, dummies], axis=1)
    
    # rename columns
    
    df.columns = ['customer_id',
 'senior_citizen',
 'tenure',
 'monthly_charges',
 'total_charges',
 'churn',
 'average_charges',
 'no_pd',
 'phone_lines',
 'stream_tv_mov',
 'online_sec_bkup',
 'female',
 'male',
 'no_partner',
 'has_partner',
 'dependents_no',
 'dependents_yes',
 'device_protection_no',
 'device_protection_no_int',
 'device_protection_yes',
 'tch_support_no',
 'tch_support_no_int',
 'tch_support_yes',
 'paperless_billing_no',
 'paperless_billing_yes',
 'monthly_contract',
 'one_yr_contract',
 'two_yr_contract',
 'has_dsl',
 'has_fiber_optic',
 'no_internet',
 'pmt_bank transfer',
 'pmt_cc',
 'pmt_electronic_check',
 'pmt_mailed_check']

    

    return df


def train_validate_test_split(df, seed=123):
    train_and_validate, test = train_test_split(
        df, test_size=0.2, random_state=seed, stratify=df.churn
    )
    train, validate = train_test_split(
        train_and_validate,
        test_size=0.3,
        random_state=seed,
        stratify=train_and_validate.churn,
    )
    return train, validate, test