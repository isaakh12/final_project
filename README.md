# final_project

## Steps needed to run code
1. Add data file to working directory
2. Download ipynb file "final_project.ipynb"
3. Run notebook on Jupyter or as a .py file in bash

## Dependencies
1. Data must be a .csv with the following columns:

   A) 'longitude' == Longitudinal coordinates of data collection
  
   B) 'latitude' == Latitudinal coordinates of data collection
  
   C) 'rangetobot' == Depth above seafloor of data collection
  
   D) data values == data collected (oxygen here, can also be temperature, salinity, etc.)

2. Must have the following packages downloaded: matplotlib, numpy, pandas, scipy
  
## Data Source
Data was procured using CTD data from a cruise in 2014 off the coast of British Columbia by Dr. Amanda Kahn and colleagues. Data was transformed using the Seabird Scientific Data Processing Application by myself in December, 2020. CTD data was combined with navigation data in SQL by myself in December, 2020. 

## Location of data
Data is located in final_project repository as a csv named "alltransects.csv"
