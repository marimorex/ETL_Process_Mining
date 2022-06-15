import numpy as np 
import pandas as pd 
import os 
from decouple import config
from pycelonis import get_celonis

CELONIS_URL = config('CELONIS_URL')
API_TOKEN = config('API_TOKEN')

celonis = get_celonis(celonis_url= CELONIS_URL,api_token= API_TOKEN)
print("Successsull Login")

df = pd.read_csv(config('OUTPUT_FILE_NAME') + '.csv')

column_config = [{'fieldLength': 20, 'columnName': 'resource', 'columnType': 'STRING'}, {'fieldLength': 20, 'columnName': 'status', 'columnType': 'STRING'}, {'columnName': 'case_id', 'columnType': 'INTEGER'}, {'columnName': 'timestamp', 'columnType': 'DATE'}, {'fieldLength': 20, 'columnName': 'activity', 'columnType': 'STRING'}]
column_config_grades = [{'columnName': 'case_id', 'columnType': 'STRING'}, {'columnName': 'final_mark', 'columnType': 'FLOAT'}]

#### CELONIS_DATA_POOL_NAME
print(config('CELONIS_DATA_POOL_NAME'))
dp = celonis.pools
   
if config('CELONIS_DATA_POOL_NAME') not in dp.names:
    celonis.create_pool(config('CELONIS_DATA_POOL_NAME'))
    dp = celonis.pools
    
data_pool = dp.find(config('CELONIS_DATA_POOL_NAME'))  
print(data_pool)
print("data_pool configured")
#### -----------------------------

### CELONIS_DATA_MODEL_NAME
print(config('CELONIS_DATA_MODEL_NAME'))
dm = celonis.datamodels

if config('CELONIS_DATA_MODEL_NAME') not in dm.names:
    celonis.create_datamodel(config('CELONIS_DATA_MODEL_NAME'),data_pool)
    dm = celonis.datamodels

data_model = dm.find(config('CELONIS_DATA_MODEL_NAME'))  
print(data_model)
print("data_model configured")
### ----------------------------------

### CELONIS_WORKSPACE_NAME
print(config('CELONIS_WORKSPACE_NAME'))
ws = celonis.workspaces

if config('CELONIS_WORKSPACE_NAME') not in ws.names:
    celonis.create_workspace(config('CELONIS_WORKSPACE_NAME'), data_model)
    ws = celonis.workspaces

work_space = ws.find(config('CELONIS_WORKSPACE_NAME'))  
print(work_space)
print("work_space configured")
### -------------------------------

### CELONIS_ANALYSIS_NAME
print(config('CELONIS_ANALYSIS_NAME'))
analyses = celonis.analyses

if config('CELONIS_ANALYSIS_NAME') not in analyses.names:
    celonis.create_analysis(config('CELONIS_ANALYSIS_NAME'),work_space)
    analyses = celonis.analyses

analysis = analyses.find(config('CELONIS_ANALYSIS_NAME'))
print(analysis)
print("analysis configured")
### --------------------------------


#### DATA_UPLOAD
data_pool.create_table(table_name=config('CELONIS_TABLE_NAME'),
                       df_or_path=df,
                       if_exists="drop",
                       column_config=column_config)

if config('CELONIS_TABLE_NAME') in data_model.tables.names:
    data_model_table = data_model.tables.find(config('CELONIS_TABLE_NAME'))
    data_model_table.delete()
    data_model = dm.find(config('CELONIS_DATA_MODEL_NAME')) 

data_model.add_table_from_pool(table_name=config('CELONIS_TABLE_NAME'), 
                               alias= config('CELONIS_TABLE_NAME'),
                               reload="FORCE_COMPLETE")

data_model.create_process_configuration(
        case_table=None,
        activity_table=config('CELONIS_TABLE_NAME'),
        case_column="case_id",
        activity_column="activity",
        timestamp_column="_CELONIS_CHANGE_DATE",
        sorting_column="status")

data_model.reload(tables=config('CELONIS_TABLE_NAME'))

print("Events Logs sent and Model configured, Analysis available in celonis platform")
### -----------------------------------------