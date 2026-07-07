"""
rte-examples: Sets of uniform atmospheric profiles for pyRTE
"""
import numpy as np
import xarray as xr 
from .pooch_config import list_files
import pandera.xarray as pa

__all__ = ["rfmip", "ckdmip", "rce"]

#
# Conventions 
#
_rte_example_vars = {
        "pres_layer": pa.DataVar(dtype=np.float64, dims=("variant", "layer", "col")),
        "pres_level": pa.DataVar(dtype=np.float64, dims=("variant", "level", "col")),
        "temp_layer": pa.DataVar(dtype=np.float64, dims=("variant", "layer", "col")),
        "temp_level": pa.DataVar(dtype=np.float64, dims=("variant", "level", "col")),
        "h2o":        pa.DataVar(dtype=np.float64, dims=("variant", "layer", "col")),
        "o3":         pa.DataVar(dtype=np.float64, dims=("variant", "layer", "col")),
}
_rte_example_vars.update(
	{"co2": pa.DataVar(dtype=np.float64, dims=("variant")),
	 "ch4": pa.DataVar(dtype=np.float64, dims=("variant")), 
	 "n2o": pa.DataVar(dtype=np.float64, dims=("variant")),  
	 "co" : pa.DataVar(dtype=np.float64, dims=("variant")), 
	 "n2" : pa.DataVar(dtype=np.float64, dims=("variant")), 
	 "o2" : pa.DataVar(dtype=np.float64, dims=("variant")),
    }
)
_rte_example_vars.update(
   {"surface_temperature": pa.DataVar(dtype=np.float64, dims=("variant", "col")),
    "surface_emissivity":  pa.DataVar(dtype=np.float64, dims=("variant", "col")),
    "surface_albedo":      pa.DataVar(dtype=np.float64, dims=("variant", "col")),
    "solar_zenith_angle":  pa.DataVar(dtype=np.float64, dims=("variant", "col")),
   }
)

rte_examples_schema = pa.DatasetSchema(
    data_vars=_rte_example_vars
)
