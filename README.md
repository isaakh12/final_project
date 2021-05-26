# final_project

## Utility
This project is used to interpolate and visualize spatial data (latitude/longitude) collected over transects as well as conduct a PCA on response variables (in this case oxygen, temperature, and salinity) and run linear models on various potential predictor variables. 

## Steps needed to run code
1. Add data file to working directory
2. Download modules (create_datasets.py, make_plots.py, make_pca.py) and final_project.ipynb from repository to working directory
3. Install matplotlib, numpy, pandas, scipy, statsmodels, cartopy, jupyter, and jupyterlab by running the following code in the terminal: `conda install matplotlib numpy pandas scipy jupyter jupyterlab statsmodels cartopy' 
4. Run `pip install git+https://github.com/physoce/physoce-py` on terminal to install physoce module
5. Run final_project.ipynb notebook on Jupyter or as a .py file in bash (after saving as a .py file from Jupyter). To open a jupyter notebook, navigate to your working directory (with the datafile and modules) and run the following code: `jupyter lab`
   ### Output
   1. Raw data figures and interpolated data for each transect
   2. PCA for all data variables

## Dependencies
1. Data must be a .csv with the following columns:

   A) 'longitude' == Longitudinal coordinates of data collection

   B) 'latitude' == Latitudinal coordinates of data collection

   C) 'rangetobot' == Depth above seafloor of data collection

   D) 'transect' == transect number (integer)

   D) data values == data collected (oxygen here, can also be temperature, salinity, etc.)

2. Must have the following packages downloaded: matplotlib, numpy, pandas, scipy, statsmodels, cartopy, physoce

## Data Source
Data was procured using CTD data from a cruise in 2014 off the coast of British Columbia by Dr. Amanda Kahn and colleagues. Data was transformed to csv format using the Seabird Scientific Data Processing Application by myself in December, 2020. CTD data was combined with navigation data in SQL by myself in December, 2020.

## Location of data
Data is located in final_project repository as a csv named "alltransects.csv"