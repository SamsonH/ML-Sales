# project-sales
Repository for sales project for CMSE 202

# Contents

* 2 CSV files containing data sets 
 
 -> super_sample_data
 
 -> crabs_FINAL.csv

* 1 python script
 
 -> machine.py
 
* 2 Jypyter notebooks
 
 -> Sales_Project.ipynb
 
 -> datafilter.ipynb
 
* 2 Folders

 -> data
 
 -> templates
 
 
 ---------------------------------------------------------------
 

## [super_sample_data.csv]

The name of the data set we’ll be using, formatted as a csv file. It
contains a sample of data from our whole data set. Note that our main
set of data was too big to store on github.
Source: https://www.kaggle.com/marcinex1423/salesdb-grocery


## [crabs_FINAL.csv]

The data set that contains all the data for a single product (crab). This
is used for the machine learning algorithms.



---------------------------------------------------------------


## [machine.py]

This file contains all the code that will run the machine learning 
algorithms for PCA and random forests



---------------------------------------------------------------


## [Sales_Project.ipynb]

This notebook will contain the code necessary to run all 
the code together. It imports the machine algorithms we created earlier 
and takes in the data. 

- It uses the data class to clean it up and split

- It trains the machine learning algorithm 

- It displays the results


## [datafilter.ipynb]

This notebook builds the crabs data set in the format we need it 
to use in the machine learning algorithms. It makes the crabs_FINAL.csv file.


---------------------------------------------------------------


## [data]

Contains all old data sets used by past notebooks. Some of the data
contained in this folder is formatted incorrectly for use by code,
but other parts may be used. 

In general, only some notebooks rely on data within the folder, but they
should be able to access the data.


## [templates]

This folder contains old notebooks that were used either as reference
from outside sources (like the internet) and other notebooks that were 
used as scratch assignments for other code. 

Note: some of the old notebooks might have code that does not work
anymore with the git changes. The final working notebook is NOT in this
folder. 







