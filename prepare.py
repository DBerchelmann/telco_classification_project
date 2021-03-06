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
    
     # Encode gender in one column.
    df['churn'] = df['churn'].map( 
                   {'Yes':1 ,'No':0})
    
    # Converting the total charges column to a numeric type from object
    df["total_charges"] = pd.to_numeric(df.total_charges, errors='coerce')
    
    # Fill NaN values in total_charges column with 0
    df['total_charges'] = df['total_charges'].fillna(value=0)
    
    # create dummy columns of encoded categorical variables
    dummies = pd.get_dummies(df[['gender', 'partner', 'dependents', 'phone_service', 'device_protection','online_security', 'online_backup', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'contract_type', 'internet_service_type', 'payment_type']], drop_first=False)
   
    # create a dropcols where all columns that were created into dummies will be dropped
    dropcols = ['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'multiple_lines', 'gender', 'partner', 'dependents', 'phone_service', 'device_protection','online_security', 'online_backup', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'contract_type', 'internet_service_type', 'payment_type']
    
    
    df.drop(columns=dropcols, inplace=True)
    
    return pd.concat([df, dummies], axis=1)


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