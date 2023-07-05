import pandas as pd
import os

version = "v02"
path = f"/data1/users/krause/share/high_lvl/{version}/"
periods = os.listdir(path)

df_r0 =pd.read_hdf(f'{path}p03/p03_r000_high_level_{version}.hdf')
df_r1 =pd.read_hdf(f'{path}p03/p03_r001_high_level_{version}.hdf')
df_r2 =pd.read_hdf(f'{path}p03/p03_r002_high_level_{version}.hdf')
df_r3 =pd.read_hdf(f'{path}p03/p03_r003_high_level_{version}.hdf')
df_r4 =pd.read_hdf(f'{path}p03/p03_r004_high_level_{version}.hdf')
df_r5 =pd.read_hdf(f'{path}p03/p03_r005_high_level_{version}.hdf')
df_4r0 =pd.read_hdf(f'{path}p04/p04_r000_high_level_{version}.hdf')
df_4r1 =pd.read_hdf(f'{path}p04/p04_r001_high_level_{version}.hdf')

# concatenate more dataframes for a given period (eg p03)
df_all_p03 = pd.concat([df_r0, df_r1, df_r2, df_r3, df_r4, df_r5], verify_integrity=True)
