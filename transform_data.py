import xarray as xr
from data_transforms import *
from data_transforms import rte_examples_schema
import pandera.xarray as pa
import json 

ckdmip.transform_files().to_netcdf(ckdmip.OUTPUT_FILE, engine = "netcdf4",)
try:
	rte_examples_schema.validate(ckdmip.transform_files(), lazy=True)
except pa.errors.SchemaErrors as exc:
    print(json.dumps(exc.message, indent=2))
    print ("CKDMIP transform doesn't comply with conventions")

rfmip.transform_files().to_netcdf(rfmip.OUTPUT_FILE, engine = "netcdf4",)
try:
	rte_examples_schema.validate(rfmip.transform_files(), lazy=True)
except pa.errors.SchemaErrors as exc:
    print(json.dumps(exc.message, indent=2))
    print ("RFMIP transform doesn't comply with conventions")

rce.create_files().to_netcdf(rce.OUTPUT_FILE, engine = "netcdf4",)
try:
	rte_examples_schema.validate(rce.create_files(), lazy=True)
except pa.errors.SchemaErrors as exc:
    print(json.dumps(exc.message, indent=2))
    print ("RCE output doesn't comply with conventions")
