# Process Mining Model to visualize and analyze the Learning Process - HYPE 13 UPPA 

# Content

## **[Introduction](#introduction)**
- [Requirements](#requirements)

## **[Project Hype 13](#project-hype-13)**
- [Context](#context)
- [Purpose](#purpose)

## **[Process Mining Model to visualize and analyze the Learning Process](#process-mining-model-to-visualize-and-analyze-the-learning-process)** 
- [Overview](#overview)
- [Data Sources](#data-source)
    - [Moodle Data Extraction](#moodle-data-extraction)
- [Data Transformation](#data-transformation)
    - [Example of Event Logs](#example-of-event-logs)
    - [Data Transformation Script](#data-transformation-script)
- [Process Mining](#process-mining)
    - [Data Analysis Script](#data-analysis-script)
    - [Benefits of the approach](#benefits-of-the-approach)
- [Data Visualization](#)

| Version and date of the document | V1 01/06/2022 |
| --- | --- |
| Author | [mgmexposito@univ-pau.fr]() |


# **Introduction** 

In online learning environments, the teacher provides students with a learning path to follow in order to acquire the expected competencies and skills. However, students' profiles are different as they can learn according to different learning paces or media content. Therefore, the actual learning path followed by each learner may vary from the initial path provided in the learning management system (LMS). The learning traces left by students in their learning environment could be exploited in order to better understand and guide learning processes. Unfortunately, with large-scale education, the analysis of different learning paths can be a complex task to be manually carried out by teachers. For this reason, our objective is to propose an approach to model, visualize, and analyze the most efficient learning process in order to improve students’ education experience and results. The approach adopted is based on the learning traces left by the students following their interactions with the Learning Management System (LMS). After collecting, processing, and storing these learning traces, Process Mining technologies are used to analyze the data through an exploration of the learning process, as well as the students’ learning paths. The first results obtained have made it possible to visualize the learning process, as well as the learning paths followed by each learner. They also provide analysis indicators for understanding and optimizing the learning process and the students’ paths in digital learning environments. These results allow the stakeholders (training managers, teachers, and students) to improve the way they teach and learn. This approach made it possible to comprehensively understand the learning processes and the learning paths of each learner, to visualize their differences, as well as their advantages and disadvantages. This allows teachers to have an integrated tool for analyzing learning traces through a monitoring, diagnostic, alert, and early intervention system in order to better promote the success of students.

- This repository is the technical representation of the following research paper  **[paper](https://aaee.net.au/wp-content/uploads/2021/11/REES_AAEE_2021_paper_311.pdf)**  developed as part of the third axis of the project HyPE13 “Support of Learning Analytics for asynchronous monitoring and continuous improvement process” more specifically the Livrable 6 “L6: Success with Learning Analytics (LA)”.


## **Requirements**

- Course deployed in the moodle platform
    - Access to the Moodle logs of the course 
- [Celonis Account](https://www.celonis.com/) 
- Python > 3.x
- Python Libraries
    - numpy 
    - pandas 
    - [pycelonis](https://celonis.github.io/pycelonis/1.7.0/getting_started/installation/) 


# **Project Hype 13**

## **Context** 

Following the exceptional health situation, several "brakes" were noted. We noticed that the sharing and reuse of existing resources (within a consortium of universities or not) were not well exploited. The idea is therefore to better exploit these resources and to build a common strategy for the development and use of resources. We will talk about hybridization to talk about teaching that is done in several ways (mix of live courses, provision, online assessment).

## **Purpose**

This project aims to offer a "hybrid" start to the school year (online access to courses and more...) to students. To do this, it is necessary to create an online course "format" that ensures maximum success for learners. It will therefore be necessary to provide support to teachers in the creation of their online courses. It will also be necessary to do personalized follow-up of the learners in order to mitigate the risks of abandonment and to guarantee the success of the learning process. It will be necessary to foresee a tool allowing teachers to evaluate the effectiveness of the device (in order to continuously improve it). In order to add value to the project, it will be necessary to create an impact indicator based on the reuse of the resources. Also, it would be necessary to think about the virtual mobility of courses (multiple universities, national, international, ...).

# **Process Mining Model to visualize and analyze the Learning Process**

## **Overview** 

The main goal of this model is to generate a generic approach. A step-by-step guide that helps institutions acknowledge all the concepts related to the implementation of Learning Analytics using Process Mining to visualize the learning process that takes place on an LMS. 

![Fig1.png](/images/fig1.png)

In general, to accomplish this goal is necessary to visualize the learning process, and for that, several steps need to be carried out. The first one is to collect all the interactions made by students on the LMSs with an specific structure and relevant information "[Data sources](#data-sources)", the next step is to transform that data into a new structure called Event Logs which is the entry point to the analysis phase [Data Transformation](#data-transformation), after this the process mining is applied and where will be possible to discover, monitor and improve real processes (learning processes) by extracting knowledge from these event logs, to understand how the learning process occur, what are the most common ways to learn that works for most students, what are the atypical ways to learn, what are the most successful and unsuccessful learning paths [Process Mining](#process-mining). 

## **Data Sources**

In order to visualize the learning process, it is necessary to extract all the relevant information referring to how these processes occur, and the places where such activities happen are systems like OLE Online Learning Environment, LMS Learning Management Systems, VLE Virtual Learning Environments, KMS Knowledge Management System. In those systems each click, view, answer, error, success, time consumed, resource downloaded, viewed, listened or score obtained, has an important meaning, and all of those interactions build some digital footprint, also called Learning Records which are the one's vitals to collect.

### **Moodle Data Extraction** 
We will extract the data from the moodle Logs in Excel format. As explained **[here](https://docs.moodle.org/400/en/Logs)**. 

## **Data Transformation** 

The process mining analysis starts with an ‘Event Log’ and inside this structure, a process is described as follows, a process consists of cases, a case consists of events such that each event relates to precisely one case and each sequence of activities executed for a case is a trace. Each line in the event log presents one event. Events within a case are ordered. Events can have attributes (e.g., activity, time, cost, resource, etc). The event log structure can be summarized as follows:
- Case ID: indicates at which case or instance belongs to an event or activity.
- Activity: Action captured by the event.
- Timestamp: Indicate the time when the event took place.

###  Example of Event Logs

| case_id | activity | timestamp | status |
| --- | --- | --- | --- |
|55138| Data Integration Introduction |12/01/21 08:23 |viewed|
|55138|Data Integration Introduction|12/01/21 08:23|completed|
|67108|Data Integration Introduction|12/01/21 08:32|viewed|
|67108|Data Integration Introduction|12/01/21 08:32|completed|
|67108|Data Integration Introduction|12/01/21 08:36|viewed|
|67108|Data Integration Introduction|12/01/21 08:38|viewed|
|67108|Data Integration Introduction|12/01/21 09:01|viewed|
|67108|Data Integration Introduction|12/01/21 09:01|completed|
|67108|Data Integration Introductions - slides|12/01/21 09:06|completed|
|67108|Data Integration Introductions - slides|12/01/21 09:06|viewed|
|67108|Data Integration Introduction|12/01/21 09:06|completed|
|---|---|---|---|
| --- | --- | --- | --- |
| | | | |


### **Data Transformation Script**

To construct the preceding event log, it was used Python programming language and the pandas library which is an open-source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

The python script **"etl.py"** developed was applied to the trace data (learning records) from the moodle platform. The main activities, performed in the transformation were the following:  

- Specify the useful columns from the trace data.
- Extract case Id, from the description column.
- Modify the timestamp format.
- Extract activity name from the event context column.
- Delete not relevant events, such as system events.
- Delete events performed by teachers and test users. 

The next step is to use the script **etl.py** to transform the data extracted from moodle, however before that, you need to modify the environment variables (.env file) according to your course, more specifically: 

- TRACE_DATA_FILE_NAME : name of the file extracted from moodle platform
- USERS_IDS_TO_DELETE : you can identify some ids that you wish to delete to not analyze those logs, for example teachers, staff or test users. 
- NAME_OF_COURSE : name of your course, as is displayed on the moodle platform. 

After this configuration: 
- Be sure to load the environment variables (.env file) to your environment. 
- Run the script  etl.py to transform the data from the moodle platform and get the event logs into the form of a zip file called output_event_logs_file.zip and inside this compress file you will find another file called the same way but with the CSV extension output_event_logs_file.csv (this is the event logs file). 

## **Process Mining** 

Once the data have been transformed to the necessary structure and is available in the required event log, it is possible to conduct three types of process mining techniques. The first one is “discovery”, this technique takes an event log and produces a model without using any a-priori information. The second type is “conformance”, with this an existing process model is compared with an event log of the same process; the conformance checking can be used to check if reality, as recorded in the log, conforms to the model and vice versa. The third type is “enhancement”, the main idea is to extend or improve an existing process model using information about the actual process recorded in the event log. 

Concerning the proposed model, one of the most suitable algorithms to implement in this step is the “discovery” type, since the current model is unknown, and is essential to build it and describe it; these are some of the tasks that this kind of algorithm would contribute to perform.

###  **Data Analysis Script** 

Descriptive Analysis: Using Process Mining -  Celonis API: [Celonis platform](https://www.celonis.com/) has an API available called [PyCelonis](https://celonis.github.io/pycelonis/1.7.0/getting_started/installation/) , which is a python package that allows connecting to Celonis from Python. Using this package it is possible to programmatically interact with Analyses, Workspaces, Data Models, Data Pools and other Celonis objects. The package also allows pushing and pulling data to and from Data Pools and Data Models. This API was implemented to send the event logs, already constructed from the learning records from Moodle platform, to the celonis platform, where the process mining techniques can be implemented. 

The next step is to use the script **celonis.py** to configure and sent the event logs created to the celonis platform, however before that, you need to modify the environment variables (.env file) according to your celonis user, more specifically: 

- API_TOKEN= on the celonis platform on your profile, creat an API-Keys and add it here.  
- CELONIS_URL= url of your username, be sure that this finishes by "celonis.cloud/"
- CELONIS_WORKSPACE_NAME= "chose a name or leave the name test"
- CELONIS_DATA_POOL_NAME= "chose a name or leave the name test"
- CELONIS_DATA_MODEL_NAME= "chose a name or leave the name test"
- CELONIS_TABLE_NAME= "chose a name or leave the name test"
- CELONIS_ANALYSIS_NAME= "chose a name or leave the name test"

After this is configuration: 
- Be sure to load the environment variables (.env file) to your environment. 
- Run the script  **celonis.py** to send the data and configure the data discovery analysis on the celonis platform. 
- Finally log in to your celonis platform using your credentials, navigate to the workspace created, choose the analysis ***et voilà!*** 

### **Benefits of the approach**
All benefits of this approach regarding educators, training managers, and students are summarized in the following research **[paper](https://aaee.net.au/wp-content/uploads/2021/11/REES_AAEE_2021_paper_311.pdf)** 

