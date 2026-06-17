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
- profiles are  `col` and optionally `variant`
- vertical dimensions are `layer` and `level`. There is one more `level` than `layer. 
- state variables are `pres_layer`, `pres_level`, `temp_layer`, `temp_level`, `surface_temperature`
- composition variables are the molar mixing ratios of `h2o`, `co2`, `ch4`, `n2o`, `co`, `n2`, `o2`
as required by RRTMGP
- radiative variables are `surface_emissivity` and `surface_albedo` (both broadband) and `solar_zenith_angle`

## Use

- `environment.yml` can be used to set up a virtual environment with `mamba`
- `transform_data.py` downloads source data and produces homogenized files
- `driver.py` reads each transformed file and computes fluxes with pyRTE and RRTMGP