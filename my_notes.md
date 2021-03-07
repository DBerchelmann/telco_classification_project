<b>Friday workflow recap:</b>

* We set up our Trello Project Flow
* Our github repository was created & cloned to our local folder
* The README was created and is partially complete
     * still have the data dictionary and hypothesis to put in
    
* The .gitignore, acquire.py, prepare.py, & explore.py files were all created
     * .gitignore has been completed with the env.py while .acquire is complete and has been tested to make sure a data frame can be pull in
    
* The Final Jupyter Notebook was created and the main sections have been created and place-holders given for information
    

<b>Saturday work-flow recap:</b>

* consult the syllabus to make sure all rubric points are being touched and completed <b>completed</b>

* maybe create seperate notebooks where we test out what we want to put in the acquire, prepare, and explore...keep from muddying up final notebook <b>complete</b>

* <font color = red>( Complete some initial data summarization (.info(), .describe(), .value_counts(), ...).Plot distributions of individual variables.)</font> <b> completed</b>

* Create . prepare file
    * go over check list <b>complete</b>
    
* train/split/validate function needs to be in prepared <b>complete</b>

* continue to make good notes as the project is worked on, taking note of the time needed to complete each section <b>complete</b>

* create the explore.py file

 Prepare Notes
 ---------------
 
 Drop duplicates first
 Drop these:
     payment_type_id
     internet_service_type_id
     contract_type_id
     customer_id
     multiple_lines
     
     
     
     

 Get dummies for the following:
 
     gender
     partner
     dependents
     phone_service
     online_security
     online_backup
     tech_support
     streaming_tv
     streaming_movies
     paperless_billing
     contract_type
     internet_service_type
     payment_type
     
    
* Decided to keep customer id for later on in exercise since we need an identifier

* should a new column be created that would be partner with fiber optic on month 2 month? (1 = Yes, 0 = No)


* should we create an average monthly charges column?


<b>Sunday to-do:</b>

- complete prepare (add extra columns?)
- fill out questions to be asked/hypos in README
- fill out prepare section of final notebook
- fill in prepare.py file
- create explore file, get observations down
- fill out explore section of notebook
- look at evaluate/modeling section
- go over rubric, gauge progress
- plan out Monday to-do

-create column where user is monthly, fiber-optic, has partner

df['monthly_fo_w/ptnr'] = df['']

Quick stats

 - 1869 total people churned out of 7043
 - customers churn most on month to month contract (1655)
 - customers churn most with phone service (1699)
 - gender churn is pretty much even (939-m, 930 f)
 - partner churn is highest for those with no partner (1200) 669 have partner
 - median tenure for churn is 10 months, mean is 17.9 months for all
 - churn is highest for those with no dependents (1543) 326 churned have dependents
 - churn is high for those with no tech support (1446)
 - streaming tv churn is a mix, almost half and half, not a player
 - streaming movies churn is mix, almost half and half, not a player
 - 1400 have paperless billing that churned, factor?
 - 1393 that churned are not senior citizens, seniors not churning as much
 - 1297 churned that have fiber optic
 - 1071 churned that have electronic check
 
 **Thoughts On Churn**
 Those most likely to churn are on month to month contracts, not seniors, no tech support, no partner/no dependents, on fiber optic, pay with Electronic check
 

def conditions(s):
    if (s['partner'] == 'No') & (s['dependents'] == 'No') & (s['contract_type'] == 'Month-to-month') & (s['internet_service_type'] == 'Fiber optic'):
        return 1
    else:
        return 0

df['no_partner_depend'] = df.apply(conditions, axis=1)

This returned a value count of 1222 people who churned out of 1869

By creating a new column based on those who have no partner or dependents, the total who churn is 1123.

Churn for those with no dependents was 1543

Churn for those with no partner was 1200

no dependents, no fiber, on month to month captures all those who churned

   # Encode gender in one column.
    df['no_pd_havefiber'] = df['no_pd_havefiber'].map( 
                   {'True':1 ,'False':0})
                   
Features I'll want to train on are (monthly contract, fiber internet, partner/dependents, tenure, average monthly bill)