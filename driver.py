import xarray as xr
import pyrte_rrtmgp.rte as rte
from pyrte_rrtmgp.rrtmgp_data_files import (
    CloudOpticsFiles,
    GasOpticsFiles,
)
from pyrte_rrtmgp.rrtmgp import GasOptics

gas_optics_lw = GasOptics(
    gas_optics_file=GasOpticsFiles.LW_G256
)
gas_optics_sw = GasOptics(
    gas_optics_file=GasOpticsFiles.SW_G224
)

atmosphere = xr.open_dataset("rfmip-states.nc")

fluxes = xr.merge([
    xr.merge([
        gas_optics_lw.compute(f, add_to_input = False), 
        f.surface_emissivity, 
    ]).rte.solve(add_to_input = False),  
    xr.merge([
        gas_optics_sw.compute(f, add_to_input = False), 
        f.surface_albedo, 
        f.solar_zenith_angle, 
    ]).rte.solve(add_to_input = False)
]) 
