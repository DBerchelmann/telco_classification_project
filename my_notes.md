<b>Friday workflow recap:</b>

* We set up our Trello Project Flow
* Our github repository was created & cloned to our local folder
* The README was created and is partially complete
     * still have the data dictionary and hypothesis to put in
    
* The .gitignore, acquire.py, prepare.py, & explore.py files were all created
     * .gitignore has been completed with the env.py while .acquire is complete and has been tested to make sure a data frame can be pull in
    
* The Final Jupyter Notebook was created and the main sections have been created and place-holders given for information
    

<b>Saturday to-do:</b>

* consult the syllabus to make sure all rubric points are being touched and completed <b>completed</b>

* maybe create seperate notebooks where we test out what we want to put in the acquire, prepare, and explore...keep from muddying up final notebook

* <font color = red>( Complete some initial data summarization (.info(), .describe(), .value_counts(), ...).Plot distributions of individual variables.)</font> <b> completed</b>

* Create . prepare file
    * go over check list
    
* train/split/validate function needs to be in prepared

* continue to make good notes as the project is worked on, taking note of the time needed to complete each section

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