import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import graphviz
from graphviz import Graph
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


from acquire import get_connection, new_telco_data, get_telco_data
from prepare import clean_telco, train_validate_test_split






def run_model():
   
    df = get_telco_data()
    
    #clean the data
    
    df = clean_telco(df)

    # train, validate, split the data
    
    train, validate, test = train_validate_test_split(df, seed=123)
    
    
    
    # Select features to be used in the model
    cols = ['has_fiber_optic', 
            'tch_support_no',
            'monthly_contract',
            'no_partner_depend',
            'pmt_electronic_check',
           'online_sec_bkup']

    X = test[cols]
    y = test.churn
    
    # Create and fit the model
    forest = RandomForestClassifier(bootstrap=True, 
                            class_weight=None, 
                            criterion='gini',
                            min_samples_leaf=1,
                            n_estimators=100,
                            max_depth=10, 
                            random_state=123).fit(X, y)

    # Create a DataFrame to hold predictions
    results = pd.DataFrame(
        {'Customer_ID': test.customer_id,
         'Actual_Churn': test.churn,
         'Model_Predictions': forest.predict(X),
         'Model_Probabilities': forest.predict_proba(X)[:,1]
        })

    # Generate csv
    results.to_csv('model_results.csv')

    return results