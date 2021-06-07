import numpy as np 
import pandas as pd 
import os 
from decouple import config
import json

COLS_TO_USE = json.loads(config('COLS_TO_USE'))
FILE_NAME = config('TRACE_DATA_FILE_NAME')
LIST_IDS_TO_DELETE = json.loads(config('USERS_IDS_TO_DELETE'))
print(LIST_IDS_TO_DELETE)

nan_value = float("NaN")

df = pd.read_excel(FILE_NAME, usecols= COLS_TO_USE)

# Get user id as case id
df['case_id'] = df['Description'].str.split("'").str[1]
# Fix timestamp  format 
df['timestamp'] = df['Time'].str.replace(r',', '')
# extract the activity name from the event context 
df['activity'] = df['Event context'].str.split(':').str[1]

# Conditions to delete not important rows
system_logs = df[(df['Component'] == 'System') & (df['Event name'] == 'Course viewed')].index
system_course_reports = df[(df['Component'] == 'System') & (df['Event name'] == 'Course user report viewed')].index
system_grades_reports = df[(df['Event name'] == 'Grade user report viewed')].index

system_tours = df[(df['Component'] == 'User tours')].index
system_rewards = df[(df['Component'] == 'Stash')].index
system_grades = df[(df['Component'] == 'System') & (df['Event name'] == 'User graded')].index
system_evidences = df[(df['Component'] == 'System') & (df['Event name'] == 'Evidence created.')].index
system_rewards2 = df[(df['Component'] == 'Page') & (df['Event context'] == 'Page: Reward')].index
system_profile = df[(df['Component'] == 'System') & (df['Event name'] == 'User profile viewed')].index
system_profile2 = df[(df['Component'] == 'System') & (df['Event name'] == 'User list viewed')].index
component_formun = df[(df['Component'] == 'Forum')].index
component_choise = df[(df['Component'] == 'Choice')].index


# Delete rows by conditions. 
df.drop(system_logs , inplace=True)
df.drop(system_tours , inplace=True)
df.drop(system_rewards , inplace=True)
df.drop(system_grades , inplace=True)
df.drop(system_evidences , inplace=True)
df.drop(system_rewards2 , inplace=True)
df.drop(system_profile , inplace=True)
df.drop(system_profile2 , inplace=True)
df.drop(system_course_reports , inplace=True)
df.drop(system_grades_reports , inplace=True)
df.drop(component_formun , inplace=True)
df.drop(component_choise , inplace=True)


# Extract status of the event name. 
df['Event name'] = df['Event name'].str.replace('.', '', regex=True)
df['Event name'] = df['Event name'].str.replace(' ', ':', regex=True)
df['Event name'] = df['Event name'].str[-10:]
df['Event name'] = df['Event name'].str.split(':').str[1]

# Rename columns to match event logs creteria 
df.rename(columns={'Component': 'resource', 'Event name': 'status'}, inplace=True)

# delete status 'uploaded' and 'created'
status_uploaded = df[(df['status'] == 'uploaded') | (df['status'] == 'created') | (df['status'] == 'posted')].index
df.drop(status_uploaded , inplace=True)


#delete empty rows
df.replace("", nan_value, inplace=True)
df.dropna(subset = ["activity", "status", "case_id", "timestamp"], inplace=True)

empty_rows= df[(df['activity'] == '') | (df['status'] == '') | (df['case_id'] == '')  | (df['timestamp'] == '')].index
df.drop(empty_rows , inplace=True)


# change status 

df['status'].loc[(df['resource'] == 'System') & (df['status'] == 'updated')] = 'completed'
df['status'].loc[(df['status'] == 'submitted')] = 'compleated'

# delete other status
status_not_view_or_compleated = df[(df['status'] != 'completed') & (df['status'] != 'viewed')].index
df.drop(status_not_view_or_compleated , inplace=True)

# delete case ids of teachers

#case_ids_teachers = df[(df['case_id'] == '4') | (df['case_id'] == '5') | (df['case_id'] == '8')  | (df['case_id'] == '12') | (df['case_id'] == '17') | (df['case_id'] == '18') | (df['case_id'] == '19') | (df['case_id'] == '21') | (df['case_id'] == '22') | (df['case_id'] == '23') | (df['case_id'] == '24')].index
#case_ids_teachers = df[(df['case_id'] == '5683') | (df['case_id'] == '0') | (df['case_id'] == '7')].index

case_ids_teachers_serie = df[df['case_id'].isin(LIST_IDS_TO_DELETE)].index 
df.drop(case_ids_teachers_serie, inplace=True)


# Delete innecesary columns 
df.drop(columns=['Description', 'Event context', 'Time'], inplace=True)

df.replace("", nan_value, inplace=True)
  
df.dropna(how='all', axis=1, inplace=True)

df.drop_duplicates(['resource', 'status', 'case_id', 'timestamp', 'activity'], keep='first', inplace=True)

# output file
compression_opts = dict(method='zip', archive_name='advanced_db_event_logs.csv') 
df.to_csv('advanced_db_out.zip', index=False,compression=compression_opts) 

df.head()

