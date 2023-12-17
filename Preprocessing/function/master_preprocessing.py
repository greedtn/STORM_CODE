# -*- coding: utf-8 -*-
"""
This module is part of the STORM model

For more information, please see 
Bloemendaal, N., Haigh, I.D., de Moel, H. et al. 
Generation of a global synthetic tropical cyclone hazard dataset using STORM. 
Sci Data 7, 40 (2020). https://doi.org/10.1038/s41597-020-0381-2

This is the master program for the data pre-processing. 
This script is made for the data pre-processing of the IBTrACS dataset. For other input datasets, 
please change the syntax accordingly. 
This script will generate multiple output files in the working directory. 

The script is split up in multiple cells, with each cell running a specific part of the data
preprocessing. We advise you to read what is done per cell, and to run per cell rather than
the whole script at once. To keep the script as clean as possible, most of the code has been placed in 
seperate functions in the "preprocessing"-module. 
 
Copyright (C) 2020 Nadia Bloemendaal. All versions released under GNU General Public License v3.0
"""
import xarray as xr
import preprocessing
import coefficients
import environmental
# import genesis_matrix
import genesis_matrix_python3  # python3対応のこちらに変更
import os
import sys
dir_path=os.path.dirname(os.path.realpath(sys.argv[0]))
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# 現在のファイルのディレクトリパスを取得
current_dir = os.path.dirname(__file__)
# output_data ディレクトリへの相対パスを作成
output_dir = os.path.join(current_dir, '..', 'output_data')
# input_data ディレクトリへの相対パスを作成
input_dir = os.path.join(current_dir, '..', 'input_data')

#%%
"""
Open the IBTrACS dataset. The IBTrACS dataset can be downloaded via https://www.ncdc.noaa.gov/ibtracs/
or ftp://eclipse.ncdc.noaa.gov/pub/ibtracs/v04r00/provisional/netcdf/ 
Here, we use the global dataset (version 4) from 1980-2017.
"""

data=xr.open_dataset(os.path.join(input_dir,'IBTrACS.since1980.v04r00.nc'), decode_times=False)
preprocessing.extract_data(data)
data.close()

#%%
"""
Extract the important parameters necessary for the fitting of the regression formulas (and other parts
of the storm model
"""
preprocessing.TC_variables()
 
#%%
"""
Calculate the coefficients for the track and pressure regression formulas
"""
coefficients.track_coefficients()

#%%
"""
Calculate the monthly mean SST and MSLP fields
ECMWF has monthly mean MSLP fields available via the CDS (cds.climate.copernicus.eu)
These should be downloaded and stored as "Monthly_mean_MSLP.nc" and "Monthly_mean_SST.nc"
"""
    
data=xr.open_dataset(os.path.join(__location__,'Monthly_mean_MSLP.nc'))
environmental.monthly_mean_pressure(data)
data.close()

data=xr.open_dataset(os.path.join(__location__,'Monthly_mean_SST.nc'))
environmental.monthly_mean_sst(data)
data.close()

environmental.wind_pressure_relationship()

environmental.calculate_MPI_fields()

environmental.pressure_coefficients()

#%%

"""
以下、Python2用のコードなので、コメントアウト
monthsall=[[6,7,8,9,10,11],[6,7,8,9,10,11],[4,5,6,9,10,11],[1,2,3,4,11,12],[1,2,3,4,11,12],[5,6,7,8,9,10,11]]
for basin_index in range(0,6):
    for month in monthsall[basin_index]:
        genesis_matrix.Makegrid(basin_index,month)
"""


genesis_matrix_python3.Change_genesis_locations()
