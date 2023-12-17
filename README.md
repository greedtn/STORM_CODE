# 構造
## Preprocessing
STORMを実行するための準備をするファイル群
※ 以下、本家のREADMEの抜粋
---
These are the scripts to conduct the data-preprocessing for the STORM model. Input data is taken from IBTrACS, see https://www.ncdc.noaa.gov/ibtracs/. 

**IMPORTANT: Please be aware that these scripts are not maintained and NO support is provided!!**

Please run the scripts as follows:

1. preprocessing.py (this is a module)
2. coefficients.py  (this is a module)
3. environmental.py (this is a module)
4. Make_land_ocean_mask.py <-- in Python 2.7 (uses Basemap), this file stores a .txt file that can be loaded in Python 3.x. These files are now added to the repository, see the Land_ocean_mask_{basin}.txt files
5. genesis_matrix.py  (this is a module)
6. master_preprocessing.py  (this is the master script using the other modules)
---

## Execution
STORMを実行する（実際に架空の台風データを生成する）
※ 以下、本家のREADMEの抜粋
---
This is the STORM (Synthetic Tropical cyclOne geneRation Model) Model. For details, see https://doi.org/10.1038/s41597-020-0381-2

**IMPORTANT: Please be aware that these scripts are not maintained and NO support is provided!!**

These python programs are all modules:
1. SELECT_BASIN.py <--- generates the basin boundaries, no of cyclones, month of occurrence
2. SAMPLE_STARTING_POINT.py <--- generates the genesis locations
3. SAMPLE_TC_MOVEMENT.py <--- creates the tropical cyclone track
4. SAMPLE_TC_PRESSURE.py <--- creates the pressure and wind speed changes along track
5. SAMPLE_RMAX.py <--- samples the radius to maximum wind along the track

MASTER.py is the master-program, which is the one you should run to generate the synthetic tracks.
Input data for each of the modules is generated using the pre-processing scripts, see respective repository for those scripts.
---