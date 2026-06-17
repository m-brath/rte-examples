import xarray as xr
from data_transforms import *

ckdmip.transform_files().to_netcdf(ckdmip.OUTPUT_FILE, engine = "netcdf4",)

rfmip.transform_files().to_netcdf(rfmip.OUTPUT_FILE, engine = "netcdf4",)

rce.create_files().to_netcdf(rce.OUTPUT_FILE, engine = "netcdf4",)
