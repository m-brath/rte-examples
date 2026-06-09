import urllib.request
import numpy as np 
import xarray as xr
from pyrte_rrtmgp.rrtmgp.data_files import (
    CloudOpticsFiles,
    GasOpticsFiles,
)
from pyrte_rrtmgp.rrtmgp import GasOptics

INPUT_FILE = "https://github.com/earth-system-radiation/rrtmgp-data/raw/refs/heads/main/" +\
             "examples/rfmip-clear-sky/inputs/" + \
             "multiple_input4MIPs_radiation_RFMIP_UColorado-RFMIP-1-2_none.nc"
LOCAL_FILE = "rfmip_esgf.nc"
OUTPUT_FILE = "rfmip-states.nc"

urllib.request.urlretrieve(INPUT_FILE, LOCAL_FILE)
#
# Which gases are available in the RRTMGP gas optics? 
# 
gas_optics_lw = GasOptics(
    gas_optics_file=GasOpticsFiles.LW_G256
)
gas_optics_sw = GasOptics(
    gas_optics_file=GasOpticsFiles.SW_G224
)
var_list = list(set(gas_optics_sw.available_gases.union(gas_optics_sw.available_gases)))

#
# What other variables are required? 
#
state_vars = ["pres_layer", "pres_level", 
              "temp_layer", "temp_level", 
              "surface_temperature", "surface_emissivity", "surface_albedo", 
              "solar_zenith_angle", 
               "col", "variant",]
for v in state_vars: var_list.append(v) 

f = xr.open_dataset(LOCAL_FILE, decode_cf=False)

f = f.rename_dims({"site":"col", "expt":"variant"}).\
    rename_vars({v:v.split("_GM")[0] for v in f.variables}). \
    drop_vars(["time", "lat", "lon", "sst", "total_solar_irradiance",]). \
    rename_vars({"expt_label":"variant_label",
                 "water_vapor":"h2o", 
                 "ozone":"o3", 
                 "carbon_dioxide":"co2", 
                 "carbon_monoxide":"co", 
                 "methane":"ch4", 
                 "nitrous_oxide":"n2o", 
                 "oxygen":"n2", 
                 "nitrogen":"o2", 
                })

f = f.drop_vars([v for v in f.variables if v not in var_list])

#
# Gas optics doesn't work when coordinates are assigned i.e. with 
# f.assign_coords({"layer":np.arange(1, f.sizes["layer"]+1), 
#                   "level":np.arange(0.5, f.sizes["level"]),
#                 })
#

_ = gas_optics_lw.compute(f, add_to_input = False)

 f.to_netcdf(OUTPUT_FILE, engine = "h5netcdf",)

