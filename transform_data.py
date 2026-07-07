import xarray as xr
from data_transforms import *
from data_transforms import rte_examples_schema

ckdmip.transform_files().to_netcdf(ckdmip.OUTPUT_FILE, engine = "netcdf4",)
try:
	rec_examples_schema(ckdmip.transform_files())
except:
	print ("CKDMIP transform doesn't comply with conventions")

rfmip.transform_files().to_netcdf(rfmip.OUTPUT_FILE, engine = "netcdf4",)
try:
	rec_examples_schema(rfmip.transform_files())
except:
	print ("RFMIP transform doesn't comply with conventions")

rce.create_files().to_netcdf(rce.OUTPUT_FILE, engine = "netcdf4",)
try:
	rec_examples_schema(rce.create_files())
except:
	print ("RCE output doesn't comply with conventions")
