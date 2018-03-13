
# coding: utf-8

# In[ ]:


"""
In summary, the required conversions are as follows:

The Name column should be split into separate First Name and Last Name columns.
The DOB data should be re-written into DD/MM/YYYY format.
The SSN data should be re-written such that the first five numbers are hidden from view.
The State data should be re-written as simple two-letter abbreviations.



"""


# In[ ]:


import os
import csv
import datetime


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

employer_id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []

csvpath = os.path.join("/Users/AP/LearnPython/Python/Resources/employee_data1.csv" )
with open(csvpath, newline = "") as employer_data:
    csvreader = csv.reader(employer_data, delimiter=",")
        
        for row in csvreader:
            
            employer_id = employer_id + [row["Emp ID"]]
            
            splitname = [row["Name"]].split(" ")
            
            first_name = first_name + [splitname[0]]
            
            last_name = last_name + [splitname[1]]
            
            dob = datetime.strptime(row["DOB"], "%Y-%m-%d")
            
            dob = dob.strftime("%d-%m-%y")
            
            #store info into new row called dob
            #how to mask digits of ssn, in form of an asterisk
            #how to use the abberviations from the dictionary
                #use zip function to combine all of the values (refer to problem from class)
                
            
            
            

