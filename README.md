# RTE examples

This repo provides homgenenized sets of atmospheric conditions for testing radiative 
transfer codes. Scripts download or generate the original data; rename variables and 
dimensions; reorder the dimensions of fields, and strip global attributes. 

## Data sources
- [Radiative Forcing Model Intercomparision Project](
https://doi.org/10.5194/gmd-9-3447-2016)
- Radiative-convective equilibrium (RCE): temperature and fixed-relative humidity from surface 
temperature to a fixed tropopause temperature with an isothermal stratosphere. 
- A subset of the [Correlated k-distribution Model Intercomparison Project](
https://confluence.ecmwf.int/display/CKDMIP/CKDMIP%3A+Correlated+K-Distribution+Model+Intercomparison+Project+Home)

## Data format
Data roughly follow the conventions used in [pyRTE](https://github.com/earth-system-radiation/pyRTE-RRTMGP)
- state variables are `pres_layer`, `pres_level`, `temp_layer`, `temp_level`, `surface_temperature`
- vertical dimensions are `layer` and `level`. There is one more `level` than `layer. 
- most state variables, `h2o`, and `o3` depend on  `col`, `layer`/`level`, and  `variant`, but
- `pres_layer` and `pres_level`depend only on`col`and `layer`/`level to work around a bug in pyRTE
- boundary conditions are `surface_emissivity` and `surface_albedo` (both broadband) 
  and `solar_zenith_angle`; these depend on `col` and `variant`
- composition variables are the molar mixing ratios of `h2o` and `o3` (spatially resolved as above). 
   Variables `co2`, `ch4`, `n2o`,  `co`, `n2`, `o2` are required as determined by RRTMGP
- any variable depending on `variant` is treated like a gas concentration (with the exception of `expt_names`)
- `total_solar_irradiance` is provided as a scalar in each data set
- Dimensions are ordered `col`, `layer`, `variant` (in Fortran notation) i.e. `col`s are contiguous in memory

Data may need to be replicated across dimensions where it doesn't vary; this is to ensure simplicity in the Fortran 
interface. Conformance with these conventions is ensured with [pandera](https://pandera.readthedocs.io/en/stable/xarray_guide/index.html). 

## Use

- `environment.yml` can be used to set up a virtual environment with `mamba`
- `transform_data.py` downloads source data and produces homogenized files
- `driver.py` reads each transformed file and computes fluxes with pyRTE and RRTMGP